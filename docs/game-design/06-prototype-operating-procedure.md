# Prototype Operating Procedure

This document is the game master's runbook for the first live, supervised campaign. It is written so a new group can understand what happens during an active day, what happens at night, and how the game handles a player who is temporarily unavailable.

## Campaign clock

The prototype uses one shared local time zone and a seven-day scenario clock.

- **Active window:** 08:00–22:00. Orders may be submitted, acknowledged, and resolved. Movement, observation, combat, and other permitted actions continue according to their stated times.
- **Frozen window:** 22:00–08:00. The clock advances to 08:00, but no new player action resolves and no action timer counts down. The game master may prepare records and private notes, but does not create a new operational result during the freeze.
- **Daily boundary:** At 22:00, the game master records every in-progress order, its remaining time, and its current conditions. At 08:00, those orders resume with the same remaining time unless a written scenario rule says otherwise.

The clock remains live during the active window, but player attention is flexible rather than continuously online. Players may check in briefly from work or another obligation, submit orders, receive GM notifications or situation reports, or remain immersed for longer periods. The GM continues processing accepted orders and events even when a player is away. The schedule is a pacing aid, not a reason to punish players for sleeping.

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

### Urgent decisions and response windows

An urgent report or decision request must include a response-by time. The GM sends it through the role-based game channel and records when it was delivered. A player may respond with a decision, a standing instruction, or an explicit request for more time.

If the response window expires, the GM uses the last accepted order and any standing limits or fallback instruction already recorded for that unit. If no safe fallback exists, the GM pauses only that decision, takes the least-committal action consistent with the unit's last accepted order, and records the reason. The active clock and unrelated orders continue. A full-day-or-longer absence still uses the separate temporary-command and succession procedure below.

## Communication and chain of command

Use a role-based chain of command for all game communication:

- One group channel is available for non-sensitive game communication, public updates, and rules procedure.
- Each player communicates through their superior and subordinate roles where those roles exist. A player should not bypass an available superior or subordinate to issue or request an operational decision.
- The GM may contact commanders privately when a report, order clarification, or other information is sensitive.
- Players may contact opposing players only with permission from their superior and with the GM able to see or review the exchange.
- Game-related communication must stay separate from personal chat so the GM can request, review, and preserve the operational record.

The first test only requires agreed channels that follow this structure; it does not require a dedicated Discord implementation. A future Discord setup is an optional delivery method, not a prototype rule.

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

## Shared session and continuity

The campaign is simultaneous during each active window: the game clock and GM processing continue from 08:00 to 22:00, while players may participate asynchronously through brief check-ins or longer periods of attention. It still has one authoritative operational record. The game master keeps:

- A master clock log with active/frozen boundaries.
- An order register containing every order, status, timer, and result.
- A master map version or dated snapshot.
- A report register showing which side received each report and when.
- A short decisions log for temporary rulings and unresolved questions.

At 08:00, the game master gives each commander a compact private briefing containing the current time, friendly status, known reports, in-progress orders, pending decisions, and the next deadline. The commander confirms receipt before issuing a new order. The briefing does not include information that role has not earned.

During the active window, the game master actively manages the session: acknowledging orders, tracking timers, resolving contacts, updating the master map, and sending reports as events occur. Players may take short breaks or be briefly unavailable, but the game remains live and the GM continues to apply the rules and record events. Urgent decisions use the response-window and fallback procedure above.

If records conflict, the latest time-stamped master log and map snapshot take precedence. The game master announces the correction, preserves the earlier entry for auditability, and applies the same correction standard to both sides.

## Temporary command and player absence

The game is live during the active window, but a player may be unavailable for a full day or more because of illness, an emergency, or another real-world obligation. The game master records the absence and appoints temporary command before that player's forces need a decision. The absent player does not receive retroactive knowledge when they return; they receive the normal handoff for their role. Brief check-ins and missed response windows do not by themselves trigger succession.

Use this succession order:

1. A superior commander on the absent commander's side takes temporary command of the absent commander's forces.
2. If no superior is available, a commander at the same level on the absent commander's side may take temporary command.
3. If no superior or equivalent commander is available, a subordinate from the absent commander's own company is preferred.
4. If no suitable player from that company is available or willing, the game master may temporarily promote another available player from the same side.
5. If no player from that side can take the role, the game master controls the company using the same limited-information and decision standards that apply to a non-player company.

Temporary command never crosses faction lines. The temporary commander receives the absent role's current orders, status, reports, and pending decisions, but not information that role has not earned. The game master records who assumed command, when the transfer began, and what authority was delegated.

- A subordinate temporarily promoted to company commander controls the absent company for the duration of the appointment. When the appointment ends, they return to their original unit and retain only that unit's authority.
- A commander at the same level who assumes the absent role controls both their original forces and the temporary forces until the appointment ends.
- A superior commander does not micromanage the temporary company. They issue objectives, priorities, and broad instructions, while the company is handled under the same higher-level abstraction used for subordinate or non-player formations.

When the original player returns, or another eligible commander formally assumes the role, the game master announces the transfer, updates the command record, and returns the temporary commander to their normal authority. Orders already accepted remain valid unless the newly recognized commander changes or cancels them through the normal order procedure.

## Fairness and continuity rules

- The same timing aid and adjudication principle applies to equivalent actions by both sides.
- A commander may correct an unclear order before it starts, but may not rewrite an action after learning its result.
- A player who was offline does not gain retroactive knowledge; they receive the same handoff their role would have received.
- Rules questions are logged and answered with a temporary ruling so play can continue.
- Temporary rulings are reviewed after the scenario, not repeatedly reopened during the active clock.

Advanced intelligence, cyberwarfare, vehicles, air support, and other expansion systems are outside this procedure. The prototype uses observation, written reports, infantry movement, and game-master adjudication only.
