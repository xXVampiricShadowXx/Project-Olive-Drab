from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_map


FIXTURE = ROOT / "tests" / "fixtures" / "fictional-game.toml"
BUILD_SHEET = ROOT / "docs" / "playtesting" / "shared-map-build-sheet.md"
MAP_SPEC = ROOT / "docs" / "game-design" / "12-town-map-and-terrain-sectors.md"


class BaseMapTests(unittest.TestCase):
    def test_base_matches_build_sheet_cells_and_doc_12_terrain_table(self):
        base = render_map.load_base()
        sectors = {sector["id"]: sector for sector in base["sectors"]}
        sheet_lines = BUILD_SHEET.read_text(encoding="utf-8").splitlines()
        grid_start = next(index for index, line in enumerate(sheet_lines) if line.startswith("| 1 |"))
        for row in range(1, 6):
            cells = [cell.strip() for cell in sheet_lines[grid_start + row - 1].strip("|").split("|")]
            self.assertEqual(cells[0], str(row))
            for column, cell in zip("ABCDEF", cells[1:], strict=True):
                match = re.fullmatch(r"([A-F][1-5]) (.+) \((open|road|broken|built|woods)\)", cell)
                self.assertIsNotNone(match, cell)
                sector_id, name, terrain = match.groups()
                self.assertEqual(sector_id, f"{column}{row}")
                self.assertEqual((sectors[sector_id]["name"], sectors[sector_id]["terrain"]), (name, terrain))

        spec = MAP_SPEC.read_text(encoding="utf-8")
        table = spec.split("## Named sectors and terrain categories", 1)[1].split("## Approaches", 1)[0]
        spec_terrain = {}
        for line in table.splitlines():
            if not line.startswith("| ") or line.startswith("| Category"):
                continue
            fields = [field.strip() for field in line.strip("|").split("|")]
            if len(fields) < 2 or fields[0] not in {"Open", "Road", "Broken", "Built", "Woods"}:
                continue
            terrain = fields[0].lower()
            for sector_id in re.findall(r"[A-F][1-5]", fields[1]):
                self.assertNotIn(sector_id, spec_terrain)
                spec_terrain[sector_id] = terrain
        self.assertEqual(
            {sector_id: sector["terrain"] for sector_id, sector in sectors.items()},
            spec_terrain,
        )

        self.assertEqual(len(sectors), 30)
        self.assertEqual(base["river_name"], "Bluewater River")
        self.assertEqual(base["river_boundary"], "between rows 4 and 5")
        self.assertEqual(base["crossings"], ["C4-C5", "D4-D5"])
        self.assertEqual(
            [(item["name"], item["sectors"]) for item in base["control_pairs"]],
            [("Market Square", ["C3", "D3"]), ("Town Hall Quarter", ["C4", "D4"])],
        )
        self.assertEqual(
            [(item["name"], item["sectors"]) for item in base["objectives"]],
            [
                ("Market Square", ["C3", "D3"]),
                ("Town Hall Quarter", ["C4", "D4"]),
                ("Mill Road Junction", ["C2", "D2"]),
                ("Station Street", ["E3", "F3"]),
            ],
        )
        self.assertEqual(
            [(item["name"], item["sectors"]) for item in base["approaches"]],
            [
                ("Pine Road (N)", ["A1", "F1"]),
                ("East Road (E)", ["F2", "F3", "F4"]),
                ("River Road (S)", ["A5", "F5"]),
                ("West Approach (W)", ["A2", "A3", "A4"]),
            ],
        )
        for phrase in (
            "Bluewater River",
            "C4–C5",
            "D4–D5",
            "Pine Road (N)",
            "East Road (E)",
            "River Road (S)",
            "West Approach (W)",
            "Market Square",
            "Town Hall Quarter",
            "Mill Road Junction",
            "Station Street",
        ):
            self.assertIn(phrase, spec)
            self.assertIn(phrase, BUILD_SHEET.read_text(encoding="utf-8"))
        expected_approaches = {
            "Pine Road (N)": ["A1", "F1"],
            "East Road (E)": ["F2", "F3", "F4"],
            "River Road (S)": ["A5", "F5"],
            "West Approach (W)": ["A2", "A3", "A4"],
        }
        spec_approach_table = spec.split("## Approaches and route choices", 1)[1].split("## Objectives", 1)[0]
        parsed_spec_approaches = {}
        for line in spec_approach_table.splitlines():
            if not line.startswith("| ") or line.startswith("| Approach"):
                continue
            fields = [field.strip() for field in line.strip("|").split("|")]
            if len(fields) >= 2 and fields[0] in expected_approaches:
                parsed_spec_approaches[fields[0]] = re.findall(r"[A-F][1-5]", fields[1])
        sheet_feature_table = BUILD_SHEET.read_text(encoding="utf-8").split("## Views and updates", 1)[0]
        parsed_sheet_approaches = {}
        for line in sheet_feature_table.splitlines():
            if not line.startswith("| ") or line.startswith("| Public feature"):
                continue
            fields = [field.strip() for field in line.strip("|").split("|")]
            if len(fields) >= 2 and fields[0] in expected_approaches:
                parsed_sheet_approaches[fields[0]] = re.findall(r"[A-F][1-5]", fields[1])
        self.assertEqual(parsed_spec_approaches, expected_approaches)
        self.assertEqual(parsed_sheet_approaches, expected_approaches)
        self.assertEqual(
            {item["name"]: item["sectors"] for item in base["approaches"]},
            expected_approaches,
        )
        for approach, sectors in (
            ("Pine Road (N)", "A1, F1"),
            ("East Road (E)", "F2, F3, F4"),
            ("River Road (S)", "A5, F5"),
            ("West Approach (W)", "A2, A3, A4"),
        ):
            self.assertIn(f"{approach} |", BUILD_SHEET.read_text(encoding="utf-8"))
            self.assertIn(sectors, BUILD_SHEET.read_text(encoding="utf-8"))
            self.assertIn(f"| {approach} |", spec)
            self.assertIn(sectors, spec)


