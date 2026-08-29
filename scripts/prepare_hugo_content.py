#!/usr/bin/env python3
"""Prepare Markdown for Hugo without changing the Obsidian source files.

Goldmark parses block-level Markdown before its passthrough extension runs. A
line containing only ``=`` inside a multiline ``$$`` block can therefore turn
the preceding formula line into a Setext heading. This script copies the
content tree and folds MathJax display blocks onto one physical line before
Hugo reads them. Typst display blocks are instead encoded into an internal
shortcode, preserving comments and physical newlines verbatim.

The same pass also turns Obsidian TikZJax ``tikz`` fences into cached SVG
assets. Authors can therefore use one ``tikz-cd`` source block in Obsidian and
on the published site; readers only download the finished SVG.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


MARKDOWN_CONTAINER_PREFIX = r" {0,3}(?:>[ \t]*)*"
DISPLAY_DELIMITER = re.compile(
    rf"^(?P<prefix>{MARKDOWN_CONTAINER_PREFIX})\$\$[ \t]*$"
)
TYPST_DISPLAY_OPEN = re.compile(
    rf"^(?P<prefix>{MARKDOWN_CONTAINER_PREFIX})\$\$typ"
    r"(?P<rest>(?::.*|[ \t].*)?)$"
)
DISPLAY_CONTENT_OPEN = re.compile(
    rf"^(?P<prefix>{MARKDOWN_CONTAINER_PREFIX})\$\$(?P<initial>.+)$"
)
FENCE = re.compile(
    rf"^(?P<prefix>{MARKDOWN_CONTAINER_PREFIX})"
    r"(?P<marker>`{3,}|~{3,})(?P<rest>.*)$"
)
TIKZ_FENCE = re.compile(
    r"^(?P<prefix> {0,3})(?P<marker>`{3,}|~{3,})"
    r"tikz(?:[ \t]+.*)?[ \t]*$",
    re.IGNORECASE,
)
TIKZ_CACHE_VERSION = "tikz-svg-v1"
TIKZ_PUBLIC_PREFIX = "generated/tikz"
TIKZ_TIMEOUT_SECONDS = 60
SUPPORTED_MATH_ENGINES = {"mathjax", "latex", "typst"}
YAML_MATH_ENGINE = re.compile(
    r"^[ \t]*math_engine[ \t]*:[ \t]*['\"]?(?P<engine>[A-Za-z0-9_-]+)['\"]?[ \t]*(?:#.*)?$"
)
TOML_MATH_ENGINE = re.compile(
    r"^[ \t]*math_engine[ \t]*=[ \t]*['\"](?P<engine>[A-Za-z0-9_-]+)['\"][ \t]*(?:#.*)?$"
)


def strip_quote_prefix(line: str, prefix: str) -> str:
    """Remove the structural quote prefix while preserving TeX ``>`` signs."""
    if line.startswith(prefix):
        return line[len(prefix) :]

    quote_depth = prefix.count(">")
    if quote_depth == 0:
        return line

    match = re.match(rf"^[ \t]*(?:>[ \t]*){{{quote_depth}}}", line)
    return line[match.end() :] if match else line


def strip_tex_comment(line: str) -> str:
    """Discard an unescaped TeX comment before physical lines are joined."""
    for index, char in enumerate(line):
        if char != "%":
            continue
        slash_count = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            slash_count += 1
            cursor -= 1
        if slash_count % 2 == 0:
            return line[:index]
    return line


def math_engine_from_front_matter(text: str, source: Path) -> str:
    """Read the optional per-page engine without adding a YAML dependency."""
    lines = text.splitlines()
    if not lines or lines[0].strip() not in {"---", "+++"}:
        return "mathjax"

    delimiter = lines[0].strip()
    matcher = YAML_MATH_ENGINE if delimiter == "---" else TOML_MATH_ENGINE
    for line in lines[1:]:
        if line.strip() == delimiter or (delimiter == "---" and line.strip() == "..."):
            break
        match = matcher.match(line)
        if not match:
            continue
        engine = match.group("engine").lower()
        if engine not in SUPPORTED_MATH_ENGINES:
            raise ValueError(
                f"{source}: unsupported math_engine {engine!r}; "
                "use mathjax, latex, or typst"
            )
        return engine
    return "mathjax"


def encode_shortcode_value(value: str) -> str:
    """Encode arbitrary source text as a quoted Hugo shortcode parameter."""
    return base64.b64encode(value.encode("utf-8")).decode("ascii")


def front_matter_end_line(lines: list[str]) -> int:
    """Return the one-based closing line for YAML/TOML front matter."""
    if not lines or lines[0].strip() not in {"---", "+++"}:
        return 0

    delimiter = lines[0].strip()
    for line_number, line in enumerate(lines[1:], start=2):
        if line.strip() == delimiter or (
            delimiter == "---" and line.strip() == "..."
        ):
            return line_number
    return len(lines)


def same_quote_depth(first_prefix: str, second_prefix: str) -> bool:
    """Keep display-math delimiters inside the same blockquote container."""
    return first_prefix.count(">") == second_prefix.count(">")


def display_close_matches(
    opening_prefix: str, closing_prefix: str, math_lines: list[str]
) -> bool:
    """Match the container, while retaining compatibility with old notes.

    A few existing articles start a formula with ``> $$`` but omit ``>`` on
    the formula body and closing delimiter. Treat that established shape as a
    deliberately escaped container. A lone delimiter outside an otherwise
    well-formed blockquote formula must not close it.
    """
    if same_quote_depth(opening_prefix, closing_prefix):
        return True

    opening_depth = opening_prefix.count(">")
    closing_depth = closing_prefix.count(">")
    if closing_depth >= opening_depth:
        return False

    for line in math_lines:
        if not line.strip():
            continue
        prefix = re.match(MARKDOWN_CONTAINER_PREFIX, line)
        if prefix and prefix.group(0).count(">") == closing_depth:
            return True
    return False


def split_display_content_close(line: str) -> tuple[str, str] | None:
    """Return the container prefix and content before a trailing ``$$``."""
    prefix_match = re.match(MARKDOWN_CONTAINER_PREFIX, line)
    prefix = prefix_match.group(0) if prefix_match else ""
    inner = strip_quote_prefix(line, prefix).rstrip()
    if len(inner) <= 2 or not inner.endswith("$$"):
        return None

    delimiter_start = len(inner) - 2
    slash_count = 0
    cursor = delimiter_start - 1
    while cursor >= 0 and inner[cursor] == "\\":
        slash_count += 1
        cursor -= 1
    if slash_count % 2:
        return None

    return prefix, f"{prefix}{inner[:delimiter_start]}"


def has_same_line_display_close(line: str, prefix: str) -> bool:
    """Leave complete one-line ``$$...$$`` expressions to Goldmark."""
    closing = split_display_content_close(line)
    return bool(closing and same_quote_depth(prefix, closing[0]))


def closes_fence(
    line: str,
    marker_char: str,
    marker_length: int,
    opening_prefix: str = "",
) -> bool:
    """Return whether a line is a valid close for the current fenced block."""
    match = FENCE.match(line)
    if not match:
        return False
    marker = match.group("marker")
    return (
        marker[0] == marker_char
        and len(marker) >= marker_length
        and not match.group("rest").strip()
        and same_quote_depth(opening_prefix, match.group("prefix"))
    )


def tikz_digest(source: str) -> str:
    """Return a stable cache key, including the renderer schema version."""
    normalized = source.replace("\r\n", "\n").replace("\r", "\n").strip() + "\n"
    payload = f"{TIKZ_CACHE_VERSION}\0{normalized}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:24]


def cached_svg_is_valid(path: Path) -> bool:
    """Reject missing, empty, or obviously incomplete cache entries."""
    if not path.is_file() or path.stat().st_size == 0:
        return False
    try:
        return "<svg" in path.read_text(encoding="utf-8", errors="ignore")[:4096]
    except OSError:
        return False


def run_checked(command: list[str], cwd: Path, source: Path, line: int) -> None:
    """Run one renderer command and turn its diagnostics into a useful error."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=TIKZ_TIMEOUT_SECONDS,
            check=False,
        )
    except FileNotFoundError as error:
        raise RuntimeError(
            f"{source}:{line}: cannot render TikZ because {command[0]!r} "
            "is not installed"
        ) from error
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(
            f"{source}:{line}: TikZ rendering exceeded "
            f"{TIKZ_TIMEOUT_SECONDS} seconds"
        ) from error

    if result.returncode != 0:
        diagnostics = result.stdout[-6000:].strip()
        raise RuntimeError(
            f"{source}:{line}: TikZ renderer failed:\n{diagnostics}"
        )


