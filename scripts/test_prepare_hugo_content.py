import base64
import re
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import prepare_hugo_content as prepare


class PrepareHugoContentTests(unittest.TestCase):
    def test_multiline_math_is_folded_outside_code_fences(self) -> None:
        source = Path("article.md")
        markdown = "Before\n$$\na &= b \\\\\n= c\n$$\n\n```cpp\n$$\n=\n$$\n```\n"

        result, count = prepare.normalize_markdown(markdown, source)

        self.assertEqual(count, 1)
        self.assertIn("$$a &= b \\\\ = c$$", result)
        self.assertIn("```cpp\n$$\n=\n$$\n```", result)

    def test_typst_multiline_math_preserves_comments_and_newlines(self) -> None:
        source = Path("typst-article.md")
        formula = 'x + 10% // keep the following line separate\ntext("a // b") + y'
        markdown = f"Before\n$$\n{formula}\n$$\nAfter\n"

        result, count = prepare.normalize_markdown(markdown, source, "typst")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, formula)
        self.assertNotIn("$$", result)

    def test_typ_processor_marker_forces_typst_on_mathjax_page(self) -> None:
        source = Path("mixed-article.md")
        formula = "sum_(i=1)^n i"
        markdown = f"Before\n$$typ\n{formula}\n$$\nAfter\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, formula)
        self.assertNotIn("$$typ", result)

    def test_typ_processor_marker_accepts_optional_colon_for_display(self) -> None:
        source = Path("mixed-article.md")
        markdown = "$$typ:\nmat(1, 2; 3, 4)\n$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, "mat(1, 2; 3, 4)")

    def test_typ_processor_block_can_close_after_formula_content(self) -> None:
        source = Path("mixed-article.md")
        markdown = "$$typ x + y\nz$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, "x + y\nz")

    def test_typst_page_block_can_close_after_formula_content(self) -> None:
        source = Path("typst-article.md")
        markdown = "$$\nx + y\nz$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "typst")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, "x + y\nz")

    def test_mathjax_block_can_close_after_formula_content(self) -> None:
        source = Path("mathjax-article.md")
        markdown = "$$\nx + y\nz$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, "$$x + y z$$\n")
        self.assertEqual(count, 1)

    def test_mathjax_display_with_space_is_not_a_typst_marker(self) -> None:
        source = Path("mixed-article.md")
        markdown = "$$ typ\nx + y\n$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_raw_display_with_content_on_both_delimiters_is_untouched(self) -> None:
        source = Path("legacy-display.md")
        markdown = "$$mn=pos_x,\n\\qquad\nmx=pos_x+s-1.$$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_typst_marker_in_front_matter_is_untouched(self) -> None:
        source = Path("front-matter.md")
        markdown = (
            "---\n"
            "title: Test\n"
            "description: |\n"
            "  $$typ\n"
            "  x + y\n"
            "  $$\n"
            "---\n"
            "Body\n"
        )

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_four_space_indented_typst_marker_is_untouched(self) -> None:
        source = Path("indented-code.md")
        markdown = "    $$typ\n    sum_(i=1)^n i\n    $$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_indented_pseudo_fence_does_not_close_outer_fence(self) -> None:
        source = Path("fenced-code.md")
        markdown = (
            "````markdown\n"
            "    ````\n"
            "$$typ\n"
            "x + y\n"
            "$$\n"
            "````\n"
        )

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_fence_close_must_have_the_same_blockquote_depth(self) -> None:
        source = Path("quoted-fence.md")
        markdown = (
            "> ````markdown\n"
            "> code\n"
            "````\n"
            "$$typ\n"
            "x + y\n"
            "$$\n"
            "> ````\n"
        )

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(result, markdown)
        self.assertEqual(count, 0)

    def test_display_close_must_have_the_same_blockquote_depth(self) -> None:
        source = Path("quoted-math.md")
        markdown = "> $$typ\n> x + y\n$$\n> $$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(count, 1)
        match = re.search(r'source="([A-Za-z0-9+/=]+)"', result)
        self.assertIsNotNone(match)
        decoded = base64.b64decode(match.group(1)).decode("utf-8")
        self.assertEqual(decoded, "x + y\n$$")

    def test_legacy_blockquote_math_with_unquoted_body_still_closes(self) -> None:
        source = Path("legacy-quote.md")
        markdown = "> $$\n x + y\n $$\n"

        result, count = prepare.normalize_markdown(markdown, source, "mathjax")

        self.assertEqual(count, 1)
        self.assertEqual(result, "> $$x + y$$\n")

    def test_math_engine_is_read_from_yaml_or_defaults_to_mathjax(self) -> None:
        typst = "---\ntitle: Test\nmath_engine: typst\n---\n"
        default = "---\ntitle: Test\n---\n"

        self.assertEqual(
            prepare.math_engine_from_front_matter(typst, Path("typst.md")),
            "typst",
        )
        self.assertEqual(
            prepare.math_engine_from_front_matter(default, Path("latex.md")),
            "mathjax",
        )

    def test_unknown_math_engine_is_rejected(self) -> None:
        markdown = "---\nmath_engine: typso\n---\n"
        with self.assertRaisesRegex(ValueError, "unsupported math_engine"):
            prepare.math_engine_from_front_matter(markdown, Path("article.md"))

    def test_cached_tikz_fence_becomes_shortcode(self) -> None:
        source = Path("article.md")
        tikz = (
            "\\usepackage{tikz-cd}\n"
            "\\begin{document}\n"
            "\\begin{tikzcd} A \\arrow[r] & B \\end{tikzcd}\n"
            "\\end{document}\n"
        )
        markdown = f"Before\n\n```tikz\n{tikz}```\n\nAfter\n"

        with tempfile.TemporaryDirectory() as temp_name:
            output_dir = Path(temp_name)
            digest = prepare.tikz_digest(tikz)
            (output_dir / f"{digest}.svg").write_text("<svg/>", encoding="utf-8")

            result, diagrams, compiled = prepare.render_tikz_blocks(
                markdown, source, output_dir
            )

        self.assertEqual(diagrams, 1)
        self.assertEqual(compiled, 0)
        self.assertIn(
            f'{{{{< tikz src="generated/tikz/{digest}.svg" alt="交换图" >}}}}',
            result,
        )
        self.assertNotIn("```tikz", result)

    def test_tikz_fence_can_request_a_larger_web_size(self) -> None:
        source = Path("article.md")
        tikz = "\\begin{document}\n\\end{document}\n"
        markdown = f"```tikz size=large\n{tikz}```\n"

        with tempfile.TemporaryDirectory() as temp_name:
            output_dir = Path(temp_name)
            digest = prepare.tikz_digest(tikz)
            (output_dir / f"{digest}.svg").write_text("<svg/>", encoding="utf-8")
            result, diagrams, compiled = prepare.render_tikz_blocks(
                markdown, source, output_dir
            )

        self.assertEqual(diagrams, 1)
        self.assertEqual(compiled, 0)
        self.assertIn('size="large"', result)

    def test_tikz_fence_rejects_unknown_size(self) -> None:
        markdown = "```tikz size=huge\n\\begin{document}\n\\end{document}\n```\n"
        with self.assertRaisesRegex(ValueError, "unsupported tikz size"):
            prepare.render_tikz_blocks(markdown, Path("article.md"), Path("tikz"))

    def test_compile_tikz_uses_equals_for_dvisvgm_output(self) -> None:
        commands: list[list[str]] = []

        def fake_run_checked(
            command: list[str], cwd: Path, source: Path, line: int
        ) -> None:
            commands.append(command)
            if command[0] == "latex":
                (cwd / "diagram.dvi").write_bytes(b"DVI")
                return

            output_option = next(
                argument for argument in command if argument.startswith("--output=")
            )
            Path(output_option.partition("=")[2]).write_text(
                "<svg/>", encoding="utf-8"
            )

        with tempfile.TemporaryDirectory() as temp_name:
            destination = Path(temp_name) / "diagram.svg"
            source_text = (
                "\\begin{document}\n"
                "\\begin{tikzpicture}\\end{tikzpicture}\n"
                "\\end{document}"
            )
            with mock.patch.object(
                prepare, "run_checked", side_effect=fake_run_checked
            ):
                prepare.compile_tikz(source_text, destination, Path("article.md"), 7)

            self.assertTrue(destination.is_file())

        dvisvgm_command = next(
            command for command in commands if command[0] == "dvisvgm"
        )
        self.assertNotIn("--output", dvisvgm_command)
        self.assertEqual(
            sum(argument.startswith("--output=") for argument in dvisvgm_command), 1
        )

    def test_tikz_fence_requires_output_directory(self) -> None:
        markdown = "```tikz\n\\begin{document}\n\\end{document}\n```\n"
        with self.assertRaisesRegex(ValueError, "--tikz-output"):
            prepare.render_tikz_blocks(markdown, Path("article.md"), None)

    def test_tikz_example_inside_larger_fence_is_not_rendered(self) -> None:
        markdown = (
            "````markdown\n"
            "```tikz\n"
            "\\begin{document}\n"
            "\\end{document}\n"
            "```\n"
            "````\n"
        )

        result, diagrams, compiled = prepare.render_tikz_blocks(
            markdown, Path("article.md"), None
        )

        self.assertEqual(result, markdown)
        self.assertEqual(diagrams, 0)
        self.assertEqual(compiled, 0)

    def test_prepare_rejects_source_parent_as_destination(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            parent = Path(temp_name)
            source = parent / "content"
            source.mkdir()
            (source / "post.md").write_text("text", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "parent directories"):
                prepare.prepare_content(source, parent)

    def test_prepare_removes_unreferenced_cached_svg(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            parent = Path(temp_name)
            source = parent / "content"
            destination = parent / "prepared"
            tikz_output = parent / "tikz"
            source.mkdir()
            tikz_output.mkdir()
            (source / "post.md").write_text("text", encoding="utf-8")
            stale = tikz_output / "stale.svg"
            stale.write_text("<svg/>", encoding="utf-8")

            prepare.prepare_content(source, destination, tikz_output)

            self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