class FilteringTests(unittest.TestCase):
    def setUp(self):
        self.game = render_map.validate_game(tomllib.loads(FIXTURE.read_text(encoding="utf-8")), render_map.load_base())
        self.base = render_map.load_base()

    def test_side_allowlist_uses_own_data_and_only_that_sides_releases(self):
        nato_records = render_map.marker_records(self.game, "nato")
        russia_records = render_map.marker_records(self.game, "russia")
        self.assertEqual([item["sector"] for item in nato_records], ["C1", "A2"])
        self.assertEqual([item["sector"] for item in russia_records], ["F2", "B3"])
        self.assertEqual(nato_records[1]["confidence"], "reported")
        self.assertEqual(russia_records[1]["confidence"], "suspected")
        self.assertTrue(all(item["kind"] == "friendly" or item["release_id"] == "R-N-001" for item in nato_records))
        self.assertTrue(all(item["kind"] == "friendly" or item["release_id"] == "R-R-001" for item in russia_records))
        self.assertNotIn("unit-rus-7-private", "\n".join(render_map.visible_text_inputs(self.game, self.base, "nato")))
        self.assertNotIn("GM_SECRET_NEVER_RENDER", "\n".join(render_map.visible_text_inputs(self.game, self.base, "nato")))
        self.assertNotIn("order-private-99", "\n".join(render_map.visible_text_inputs(self.game, self.base, "nato")))
        self.assertNotIn("report-private-42", "\n".join(render_map.visible_text_inputs(self.game, self.base, "russia")))

    def test_side_zones_exclude_opposing_zone(self):
        for side, opponent in (("nato", "russia"), ("russia", "nato")):
            zones = render_map.visible_zones(self.game, side)
            self.assertEqual(set(zones), {side})
            self.assertNotIn(opponent, zones)
            self.assertEqual(zones[side], self.game["zones"][side])

    def test_stale_release_stays_at_reported_sector_after_master_moves(self):
        stale = self.game["releases"]["nato"][0]
        self.assertEqual(stale["sector"], "A2")
        self.game["master_markers"][0]["sector"] = "B3"
        self.game["master_markers"][0]["description"] = "INTERNAL_MASTER_LOCATION_B3"
        visible = render_map.visible_text_inputs(self.game, self.base, "nato")
        self.assertIn("Opposing test unit A2 REPORTED", visible)
        self.assertNotIn("Opposing test unit B3", visible)
        self.assertNotIn("INTERNAL_MASTER_LOCATION_B3", "\n".join(visible))
        caption = render_map.caption_text(self.game, "nato")
        self.assertIn("Fictional opposing unit reported at A2.", caption)
        self.assertNotIn("B3", caption)
        self.assertNotIn("order-private-99", caption)

    def test_captions_contain_only_released_descriptions_and_matching_header(self):
        caption = render_map.caption_text(self.game, "nato")
        self.assertTrue(caption.startswith("v3 NATO 2026-10-01T12:30:00Z\n"))
        self.assertIn("Fictional opposing unit reported at A2.", caption)
        for forbidden in ("GM_SECRET_NEVER_RENDER", "order-private-99", "unit-rus-7-private", "INTERNAL_MASTER_LOCATION_A2"):
            self.assertNotIn(forbidden, caption)
        russia_caption = render_map.caption_text(self.game, "russia")
        self.assertTrue(russia_caption.startswith("v3 RUSSIA 2026-10-01T12:30:00Z\n"))
        self.assertIn("Fictional test contact suspected near B3.", russia_caption)
        self.assertNotIn("report-private-42", russia_caption)
        self.assertNotIn("unit-nato-2", russia_caption)


