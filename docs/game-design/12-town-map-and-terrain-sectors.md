# Town Map and Terrain Sectors

This is the first playable town map specification. It is intentionally abstract: the
map supports movement, observation, control, and hidden starting positions without
requiring a detailed real-world map or a scale model.

## Map identity and conventions

- **Town:** Brackenford
- **Grid:** Six columns (`A`–`F`) west to east and five rows (`1`–`5`) north to
  south. A cell is a named sector, not a precise position.
- **North:** The top of the diagram is north. The GM may rotate or redraw the map
  only if the grid labels and named approaches remain unchanged.
- **Adjacent:** Sectors sharing an edge are adjacent. Diagonal movement is not
  adjacent and requires a route through an edge-sharing sector.
- **Routes:** A route is a sequence of adjacent sectors. Roads affect movement time;
  they do not guarantee safety or control.
- **Edges:** The north, east, south, and west map edges are named approaches and are
  the only off-map entry or exit points for the first test.
- **Force markers:** Put a force marker in the sector it occupies. If a force marker
  is moving between sectors, the GM records the current sector and next sector in
  the order register; do not create an unruled halfway position.

## Future continuous-playspace model

The final game is intended to use a continuous playspace. Forces should be able to
occupy positions and move freely rather than snapping to map cells or treating
sector edges as physical barriers. A military-style coordinate and reference grid,
potentially an MGRS-like system, should support reports, orders, and the location of
terrain features, units, and objectives. Those references identify positions;
they do not define movement cells, impose hard boundaries, or replace route and
terrain judgments.

The Brackenford 6-by-5 sector grid remains authoritative for the Phase 3
prototype. It is a deliberate simplification that makes a first live, flexible-
attention playtest easy to run with a shared digital map, limited force markers, and
consistent timing. The sector grid should therefore be treated as named areas and
reference anchors for this test, not as a commitment to the final movement model.
Any future continuous map must preserve the prototype's named features, objectives,
information boundaries, and reporting clarity while allowing finer positions.

## Text map

```text
                         NORTH: Pine Road (N)
              A              B              C              D              E              F
        +--------------+--------------+--------------+--------------+--------------+--------------+
  1     | A1 Pine Rise | B1 North     | C1 Old Quarry| D1 Old Quarry| E1 North     | F1 Pine Road |
        |    (woods)   |    Fields    |    (broken)  |    (broken)  |    Fields    |    (open)   |
        +--------------+--------------+--------------+--------------+--------------+--------------+
  2     | A2 West      | B2 West      | C2 Mill      | D2 Mill      | E2 East      | F2 East      |
        |    Approach  |    Verge     |    Road      |    Yard      |    Verge     |    Approach |
        |    (open)    |    (open)    |    (road)    |    (built)   |    (open)    |    (open)   |
        +--------------+--------------+--------------+--------------+--------------+--------------+
  3     | A3 South     | B3 Orchard  | C3 Market    | D3 Market    | E3 Station   | F3 Station   |
        |    West      |    (broken)  |    Square    |    Square    |    Street    |    Street    |
        |    (open)    |    (broken)  |    (built)   |    (built)   |    (built)   |    (built)  |
        +--------------+--------------+--------------+--------------+--------------+--------------+
  4     | A4 South     | B4 Orchard  | C4 Town Hall | D4 Town Hall | E4 East      | F4 East      |
        |    Track     |    (road)   |    Quarter   |    Quarter   |    Blocks    |    Blocks    |
        |    (road)    |    (road)   |    (built)   |    (built)   |    (built)   |    (built)  |
        +--------------+--------------+--------------+--------------+--------------+--------------+
                 Bluewater River: boundary between rows 4 and 5
  5     | A5 South    | B5 South   | C5 South     | D5 South     | E5 Fields    | F5 South    |
        |    Woods    |    Fields   |    Bank       |    Bank       |    (open)    |    Road      |
        |    (woods)  |    (open)   |    (open)     |    (open)     |    (open)    |    (road)   |
        +--------------+--------------+--------------+--------------+--------------+--------------+
                         SOUTH: River Road (S)
```

The ASCII diagram and the sector tables in this document are the authoritative map
specification. A player-facing implementation must reproduce them rather than
silently changing geometry, labels, adjacency, route features, or objective
locations.

## Shared digital map implementation

