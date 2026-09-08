# Prototype Operating Procedure

This document is the game master's runbook for the first asynchronous campaign. It is written so a new group can understand what happens during an active day, what happens at night, and how a player can participate without being online continuously.

## Campaign clock

The prototype uses one shared local time zone and a seven-day scenario clock.

- **Active window:** 08:00–22:00. Orders may be submitted, acknowledged, and resolved. Movement, observation, combat, and other permitted actions continue according to their stated times.
- **Frozen window:** 22:00–08:00. The clock advances to 08:00, but no new player action resolves and no action timer counts down. The game master may prepare records and private notes, but does not create a new operational result during the freeze.
- **Daily boundary:** At 22:00, the game master records every in-progress order, its remaining time, and its current conditions. At 08:00, those orders resume with the same remaining time unless a written scenario rule says otherwise.

The schedule is a pacing aid, not a reason to punish players for sleeping. A player who misses an active window may submit an order for the next available processing period.

## Order lifecycle

Every action that can change the shared situation uses the same short lifecycle:

1. **Draft:** The commander writes the order using the standard fields: unit, action, destination or target, purpose, start condition, and any limits.
2. **Submitted:** The commander sends the order to the game master through the agreed channel. The submission time is recorded in the shared log.
3. **Acknowledged:** The game master confirms that the order is legible, identifies the unit and intended action, and states whether anything is missing. Acknowledgment is not approval and does not reveal hidden information.
4. **Accepted or returned:** A complete order is accepted for processing. An incomplete, impossible, or contradictory order is returned with one clear question; its timer does not start until the commander resubmits it.
5. **In progress:** The game master records the start time, expected completion time, route or target, and any conditions that can interrupt it. The commander may clarify an order, but a changed objective is a new order.
6. **Resolved:** The game master updates the master map, affected status, and any reports. The commander receives the information their side could know.

Commanders should submit one purpose per order. Short, explicit orders are easier to acknowledge and less likely to be interpreted differently between sessions.

### Minimum order form

```text
Order ID:
Submitted at:
Unit:
Action:
Destination or target:
Purpose:
Start condition:
Route or formation:
Limits (engage, halt, withdraw, or avoid):
Commander:
```

The game master may assign the next sequential order ID if a commander does not provide one.

## Game-master active-window workflow

At the start of an active window, the game master:

1. Publishes the current public clock and any scheduled environmental change.
2. Reconciles the previous day's in-progress orders with the master log.
3. Sends each commander their private status and reports.
4. Lists orders awaiting clarification or acknowledgment.

During the active window, the game master:

1. Time-stamps new submissions in arrival order.
2. Acknowledges or returns each order promptly.
3. Starts routine timers and resolves completed actions.
4. Interrupts a timer when contact, a blocked route, or another contested condition occurs.
5. Adjudicates contested movement, combat, captures, and unusual cases.
6. Sends reports as soon as the relevant side could reasonably receive them.
7. Updates the master map first, then produces filtered commander-map updates.

At the end of an active window, the game master:

1. Stops all active timers at 22:00.
2. Records each order's remaining time and current condition.
3. Publishes the public end-of-day note and any control changes.
4. Stores the authoritative log and a backup copy before the freeze.

## Reports and map updates

The master map is the source of truth. A commander receives a filtered map or update sheet, never the master map.

Each report should include:

- Report ID and time observed.
- Reporting unit or source.
- Location or area, using the map grid or named feature.
- What was observed, including uncertainty.
- When the information may be stale.
- Any immediate action or decision required.

Use plain confidence labels: **confirmed**, **reported**, or **suspected**. A suspected location may guide a commander's plan but cannot be treated as a confirmed enemy position.

The game master issues a commander-map update when a friendly unit moves, a known condition changes, a report changes the side's usable information, or control of a location changes. Each update replaces the previous marker and cites the order or report that caused it.

## Separate sessions and continuity

The campaign is asynchronous, but it has one authoritative operational record. The game master keeps:

- A master clock log with active/frozen boundaries.
- An order register containing every order, status, timer, and result.
- A master map version or dated snapshot.
- A report register showing which side received each report and when.
- A short decisions log for temporary rulings and unresolved questions.

When a commander joins from a separate session, the game master sends a compact handoff containing the current time, friendly status, known reports, in-progress orders, pending decisions, and the next deadline. The commander confirms receipt before issuing a new order. The handoff does not include information that role has not earned.

If records conflict, the latest time-stamped master log and map snapshot take precedence. The game master announces the correction, preserves the earlier entry for auditability, and applies the same correction standard to both sides.

## Fairness and continuity rules

- The same timing aid and adjudication principle applies to equivalent actions by both sides.
- A commander may correct an unclear order before it starts, but may not rewrite an action after learning its result.
- A player who was offline does not gain retroactive knowledge; they receive the same handoff their role would have received.
- Rules questions are logged and answered with a temporary ruling so play can continue.
- Temporary rulings are reviewed after the scenario, not repeatedly reopened during the active clock.

Advanced intelligence, cyberwarfare, vehicles, air support, and other expansion systems are outside this procedure. The prototype uses observation, written reports, infantry movement, and game-master adjudication only.