class SchemaTests(unittest.TestCase):
    def validate_copy(self, mutate):
        game = tomllib.loads(FIXTURE.read_text(encoding="utf-8"))
        mutate(game)
        return render_map.validate_game(game, render_map.load_base())

    def test_unknown_fields_and_values_fail_closed(self):
        with self.assertRaisesRegex(render_map.MapError, "unknown field"):
            self.validate_copy(lambda game: game.update(secret_field="unexpected"))
        with self.assertRaisesRegex(render_map.MapError, "confidence"):
            self.validate_copy(lambda game: game["releases"]["nato"][0].update(confidence="inferred"))
        with self.assertRaisesRegex(render_map.MapError, "visibility"):
            self.validate_copy(lambda game: game["releases"]["nato"][0].update(visibility="everyone"))

    def test_missing_release_id_and_unreleased_opposing_marker_fail_closed(self):
        def missing_id(game):
            del game["releases"]["nato"][0]["release_id"]

        with self.assertRaisesRegex(render_map.MapError, "missing field"):
            self.validate_copy(missing_id)

        def wrong_visibility(game):
            game["releases"]["nato"][0]["visibility"] = "russia"

        with self.assertRaisesRegex(render_map.MapError, "visibility must be nato"):
            self.validate_copy(wrong_visibility)

    def test_master_markers_cannot_be_side_visible(self):
        def make_opponent_visible(game):
            game["master_markers"][0]["visibility"] = "nato"

        with self.assertRaisesRegex(render_map.MapError, "visibility must be master"):
            self.validate_copy(make_opponent_visible)

    def test_own_markers_require_cited_ids_and_all_ids_match_schema(self):
        with self.assertRaisesRegex(render_map.MapError, "missing field.*cite"):
            self.validate_copy(lambda game: game["own"]["nato"][0].pop("cite"))

        for field, value in (
            ("cite", "invalid order id"),
            ("cite", "O" * 25),
        ):
            def mutate(game, field=field, value=value):
                game["own"]["nato"][0][field] = value

            with self.subTest(field=field, value=value):
                with self.assertRaisesRegex(render_map.MapError, "must match"):
                    self.validate_copy(mutate)

        for invalid_id in ("release id", "R" * 25):
            def mutate(game, invalid_id=invalid_id):
                game["releases"]["nato"][0]["release_id"] = invalid_id

            with self.subTest(release_id=invalid_id):
                with self.assertRaisesRegex(render_map.MapError, "must match"):
                    self.validate_copy(mutate)