def compile_tikz(source_text: str, destination: Path, source: Path, line: int) -> None:
    """Compile one Obsidian-compatible TikZ block to a path-only SVG."""
    if re.search(r"\\documentclass(?:\s|\[|\{)", source_text):
        raise ValueError(
            f"{source}:{line}: omit \\documentclass from a tikz block; "
            "Obsidian and the blog add the standalone class automatically"
        )
    if "\\begin{document}" not in source_text or "\\end{document}" not in source_text:
        raise ValueError(
            f"{source}:{line}: a tikz block needs both \\begin{{document}} and "
            "\\end{document}"
        )

    latex_source = (
        "\\documentclass[border=3pt]{standalone}\n"
        "\\def\\pgfsysdriver{pgfsys-dvisvgm.def}\n"
        "\\usepackage{tikz}\n"
        f"{source_text.strip()}\n"
    )

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="hugo-tikz-") as temp_name:
        temp_dir = Path(temp_name)
        tex_path = temp_dir / "diagram.tex"
        tex_path.write_text(latex_source, encoding="utf-8", newline="\n")

        run_checked(
            [
                "latex",
                "-no-shell-escape",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-output-directory={temp_dir}",
                str(tex_path),
            ],
            temp_dir,
            source,
            line,
        )

        dvi_path = temp_dir / "diagram.dvi"
        if not dvi_path.is_file():
            raise RuntimeError(f"{source}:{line}: LaTeX did not produce a DVI file")

        temporary_svg = destination.with_suffix(".svg.tmp")
        run_checked(
            [
                "dvisvgm",
                "--no-fonts",
                "--exact-bbox",
                f"--output={temporary_svg}",
                str(dvi_path),
            ],
            temp_dir,
            source,
            line,
        )
        if not temporary_svg.is_file() or temporary_svg.stat().st_size == 0:
            raise RuntimeError(f"{source}:{line}: dvisvgm produced an empty SVG")
        temporary_svg.replace(destination)


