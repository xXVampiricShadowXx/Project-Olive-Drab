# Phase 4 AI-Assisted Rules and Operations Playtest Packet

This packet is for a documentation-first, AI-assisted dry run of the Phase 3
Brackenford prototype. It tests whether the written rules can be followed by
separate role instructions and a neutral record, before any human session or
software implementation.

This is not a simulation result. No outcome, balance claim, or playability claim
should be treated as evidence until the packet has been run and recorded.

## What this test is and is not

The test examines:

- rules clarity and whether a role can identify the next legal action;
- GM workload, handoffs, adjudication, and record maintenance;
- timing, response windows, overnight freeze, and restart behavior;
- information flow, confidence labels, filtered views, and stale reports;
- standing behaviors, order completion, fallbacks, and commander decisions;
- the infantry-only combat and contested-action procedure; and
- map position, sector control, control pairs, and victory logic.

It does **not** test human enjoyment, entertainment value, social dynamics,
friendship, table chemistry, roleplay quality, or whether people want to play
again. Those require a later human playtest and a separate research question.

Real life always takes precedence. The GM may pause, suspend, place the test on
hiatus, adjust it, or end it, while preserving the current state and recording
the reason.

## Authority and version control

Use the Phase 3 packet as the rules authority:

1. [Prototype packet index](../game-design/09-prototype-packet-index.md)
2. [Prototype operating procedure](../game-design/06-prototype-operating-procedure.md)
3. [Town map and terrain sectors](../game-design/12-town-map-and-terrain-sectors.md)
4. [Prototype combat and contested actions](../game-design/13-prototype-combat-and-contested-actions.md)
5. [Commander role sheets](../game-design/11-commander-role-sheets.md)
6. [Final GM preflight](../game-design/16-final-gm-preflight-readiness-checklist.md)

The AI test may expose an ambiguity, but it must not silently resolve one by
inventing a rule. The GM records a temporary, symmetrical ruling and labels it
as a decision needed for the next rules revision. Do not add vehicles,
artillery, air support, cyberwarfare, national politics, detailed equipment,
casualty tables, or a new map model.

Record the commit or rules version, packet version, scenario label, and map
version at the top of every transcript and report. Do not use real-world
calendar dates in the scenario clock; use scenario day and time.

## Role separation

Run each role from a separate prompt or document context. Do not give one role
another role's private state.

### GM role

The GM is the neutral authority and sole owner of the master state.

The GM may:

- receive orders and reports, assign sequential IDs, and accept or return
  incomplete orders;
- maintain the master map, order/report/contact registers, timers, rulings,
  and information-release log;
- send only the appropriate public or private information to each role;
- pause affected timers at contact, validate behaviors, set response deadlines,
  and apply the Phase 3 transparent resolution sequence;
- show affected players the resolution rolls without exposing hidden facts or
  unreleased situation bands; and
- issue a recorded temporary ruling when the packet has no applicable rule.

The GM must not optimize for either side, fill gaps with unstated capabilities,
turn suspected information into confirmed information, or treat a commander
status submission as authoritative without verification. The GM records
processing time and every unresolved question.

### NATO commander role

The NATO commander controls one fictional infantry company using only the NATO
filtered view, earned reports, public updates, and the Phase 3 commander sheet.
The role must:

- distinguish confirmed, reported, and suspected information;
- submit one clear order per purpose with route, limits, and timing intent;
- attach a complete standing behavior when flexible attention requires it;
- maintain a status card and engagement submission when requested;
- choose among the published contact responses rather than inventing combat
  actions; and
- state uncertainty or request clarification instead of assuming hidden facts.

The role must not inspect the master map, Russia's private information, GM-only
conditions, or hidden situation bands.

### Russia commander role

The Russia commander follows the same authority, lifecycle, information
discipline, and resolution procedure as NATO, using only the Russia filtered
view. The scenario strengths and limitations remain those already published in
the Phase 3 role sheet. They are not permission to add capabilities or
mechanical modifiers.

The role must not inspect the master map, NATO's private information, GM-only
conditions, or hidden situation bands.

### Observer role

The observer is a silent auditor, not a third commander and not a second GM.
The observer receives the public transcript and a timestamped observation feed,
but no unearned private information. If private observation is required to
measure information boundaries, the observer receives a redacted copy after
the checkpoint, never live access to the other side's hidden state.

The observer:

- timestamps starts, acknowledgements, clarifications, deadlines, pauses,
  resolutions, map updates, and reports;
- marks whether the written rule used was clear, ambiguous, or absent;
- records GM effort and rework without suggesting a tactical choice;
- counts information-boundary leaks, premature reveals, and unlabelled
  inferences;
- checks that control and map updates follow the authoritative specification;
  and
- does not correct a role during the test unless the GM invokes a safety or
  real-life pause.

## Information boundaries

| Information | GM | NATO commander | Russia commander | Observer |
|---|---|---|---|---|
| Complete master map and hidden conditions | Yes | No | No | No |
| Own force, orders, readiness, and earned status | Yes | NATO only | Russia only | Redacted |
| Opposing force locations and strength | Yes | Only when earned | Only when earned | Redacted |
| Public terrain, sectors, approaches, and control state | Yes | Yes | Yes | Yes |
| Other side's private reports and channels | Yes | No | No | No |
| Rulings and unresolved questions | Yes | Released portion only | Released portion only | Public/redacted |
| Situation band or hidden comparison | Yes | No, unless released by rule | No, unless released by rule | No |
| Orders, events, and public results | Yes | Applicable released records | Applicable released records | Yes |

Every release must identify its confidence (`confirmed`, `reported`, or
`suspected`) and possible staleness. Personal chat is never a game record.

## One-day Brackenford test sequence