class PathAndOutputTests(unittest.TestCase):
    def test_cli_check_validates_and_prints_manifest_without_writing_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            outside_game = Path(temporary) / "fictional-game.toml"
            output = Path(temporary) / "out"
            shutil.copyfile(FIXTURE, outside_game)
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "render_map.py"),
                    str(outside_game),
                    "--out",
                    str(output),
                    "--check",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("v3-nato.png -> #nato-private", result.stdout)
            self.assertIn("v3-russia.png -> #russia-private", result.stdout)
            self.assertIn("v3-GM-MASTER-DO-NOT-POST.png -> #gm-map-record", result.stdout)
            self.assertFalse(output.exists())

    def test_output_names_match_allowlists_and_map_to_discord_channels(self):
        with tempfile.TemporaryDirectory() as temporary:
            outside_game = Path(temporary) / "fictional-game.toml"
            shutil.copyfile(FIXTURE, outside_game)
            manifest = render_map.render(outside_game, Path(temporary) / "out", check_only=True)
            self.assertEqual(len(manifest), 5)
            for path, channel in manifest:
                self.assertIn(channel, {"#nato-private", "#russia-private", "#gm-map-record"})
                self.assertTrue(render_map.PNG_NAME.fullmatch(path.name) or render_map.CAPTION_NAME.fullmatch(path.name))
                if "nato" in path.parts:
                    self.assertEqual(channel, "#nato-private")
                if "russia" in path.parts:
                    self.assertEqual(channel, "#russia-private")
                if "gm-master" in path.parts:
                    self.assertEqual(channel, "#gm-map-record")

    def test_paths_inside_repo_and_uncommitted_game_files_are_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            outside_game = Path(temporary) / "game.toml"
            shutil.copyfile(FIXTURE, outside_game)
            with self.assertRaisesRegex(render_map.MapError, "--out must resolve outside"):
                render_map.check_paths(outside_game, ROOT / "map-output")
        with tempfile.TemporaryDirectory(dir=ROOT / "tests" / "fixtures") as fixture_folder:
            temporary_game = Path(fixture_folder) / "temporary-game.toml"
            shutil.copyfile(FIXTURE, temporary_game)
            with tempfile.TemporaryDirectory() as temporary:
                with self.assertRaisesRegex(render_map.MapError, "outside the repository"):
                    render_map.check_paths(temporary_game, Path(temporary) / "out")


