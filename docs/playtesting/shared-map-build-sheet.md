# Shared Map Build Sheet (Refs #15)

The [Brackenford map specification](../game-design/12-town-map-and-terrain-sectors.md)
is authoritative (map v1.0 in the
[packet manifest](human-playtest-packet-manifest.md)); this sheet only
implements it. A repository-built static PNG renderer is the **proposed**
method for issue #15, pending user confirmation and human verification; no
map or human access has been configured. If a rendering conflicts with the
source's ASCII grid or sector tables, correct the rendering and record the
correction against the time-stamped GM master. This proposal adds no game
mechanics and does not change the authority of doc 12.

## Reproduce the public base

1. The committed public definition is `data/map/base.toml`: a **six-column
   (`A`–`F`, west to east) by five-row (`1`–`5`, north to south)** grid, north
   at top, with edge-sharing adjacency only. It records each cell ID, name,
   terrain, the four approaches, river boundary and crossings, objectives,
   and control pairs. It does not reinterpret a cell as a precise position.
2. The map renderer builds separate master, NATO, and Russia PNGs from the
   public base and a private GM TOML file. The GM keeps that file outside the
   repository; it contains version/time, control, zones, live master markers,
   side-owned markers, GM notes, and a separate release record for each side.
   Give every side-owned marker a `cite` containing that side's own order or
   report ID. Each opposing release has a side-visible `release_id` and
   `released_at`; its `source_id` and `marker_id` remain private.
   A sector in `control` is an announced public state only; keep unannounced
   internal control assessments in GM notes, not in that public table.
   A side image reads opposing locations **only** from that side's release
   records. Updating a live marker does not move or refresh an already released
   report; stale reports remain stale. A report may have a different confidence
   for each side.
3. The public base is identical across outputs. Side PNGs contain only their
   own zone and markers plus the portion released to that side. A route or
   control-pair label does not by itself change control. The GM privately
   records approved starting placements and the initial map version before
   adding live force markers.

The GM machine is the user's PC, which has Python 3.12.10 available as
`py -3`; Pillow is not installed yet. Install the pinned renderer dependency
from the repository root with `py -3 -m pip install -r requirements-map.txt`.
The GM dry run still needs to confirm that rendering works on this machine.
In Command Prompt, from the repository root, create the private game file
outside the repository from the fictional fixture, then **replace all test
content** with approved live-game data before real use:

```text
mkdir "%USERPROFILE%\OliveDrabPrivate"
copy tests\fixtures\fictional-game.toml "%USERPROFILE%\OliveDrabPrivate\game.toml"
```

Keep all private paths outside the repository. After replacing the fixture's
test data, validate the game file and preview the five-entry posting manifest:

```text
py -3 scripts/render_map.py %USERPROFILE%\OliveDrabPrivate\game.toml --out %USERPROFILE%\OliveDrabPrivate\exports --check
```

If validation succeeds, render using the same inputs without `--check`:

```text
py -3 scripts/render_map.py %USERPROFILE%\OliveDrabPrivate\game.toml --out %USERPROFILE%\OliveDrabPrivate\exports
```

The output directory must resolve outside the repository, including through
symlinks, and the game file must also be outside the repository (except the
committed fictional test fixture). Write `updated_at` and each `released_at`
with the shared local time-zone offset (for example, `-07:00`). Each
side receives its own output folder, a PNG, and a text caption. Filenames
include only the map version and side; every PNG banner and caption carries
the matching version and update time. The tool refuses unknown fields,
visibility values, confidence values, and unearned opposing markers rather
than guessing. Do not place real personal data in the game file, fixtures, or
repository.
The [fictional test fixture](../../tests/fixtures/fictional-game.toml) is a
schema example for automated tests only; it is not a live game file.

| Row | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | A1 Pine Rise (woods) | B1 North (open) | C1 Old Quarry (broken) | D1 Old Quarry (broken) | E1 North (open) | F1 Pine Road (open) |
| 2 | A2 West Approach (open) | B2 West Verge (open) | C2 Mill Road (road) | D2 Mill Yard (built) | E2 East Verge (open) | F2 East Approach (open) |
| 3 | A3 South West (open) | B3 Orchard (broken) | C3 Market Square (built) | D3 Market Square (built) | E3 Station Street (built) | F3 Station Street (built) |
| 4 | A4 South Track (road) | B4 Orchard (road) | C4 Town Hall Quarter (built) | D4 Town Hall Quarter (built) | E4 East Blocks (built) | F4 East Blocks (built) |
| 5 | A5 South Woods (woods) | B5 South Fields (open) | C5 South Bank (open) | D5 South Bank (open) | E5 Fields (open) | F5 South Road (road) |

