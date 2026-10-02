#!/usr/bin/env python3
"""Render safe, side-specific static Brackenford maps from a private TOML file."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "data" / "map" / "base.toml"
SIDES = ("nato", "russia")
CONFIDENCE = {"confirmed", "reported", "suspected"}
VISIBILITY = {"master", *SIDES}
CONTROL_STATES = {"nato", "russia", "contested", "uncontrolled"}
PNG_NAME = re.compile(r"^v[1-9][0-9]*-(?:nato|russia|GM-MASTER-DO-NOT-POST)\.png$")
CAPTION_NAME = re.compile(r"^v[1-9][0-9]*-(?:nato|russia)-caption\.txt$")
CHANNELS = {
    "nato": "#nato-private",
    "russia": "#russia-private",
    "master": "#gm-map-record",
}
FIXTURE_PATH = Path("tests/fixtures/fictional-game.toml")
ID_PATTERN = re.compile(r"^[A-Za-z0-9-]{1,24}$")

CANVAS = (1600, 1700)
GRID_LEFT, GRID_TOP, CELL_WIDTH, CELL_HEIGHT = 95, 300, 235, 190
# Legibility floor for a 1600px PNG shown at roughly phone width in Discord.
MIN_FONT_PX = 22
MARKER_GLYPH_PX = 30
CELL_TEXT_PX = 24
CELL_MARKER_SLOTS = 3


class MapError(ValueError):
    """Raised when the game file is not safe to render."""


def _keys(
    value: Any, expected: set[str], where: str, required: set[str] | None = None
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise MapError(f"{where} must be a TOML table")
    unknown = set(value) - expected
    missing = (required or expected) - set(value)
    if unknown:
        raise MapError(f"{where} contains unknown field(s): {', '.join(sorted(unknown))}")
    if missing:
        raise MapError(f"{where} is missing field(s): {', '.join(sorted(missing))}")
    return value


def _text(value: Any, where: str, *, nonempty: bool = True) -> str:
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise MapError(f"{where} must be {'a non-empty ' if nonempty else 'a '}string")
    return value


def _identifier(value: Any, where: str) -> str:
    identifier = _text(value, where)
    if not ID_PATTERN.fullmatch(identifier):
        raise MapError(f"{where} must match ^[A-Za-z0-9-]{{1,24}}$")
    return identifier


def _list_of_strings(value: Any, where: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise MapError(f"{where} must be an array of strings")
    return value


def load_base() -> dict[str, Any]:
    with BASE_PATH.open("rb") as stream:
        base = tomllib.load(stream)
    ids = [sector["id"] for sector in base["sectors"]]
    expected_ids = [f"{column}{row}" for row in range(1, 6) for column in "ABCDEF"]
    if ids != expected_ids:
        raise MapError("base.toml must define the 30 sectors in grid order")
    return base


def _validate_timestamp(value: Any, where: str) -> str:
    timestamp = _text(value, where)
    try:
        parsed = dt.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as error:
        raise MapError(f"{where} must be an ISO-8601 timestamp") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise MapError(f"{where} must include a timezone")
    return timestamp


def _validate_marker(
    item: Any,
    where: str,
    sectors: set[str],
    *,
    expected_owner: str | None = None,
    expected_visibility: str | None = None,
    own_marker: bool = False,
) -> dict[str, Any]:
    marker_fields = {"id", "owner", "sector", "label", "description", "visibility", "confidence"}
    if own_marker:
        marker_fields.add("cite")
    marker = _keys(
        item,
        marker_fields,
        where,
    )
    for field in ("owner", "sector", "label", "description", "visibility", "confidence"):
        _text(marker[field], f"{where}.{field}")
    _identifier(marker["id"], f"{where}.id")
    if own_marker:
        _identifier(marker["cite"], f"{where}.cite")
    if marker["owner"] not in SIDES:
        raise MapError(f"{where}.owner must be nato or russia")
    if expected_owner and marker["owner"] != expected_owner:
        raise MapError(f"{where}.owner must be {expected_owner}")
    if marker["sector"] not in sectors:
        raise MapError(f"{where}.sector is not a public sector")
    if marker["visibility"] not in VISIBILITY:
        raise MapError(f"{where}.visibility is not an allowed value")
    if expected_visibility and marker["visibility"] != expected_visibility:
        raise MapError(f"{where}.visibility must be {expected_visibility}")
    if marker["confidence"] not in CONFIDENCE:
        raise MapError(f"{where}.confidence is not an allowed value")
    if own_marker and marker["confidence"] != "confirmed":
        raise MapError(f"{where}.confidence for own units must be confirmed")
    return marker


def validate_game(game: Any, base: dict[str, Any]) -> dict[str, Any]:
    game = _keys(
        game,
        {"version", "updated_at", "control", "zones", "master_markers", "own", "releases", "gm_notes"},
        "game",
    )
    if type(game["version"]) is not int or game["version"] < 1:
        raise MapError("version must be a positive integer")
    _validate_timestamp(game["updated_at"], "updated_at")
    sectors = {sector["id"] for sector in base["sectors"]}

    control = game["control"]
    if not isinstance(control, dict):
        raise MapError("control must be a TOML table")
    for sector, state in control.items():
        if sector not in sectors:
            raise MapError(f"control contains unknown sector {sector}")
        if not isinstance(state, str) or state not in CONTROL_STATES:
            raise MapError(f"control.{sector} is not an allowed control state")

    zones = _keys(game["zones"], set(SIDES), "zones")
    seen_zones: set[str] = set()
    for side in SIDES:
        zone = _list_of_strings(zones[side], f"zones.{side}")
        if not zone or any(sector not in sectors for sector in zone):
            raise MapError(f"zones.{side} must contain known sectors")
        if len(zone) != len(set(zone)) or seen_zones.intersection(zone):
            raise MapError("zone sectors must be unique and disjoint")
        seen_zones.update(zone)

    if not isinstance(game["master_markers"], list):
        raise MapError("master_markers must be an array of tables")
    marker_ids: dict[str, str] = {}
    for index, item in enumerate(game["master_markers"]):
        marker = _validate_marker(item, f"master_markers[{index}]", sectors, expected_visibility="master")
        if marker["id"] in marker_ids:
            raise MapError(f"duplicate master marker id {marker['id']}")
        marker_ids[marker["id"]] = marker["owner"]

    own = _keys(game["own"], set(SIDES), "own")
    for side in SIDES:
        if not isinstance(own[side], list):
            raise MapError(f"own.{side} must be an array of tables")
        ids: set[str] = set()
        for index, item in enumerate(own[side]):
            marker = _validate_marker(
                item,
                f"own.{side}[{index}]",
                sectors,
                expected_owner=side,
                expected_visibility=side,
                own_marker=True,
            )
            if marker["id"] in ids:
                raise MapError(f"duplicate own.{side} marker id {marker['id']}")
            ids.add(marker["id"])

    releases = _keys(game["releases"], set(SIDES), "releases")
    release_ids: set[str] = set()
    for side in SIDES:
        if not isinstance(releases[side], list):
            raise MapError(f"releases.{side} must be an array of tables")
        for index, item in enumerate(releases[side]):
            where = f"releases.{side}[{index}]"
            release = _keys(
                item,
                {
                    "release_id",
                    "marker_id",
                    "sector",
                    "confidence",
                    "label",
                    "description",
                    "released_at",
                    "source_id",
                    "visibility",
                },
                where,
            )
            for field in ("sector", "confidence", "label", "description"):
                _text(release[field], f"{where}.{field}")
            for field in ("release_id", "marker_id", "source_id"):
                _identifier(release[field], f"{where}.{field}")
            if release["release_id"] in release_ids:
                raise MapError(f"duplicate release id {release['release_id']}")
            release_ids.add(release["release_id"])
            if release["marker_id"] not in marker_ids or marker_ids[release["marker_id"]] == side:
                raise MapError(f"{where}.marker_id must identify an opposing master marker")
            if release["sector"] not in sectors:
                raise MapError(f"{where}.sector is not a public sector")
            if release["confidence"] not in CONFIDENCE:
                raise MapError(f"{where}.confidence is not an allowed value")
            if release["visibility"] not in VISIBILITY:
                raise MapError(f"{where}.visibility is not an allowed value")
            if release["visibility"] != side:
                raise MapError(f"{where}.visibility must be {side}")
            _validate_timestamp(release["released_at"], f"{where}.released_at")

    _list_of_strings(game["gm_notes"], "gm_notes")
    return game


def load_game(path: Path, base: dict[str, Any]) -> dict[str, Any]:
    try:
        with path.open("rb") as stream:
            parsed = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise MapError(f"cannot read game TOML: {error}") from error
    return validate_game(parsed, base)


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def check_paths(game_path: Path, output_path: Path) -> None:
    game_resolved = game_path.resolve(strict=True)
    output_resolved = output_path.resolve(strict=False)
    repo_resolved = ROOT.resolve(strict=True)
    if _inside(output_resolved, repo_resolved):
        raise MapError("--out must resolve outside the repository")
    if _inside(game_resolved, repo_resolved):
        if not _inside(game_resolved, repo_resolved / "tests" / "fixtures"):
            raise MapError("game file must be outside the repository")
        relative = game_resolved.relative_to(repo_resolved).as_posix()
        if relative != FIXTURE_PATH.as_posix():
            raise MapError("game file must be outside the repository")
        tracked = subprocess.run(
            ["git", "cat-file", "-e", f"HEAD:{relative}"],
            cwd=repo_resolved,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if tracked.returncode != 0:
            raise MapError("in-repository game files are allowed only as committed test fixtures")


def marker_records(game: dict[str, Any], side: str) -> list[dict[str, Any]]:
    """Return only friendly-side data and that side's explicit release records."""
    marker_owners = {marker["id"]: marker["owner"] for marker in game["master_markers"]}
    records = [
        {**marker, "kind": "friendly"}
        for marker in game["own"][side]
    ]
    records.extend(
        {**release, "owner": marker_owners[release["marker_id"]], "kind": "released"}
        for release in game["releases"][side]
    )
    return records