Use one scenario day to exercise the rules. This is a focused operational
sequence, not a replacement for the seven-day scenario rules.

| Scenario time | Exercise | Expected record |
|---|---|---|
| 08:00 | GM opens the day and sends separate private briefings | Day state, weather, map version, briefing IDs, receipt times |
| 08:15 | Both commanders submit a complete opening order | Two order IDs, acceptance times, route, purpose, limits, expected completion |
| 08:45 | GM returns one intentionally incomplete order | Return reason, no timer start, corrected order and new acceptance |
| 09:30 | NATO submits a bounded standing behavior; Russia submits a route change | Behavior fields, validation, replacement order linkage |
| 10:30 | GM releases a suspected observation to one side | Report ID, source, confidence, staleness, filtered release |
| 11:30 | A planned movement creates contact in an approach sector | Contact ID, paused order, remaining time, separate reports, deadline |
| 12:00 | Both commanders submit engagement status and responses | Snapshot, verified/unverified fields, intent read-back |
| 12:30 | GM resolves one exchange using the Phase 3 sequence | Rolls, hidden-information handling, result pair, consequences |
| 13:30 | Map/control update tests an approach pair without town control | Master update first, filtered updates, control state explanation |
| 15:00 | One response deadline expires while a commander is unreachable | Reminder, fallback, reason, no invented attack order |
| 16:00 | An order crosses a simulated 22:00 freeze boundary | Remaining time, freeze record, no overnight resolution |
| 08:00 next day | GM restarts the frozen order for the final checkpoint | Morning briefing, unchanged remaining time, restart receipt |

At each exercise, the observer records the first point at which a role needed
clarification, the elapsed GM processing time, and whether the expected state
transition could be reconstructed from the transcript.

## Dry-run checkpoints and pass criteria

Do not call the test a pass because all messages were produced. Mark each
checkpoint `pass`, `fail`, or `blocked`, with evidence.

| Checkpoint | Question | Minimum pass evidence |
|---|---|---|
| Role isolation | Did each role act only on permitted information? | No boundary leak; every private release has a recipient |
| Order lifecycle | Can an incomplete order be returned without starting a timer? | Arrival, clarification, corrected order, and acceptance are linked |
| Timing | Can active time, response deadlines, freeze, and restart be reconstructed? | Remaining time is recorded before and after freeze |
| Behavior | Is a standing behavior bounded and cancellable? | Trigger, action, limits, expiry, and fallback are all present |
| Contact | Does contact pause only the affected routine order? | Paused order and unrelated continuing work are explicit |
| Combat | Can the GM apply the published sequence without invented modifiers? | Snapshot, intent, band, rolls, result, consequences, and update are present |
| Information flow | Are facts separated from inference and confidence preserved? | Released report matches the relevant filtered view |
| Map/control | Does the result preserve sector and control-pair logic? | Approach occupation is not incorrectly reported as town control |
| GM workload | Can one GM process the sequence with a stable record? | GM time and rework are measured for each checkpoint |
| Observer audit | Can an independent observer reconstruct what happened? | Event IDs, timestamps, and links are complete |

## Event and order transcript format

Use one append-only transcript. Never overwrite an entry; correct mistakes with
a linked correction.

### Header

```text
Test packet version:
Phase 3 rules version/commit:
Scenario label:
Scenario day/time window:
Map version:
GM:
NATO commander:
Russia commander:
Observer:
```

### Event entry

```text
Event ID:
Scenario day/time:
Wall-clock timestamp (optional):
Actor/role:
Event type: briefing / order / report / contact / ruling / timer / map update / pause / resolution
Visibility: public / NATO-private / Russia-private / GM-only / redacted-observer
Source or linked ID:
Observed fact:
Inference (if any):
Confidence: confirmed / reported / suspected / not applicable
Rule or section used:
State before:
Action or decision:
State after:
GM processing time:
Observer clarity: clear / ambiguous / absent
Open question or correction link:
```

### Order entry

```text
Order ID:
Submitted at:
Accepted / returned:
Unit:
Action:
Destination or target:
Purpose:
Start condition:
Route or formation:
Limits:
Behavior: trigger / action / limits / expiry-cancel / unreachable fallback
Expected completion:
Paused or replaced by:
```

## Observer metrics

Record counts and durations, not impressions. If a metric cannot be measured,
mark it `not measured` and explain why.

| Metric | Measurement |
|---|---|
| Rule clarity | Clear, ambiguous, or absent at first use; include linked rule |
| Clarification rate | Clarifying questions per accepted order or event |
| Order rework | Returned orders and minutes from first submission to acceptance |
| GM processing time | Time from received input to acknowledgement, ruling, or update |
| Timer integrity | Timer starts, pauses, resumes, or expiries with complete records |
| Deadline handling | Reminders, extensions, expiries, and fallback correctness |
| Information integrity | Boundary leaks, confidence-label errors, stale-report errors |
| Transcript completeness | Entries missing IDs, timestamps, visibility, links, or state |
| Combat procedure load | Minutes and rework per contact resolution |
| Map/control integrity | Incorrect sector, pair, contest, or town-control transitions |
| Role dependency | Events blocked because a required role, report, or handoff was unclear |
| Temporary rulings | Count, reason, rule gap, and whether the ruling was symmetrical |

Do not convert these metrics into claims about enjoyment or social behavior.

## Closeout

The GM freezes the transcript, saves the master-map snapshot and filtered
releases, and lists unresolved questions. The observer completes the report
using the [playtest report template](playtest-report-template.md). The result
must be one of:

- `rules-ready for human test`;
- `rules revision required`;
- `blocked by setup or recording failure`; or
- `inconclusive; repeat the same test`.

Do not revise a Phase 3 rule during the sequence. Propose changes only after
the closeout separates observed behavior, rule ambiguity, and design preference.
