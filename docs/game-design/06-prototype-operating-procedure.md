# Prototype Operating Procedure

This document is the game master's runbook for the first live, supervised test and the broader multi-day prototype procedure. It is written so a new group can understand what happens during an active day, what happens at night when the broader campaign continues, and how the game handles a player who is temporarily unavailable.

## Campaign clock

The broader prototype uses one shared local time zone and a seven-day scenario clock. The **first human test uses only Day 1, 08:00–22:00**, ending after the final control-state check.

- **Active window:** 08:00–22:00. Orders may be submitted, acknowledged, and resolved. Movement, observation, combat, and other permitted actions continue according to their stated times.
- **Frozen window:** 22:00–08:00. When the broader multi-day campaign continues, the clock advances to 08:00, but no new player action resolves and no action timer counts down. The game master may prepare records and private notes, but does not create a new operational result during the freeze.
- **Daily boundary:** For the broader multi-day campaign, at 22:00 the game master records every in-progress order, its remaining time, and its current conditions. At 08:00, those orders resume with the same remaining time unless a written scenario rule says otherwise.
- **First-human-test end:** At the end of Day 1 active time, perform the final control-state check and close the first human session. Do not start a second scenario day solely to continue the first test.

## Command hierarchy and unit terminology

The prototype uses a fixed hierarchical organization so command authority and map representation remain consistent at every playable echelon. The player's organization is the echelon they command; **unit** means a subordinate organizational element under that commander's control.

For the first prototype scenario, the player is a company commander. The company contains **1–4 echelons**. Each echelon contains **2 platoons**; each platoon contains **2 sections**; each section contains **2 squads**; and each squad contains **2 fireteams**. This is a deliberate game abstraction rather than a claim about real-world organization.

A company commander therefore has **1–4 echelon units** under command. An echelon commander has **2 platoon units**. A platoon commander has **2 section units**. A section commander has **2 squad units**. A squad commander has **2 fireteam units**. The hierarchy continues by this same relationship wherever the game assigns a player to a lower echelon. Real military terminology and echelon structures vary by country; the prototype uses this rigid hierarchy for repeatable play while preserving the general distinction between a commander's organization and subordinate units.

The map mirrors the same relationship: each immediate subordinate unit at the commander's active echelon is represented by one force marker. For the first prototype, the company commander therefore receives **1–4 echelon force markers**. If an echelon is separately player-controlled, its commander receives **2 platoon force markers**, and so on down the hierarchy. A force marker is the map representation of a subordinate unit; it is not itself a separate command authority.

This definition determines the scope of the existing order and status rules. When a rule says **unit**, use the subordinate unit identified by the commander in the order or record. When a commander has several subordinate units, each is a distinct command target and has its own current order/state record. No additional force-management mechanic is implied by this terminology.

The clock remains live during the active window, but player attention is flexible rather than continuously online. Players may check in briefly from work or another obligation, submit an order, receive GM notifications or situation reports, or remain immersed for longer periods. The GM continues processing accepted orders and events even when a player is away. The schedule is a pacing aid, not a reason to punish players for sleeping.

## Order lifecycle

Every action that can change the shared situation uses the same short lifecycle:

1. **Draft:** The commander writes the order using the standard fields: unit, action, destination or target, purpose, start condition, any limits, and optional standing behaviors.
2. **Submitted:** The commander sends the order to the game master through the agreed channel. The submission time is recorded in the shared log.
3. **Acknowledged:** The game master confirms that the order is legible, identifies the unit and intended action, and states whether anything is missing. Acknowledgment is not approval and does not reveal hidden information.
4. **Accepted or returned:** A complete order is accepted for processing. An incomplete, impossible, or contradictory order is returned with one clear question; its timer does not start until the commander resubmits it.
5. **In progress:** The game master records the start time, expected completion time, route or target, and any conditions that can interrupt it. An accepted behavior may execute during the order without a new notification, subject to GM trigger validation. The commander may clarify an order, but a changed objective is a new order.
6. **Resolved:** The game master updates the master map, affected status, and any reports. The commander receives the information their side could know.

For the first prototype, a **unit may have only one active operational order at a time**. Here, unit means the specific subordinate organizational element named in the order. A new accepted operational order for that same unit supersedes its previous active operational order, including its attached behaviors, unless the GM explicitly records that the new order is a non-conflicting action that can run concurrently. This prevents two orders from silently controlling the same subordinate unit at once.

A concurrent action may run only when it clearly does not direct or alter that unit's operational task/state. An action that directs movement, position, posture, destination, or another operational task supersedes the prior active operational order. When concurrency is permitted, the GM records it separately from the unit's single active operational order.