For the first playtest, prepare a shared digital map from the authoritative ASCII
specification. Do not choose a platform as part of the rules packet. A suitable
implementation may be a shared drawing, board, spreadsheet, or other tool, provided
the GM can maintain the authoritative state and each commander can receive only
their permitted view.

The digital map should provide:

- A visible six-column by five-row grid with the exact cell IDs and sector names.
- A persistent north arrow, approach labels, terrain labels, and control-pair
  markers.
- Separate GM master state and filtered commander views, whether implemented as
  separate boards, layers, exports, or screens.
- Moveable friendly force-marker positions, a way to show public control state,
  and a separate place for suspected enemy markers.
- A map version or update timestamp so a commander can tell which view is current.
- An export or snapshot method for the dated master-map record.

The GM should build and test the shared map before the scenario starts:

1. Reproduce the ASCII grid exactly and compare every cell against the sector table.
2. Add the public terrain, approaches, objectives, and control-pair labels.
3. Create the master state and one filtered starting view per commander.
4. Verify that hidden force markers, hidden zone boundaries, GM-only conditions, and stale
   reports cannot appear in the other side's view.
5. Place no live force markers until the GM has recorded the approved private starting
   placements and the initial map version.

The digital map is a presentation and record-keeping layer, not a new rules
authority. If the digital view conflicts with the ASCII specification or the
time-stamped master record, the GM corrects the digital view and records the
correction. A platform decision and any access-control details belong in the
pre-play setup record, not in this map specification.

## First-playtest communication implementation

The first playtest uses a Discord server for game communication. Discord is a
delivery platform, not a change to the map rules or information model. The server
must implement the existing role-based structure with GM visibility:

- A public group channel for non-sensitive game communication and public updates.
- Private, GM-visible channels for each commander and the role-based superior or
  subordinate communication paths used by the scenario.
- A GM-visible channel or approved procedure for any opposing-side contact.
- No use of personal direct messages for orders, reports, map updates, or rulings.

For this first prototype, each commander is the highest player-controlled role on
their side. Therefore, **opposing-player contact requires GM approval and GM
visibility; superior permission is required only where a higher player-controlled
role actually exists.** This avoids making opposing contact impossible in the
three-person prototype while preserving the intended chain-of-command restriction
for future multi-level tests.

The channel structure and information boundaries are authoritative. The GM must
confirm channel permissions before play and record the channel names in the setup
record. A Discord channel must not expose the master map, hidden starting zones,
GM-only conditions, or another side's private reports. The shared digital map may
use Discord or another tool, but its access rules must match the master-map and
filtered-view rules above.

## Named sectors and terrain categories

Use six terrain categories and features so the existing timing aid can be applied
consistently:

| Category | Sectors | Default movement aid | Observation/use |
|---|---|---:|---|
| Open | B1, E1, F1, A2, B2, E2, F2, A3, B5, E5 | 30 min | Long sight lines unless blocked by a town or weather condition |
| Road | C2, A4, B4, F5 | 30 min | Known route; road movement does not remove opposition or observation risk |
| Broken | C1, D1, B3 | 45 min | Orchards, quarry margins, and scattered obstacles limit observation |
| Built | D2, C3, D3, E3, F3, C4, D4, E4, F4 | 60 min | Dense town movement; observation is sector-limited unless the GM rules otherwise |
| Difficult crossing route | C4–C5, D4–D5 | 60 min | Bluewater River crossings; use the difficult-crossing guidance and adjudicate opposition |
| Woods | A1, A5 | 45 min | Concealment is stronger; observation across or through the sector is limited |

If a future redraw gives a sector more than one terrain label, the more restrictive
category applies to the action. The GM records that interpretation rather than
adding a new terrain type.

## Approaches and route choices

The four named approaches create different tradeoffs without giving either side a
free route to the objective:

| Approach | Entry sectors | Character | Primary tradeoff |
|---|---|---|---|
| Pine Road (N) | A1, F1 | Woods at the west end, open fields at the east end | Concealment versus long observation |
| East Road (E) | F2, F3, F4 | Open approach into built streets | Fast access but easy to observe |
| River Road (S) | A5, F5 | Woods and fields with Bluewater River crossings at the row 4/5 boundary | Broad frontage, but the crossings are slow and vulnerable |
| West Approach (W) | A2, A3, A4 | Open edge feeding the mill and orchard | Several routes, but little concealment before town |

