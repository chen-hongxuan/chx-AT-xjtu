#!/usr/bin/env python3
"""Prepare Markdown for Hugo without changing the Obsidian source files.

Goldmark parses block-level Markdown before its passthrough extension runs. A
line containing only ``=`` inside a multiline ``$$`` block can therefore turn
the preceding formula line into a Setext heading. This script copies the
content tree and folds each display-math block onto one physical line before
Hugo reads it.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


DISPLAY_DELIMITER = re.compile(r"^(?P<prefix>[ \t]*(?:>[ \t]*)*)\$\$[ \t]*$")
FENCE = re.compile(r"^[ \t]*(?:>[ \t]*)*(?P<marker>`{3,}|~{3,})")


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
            elif marker[0] == fence_char and len(marker) >= fence_length:
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


def prepare_content(source: Path, destination: Path) -> tuple[int, int]:
    source = source.resolve()
    destination = destination.resolve()
    if not source.is_dir():
        raise ValueError(f"content directory does not exist: {source}")
    if source == destination or source in destination.parents:
        raise ValueError("destination must be outside the source content tree")

    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

    markdown_files = 0
    math_blocks = 0
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
            continue
        markdown_files += 1
        text = path.read_text(encoding="utf-8-sig")
        normalized, count = normalize_markdown(text, path)
        path.write_text(normalized, encoding="utf-8", newline="\n")
        math_blocks += count
    return markdown_files, math_blocks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()

    markdown_files, math_blocks = prepare_content(args.source, args.destination)
    print(
        f"Prepared {markdown_files} Markdown files; "
        f"protected {math_blocks} multiline display-math blocks."
    )


if __name__ == "__main__":
    main()