| Public feature | Exact location |
|---|---|
| Pine Road (N) | North approach; entry sectors A1, F1 |
| East Road (E) | East approach; entry sectors F2, F3, F4 |
| River Road (S) | South approach; entry sectors A5, F5 |
| West Approach (W) | West approach; entry sectors A2, A3, A4 |
| Bluewater River | Boundary between rows 4 and 5; difficult crossing routes C4–C5 and D4–D5 |
| Market Square | Central control pair C3 and D3 |
| Town Hall Quarter | Civic control pair C4 and D4 |
| Mill Road Junction | Northern route/approach pair C2 and D2 |
| Station Street | Eastern approach pair E3 and F3 |

Use the source's terrain categories: open, road, broken, built, woods,
and difficult crossing route. The two crossing routes are features between
sectors, not replacement terrain labels for their endpoint cells. Keep
control-pair labels distinct from the public control state issued by the GM.

## Views and updates

| View | Contents and boundary |
|---|---|
| GM master | All live master markers, both hidden starting zones, public control, version/time, and the GM's private working state. Keep the source TOML and master PNG in GM-controlled private storage. The Observer (if used) has read-only audit access to the actual channels; the GM master is never posted to a side channel. |
| NATO filtered | Public terrain/grid/approaches/objectives and public control; own zone and current friendly markers from NATO's own data, with each friendly marker's `cite` order/report ID; opposing positions only from NATO's released records, with side-visible `release_id` and `released_at`. Commander suspected-position notes, if used, remain in a separate private note/copy and do not alter the GM markers. No Russia zone, live master position, GM notes, opposing `marker_id`, private `source_id`, or master descriptions. |
| Russia filtered | Same public base and release boundary; own zone and current friendly markers from Russia's own data, with each friendly marker's `cite` order/report ID; opposing positions only from Russia's released records, with side-visible `release_id` and `released_at`. Separate commander notes are non-mechanical and never overwrite a GM marker. No NATO zone, live master position, GM notes, opposing `marker_id`, private `source_id`, or master descriptions. |
| Observer audit (only if Observer used) | The Observer has read-only access to the Discord channels needed for audit, including both side channels and `#gm-map-record`. The Observer never reveals master or opposing content to either commander. |

The GM updates and time-stamps the master first, then records separately for
each side the released sector, confidence, label/description, `released_at`,
and side-visible `release_id`. The side PNG shows these release IDs and times
plus each friendly marker's own `cite`; the text caption lists only released
descriptions. Neither output includes GM notes, opposing internal `marker_id`,
private `source_id`, or master descriptions. A `suspected` marker must represent a report actually released
to that side, not GM inference. The renderer never draws private content and
then hides or crops it. It renders each side from an allowlisted set of that
side's own data and release records.

## Proposed method, pending confirmation

This static renderer is proposed in issue #15; user confirmation is still
pending. It writes `nato/v{N}-nato.png` and
`nato/v{N}-nato-caption.txt` for the NATO private channel,
`russia/v{N}-russia.png` and `russia/v{N}-russia-caption.txt` for the Russia
private channel, and `gm-master/v{N}-GM-MASTER-DO-NOT-POST.png` for
`#gm-map-record`. Confirm and record the exact NATO and Russia Discord text
channel labels in the private setup record; the manifest's channel names must
match the real channel labels before use. The `GM-MASTER-DO-NOT-POST` file is
never for commander posting.

### Pre-post checklist

1. Run `--check` against the private game file and output path immediately
   before rendering. Read its five-entry manifest: NATO PNG and caption to
   `#nato-private`, Russia PNG and caption to `#russia-private`, and
   `GM-MASTER-DO-NOT-POST` to `#gm-map-record`. Confirm that those exact
   channel labels match the private setup record; resolve any mismatch before
   posting.
2. Render and post **one generated file at a time**, checking before each
   upload that **destination channel = banner side = filename side = map
   version** (and that each caption matches its paired PNG). Keep sides in
   separate folders; never multi-file drag or select from mixed folders.
   Upload the PNG and its caption file directly, not a screenshot, re-export,
   clipboard copy, or URL.
3. Post both sides' PNGs and captions at the same version before posting the
   master record.