def render_tikz_blocks(
    text: str,
    source: Path,
    output_dir: Path | None,
    used_assets: set[str] | None = None,
) -> tuple[str, int, int]:
    """Replace top-level ``tikz`` fences with Hugo SVG shortcodes."""
    lines = text.splitlines()
    output: list[str] = []
    block_lines: list[str] = []
    marker_char = ""
    marker_length = 0
    marker_prefix = ""
    block_start = 0
    outer_fence_char = ""
    outer_fence_length = 0
    outer_fence_prefix = ""
    diagram_count = 0
    compiled_count = 0

    for line_number, line in enumerate(lines, start=1):
        if block_start:
            if closes_fence(line, marker_char, marker_length, marker_prefix):
                if output_dir is None:
                    raise ValueError(
                        f"{source}:{block_start}: found a tikz block but "
                        "--tikz-output was not provided"
                    )
                tikz_source = "\n".join(block_lines) + "\n"
                digest = tikz_digest(tikz_source)
                svg_name = f"{digest}.svg"
                svg_path = output_dir / svg_name
                if not cached_svg_is_valid(svg_path):
                    compile_tikz(tikz_source, svg_path, source, block_start)
                    compiled_count += 1
                if used_assets is not None:
                    used_assets.add(svg_name)
                output.append(
                    '{{< tikz src="'
                    + f"{TIKZ_PUBLIC_PREFIX}/{svg_name}"
                    + '" alt="交换图" >}}'
                )
                block_lines = []
                marker_char = ""
                marker_length = 0
                marker_prefix = ""
                block_start = 0
                diagram_count += 1
            else:
                block_lines.append(line)
            continue

        if outer_fence_char:
            if closes_fence(
                line,
                outer_fence_char,
                outer_fence_length,
                outer_fence_prefix,
            ):
                outer_fence_char = ""
                outer_fence_length = 0
                outer_fence_prefix = ""
            output.append(line)
            continue

        opening = TIKZ_FENCE.match(line)
        if opening:
            marker = opening.group("marker")
            marker_char = marker[0]
            marker_length = len(marker)
            marker_prefix = opening.group("prefix")
            block_start = line_number
            block_lines = []
            continue


        generic_fence = FENCE.match(line)
        if generic_fence:
            marker = generic_fence.group("marker")
            outer_fence_char = marker[0]
            outer_fence_length = len(marker)
            outer_fence_prefix = generic_fence.group("prefix")

        output.append(line)

    if block_start:
        raise ValueError(f"{source}:{block_start}: tikz block is missing its closing fence")

    trailing_newline = "\n" if text.endswith(("\n", "\r")) else ""
    return "\n".join(output) + trailing_newline, diagram_count, compiled_count