def visible_zones(game: dict[str, Any], side: str) -> dict[str, list[str]]:
    if side == "master":
        return game["zones"]
    if side not in SIDES:
        raise MapError("side must be nato, russia, or master")
    return {side: game["zones"][side]}


def visible_text_inputs(game: dict[str, Any], base: dict[str, Any], side: str) -> list[str]:
    """Expose dynamic strings approved for a view image or its caption."""
    if side == "master":
        records = [{**marker, "kind": "master"} for marker in game["master_markers"]]
    elif side in SIDES:
        records = marker_records(game, side)
    else:
        raise MapError("side must be nato, russia, or master")
    text = [
        *banner_lines(game, side),
        base["name"],
        base["river_name"],
    ]
    text.extend(f"{sector['id']} {sector['name']} {sector['terrain']}" for sector in base["sectors"])
    text.extend(approach["name"] for approach in base["approaches"])
    text.extend(objective["name"] for objective in base["objectives"])
    text.extend(f"{sector} {state.upper()}" for sector, state in game["control"].items())
    for item in records:
        text.append(f"{item['label']} {item['sector']} {item['confidence'].upper()}")
        if item["kind"] == "friendly":
            text.append(f"Cite: {item['cite']}")
        elif item["kind"] == "released":
            text.append(f"{item['release_id']}  {item['released_at']}")
            text.append(item["description"])
    return text


