import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_markdown_links as links


class MarkdownLinkTests(unittest.TestCase):
    def test_heading_anchors_duplicates_and_explicit_ids(self):
        text = (
            "# Common Actions & Their Effects\n"
            "## Repeat\n## Repeat\n"
            '<a id="legacy-fragment"></a>\n'
            "```markdown\n# Not a heading\n```\n"
        )
        self.assertEqual(
            links.anchors(text),
            {"common-actions--their-effects", "repeat", "repeat-1", "legacy-fragment"},
        )

    def test_relative_and_same_file_fragments_are_checked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "target.md").write_text("# Current source\n", encoding="utf-8")
            document = root / "index.md"
            document.write_text(
                "# Entry\n[Local](#entry)\n[Source](target.md#current-source)\n",
                encoding="utf-8",
            )
            self.assertEqual(links.validate(root), [])
            document.write_text("[Broken](target.md#missing)\n", encoding="utf-8")
            self.assertIn("missing fragment", links.validate(root)[0])

    def test_redirect_preserves_old_fragment_and_points_to_new_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "new.md").write_text("# Renamed section\n", encoding="utf-8")
            (root / "old.md").write_text(
                "# Old section\n[Current](new.md#renamed-section)\n", encoding="utf-8"
            )
            (root / "index.md").write_text("[Bookmark](old.md#old-section)\n", encoding="utf-8")
            self.assertEqual(links.validate(root), [])

    def test_missing_paths_and_repository_escape_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "index.md").write_text(
                "[Absent](missing.md)\n[Escape](../outside.md)\n", encoding="utf-8"
            )
            failures = links.validate(root)
            self.assertEqual(len(failures), 2)
            self.assertTrue(any("missing target" in error for error in failures))
            self.assertTrue(any("escapes repository" in error for error in failures))

    def test_percent_encoded_paths_and_fragments_and_external_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "with space.md").write_text("# Source\n", encoding="utf-8")
            (root / "index.md").write_text(
                "[Encoded](with%20space.md#%73ource)\n"
                "[External](https://example.org/absent#unknown)\n",
                encoding="utf-8",
            )
            self.assertEqual(links.validate(root), [])