def normalize_markdown(
    text: str, source: Path, math_engine: str = "mathjax"
) -> tuple[str, int]:
    lines = text.splitlines()
    output: list[str] = []
    math_lines: list[str] = []
    math_prefix = ""
    math_start = 0
    math_is_typst = False
    raw_math_opening = ""
    fence_char = ""
    fence_length = 0
    fence_prefix = ""
    normalized_blocks = 0
    front_matter_end = front_matter_end_line(lines)

    for line_number, line in enumerate(lines, start=1):
        if line_number <= front_matter_end:
            output.append(line)
            continue

        if math_lines or math_start:
            closing = DISPLAY_DELIMITER.match(line)
            closing_prefix = closing.group("prefix") if closing else ""
            closing_candidate = closing is not None
            content_closing = None
            if not closing:
                content_closing = split_display_content_close(line)
            if content_closing:
                closing_prefix = content_closing[0]
                closing_candidate = True

            if closing_candidate:
                closes_math = display_close_matches(
                    math_prefix, closing_prefix, math_lines
                )
            else:
                closes_math = False

            if closes_math:
                was_raw_math = bool(raw_math_opening)
                if content_closing and not was_raw_math:
                    math_lines.append(content_closing[1])
                if raw_math_opening:
                    output.append(raw_math_opening)
                    output.extend(math_lines)
                    output.append(line)
                elif math_is_typst:
                    # Preserve Typst comments, strings, and physical newlines.
                    # A shortcode keeps the raw source away from Goldmark's
                    # block parser, so lines such as ``=`` cannot become a
                    # Setext heading and ``//`` comments keep their scope.
                    typst_source = "\n".join(
                        strip_quote_prefix(math_line, math_prefix)
                        for math_line in math_lines
                    )
                    source64 = encode_shortcode_value(typst_source)
                    origin64 = encode_shortcode_value(f"{source}:{math_start}")
                    output.append(
                        f'{math_prefix}{{{{< typst-math source="{source64}" '
                        f'origin="{origin64}" >}}}}'
                    )
                else:
                    parts = []
                    for math_line in math_lines:
                        part = strip_quote_prefix(math_line, math_prefix)
                        part = strip_tex_comment(part).strip()
                        if part:
                            parts.append(part)
                    output.append(f"{math_prefix}$${' '.join(parts)}$$")
                math_lines = []
                math_prefix = ""
                math_start = 0
                math_is_typst = False
                raw_math_opening = ""
                if not was_raw_math:
                    normalized_blocks += 1
            else:
                math_lines.append(line)
            continue

        fence = FENCE.match(line)
        if fence:
            marker = fence.group("marker")
            if not fence_char:
                fence_char = marker[0]
                fence_length = len(marker)
                fence_prefix = fence.group("prefix")
            elif closes_fence(line, fence_char, fence_length, fence_prefix):
                fence_char = ""
                fence_length = 0
                fence_prefix = ""
            output.append(line)
            continue

        if not fence_char:
            typst_opening = TYPST_DISPLAY_OPEN.match(line)
            if typst_opening and has_same_line_display_close(
                line, typst_opening.group("prefix")
            ):
                typst_opening = None

            opening = typst_opening or DISPLAY_DELIMITER.match(line)
            if opening:
                math_prefix = opening.group("prefix")
                math_start = line_number
                math_is_typst = math_engine == "typst" or typst_opening is not None
                raw_math_opening = ""
                if typst_opening:
                    initial = typst_opening.group("rest")
                    if initial.startswith(":"):
                        initial = initial[1:]
                    initial = initial.lstrip(" \t")
                    math_lines = [f"{math_prefix}{initial}"] if initial else []
                else:
                    math_lines = []
                continue

            content_opening = DISPLAY_CONTENT_OPEN.match(line)
            if content_opening and not has_same_line_display_close(
                line, content_opening.group("prefix")
            ):
                math_prefix = content_opening.group("prefix")
                math_start = line_number
                math_is_typst = math_engine == "typst"
                if math_is_typst:
                    initial = content_opening.group("initial")
                    math_lines = [f"{math_prefix}{initial}"]
                    raw_math_opening = ""
                else:
                    math_lines = []
                    raw_math_opening = line
                continue

        output.append(line)

    if math_start:
        raise ValueError(
            f"{source}:{math_start}: display math block is missing its closing $$"
        )

    trailing_newline = "\n" if text.endswith(("\n", "\r")) else ""
    return "\n".join(output) + trailing_newline, normalized_blocks