class PillowSmokeTests(unittest.TestCase):
    @staticmethod
    def render_with_text_capture(game, base, side, image_path):
        from PIL import ImageDraw

        captured = []
        original_text = ImageDraw.ImageDraw.text

        def capture(draw, xy, text, *args, **kwargs):
            font = kwargs.get("font")
            captured.append((text, getattr(font, "size", None)))
            return original_text(draw, xy, text, *args, **kwargs)

        with patch.object(ImageDraw.ImageDraw, "text", capture):
            render_map.render_png(game, base, side, image_path)
        return captured

    @staticmethod
    def assert_png_has_only_allowed_chunks(test_case, image_path):
        from PIL import Image

        with Image.open(image_path) as image:
            test_case.assertEqual(image.format, "PNG")
            test_case.assertEqual(set(image.info), set())
        data = image_path.read_bytes()
        offset = 8
        chunk_types = []
        while offset < len(data):
            length = int.from_bytes(data[offset : offset + 4], "big")
            chunk_type = data[offset + 4 : offset + 8].decode("ascii")
            chunk_types.append(chunk_type)
            offset += 12 + length
        test_case.assertEqual(chunk_types[0], "IHDR")
        test_case.assertEqual(chunk_types[-1], "IEND")
        test_case.assertTrue(set(chunk_types) <= {"IHDR", "IDAT", "IEND"})
        test_case.assertEqual(chunk_types.count("IHDR"), 1)
        test_case.assertEqual(chunk_types.count("IEND"), 1)

    @unittest.skipUnless(importlib.util.find_spec("PIL"), "Pillow is not installed")
    def test_png_size_banner_and_chunk_allowlist(self):
        from PIL import Image

        game = render_map.validate_game(tomllib.loads(FIXTURE.read_text(encoding="utf-8")), render_map.load_base())
        with tempfile.TemporaryDirectory() as temporary:
            for side, filename in (
                ("nato", "v3-nato.png"),
                ("russia", "v3-russia.png"),
                ("master", "v3-GM-MASTER-DO-NOT-POST.png"),
            ):
                with self.subTest(side=side):
                    image_path = Path(temporary) / filename
                    render_map.render_png(game, render_map.load_base(), side, image_path)
                    with Image.open(image_path) as image:
                        self.assertEqual(image.size[0], render_map.CANVAS[0])
                        self.assertGreaterEqual(image.size[1], render_map.CANVAS[1])
                    self.assert_png_has_only_allowed_chunks(self, image_path)

            title, updated = render_map.banner_lines(game, "nato")
            self.assertEqual(title, "NATO SIDE MAP  |  VERSION 3")
            self.assertEqual(updated, "Updated: 2026-10-01T12:30:00Z")
            self.assertIn(title, render_map.visible_text_inputs(game, render_map.load_base(), "nato"))

    @unittest.skipUnless(importlib.util.find_spec("PIL"), "Pillow is not installed")
    def test_rendered_side_text_uses_only_safe_side_sources(self):
        game = render_map.validate_game(tomllib.loads(FIXTURE.read_text(encoding="utf-8")), render_map.load_base())
        base = render_map.load_base()
        token_pattern = re.compile(r"[A-Za-z0-9]+(?:[-:][A-Za-z0-9]+)*")
        static_text = (
            "NORTH: Pine Road (N)",
            "SOUTH: River Road (S) | BLUEWATER RIVER: boundary between rows 4 and 5",
            "WEST: West Approach (W) | EAST: East Road (E)",
            "Crossings: C4-C5, D4-D5",
            "Objectives:",
            "TERRAIN: open | road | broken | built | woods",
            "CONFIRMED REPORTED SUSPECTED",
            "CONTROL: N=NATO  R=RUSSIA  C=CONTESTED  U=UNCONTROLLED",
            "MARKERS (shape and status identify confidence)",
            "VERSION Updated CITE ZONE NATO ZONE RUSSIA ZONE SIDE MAP",
            "GM MASTER DO NOT POST",
            "01 02 03 04 05 06",
        )

        def allowed_tokens(side):
            safe_values = list(static_text)
            safe_values.extend((str(game["version"]), game["updated_at"]))
            safe_values.extend(game["control"].keys())
            safe_values.extend(game["control"].values())
            safe_values.extend(game["zones"][side])
            safe_values.extend((base["name"], base["river_name"], *base["crossings"]))
            for sector in base["sectors"]:
                safe_values.extend(sector.values())
            for group in ("approaches", "objectives"):
                for item in base[group]:
                    safe_values.extend(
                        value if isinstance(value, str) else " ".join(value)
                        for value in item.values()
                    )
            for marker in game["own"][side]:
                safe_values.extend(
                    marker[field]
                    for field in ("id", "cite", "owner", "sector", "label", "description", "visibility", "confidence")
                )
            for release in game["releases"][side]:
                safe_values.extend(
                    release[field]
                    for field in (
                        "release_id",
                        "sector",
                        "confidence",
                        "label",
                        "description",
                        "released_at",
                        "visibility",
                    )
                )
            source_tokens = {
                token
                for value in safe_values
                for token in token_pattern.findall(str(value))
            }
            return source_tokens | {token.upper() for token in source_tokens}

        with tempfile.TemporaryDirectory() as temporary:
            for side, opponent in (("nato", "russia"), ("russia", "nato")):
                with self.subTest(side=side):
                    captured = self.render_with_text_capture(
                        game, base, side, Path(temporary) / f"v3-{side}.png"
                    )
                    self.assertTrue(captured)
                    drawn_strings = [text for text, _ in captured]
                    joined_drawn = "\n".join(drawn_strings)
                    forbidden = [
                        *(
                            value
                            for marker in game["master_markers"]
                            for value in (marker["id"], marker["description"])
                        ),
                        *game["gm_notes"],
                        *(release["source_id"] for releases in game["releases"].values() for release in releases),
                        *(
                            value
                            for release in game["releases"][opponent]
                            for value in (release["release_id"], release["label"], release["description"])
                        ),
                    ]
                    for value in forbidden:
                        self.assertNotIn(value, joined_drawn)

                    approved = allowed_tokens(side)
                    for drawn, font_size in captured:
                        self.assertIsInstance(drawn, str)
                        self.assertIsInstance(font_size, int)
                        self.assertTrue(
                            set(token_pattern.findall(drawn)) <= approved,
                            f"drawn text contains an unapproved token: {drawn!r}",
                        )
                    own_cite = game["own"][side][0]["cite"]
                    own_release = game["releases"][side][0]
                    self.assertIn(own_cite, joined_drawn)
                    self.assertIn(own_release["release_id"], joined_drawn)
                    self.assertIn(own_release["released_at"], joined_drawn)

    @unittest.skipUnless(importlib.util.find_spec("PIL"), "Pillow is not installed")
    def test_render_outputs_side_directories_and_captions(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "out"
            outside_game = Path(temporary) / "fictional-game.toml"
            shutil.copyfile(FIXTURE, outside_game)
            manifest = render_map.render(outside_game, output)
            self.assertEqual(len(manifest), 5)
            self.assertTrue((output / "nato" / "v3-nato.png").is_file())
            self.assertTrue((output / "russia" / "v3-russia.png").is_file())
            self.assertTrue((output / "gm-master" / "v3-GM-MASTER-DO-NOT-POST.png").is_file())
            self.assertTrue((output / "nato" / "v3-nato-caption.txt").is_file())
            with self.assertRaisesRegex(render_map.MapError, "increment the map version"):
                render_map.render(outside_game, output)


if __name__ == "__main__":
    unittest.main()
