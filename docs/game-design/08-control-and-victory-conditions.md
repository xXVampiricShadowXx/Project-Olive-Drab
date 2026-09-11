# Control and Victory Conditions

These are draft conditions for the first town-control scenario. They are intentionally easy to observe and adjudicate. They should be tested before adding broader political, economic, or intelligence objectives.

## Control state

The Brackenford map defines control at the sector and control-pair level. The GM records the authoritative state on the master map and derives the town result from the named objective locations in [Town Map and Terrain Sectors](12-town-map-and-terrain-sectors.md).

- **Market Square:** `C3` and `D3` form the central control pair. A side controls the pair only when it has a **credible infantry presence** in both sectors. A credible infantry presence is an eligible force marker that is not **broken**, has not formally **withdrawn** from the scenario, and is actually occupying the named sector at the time of the control check. A **depleted** or **shaken** force remains eligible to count as present. If both sides have eligible force markers in the pair, the pair is contested and is not controlled by either side. If neither side has an eligible presence in both sectors, the pair is not controlled by either side.
- **Town Hall Quarter:** `C4` and `D4` form the civic control pair. A side controls the pair only when it has a **credible infantry presence** in both sectors. A credible infantry presence is an eligible force marker that is not **broken**, has not formally **withdrawn** from the scenario, and is actually occupying the named sector at the time of the control check. A **depleted** or **shaken** force remains eligible to count as present. If both sides have eligible force markers in the pair, the pair is contested and is not controlled by either side. If neither side has an eligible presence in both sectors, the pair is not controlled by either side.
- **Mill Road Junction:** `C2` and `D2` are an approach objective and observation position, but are not sufficient for town control by themselves.
- **Station Street:** `E3` and `F3` are an approach objective and observation position, but are not sufficient for town control by themselves.

A side controls the **town** only when it controls **both central control pairs** (`C3/D3` and `C4/D4`) and no opposing **eligible force marker** is contesting any required sector. An empty required sector does not by itself make a pair contested; it simply prevents that pair from being controlled. Town control therefore requires a complete, uncontested infantry presence across all four central sectors.

Control is one of three states:

- **Controlled:** One side controls both central control pairs and no opposing **eligible force marker** contests a required sector.
- **Contested:** At least one central control pair is contested by opposing **eligible force markers**, so the town cannot be controlled while that contest remains.
- **Uncontrolled:** Neither side currently controls the town and no central control pair is actively contested.

A side does not gain control merely by submitting an order, observing a location, occupying an approach objective, or damaging an opposing force marker. A capture attempt becomes effective when the game master resolves the action and updates the authoritative map state.

## Primary result for the first human test

The first human test runs only through **Day 1's active window, 08:00–22:00**. At the end of that window, the game master checks the town's control state:

- **Town controlled:** The controlling side wins the primary objective.
- **Town contested:** The scenario ends in a draw on the primary objective; the game master reports which side has the stronger position as a **non-authoritative narrative result**, not as a win.
- **Town uncontrolled:** Neither side wins the primary objective.

The first human session ends after this final control-state check. It does not continue into additional scenario days merely to exercise the broader seven-day campaign clock.

## Primary result for the broader prototype

The broader prototype remains compatible with a seven-day scenario. When a multi-day test is actually run, the primary deadline is the end of **Day 7's active window**:

- **Town controlled:** The controlling side wins the primary objective.
- **Town contested:** The scenario ends in a draw on the primary objective; the game master reports which side has the stronger position as a **non-authoritative narrative result**, not as a win.
- **Town uncontrolled:** Neither side wins the primary objective.

For the first human test, a company is considered **unable to field** when every one of that company's recorded echelon subordinate units is either **broken** or has a recorded **formal withdrawal from the scenario**. This condition is derived from the existing subordinate-unit states; it does not create a separate company strength state. If all recorded echelons meet that condition, the company is treated as eliminated or formally withdrawn for the immediate-victory check. Otherwise, the company remains fieldable for this purpose.

If one side is unable to field an infantry company under that definition, the other side wins immediately only if it controls the town. Otherwise, play continues until the applicable deadline for that test.

## Optional secondary conditions for testing

Use no more than one secondary condition in an early playtest. Possible choices are:

- **Preservation:** A side that controls the town while retaining more of its starting company receives the **stronger narrative outcome**.
- **Evacuation:** A side that cannot win control can still achieve a successful withdrawal if its surviving force exits through the designated edge before the applicable deadline.
- **Information discipline:** The game master records whether a side made a decision from a confirmed report or a suspected report. This is an observation for playtesting, not a score.

Secondary conditions must never override the clearly stated primary objective during the first test.

## End-of-scenario procedure

When the applicable deadline or an immediate ending condition is reached, the game master:

1. Stops all timers.
2. Resolves any action that completed before the exact deadline. Any contact or contested action still unresolved at the exact **22:00 first-test boundary** produces no new post-deadline result; its last authoritative state remains the state used for the final control-state check, and the affected order/contact remains recorded as unresolved at session close.
3. Records the final master-map state.
4. Checks the primary condition, then any selected secondary condition.
5. Sends both commanders the same public result and their final private status.
6. Preserves the order, report, and map logs for the playtest review.

## Fairness safeguards

- The victory test is published before the first order is submitted.
- The game master uses the same definition of presence, contest, and control for both sides.
- A control change is time-stamped and linked to the order or adjudication that caused it.
- If an ambiguous edge case can change the result, the game master states the temporary interpretation before resolving it and records it for review.
- Players may challenge a ruling for the post-game record, but a challenge does not pause the live clock.

The prototype does not score advanced intelligence, cyberwarfare, vehicle operations, air support, or national-level objectives. Those systems can be evaluated only after the infantry-only control loop is understandable and repeatable.
