#!/usr/bin/env python3
"""Compile Hugo Typst placeholders to cached SVG assets.

Hugo/Goldmark remains responsible for deciding which ``$`` delimiters are
math.  The passthrough render hook emits inert ``x-typst-math`` elements for
pages that opt into Typst; this script replaces only those elements after the
Hugo build.  It therefore never has to guess whether a dollar sign in Markdown
belongs to code, prose, or a formula.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import html
import os
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


PLACEHOLDER_VERSION = "1"
CACHE_SCHEMA = "typst-svg-v2-noto-cjk"
FORMULA_LIMIT_BYTES = 100_000
TYPST_TIMEOUT_SECONDS = 30
PLACEHOLDER = re.compile(
    r"<x-typst-math\b[^>]*(?:/\s*>|>\s*</x-typst-math\s*>)",
    re.IGNORECASE,
)
ESCAPED_PLACEHOLDER = re.compile(
    r"&lt;x-typst-math\b.*?&gt;\s*&lt;/x-typst-math\s*&gt;",
    re.IGNORECASE,
)
PUBLISHED_ASSET = re.compile(
    r"(?:^|/)generated/typst/(?P<name>[0-9a-f]{24}\.svg)", re.IGNORECASE
)


@dataclass(frozen=True)
class Formula:
    mode: str
    source: str
    origin: str
    asset_prefix: str


class _AttributeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.attributes: dict[str, str] | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() == "x-typst-math" and self.attributes is None:
            self.attributes = {key.lower(): value or "" for key, value in attrs}

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)


def decode_base64(value: str, field: str, html_path: Path) -> str:
    try:
        raw = base64.b64decode(value, validate=True)
        return raw.decode("utf-8")
    except (binascii.Error, UnicodeDecodeError) as error:
        raise ValueError(
            f"{html_path}: invalid {field} in a Typst placeholder"
        ) from error


def parse_placeholder(markup: str, html_path: Path) -> Formula:
    parser = _AttributeParser()
    parser.feed(markup)
    attrs = parser.attributes
    if attrs is None:
        raise ValueError(f"{html_path}: malformed Typst placeholder")

    required = {
        "data-typst-version",
        "data-typst-mode",
        "data-typst-source",
        "data-typst-origin",
        "data-typst-asset-prefix",
    }
    missing = sorted(required.difference(attrs))
    if missing:
        raise ValueError(
            f"{html_path}: Typst placeholder is missing {', '.join(missing)}"
        )
    if attrs["data-typst-version"] != PLACEHOLDER_VERSION:
        raise ValueError(
            f"{html_path}: unsupported Typst placeholder version "
            f"{attrs['data-typst-version']!r}"
        )

    mode = attrs["data-typst-mode"].lower()
    if mode not in {"inline", "block"}:
        raise ValueError(f"{html_path}: invalid Typst formula mode {mode!r}")

    source = decode_base64(attrs["data-typst-source"], "source", html_path)
    origin = decode_base64(attrs["data-typst-origin"], "origin", html_path)
    if len(source.encode("utf-8")) > FORMULA_LIMIT_BYTES:
        raise ValueError(
            f"{origin}: Typst formula exceeds {FORMULA_LIMIT_BYTES} bytes"
        )

    asset_prefix = attrs["data-typst-asset-prefix"]
    if not asset_prefix or not asset_prefix.endswith("/"):
        raise ValueError(f"{html_path}: invalid Typst asset prefix")
    return Formula(mode, source, origin, asset_prefix)


def typst_version(typst: str) -> str:
    try:
        result = subprocess.run(
            [typst, "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except FileNotFoundError as error:
        raise RuntimeError(
            f"cannot render Typst math because {typst!r} is not installed"
        ) from error
    if result.returncode != 0:
        raise RuntimeError(f"cannot query Typst version:\n{result.stdout.strip()}")
    return result.stdout.strip()


def formula_digest(
    formula: Formula, preamble: str, renderer_version: str
) -> str:
    # Hash the complete generated document so changes to page sizing, font
    # settings, display style, or the shared preamble cannot reuse stale SVGs.
    payload = "\0".join(
        [CACHE_SCHEMA, renderer_version, typst_document(formula, preamble)]
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:24]


def typst_document(formula: Formula, preamble: str) -> str:
    source = formula.source.replace("\r\n", "\n").replace("\r", "\n").strip()
    block = "true" if formula.mode == "block" else "false"
    return (
        "#set page(width: auto, height: auto, margin: 0pt, fill: none)\n"
        '#set text(font: ("New Computer Modern", "Noto Sans CJK SC"), '
        "size: 12pt, fill: black)\n"
        '#show math.equation: set text(top-edge: "bounds", '
        'bottom-edge: "bounds")\n'
        f"{preamble.rstrip()}\n"
        "#box(math.equation(\n"
        f"  block: {block},\n"
        f"  ${source}\n$\n"
        "))\n"
    )


def cached_svg_is_valid(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size == 0:
        return False
    try:
        root = ET.parse(path).getroot()
        return root.tag.rsplit("}", 1)[-1].lower() == "svg"
    except (OSError, ET.ParseError):
        return False


def compile_formula(
    formula: Formula,
    preamble: str,
    typst: str,
    destination: Path,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hugo-typst-") as temp_name:
        temp_dir = Path(temp_name)
        input_path = temp_dir / "formula.typ"
        output_path = temp_dir / "formula.svg"
        input_path.write_text(
            typst_document(formula, preamble), encoding="utf-8", newline="\n"
        )

        environment = os.environ.copy()
        environment["TYPST_PACKAGE_PATH"] = str(temp_dir / "packages")
        environment["TYPST_PACKAGE_CACHE_PATH"] = str(temp_dir / "package-cache")
        try:
            result = subprocess.run(
                [
                    typst,
                    "compile",
                    "--format",
                    "svg",
                    "--root",
                    str(temp_dir),
                    "--creation-timestamp",
                    "0",
                    "--diagnostic-format",
                    "short",
                    str(input_path),
                    str(output_path),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=TYPST_TIMEOUT_SECONDS,
                check=False,
                env=environment,
            )
        except subprocess.TimeoutExpired as error:
            raise RuntimeError(
                f"{formula.origin}: Typst rendering exceeded "
                f"{TYPST_TIMEOUT_SECONDS} seconds"
            ) from error

        if result.returncode != 0:
            diagnostics = result.stdout[-6000:].strip()
            raise RuntimeError(
                f"{formula.origin}: Typst renderer failed:\n{diagnostics}\n"
                f"Formula: {formula.source}"
            )
        if not cached_svg_is_valid(output_path):
            raise RuntimeError(f"{formula.origin}: Typst produced an invalid SVG")

        temporary = destination.with_suffix(".svg.tmp")
        shutil.copyfile(output_path, temporary)
        temporary.replace(destination)


def formula_markup(formula: Formula, asset_name: str) -> str:
    source = " ".join(formula.source.split())
    source_attr = html.escape(source, quote=True)
    asset_url = html.escape(formula.asset_prefix + asset_name, quote=True)
    if formula.mode == "inline":
        return (
            '<img class="typst-math typst-math--inline" '
            f'src="{asset_url}" alt="{source_attr}" decoding="async" />'
        )
    return (
        '<span class="typst-math typst-math--block">'
        f'<img src="{asset_url}" alt="{source_attr}" '
        'loading="lazy" decoding="async" />'
        "</span>"
    )


def clean_published_assets(directory: Path, used_assets: set[str]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for path in directory.glob("*.svg"):
        if path.name not in used_assets:
            path.unlink()
    for path in directory.glob("*.svg.tmp"):
        path.unlink()


def render_public(
    public_dir: Path,
    cache_dir: Path,
    preamble_path: Path,
    typst: str = "typst",
) -> tuple[int, int, int]:
    public_dir = public_dir.resolve()
    cache_dir = cache_dir.resolve()
    if not public_dir.is_dir():
        raise ValueError(f"public directory does not exist: {public_dir}")
    if not preamble_path.is_file():
        raise ValueError(f"Typst preamble does not exist: {preamble_path}")

    documents: list[
        tuple[Path, str, list[tuple[re.Match[str], Formula, bool]]]
    ] = []
    formula_count = 0
    existing_assets: set[str] = set()
    public_documents = list(public_dir.rglob("*.html")) + list(
        public_dir.rglob("*.xml")
    )
    for document_path in public_documents:
        text = document_path.read_text(encoding="utf-8")
        existing_assets.update(
            match.group("name").lower() for match in PUBLISHED_ASSET.finditer(text)
        )
        matches: list[tuple[re.Match[str], Formula, bool]] = []
        for match in PLACEHOLDER.finditer(text):
            matches.append(
                (match, parse_placeholder(match.group(0), document_path), False)
            )
        if document_path.suffix.lower() == ".xml":
            for match in ESCAPED_PLACEHOLDER.finditer(text):
                matches.append(
                    (
                        match,
                        parse_placeholder(
                            html.unescape(match.group(0)), document_path
                        ),
                        True,
                    )
                )
        matches.sort(key=lambda item: item[0].start())
        if matches:
            documents.append((document_path, text, matches))
            formula_count += len(matches)

    published_dir = public_dir / "generated" / "typst"
    if not formula_count:
        clean_published_assets(published_dir, existing_assets)
        return 0, 0, 0

    preamble = preamble_path.read_text(encoding="utf-8-sig")
    renderer_version = typst_version(typst)
    cache_dir.mkdir(parents=True, exist_ok=True)

    formulas_by_digest: dict[str, Formula] = {}
    digest_by_formula: dict[Formula, str] = {}
    for _, _, matches in documents:
        for _, formula, _ in matches:
            digest = formula_digest(formula, preamble, renderer_version)
            previous = formulas_by_digest.get(digest)
            if previous is not None and typst_document(
                previous, preamble
            ) != typst_document(formula, preamble):
                raise RuntimeError(f"unexpected Typst cache collision for {digest}")
            formulas_by_digest.setdefault(digest, formula)
            digest_by_formula[formula] = digest

    compiled = 0
    for digest, formula in formulas_by_digest.items():
        cached_svg = cache_dir / f"{digest}.svg"
        if not cached_svg_is_valid(cached_svg):
            compile_formula(formula, preamble, typst, cached_svg)
            compiled += 1

    new_assets = {f"{digest}.svg" for digest in formulas_by_digest}
    used_assets = existing_assets | new_assets
    clean_published_assets(published_dir, used_assets)
    for asset_name in new_assets:
        shutil.copyfile(cache_dir / asset_name, published_dir / asset_name)

    # Do not touch any generated document until every formula has compiled.
    for document_path, text, matches in documents:
        output: list[str] = []
        cursor = 0
        for match, formula, escaped_markup in matches:
            output.append(text[cursor : match.start()])
            replacement = formula_markup(
                formula, f"{digest_by_formula[formula]}.svg"
            )
            if escaped_markup:
                replacement = html.escape(replacement, quote=False)
            output.append(replacement)
            cursor = match.end()
        output.append(text[cursor:])
        temporary = document_path.with_suffix(document_path.suffix + ".tmp")
        temporary.write_text("".join(output), encoding="utf-8", newline="\n")
        temporary.replace(document_path)

    return formula_count, len(formulas_by_digest), compiled


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--preamble", type=Path, required=True)
    parser.add_argument("--typst", default="typst")
    args = parser.parse_args()

    formulas, unique, compiled = render_public(
        args.public, args.cache, args.preamble, args.typst
    )
    print(
        f"Rendered {formulas} Typst formula occurrences "
        f"({unique} unique, {compiled} newly compiled)."
    )


if __name__ == "__main__":
    main()