def banner_lines(game: dict[str, Any], side: str) -> tuple[str, str]:
    title = "GM MASTER - DO NOT POST" if side == "master" else f"{side.upper()} SIDE MAP"
    return (
        f"{title}  |  VERSION {game['version']}",
        f"Updated: {game['updated_at']}",
    )


CAPTION_LEGEND = "Legend: solid = CONFIRMED | outline = REPORTED | dashed ? = SUSPECTED"


def caption_text(game: dict[str, Any], side: str) -> str:
    """Phone-readable text layer built only from the side's own and release records."""
    if side not in SIDES:
        raise MapError("captions are only produced for nato or russia")
    lines = [f"v{game['version']} {side.upper()} {game['updated_at']}", CAPTION_LEGEND, "Markers:"]
    records = marker_records(game, side)
    lines.extend(_record_line(index, record, False) for index, record in enumerate(records, start=1))
    if not records:
        lines.append("None")
    lines.append("Released descriptions:")
    releases = game["releases"][side]
    lines.extend(f"{release['release_id']}: {release['description']}" for release in releases)
    if not releases:
        lines.append("None")
    return "\n".join(lines) + "\n"


def posting_manifest(out_dir: Path, version: int) -> list[tuple[Path, str]]:
    manifest: list[tuple[Path, str]] = []
    for side in SIDES:
        folder = out_dir / side
        manifest.extend(
            (
                (folder / f"v{version}-{side}.png", CHANNELS[side]),
                (folder / f"v{version}-{side}-caption.txt", CHANNELS[side]),
            )
        )
    manifest.append(
        (out_dir / "gm-master" / f"v{version}-GM-MASTER-DO-NOT-POST.png", CHANNELS["master"])
    )
    return manifest


