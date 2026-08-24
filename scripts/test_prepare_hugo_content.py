import tempfile
import unittest
from pathlib import Path

import prepare_hugo_content as prepare


class PrepareHugoContentTests(unittest.TestCase):
    def test_multiline_math_is_folded_outside_code_fences(self) -> None:
        source = Path("article.md")
        markdown = "Before\n$$\na &= b \\\\\n= c\n$$\n\n```cpp\n$$\n=\n$$\n```\n"

        result, count = prepare.normalize_markdown(markdown, source)

        self.assertEqual(count, 1)
        self.assertIn("$$a &= b \\\\ = c$$", result)
        self.assertIn("```cpp\n$$\n=\n$$\n```", result)

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