The named roads and approaches are reference features for orders and reports. They
do not imply that a force marker controls an entire edge by occupying one sector.

## Objectives and control locations

The primary objective is **Brackenford town control**. The GM tracks control at the
sector level and derives the town result from these locations:

- **Market Square:** C3 and D3 are the central control pair. A side must hold both
  sectors. If both sides have eligible forces in the pair, the pair is contested;
  if neither side has an eligible presence in both sectors, the pair is not
  controlled by either side.
- **Town Hall Quarter:** C4 and D4 are the civic control pair. A side must hold both
  sectors. If both sides have eligible forces in the pair, the pair is contested;
  if neither side has an eligible presence in both sectors, the pair is not
  controlled by either side.
- **Mill Road Junction:** C2 and D2 are the northern route pair. They are an
  approach objective and a useful observation position, but they are not sufficient
  for town control by themselves.
- **Station Street:** E3 and F3 are the eastern approach pair. They are an
  approach objective and a useful observation position, but they are not sufficient
  for town control by themselves.

For the first scenario, the town is **controlled** only when one side has a credible
infantry presence in both central control pairs (C3/D3 and C4/D4), with no opposing
force marker contesting any required sector. If either side occupies a required sector
against an opposing force, the affected control pair is contested and the town is
not controlled by either side. An empty required sector does not by itself create a
contested result.

The GM may mark a central pair as uncontrolled when neither side has an eligible
presence in either required sector. Control changes are time-stamped and reported to both commanders.

## Balanced asymmetric hidden starting zones

The GM selects one zone for each side before the commander chooses force-marker placement.
The zones are asymmetric in terrain and approach, but balanced by access to the
town, concealment, and route options:

- **NATO zone:** `A1`, `A2`, `B1`, `B2`, and `A3`. This zone offers covered western
  and northern approaches, strong observation from open ground, and fewer sectors
  for spreading the smaller company.
- **Russia zone:** `E1`, `E2`, `F1`, `F2`, `F3`, and `F4`. This zone offers more
  frontage and direct eastern access, but more movement through observable open and
  built sectors.

The GM may swap the side assignments for a repeat test, but must publish the zone
shapes and reason for the swap before placement. Each commander may distribute
their company's force markers anywhere inside their own zone, subject to the existing
fairness check:

- No starting force marker may begin in a central control pair.
- A company may not begin with its entire force in one sector unless the GM
  records why that is fair and both sides receive an equivalent opportunity.
- The GM must give each side at least two plausible first routes toward the town.
- The GM records starting readiness and strength privately before the shared clock
  starts.

These are permitted starting areas, not guaranteed safe areas. The GM may place
scenario information or non-player conditions outside them only on the master map.

## Information layers

The master map is authoritative. The GM maintains three information layers:

| Information | Master map | NATO commander view | Russia commander view |
|---|---|---|---|
| All force-marker locations and strength | Yes | No | No |
| Own current force-marker locations, orders, readiness, and supply notes | Yes | Yes | Yes |
| Opposing location | Yes | Only when earned by confirmed or reported information | Only when earned by confirmed or reported information |
| Control state of every sector | Yes | Public control updates plus own observations | Public control updates plus own observations |
| Hidden starting-zone boundaries | Yes | NATO zone only | Russia zone only |
| Terrain, grid, named sectors, and public approaches | Yes | Yes | Yes |
| GM-only conditions, unresolved rulings, and stale reports | Yes | Only the portion released to that side | Only the portion released to that side |

Commanders may annotate suspected positions on their own filtered map, but those
annotations must be labeled **suspected** and never overwrite a confirmed marker.
The GM updates the master map first, then creates side-specific updates using the
report confidence labels from the operating procedure.

## GM preparation and conversion checklist

Before play, the GM should:

1. Reproduce the grid and named sectors on paper or in a shared document.
2. Mark terrain categories and the four approach names.
3. Mark the two central control pairs and the two approach pairs.
4. Hide the two starting zones and record each commander's approved placement.
5. Prepare one filtered starting map per commander with only their zone, public
   terrain, their own force markers, and the published objective.
6. Keep the full map, hidden conditions, all force markers, and the information-release
   log on the master map.

The first test uses a shared digital map prepared from the ASCII layout and tables
above. A later visual asset may improve presentation, but it must preserve this
specification and cannot replace the GM's master record.
