import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import prepare_hugo_content as prepare
import render_typst_math as renderer


HUGO = os.environ.get("HUGO_BINARY") or shutil.which("hugo")


class HugoTypstIntegrationTests(unittest.TestCase):
    @unittest.skipUnless(HUGO, "Hugo is not installed")
    def test_minified_hugo_output_contains_replaceable_typst_placeholders(self) -> None:
        repository = Path(__file__).resolve().parent.parent
        fixture = repository / "scripts/fixtures/typst-content"
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            prepared = root / "content"
            public = root / "public"
            prepare.prepare_content(fixture, prepared)
            result = subprocess.run(
                [
                    HUGO,
                    "build",
                    "--gc",
                    "--minify",
                    "--contentDir",
                    str(prepared),
                    "--destination",
                    str(public),
                    "--baseURL",
                    "https://example.test/chx-AT-xjtu/",
                    "--cacheDir",
                    str(root / "hugo-cache"),
                ],
                cwd=repository,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout)

            page = public / "posts/typst-renderer-fixture/index.html"
            text = page.read_text(encoding="utf-8")
            matches = list(renderer.PLACEHOLDER.finditer(text))
            self.assertEqual(len(matches), 7)
            formulas = [
                renderer.parse_placeholder(match.group(0), page) for match in matches
            ]
            self.assertEqual(
                [formula.mode for formula in formulas],
                [
                    "inline",
                    "inline",
                    "inline",
                    "inline",
                    "block",
                    "block",
                    "block",
                ],
            )
            self.assertTrue(all('"' not in formula.origin for formula in formulas))
            self.assertTrue(all("test.md" in formula.origin for formula in formulas))
            self.assertTrue(
                all(
                    formula.asset_prefix
                    == "/chx-AT-xjtu/generated/typst/"
                    for formula in formulas
                )
            )
            self.assertIn("$this is code, not math$", text)

            mixed_page = public / "posts/typst-processor-fixture/index.html"
            mixed_text = mixed_page.read_text(encoding="utf-8")
            mixed_matches = list(renderer.PLACEHOLDER.finditer(mixed_text))
            self.assertEqual(len(mixed_matches), 3)
            mixed_formulas = [
                renderer.parse_placeholder(match.group(0), mixed_page)
                for match in mixed_matches
            ]
            self.assertEqual(
                [(formula.mode, formula.source) for formula in mixed_formulas],
                [
                    ("inline", "sum_(i=1)^n i"),
                    ("block", "mat(1, 2; 3, 4)"),
                    ("block", "sum_(i=1)^n i"),
                ],
            )
            self.assertIn(r"\frac{1}{2}", mixed_text)
            self.assertIn("$$ typ", mixed_text)
            self.assertNotIn("typ:sum", mixed_text)


if __name__ == "__main__":
    unittest.main()
