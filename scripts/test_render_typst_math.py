import base64
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest import mock

import render_typst_math as renderer


def encoded(value: str) -> str:
    return base64.b64encode(value.encode("utf-8")).decode("ascii")


def placeholder(
    source: str,
    origin: str = "content/posts/test.md:7:1",
    mode: str = "inline",
) -> str:
    return (
        '<x-typst-math data-typst-version="1" '
        f'data-typst-mode="{mode}" '
        f'data-typst-source="{encoded(source)}" '
        f'data-typst-origin="{encoded(origin)}" '
        'data-typst-asset-prefix="/chx-AT-xjtu/generated/typst/">'
        "</x-typst-math>"
    )


class RenderTypstMathTests(unittest.TestCase):
    def test_placeholder_round_trips_unicode_and_html_characters(self) -> None:
        source = 'sum_(i=1)^n i + text("<中文 & symbols>")'
        formula = renderer.parse_placeholder(placeholder(source), Path("index.html"))

        self.assertEqual(formula.source, source)
        self.assertEqual(formula.mode, "inline")
        self.assertEqual(
            formula.asset_prefix, "/chx-AT-xjtu/generated/typst/"
        )

    def test_digest_depends_on_mode_preamble_and_renderer_version(self) -> None:
        inline = renderer.Formula("inline", "x + y", "a.md:1", "/assets/")
        block = renderer.Formula("block", "x + y", "a.md:1", "/assets/")
        baseline = renderer.formula_digest(inline, "", "typst 1")

        self.assertNotEqual(baseline, renderer.formula_digest(block, "", "typst 1"))
        self.assertNotEqual(
            baseline, renderer.formula_digest(inline, "#let x = 1", "typst 1")
        )
        self.assertNotEqual(
            baseline, renderer.formula_digest(inline, "", "typst 2")
        )

    def test_render_public_deduplicates_and_reuses_cache(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            public = root / "public"
            cache = root / "cache"
            preamble = root / "preamble.typ"
            public.mkdir()
            preamble.write_text("// test\n", encoding="utf-8")
            first = public / "index.html"
            second = public / "other.html"
            first.write_text(placeholder("x + y"), encoding="utf-8")
            second.write_text(
                placeholder("x + y", origin="content/posts/other.md:3:1"),
                encoding="utf-8",
            )

            def fake_compile(formula, preamble_text, typst, destination):
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text("<svg></svg>", encoding="utf-8")

            with mock.patch.object(
                renderer, "typst_version", return_value="typst test"
            ), mock.patch.object(
                renderer, "compile_formula", side_effect=fake_compile
            ) as compile_mock:
                counts = renderer.render_public(
                    public, cache, preamble, typst="unused"
                )

            self.assertEqual(counts, (2, 1, 1))
            self.assertEqual(compile_mock.call_count, 1)
            rendered = first.read_text(encoding="utf-8")
            self.assertNotIn("x-typst-math", rendered)
            self.assertIn("/chx-AT-xjtu/generated/typst/", rendered)
            self.assertEqual(len(list((public / "generated/typst").glob("*.svg"))), 1)

            # Put the placeholder back: the second pass must hit the SVG cache.
            first.write_text(placeholder("x + y"), encoding="utf-8")
            second.write_text("plain", encoding="utf-8")
            with mock.patch.object(
                renderer, "typst_version", return_value="typst test"
            ), mock.patch.object(renderer, "compile_formula") as compile_mock:
                counts = renderer.render_public(
                    public, cache, preamble, typst="unused"
                )

            self.assertEqual(counts, (1, 1, 0))
            compile_mock.assert_not_called()

            # Rendering an already processed tree is idempotent and must not
            # delete the SVG referenced by its existing HTML.
            counts = renderer.render_public(
                public, cache, preamble, typst="unused"
            )
            self.assertEqual(counts, (0, 0, 0))
            self.assertEqual(
                len(list((public / "generated/typst").glob("*.svg"))), 1
            )

    def test_typst_document_preserves_source_comments(self) -> None:
        formula = renderer.Formula(
            "block", "x + 10% // comment\ny // final comment", "a.md:1", "/assets/"
        )
        document = renderer.typst_document(formula, "// preamble\n")

        self.assertIn("x + 10% // comment\ny // final comment\n$", document)
        self.assertIn("page(width: auto", document)
        self.assertIn("block: true", document)
        self.assertIn("Noto Sans CJK SC", document)
        self.assertIn('top-edge: "bounds"', document)

    def test_cached_svg_must_be_complete_xml(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            svg = Path(temp_name) / "formula.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg"></svg>', encoding="utf-8"
            )
            self.assertTrue(renderer.cached_svg_is_valid(svg))

            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg">', encoding="utf-8"
            )
            self.assertFalse(renderer.cached_svg_is_valid(svg))

    def test_invalid_base64_is_rejected(self) -> None:
        markup = placeholder("x").replace(encoded("x"), "not_base64!")
        with self.assertRaisesRegex(ValueError, "invalid source"):
            renderer.parse_placeholder(markup, Path("index.html"))

    def test_render_public_replaces_escaped_placeholders_in_feeds(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            public = root / "public"
            cache = root / "cache"
            preamble = root / "preamble.typ"
            public.mkdir()
            preamble.write_text("// test\n", encoding="utf-8")
            feed = public / "index.xml"
            feed.write_text(
                "<description>"
                + renderer.html.escape(placeholder("x + y"), quote=False)
                + "</description>",
                encoding="utf-8",
            )
            raw_feed = public / "raw.xml"
            raw_feed.write_text(
                "<root>" + placeholder("x + y") + "</root>", encoding="utf-8"
            )
            literal = public / "literal.html"
            literal_placeholder = renderer.html.escape(
                placeholder("shown as code"), quote=False
            )
            literal.write_text(
                "<code>" + literal_placeholder + "</code>", encoding="utf-8"
            )

            def fake_compile(formula, preamble_text, typst, destination):
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text("<svg></svg>", encoding="utf-8")

            with mock.patch.object(
                renderer, "typst_version", return_value="typst test"
            ), mock.patch.object(renderer, "compile_formula", side_effect=fake_compile):
                counts = renderer.render_public(public, cache, preamble, typst="unused")

            self.assertEqual(counts, (2, 1, 1))
            rendered = feed.read_text(encoding="utf-8")
            self.assertNotIn("x-typst-math", rendered)
            self.assertIn("&lt;img", rendered)
            self.assertIn("generated/typst/", rendered)
            ET.parse(feed)
            self.assertNotIn("x-typst-math", raw_feed.read_text(encoding="utf-8"))
            ET.parse(raw_feed)
            self.assertIn(
                literal_placeholder, literal.read_text(encoding="utf-8")
            )


if __name__ == "__main__":
    unittest.main()
