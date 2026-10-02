# Shared Map Build Sheet (Refs #15)

The [Brackenford map specification](../game-design/12-town-map-and-terrain-sectors.md)
is authoritative (map v1.0 in the
[packet manifest](human-playtest-packet-manifest.md)); this sheet only
implements it. No platform is selected and
no map or human access has been configured. If a rendering conflicts with
the source's ASCII grid or sector tables, correct the rendering and record
the correction against the time-stamped GM master.

## Reproduce the public base

1. The user creates a **six-column (`A`–`F`, west to east) by five-row
   (`1`–`5`, north to south)** sector grid, north at top, with edge-sharing
   adjacency only. Copy each cell ID, name, and terrain below exactly; do not
   reinterpret a cell as a precise position.
2. Add the north arrow, named edge approaches, Bluewater River boundary
   between rows 4 and 5, and the two difficult crossing routes `C4–C5` and
   `D4–D5`. Mark all four control pairs below. Compare the result directly
   with the source ASCII diagram and sector tables before adding state.
3. Create a separate GM master and two filtered commander views. Keep the
   public base identical in all three. Do not place live force markers before
   the GM privately records approved starting placements and the initial map
   version. A route or a control-pair label does not by itself change control.

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
| GM master | All force locations and strength, both hidden starting zones, orders/readiness/supply notes, conditions and unresolved rulings, current and stale reports, control, map version and information-release log. GM-only access. |
| NATO filtered | Public terrain/grid/approaches/objectives and public control updates; own zone and current friendly markers/status/orders/readiness/supply, own observations and information earned from confirmed or reported releases. Opposing positions appear only when earned. Commander annotations of uncertain positions are clearly `suspected` and separate from confirmed markers. No Russia zone or private reports. |
| Russia filtered | Same public base and release rules; own zone and current friendly markers/status/orders/readiness/supply, own observations and earned releases. Opposing positions appear only when earned. Uncertain commander annotations are clearly `suspected`, never overwriting confirmed markers. No NATO zone or private reports. |

The GM updates and time-stamps the master first, then publishes only the
portion earned by each side, with the operating procedure's `confirmed`,
`reported`, or `suspected` confidence label and the source report/order ID.
Replace superseded friendly markers, not the audit record. Do not copy a
stale opposing report or GM-only condition into a filtered view. Each view
shows its version/update timestamp; restricted notes and share links stay
out of the public feed and other side's view.

## Platform comparison, without a recommendation

| Option | Useful affordance | Leak and maintenance risk to test |
|---|---|---|
| Shared spreadsheet | Explicit 30-cell table, formulas/timestamps, easy dated copies | Hidden sheets, protected ranges, formulas, comments, edit history and whole-workbook export may reveal master or opposing data; separate files and access grants may be necessary. |
| Drawing/whiteboard tool | Clear visual labels, movable markers, separated boards/layers | Hidden layers, frames, previews, object metadata, share links and full-board export can expose concealed content; accidental screen share may show the master. |
| Virtual tabletop (VTT) | Map markers, tokens, role views and snapshots | GM overlays, token properties, fog/layer settings, player permissions, exports and history may expose hidden state; test the actual player account, not only GM preview. |

The user chooses and records a platform and access arrangement in issue #15
and [external setup](external-setup-and-notification-checklist.md). Dev/QA
checks the finished views against this sheet and the source, not a preferred
vendor.

## Human leak test and snapshots

Use fictional test markers and reports, not live hidden placements. For each
side, test from that side's actual access identity, plus a fresh viewer of
each share link and a screen-share recipient; GM preview alone is not proof.
Record each result as `PASS` or `FAIL` in issue #15 and the
[readiness guide section 3](human-playtest-readiness-guide.md), without
publishing private URLs, account identifiers, or unreleased map content.
Any `FAIL` blocks readiness until corrected and retested or an accepted
temporary workaround is documented.

| Test | Expected PASS | Expected FAIL |
|---|---|---|
| Grid and public base | All 30 IDs, names, terrain, approaches, crossings, river boundary and four pairs match doc 12 in all views | Any missing, changed, shifted, or extra feature |
| Layers/objects | NATO/Russia see only own zone, markers/status and earned releases; hidden layers, object metadata, formulas and stale reports stay inaccessible | Master, other zone/marker/report, GM condition or stale private state exposed by toggling or inspecting |
| Share links/permissions | Side link opens only that side's view for its intended identity; unauthorized or anonymous recipient cannot open master/other view | Link forwards or role inheritance expose any unearned content |
| Exports/downloads/print | Side export, preview, download, and print contain only that side's permitted view | Master, hidden layer, notes or other side's data appears anywhere in output |
| Version/edit history | Side can read its current version/time but cannot recover master or opposing state through history, comments, undo, deleted items or old links | Any unearned or stale private content recoverable |
| Screen sharing | Sharing the intended filtered window reveals only that view, with no master tab, notifications, thumbnails or private URLs | Master, other side, hidden state or private report appears on screen |

Record the following in the GM's
[final preflight completion fields](../game-design/16-final-gm-preflight-readiness-checklist.md)
and issue #15, without placing private links in the repository:

```text
Map version / update timestamp:
GM master view/location:
NATO filtered view/location:
Russia filtered view/location:
Access list verified (roles only):
Snapshot method and format:
Dated master snapshot (scenario day/time and local date in private record):
Separate access-controlled backup location:
Backup and restore check result:
Leak-test results and retest reference:
```

At the initial approved version and after each material map update, the GM
time-stamps the master, captures a dated master snapshot and the two permitted
filtered outputs, stores the master and backup in separate access-controlled
locations, and checks that a restore preserves the version and information
boundaries. A commander export is never a master backup. Human verification
and GM sign-off are still pending; issue #15 remains an external prerequisite.