If enemy contact, a contested route, or a threatened control location interrupts an
order, use [Prototype Combat and Contested Actions](13-prototype-combat-and-contested-actions.md).
The GM records the order as paused—contact rather than silently completing or
rewriting it.

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
Behaviors (optional; one or more):
Commander:
```

The game master may assign the next sequential order ID if a commander does not provide one.

### Behaviors and standing orders

A commander may attach one or more behaviors to an accepted movement or position
order. A behavior lets a unit act during a flexible-attention period without
requiring the commander to answer a notification immediately. It does not bypass
the GM: the GM validates whether the stated trigger actually occurred, checks
whether the behavior is still legal and in force, and resolves any contested
outcome using the prototype combat procedure.

Use this predetermined list for the first test:

- **Continue:** complete the accepted route or position order unless a stated
  limit is reached.
- **Prepare:** on arrival, spend the stated preparation time and establish the
  specified posture.
- **Observe and report:** when the trigger occurs, observe the named sector or
  route and send a report without committing the force.
- **Hold:** when the trigger occurs, stop in the current sector and hold.
- **Probe:** commit the stated limited portion to learn or pressure, preserving
  the named reserve.
- **Withdraw:** on the trigger, withdraw to the named sector by the stated
  route.
- **Engage:** on the trigger, enter contact and choose the stated posture or
  commitment limit; this is not permission to resolve a fight without GM
  adjudication.

The commander may submit an original behavior, but the GM must approve it before
the order is accepted and explain its execution in plain language. Every
behavior, including a listed one, must specify:

```text
Trigger:
Action:
Limits:
Expiry or cancel condition:
If commander cannot be reached:
```

Triggers should name a sector, route, report condition, time, or observable
unit condition. The GM may reject vague, impossible, contradictory, or
unverifiable triggers. A behavior expires when its expiry condition occurs, its
action completes, its parent order is replaced or canceled, or the unit enters
an unresolved situation outside the approved action. A new accepted operational
order for the same unit replaces the prior parent order and its attached
behaviors unless the GM explicitly records a non-conflicting concurrent action.

If a valid trigger occurs while the commander cannot be reached, the GM follows
the behavior's recorded fallback. If no fallback is recorded, the GM uses the
least-committal safe action consistent with the parent order, normally Hold or
Continue, and records why. Silence never authorizes an unlisted attack or
unlimited commitment. Behaviors do not resolve during the frozen window.

### Urgent decisions and response windows

An urgent report or decision request must include a response-by time. The GM sends it through the role-based game channel and records when it was delivered. A player may respond with a decision, a standing instruction, or an explicit request for more time.

If the response window expires, the GM uses the last accepted order and any standing limits or fallback instruction already recorded for that unit. If no safe fallback exists, the GM pauses only that decision, takes the least-committal action consistent with the unit's last accepted order, and records the reason. The active clock and unrelated orders continue. A full-day-or-longer absence still uses the separate temporary-command and succession procedure below.

## Communication and chain of command

Use a role-based chain of command for all game communication:

- One group channel is available for non-sensitive game communication, public updates, and rules procedure.
- Each player communicates through their superior and subordinate roles where those roles exist. A player should not bypass an available superior or subordinate to issue or request an operational decision.
- The GM may contact commanders privately when a report, order clarification, or other information is sensitive.
- **First-prototype opposing contact:** because the only player-controlled roles are the two company commanders, an opposing commander may be contacted only with GM approval and GM visibility. A superior's permission is required only when a higher player-controlled role actually exists.
- Game-related communication must stay separate from personal chat so the GM can request, review, and preserve the operational record.

The first test uses a Discord server with channels that follow this structure. Discord is the communication platform for orders, reports, notifications, and rulings; it does not replace the authoritative log or map. The shared digital map may use another tool, provided its access rules match the master-map and filtered-view rules.

## Game-master active-window workflow

At the start of an active window, the game master:

1. Publishes the current public clock and any scheduled environmental change.
2. Reconciles the previous day's in-progress orders with the master log when continuing a multi-day campaign.
3. Sends each commander their private status and reports.
4. Lists orders awaiting clarification or acknowledgment.

During the active window, the game master:

1. Time-stamps new submissions in arrival order.
2. Acknowledges or returns each order promptly.
3. Starts routine timers and resolves completed actions.
4. Interrupts a timer when contact, a blocked route, or another contested condition occurs.
5. Validates triggered behaviors, records their execution or expiry, and pauses them when contact requires adjudication.
6. Adjudicates contested movement, combat, captures, and unusual cases using the transparent contact sequence.
7. Sends reports as soon as the relevant side could reasonably receive them.
8. Updates the master map first, then produces filtered commander-map updates.

For contact, the GM also records the response deadline, each side's stated
posture and commitment, the resolution band, the result pair, and the graduated
consequences. A contact report must separate observation from inference and must
not reveal the master map.

Before an engagement is resolved, each commander submits their current force
status for the involved unit: position, posture, preparation, readiness,
strength, reserve/commitment, and any relevant order or behaviors. The GM checks
that submission against the authoritative order and status log, map, reports,
and observed outcomes. A commander's unverified update is a claim to check, not
an automatic change to the master state.

At the end of an active window, the game master:

1. Stops all active timers at 22:00 when the broader campaign continues or when the first human test closes.
2. Records each order's remaining time and current condition.
3. Publishes the public end-of-day note and any control changes.
4. Stores the authoritative log and a backup copy before the freeze when another scenario day will follow.

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

The first human session ends after Day 1 active time. For the broader campaign, play is operationally simultaneous during each active window: the game clock and GM processing continue from 08:00 to 22:00, while player participation may be asynchronous through brief check-ins or longer periods of attention. Accepted orders and GM-validated standing behaviors continue under their recorded limits without waiting for everyone to be online. It still has one authoritative operational record. The game master keeps:

- A master clock log with active/frozen boundaries.
- An order register containing every order, status, timer, and result.
- A master map version or dated snapshot.
- A report register showing which side received each report and when.
- A short decisions log for temporary rulings and unresolved questions.

At 08:00, the game master gives each commander a compact private briefing containing the current time, friendly status, known reports, in-progress orders, pending decisions, and the next deadline when continuing a multi-day campaign. The briefing does not include information that role has not earned.

During the active window, the game master actively manages the session: acknowledging orders, tracking timers, resolving contacts, updating the master map, and sending reports as events occur. Players may take short breaks or be briefly unavailable, but the game remains live and the GM continues to apply the rules and record events. Urgent decisions use the response-window and fallback procedure above.

If records conflict, the latest time-stamped master log and map snapshot take precedence. The game master announces the correction, preserves the earlier entry for auditability, and applies the same correction standard to both sides.

## Temporary command and player absence

The game is live during the active window, but a player may be unavailable during a longer campaign because of illness, an emergency, or another real-world obligation. The game master records the absence and appoints temporary command before that player's forces need a decision. The absent player does not receive retroactive knowledge when they return; they receive the normal handoff for their role. Brief check-ins and missed response windows do not by themselves trigger succession.

Use this succession order:

1. A superior commander on the absent commander's side takes temporary command of the absent commander's forces.
2. If no superior is available, a commander at the same level on the absent commander's side may take temporary command.
3. If no superior or equivalent commander is available, a subordinate from the absent commander's own organization is preferred.
4. If no suitable player from that organization is available or willing, the game master may temporarily promote another available player from the same side.
5. If no player from that side can take the role, the game master controls the absent commander's organization using the same limited-information and decision standards that apply to a non-player formation.

Temporary command never crosses faction lines. The temporary commander receives the absent role's current orders, status, reports, and pending decisions, but not information that role has not earned. The game master records who assumed command, when the transfer began, and what authority was delegated.

- A subordinate temporarily promoted to fill the absent commander's role controls that absent commander's organization for the duration of the appointment. When the appointment ends, they return to their original unit and retain only that unit's authority.
- A commander at the same level who assumes the absent role controls both their original forces and the temporary forces until the appointment ends.
- A superior commander does not micromanage the temporary organization. They issue objectives, priorities, and broad instructions, while the organization is handled under the same higher-level abstraction used for subordinate or non-player formations.

When the original player returns, or another eligible commander formally assumes the role, the game master announces the transfer, updates the command record, and returns the temporary commander to their normal authority. Orders already accepted remain valid unless the newly recognized commander changes or cancels them through the normal order procedure.

## Fairness and continuity rules

- The same timing aid and adjudication principle applies to equivalent actions by both sides.
- A commander may correct an unclear order before it starts, but may not rewrite an action after learning its result.
- A player who was offline does not gain retroactive knowledge; they receive the same handoff their role would have received.
- Rules questions are logged and answered with a temporary ruling so play can continue.
- Temporary rulings are reviewed after the scenario, not repeatedly reopened during the active clock.

Advanced intelligence, cyberwarfare, vehicles, air support, and other expansion systems are outside this procedure. The prototype uses observation, written orders, infantry movement, and game-master adjudication only.
