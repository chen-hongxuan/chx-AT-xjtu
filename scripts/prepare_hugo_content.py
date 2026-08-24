#!/usr/bin/env python3
"""Prepare Markdown for Hugo without changing the Obsidian source files.

Goldmark parses block-level Markdown before its passthrough extension runs. A
line containing only ``=`` inside a multiline ``$$`` block can therefore turn
the preceding formula line into a Setext heading. This script copies the
content tree and folds each display-math block onto one physical line before
Hugo reads it.

The same pass also turns Obsidian TikZJax ``tikz`` fences into cached SVG
assets. Authors can therefore use one ``tikz-cd`` source block in Obsidian and
on the published site; readers only download the finished SVG.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


DISPLAY_DELIMITER = re.compile(r"^(?P<prefix>[ \t]*(?:>[ \t]*)*)\$\$[ \t]*$")
FENCE = re.compile(
    r"^[ \t]*(?:>[ \t]*)*(?P<marker>`{3,}|~{3,})(?P<rest>.*)$"
)
TIKZ_FENCE = re.compile(
    r"^[ \t]*(?P<marker>`{3,}|~{3,})tikz(?:[ \t]+.*)?[ \t]*$",
    re.IGNORECASE,
)
TIKZ_CACHE_VERSION = "tikz-svg-v1"
TIKZ_PUBLIC_PREFIX = "generated/tikz"
TIKZ_TIMEOUT_SECONDS = 60


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


def closes_fence(line: str, marker_char: str, marker_length: int) -> bool:
    """Return whether a line is a valid close for the current fenced block."""
    match = FENCE.match(line)
    if not match:
        return False
    marker = match.group("marker")
    return (
        marker[0] == marker_char
        and len(marker) >= marker_length
        and not match.group("rest").strip()
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
                "--output",
                str(temporary_svg),
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
    block_start = 0
    outer_fence_char = ""
    outer_fence_length = 0
    diagram_count = 0
    compiled_count = 0

    for line_number, line in enumerate(lines, start=1):
        if block_start:
            if closes_fence(line, marker_char, marker_length):
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
                block_start = 0
                diagram_count += 1
            else:
                block_lines.append(line)
            continue

        if outer_fence_char:
            if closes_fence(line, outer_fence_char, outer_fence_length):
                outer_fence_char = ""
                outer_fence_length = 0
            output.append(line)
            continue

        opening = TIKZ_FENCE.match(line)
        if opening:
            marker = opening.group("marker")
            marker_char = marker[0]
            marker_length = len(marker)
            block_start = line_number
            block_lines = []
            continue


        generic_fence = FENCE.match(line)
        if generic_fence:
            marker = generic_fence.group("marker")
            outer_fence_char = marker[0]
            outer_fence_length = len(marker)

        output.append(line)

    if block_start:
        raise ValueError(f"{source}:{block_start}: tikz block is missing its closing fence")

    trailing_newline = "\n" if text.endswith(("\n", "\r")) else ""
    return "\n".join(output) + trailing_newline, diagram_count, compiled_count


def normalize_markdown(text: str, source: Path) -> tuple[str, int]:
    lines = text.splitlines()
    output: list[str] = []
    math_lines: list[str] = []
    math_prefix = ""
    math_start = 0
    fence_char = ""
    fence_length = 0
    normalized_blocks = 0

    for line_number, line in enumerate(lines, start=1):
        if math_lines or math_start:
            closing = DISPLAY_DELIMITER.match(line)
            if closing:
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
            elif closes_fence(line, fence_char, fence_length):
                fence_char = ""
                fence_length = 0
            output.append(line)
            continue

        if not fence_char:
            opening = DISPLAY_DELIMITER.match(line)
            if opening:
                math_prefix = opening.group("prefix")
                math_start = line_number
                math_lines = []
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
        text, diagrams, compiled = render_tikz_blocks(
            text, path, tikz_output, used_tikz_assets
        )
        normalized, count = normalize_markdown(text, path)
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