4. Confirm the master file went **only** to `#gm-map-record`, never to a
   commander channel. The private master TOML and backup are not uploads.

If a file goes to the wrong channel, stop **all further posting** until the
GM ruling is recorded. Deletion is not a fix: record the time, content, and
who could see it; route the incident to the GM ruling process in
[doc 06](../game-design/06-prototype-operating-procedure.md). After the
ruling, correct and re-post at a **new map version**, never by editing an
image in place or reusing the compromised version.

The master TOML and dated master snapshots/backups stay in private storage
outside the repository and Discord. `#gm-map-record` is a posting destination,
not a backup. The renderer output and the private backup are separate things.
Use the [external setup checklist](external-setup-and-notification-checklist.md)
and record the method and result in the [final GM preflight](../game-design/16-final-gm-preflight-readiness-checklist.md).

## Human leak test and snapshots

Use fictional test markers and reports, not live hidden placements. The
static-renderer equivalents for the prior leak surfaces are: layers/objects
become renderer inclusion and filtering; share links become Discord
channel permissions; exports/downloads become the generated file and
caption; edit history becomes superseded Discord posts; screen sharing
remains a separate human check. Test with each commander's actual account
and confirm that a phone can display the PNG legibly; GM preview alone is
not proof.
Record each result as `PASS` or `FAIL` in issue #15 and the
[readiness guide section 3](human-playtest-readiness-guide.md), without
publishing private URLs, account identifiers, or unreleased map content.
Any `FAIL` blocks readiness until corrected and retested or an accepted
temporary workaround is documented.

| Test | Expected PASS | Expected FAIL |
|---|---|---|
| Grid and public base | All 30 IDs, names, terrain, approaches, crossings, river boundary, two control pairs and two approach pairs match doc 12 in all views | Any missing, changed, shifted, or extra feature |
| Render inclusion/filtering | Side image contains public base, its own markers, and only records explicitly released to that side; moving a live opposing marker does not update an older release | Live master location, other side's release, hidden zone, GM note, internal ID/source, or unearned marker is drawn or placed in rendered text |
| Discord channel permissions | Commander account can view only its own private channel; GM can view all; Observer (if used) can read all channels but cannot post; `#gm-map-record` is GM record-only | Commander can read opposing private channel or master record, or Observer can post |
| Generated files and captions | Each direct-upload file and caption has the same side/version as its banner and is posted to the matching channel; the master is confined to `#gm-map-record` | A mixed-side file/caption, private text, unearned state, or master file is posted to a side |
| Superseded Discord posts | Newer versions are identifiable; private master and backup remain outside Discord | A superseded post reveals unearned content or is treated as the only backup |
| Observer audit access (if used) | Observer can open the master and both filtered views but cannot edit, comment, share, or change any marker | Any edit or share action succeeds, or a view is missing |
| Screen sharing | Sharing the intended filtered window reveals only that view, with no master tab, notifications, thumbnails or private URLs | Master, other side, hidden state or private report appears on screen |

Record the following in the GM's
[final preflight completion fields](../game-design/16-final-gm-preflight-readiness-checklist.md)
and issue #15, without placing private links in the repository:

```text
Map version / update timestamp:
GM master view/location:
NATO filtered view/location:
Russia filtered view/location:
Observer audit access (if used):
Access list verified (roles only):
Snapshot method and format:
Dated master snapshot (scenario day/time and local date in private record):
Separate access-controlled backup location:
Backup and restore check result:
Leak-test results and retest reference:
```

At the initial approved version and after each material map update, the GM
time-stamps the master, captures a dated master snapshot and the two permitted
filtered outputs, stores the master snapshot and a backup in separate
access-controlled private storage outside Discord, and checks that a restore
preserves the version and information boundaries. A commander export and
`#gm-map-record` are never a master backup.

Use this repository record template for the proposal and the [final GM
preflight completion fields](../game-design/16-final-gm-preflight-readiness-checklist.md)
for readiness. Store any private file path or access details only in the GM's
private records, never in the repository:

```text
Renderer version / map version / update time:
Private master TOML and snapshot location:
NATO output/channel (exact Discord label):
Russia output/channel (exact Discord label):
Master output/channel: #gm-map-record
Python 3.12.10 / `py -3` GM-machine dry run:
Phone readability check:
Commander account channel-boundary checks:
Observer read-only check (if used):
Private backup and restore result:
Leak-test results and incident reference:
```

Human verification and GM sign-off are still pending; issue #15 remains an
external prerequisite.