def prepare_content(
    source: Path, destination: Path, tikz_output: Path | None = None
) -> tuple[int, int, int, int]:
    source = source.resolve()
    destination = destination.resolve()
    if not source.is_dir():
        raise ValueError(f"content directory does not exist: {source}")
    if (
        source == destination
        or source in destination.parents
        or destination in source.parents
    ):
        raise ValueError(
            "destination must be separate from both the source content tree "
            "and its parent directories"
        )

    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

    markdown_files = 0
    math_blocks = 0
    tikz_blocks = 0
    compiled_diagrams = 0
    used_tikz_assets: set[str] = set()
    if tikz_output is not None:
        tikz_output = tikz_output.resolve()
        tikz_output.mkdir(parents=True, exist_ok=True)
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
            continue
        markdown_files += 1
        text = path.read_text(encoding="utf-8-sig")
        math_engine = math_engine_from_front_matter(text, path)
        text, diagrams, compiled = render_tikz_blocks(
            text, path, tikz_output, used_tikz_assets
        )
        normalized, count = normalize_markdown(text, path, math_engine)
        path.write_text(normalized, encoding="utf-8", newline="\n")
        math_blocks += count
        tikz_blocks += diagrams
        compiled_diagrams += compiled

    if tikz_output is not None:
        for cached_svg in tikz_output.glob("*.svg"):
            if cached_svg.name not in used_tikz_assets:
                cached_svg.unlink()
        for temporary_svg in tikz_output.glob("*.svg.tmp"):
            temporary_svg.unlink()

    return markdown_files, math_blocks, tikz_blocks, compiled_diagrams


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument(
        "--tikz-output",
        type=Path,
        help="directory for cached SVG files (normally static/generated/tikz)",
    )
    args = parser.parse_args()

    markdown_files, math_blocks, tikz_blocks, compiled_diagrams = prepare_content(
        args.source, args.destination, args.tikz_output
    )
    print(
        f"Prepared {markdown_files} Markdown files; "
        f"protected {math_blocks} multiline display-math blocks; "
        f"prepared {tikz_blocks} TikZ diagrams "
        f"({compiled_diagrams} newly compiled)."
    )


if __name__ == "__main__":
    main()