def _font(size: int, bold: bool = False):
    from PIL import ImageFont

    candidates = (
        [
            "DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "arialbd.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
        ]
        if bold
        else [
            "DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "arial.ttf",
            r"C:\Windows\Fonts\arial.ttf",
        ]
    )
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            pass
    raise MapError("a TrueType font is required (DejaVu Sans or Arial)")


def _wrap(draw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _draw_confidence(
    draw, x: int, y: int, confidence: str, color: tuple[int, int, int], size: int = MARKER_GLYPH_PX
) -> None:
    if confidence == "confirmed":
        draw.ellipse((x, y, x + size, y + size), fill=color, outline=(20, 30, 40), width=2)
    elif confidence == "reported":
        draw.ellipse((x, y, x + size, y + size), fill=(250, 250, 244), outline=color, width=5)
    else:
        dash, gap = 6, 5
        for start in range(0, size, dash + gap):
            stop = min(start + dash, size)
            draw.line((x + start, y, x + stop, y), fill=color, width=3)
            draw.line((x + start, y + size, x + stop, y + size), fill=color, width=3)
            draw.line((x, y + start, x, y + stop), fill=color, width=3)
            draw.line((x + size, y + start, x + size, y + stop), fill=color, width=3)
        mark_font = _font(MIN_FONT_PX, bold=True)
        box = draw.textbbox((0, 0), "?", font=mark_font)
        draw.text(
            (x + (size - (box[2] - box[0])) / 2 - box[0], y + (size - (box[3] - box[1])) / 2 - box[1]),
            "?",
            fill=(20, 30, 40),
            font=mark_font,
        )


def _record_line(index: int, record: dict[str, Any], is_master: bool) -> str:
    """One marker-list entry; side views tag ownership as text, not color alone."""
    line = f"{index:02d}  {record['sector']}  {record['label']}  {record['confidence'].upper()}"
    if is_master:
        return f"{line}  {record['owner'].upper()}"
    if record["kind"] == "friendly":
        return f"{line}  OWN  CITE {record['cite']}"
    return f"{line}  OPP  {record['release_id']}  {record['released_at']}"


def render_png(game: dict[str, Any], base: dict[str, Any], side: str, destination: Path) -> None:
    from PIL import Image, ImageDraw

    navy = (24, 42, 59)
    text = (27, 39, 48)
    is_master = side == "master"
    records = (
        [{**marker, "kind": "master"} for marker in game["master_markers"]]
        if is_master
        else marker_records(game, side)
    )
    # Draw on a tall working canvas, then trim to the laid-out content height.
    image = Image.new("RGB", (CANVAS[0], 6000), (248, 247, 239))
    draw = ImageDraw.Draw(image)
    terrain_fill = {
        "open": (240, 235, 210),
        "road": (218, 210, 191),
        "broken": (215, 222, 197),
        "built": (222, 218, 211),
        "woods": (196, 216, 194),
    }
    side_colors = {"nato": (34, 91, 150), "russia": (152, 65, 52)}
    cell_bold = _font(CELL_TEXT_PX, bold=True)
    body_font = _font(26)
    body_bold = _font(26, bold=True)
    draw.rounded_rectangle((35, 24, 1565, 172), radius=18, fill=navy)
    banner_title, banner_updated = banner_lines(game, side)
    draw.text((65, 42), banner_title, fill="white", font=_font(43, bold=True))
    draw.text((67, 108), banner_updated, fill=(225, 235, 242), font=_font(28))
    draw.text((GRID_LEFT, 238), "NORTH: Pine Road (N)", fill=text, font=_font(26, bold=True))

    indexed_records: dict[str, list[tuple[int, dict[str, Any]]]] = {}
    for index, record in enumerate(records, start=1):
        indexed_records.setdefault(record["sector"], []).append((index, record))

    zone_for = {
        sector: zone_side
        for zone_side, sectors in visible_zones(game, side).items()
        for sector in sectors
    }
    sector_by_id = {sector["id"]: sector for sector in base["sectors"]}
    name_font = _font(32, bold=True)
    slot_width = MARKER_GLYPH_PX + 4 + draw.textbbox((0, 0), "00", font=cell_bold)[2] + 8
    for row in range(1, 6):
        for column_index, column in enumerate("ABCDEF"):
            sector_id = f"{column}{row}"
            sector = sector_by_id[sector_id]
            left = GRID_LEFT + column_index * CELL_WIDTH
            top = GRID_TOP + (row - 1) * CELL_HEIGHT
            right, bottom = left + CELL_WIDTH, top + CELL_HEIGHT
            fill = terrain_fill[sector["terrain"]]
            if sector_id in zone_for:
                zone_color = side_colors[zone_for[sector_id]]
                fill = tuple(round(fill[i] * 0.82 + zone_color[i] * 0.18) for i in range(3))
            draw.rectangle((left, top, right, bottom), fill=fill, outline=(78, 86, 88), width=2)
            if sector_id in zone_for:
                draw.rectangle(
                    (left + 4, top + 4, right - 4, bottom - 4),
                    outline=side_colors[zone_for[sector_id]],
                    width=3,
                )
            draw.text((left + 12, top + 8), sector_id, fill=navy, font=_font(36, bold=True))
            terrain_label = sector["terrain"].upper()
            terrain_width = draw.textbbox((0, 0), terrain_label, font=cell_bold)[2]
            draw.text((right - 12 - terrain_width, top + 14), terrain_label, fill=(55, 62, 60), font=cell_bold)
            control = game["control"].get(sector_id)
            if control:
                control_letter = {"nato": "N", "russia": "R", "contested": "C", "uncontrolled": "U"}[control]
                draw.rounded_rectangle((left + 72, top + 9, left + 106, top + 43), radius=5, fill=navy)
                letter_box = draw.textbbox((0, 0), control_letter, font=cell_bold)
                draw.text(
                    (left + 89 - (letter_box[0] + letter_box[2]) / 2, top + 26 - (letter_box[1] + letter_box[3]) / 2),
                    control_letter,
                    fill="white",
                    font=cell_bold,
                )
            name_y = top + 52
            for line in _wrap(draw, sector["name"], name_font, CELL_WIDTH - 22)[:2]:
                draw.text((left + 12, name_y), line, fill=text, font=name_font)
                name_y += 34
            cell_records = indexed_records.get(sector_id, [])
            overflow = len(cell_records) > CELL_MARKER_SLOTS
            shown = cell_records[: CELL_MARKER_SLOTS - 1] if overflow else cell_records
            marker_y = bottom - MARKER_GLYPH_PX - 10
            for slot, (record_index, record) in enumerate(shown):
                marker_x = left + 10 + slot * slot_width
                _draw_confidence(
                    draw,
                    marker_x,
                    marker_y,
                    record["confidence"],
                    side_colors.get(record["owner"], (67, 77, 86)),
                )
                draw.text(
                    (marker_x + MARKER_GLYPH_PX + 4, marker_y + 3),
                    f"{record_index:02d}",
                    fill=text,
                    font=cell_bold,
                )
            if overflow:
                draw.text(
                    (left + 10 + len(shown) * slot_width, marker_y + 3),
                    f"+{len(cell_records) - len(shown)}",
                    fill=text,
                    font=cell_bold,
                )

    river_y = GRID_TOP + 4 * CELL_HEIGHT
    draw.line((GRID_LEFT, river_y, GRID_LEFT + 6 * CELL_WIDTH, river_y), fill=(50, 117, 158), width=8)
    for crossing_column in (2, 3):
        center_x = GRID_LEFT + crossing_column * CELL_WIDTH + CELL_WIDTH // 2
        draw.line((center_x - 42, river_y, center_x + 42, river_y), fill=(70, 55, 41), width=14)

    text_width = 6 * CELL_WIDTH
    y = GRID_TOP + 5 * CELL_HEIGHT + 16

    def paragraph(value: str, font, gap: int = 12) -> None:
        nonlocal y
        line_height = draw.textbbox((0, 0), "Ag", font=font)[3] + 8
        for line in _wrap(draw, value, font, text_width):
            draw.text((GRID_LEFT, y), line, fill=text, font=font)
            y += line_height
        y += gap

    paragraph("SOUTH: River Road (S) | BLUEWATER RIVER: boundary between rows 4 and 5", body_bold)
    paragraph("WEST: West Approach (W) | EAST: East Road (E)", body_bold)
    paragraph("Crossings: C4-C5, D4-D5", body_font)
    paragraph(
        "Objectives: "
        + " | ".join(
            f"{objective['name']} ({'/'.join(objective['sectors'])})" for objective in base["objectives"]
        ),
        _font(24, bold=True),
        gap=24,
    )
    paragraph("TERRAIN: open | road | broken | built | woods", body_bold)

    legend_items = [
        ("confirmed", "CONFIRMED", (53, 92, 128)),
        ("reported", "REPORTED", (53, 92, 128)),
        ("suspected", "SUSPECTED", (53, 92, 128)),
    ]
    x = GRID_LEFT
    for confidence, label, color in legend_items:
        _draw_confidence(draw, x, y, confidence, color)
        draw.text((x + MARKER_GLYPH_PX + 10, y + 1), label, fill=text, font=body_bold)
        x += MARKER_GLYPH_PX + 10 + draw.textbbox((0, 0), label, font=body_bold)[2] + 40
    y += MARKER_GLYPH_PX + 18
    zone_sides = list(SIDES) if is_master else [side]
    x = GRID_LEFT
    for zone_side in zone_sides:
        draw.rectangle((x, y + 2, x + MARKER_GLYPH_PX, y + 2 + MARKER_GLYPH_PX), outline=side_colors[zone_side], width=4)
        zone_label = f"{zone_side.upper()} ZONE"
        draw.text((x + MARKER_GLYPH_PX + 10, y + 3), zone_label, fill=text, font=body_bold)
        x += MARKER_GLYPH_PX + 10 + draw.textbbox((0, 0), zone_label, font=body_bold)[2] + 40
    y += MARKER_GLYPH_PX + 22
    paragraph("CONTROL: N=NATO  R=RUSSIA  C=CONTESTED  U=UNCONTROLLED", body_bold, gap=24)

    if records:
        header = (
            "MARKERS (shape and status identify confidence)"
            if is_master
            else "MARKERS (shape = confidence | OWN = your side | OPP = released opposing report)"
        )
        paragraph(header, body_bold)
        list_font = body_font
        line_height = draw.textbbox((0, 0), "Ag", font=list_font)[3] + 8
        for index, record in enumerate(records, start=1):
            entry_top = y
            _draw_confidence(
                draw,
                GRID_LEFT,
                y,
                record["confidence"],
                side_colors.get(record["owner"], (67, 77, 86)),
            )
            entry_x = GRID_LEFT + MARKER_GLYPH_PX + 12
            lines = _wrap(draw, _record_line(index, record, is_master), list_font, text_width - MARKER_GLYPH_PX - 12)
            for line in lines:
                draw.text((entry_x, y), line, fill=text, font=list_font)
                y += line_height
            y = max(y, entry_top + MARKER_GLYPH_PX) + 8

    height = max(CANVAS[1], y + 24)
    image = image.crop((0, 0, CANVAS[0], height))
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG", optimize=False)


def render(game_path: Path, output_path: Path, check_only: bool = False) -> list[tuple[Path, str]]:
    check_paths(game_path, output_path)
    base = load_base()
    game = load_game(game_path, base)
    manifest = posting_manifest(output_path, game["version"])
    if not check_only:
        existing = [path for path, _ in manifest if path.exists()]
        if existing:
            raise MapError(
                "output already exists; increment the map version instead of replacing a prior export"
            )
        for side in SIDES:
            folder = output_path / side
            render_png(game, base, side, folder / f"v{game['version']}-{side}.png")
            (folder / f"v{game['version']}-{side}-caption.txt").write_text(
                caption_text(game, side), encoding="utf-8", newline="\n"
            )
        render_png(
            game,
            base,
            "master",
            output_path / "gm-master" / f"v{game['version']}-GM-MASTER-DO-NOT-POST.png",
        )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game", type=Path, help="private GM TOML game file, stored outside the repository")
    parser.add_argument("--out", required=True, type=Path, help="output directory outside the repository")
    parser.add_argument("--check", action="store_true", help="validate and print the posting manifest only")
    args = parser.parse_args(argv)
    try:
        manifest = render(args.game, args.out, check_only=args.check)
    except (MapError, OSError, subprocess.SubprocessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    for path, channel in manifest:
        print(f"{path} -> {channel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
