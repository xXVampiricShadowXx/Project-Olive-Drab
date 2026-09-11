# Brackenford AI Rules and Operations Dry Run

**Scenario:** Brackenford one-day focused sequence, Day 1
**Rules version:** Phase 3 prototype packet at commit `cbf33f8`
**Date:** 2026-09-08 (report date only; scenario clock uses Day 1)
**Players and roles:** Controlled role contexts: GM, NATO commander, Russia commander, observer
**Approximate duration:** 08:00 Day 1 through 08:00 Day 2 scenario time
**Test type:** AI-assisted rules and operations
**Packet version or commit:** Phase 4 AI rules and operations playtest packet; branch base `cb7deae`
**Map version:** Brackenford sector specification, map v1.0

## Historical evidence status

This report is retained as historical validation of the rules snapshot identified above. Later repository revisions changed several of the rules exercised here, so this report does not establish readiness of the current `main` ruleset. Preserve the event transcript and metrics as historical evidence; use the current playtest packet, current rehearsals, and final GM preflight for present readiness decisions.

## Channel-simulation workaround

This was a controlled channel simulation, not a Discord session and not an
external-agent run. Four isolated role contexts were used: one GM context, one
NATO commander context, one Russia commander context, and one observer context.
The simulated public channel, NATO-private channel, Russia-private channel,
GM-only state, and redacted observer feed were represented by visibility labels
in this report. The simulation tests information boundaries, records, and
procedures only; it does not validate Discord permissions, delivery latency,
human enjoyment, social dynamics, or Discord integration.

The GM maintained the complete master state. Commander contexts received only
their filtered briefings and released reports. The observer received the public
transcript and redacted checkpoints, not live opposing private state.

## What were we testing?

This run tested whether the written Phase 3 rules can support a complete
one-day operational sequence: private opening briefings, complete and
incomplete order handling, movement and reporting, contact, a contested
infantry action, visible resolution rolls with protected situation bands,
bounded standing behavior, an urgent response window, temporary succession,
the 22:00 freeze, and next-day restart with unchanged remaining time.

In scope were rules clarity, GM workload, timing, information flow, standing
behaviors, combat procedure, map/control logic, continuity, and observer
reconstruction. The run does not measure human enjoyment or social behavior.

## What happened?

### Header and initial state

The GM recorded the scenario clock as Day 1, 08:00-22:00 active and
22:00-08:00 frozen. Weather was clear, visibility normal. NATO's permitted
starting zone was A1/A2/B1/B2/A3 with 120 strength, steady readiness, and
markers at A2 and B2. Russia's permitted zone was E1/E2/F1/F2/F3/F4 with
150 strength, steady readiness, and markers at F2 and F3. Neither side began
in a central control pair. The public town state was uncontrolled.

### Append-only event transcript

Wall-clock timestamps are omitted because the controlled run uses scenario time
as the authoritative clock. Every event has a sequential ID, scenario time,
actor, visibility, linked state, and observer result.

| ID | Scenario time | Actor / visibility | Type | Linked order/report | Observed fact and action | State after / observer note |
|---|---|---|---|---|---|---|
| E001 | Day 1 08:00 | GM / public | briefing | MAP-001 | Opened the active window; published weather, visibility, map v1.0, objective, and uncontrolled town state. | Active timer started. Clear; GM processing 2 min. |
| E002 | Day 1 08:00 | GM -> NATO / NATO-private | briefing | BRF-N-001 | Sent NATO only its zone, own status, routes, objective, and no opposing location. NATO acknowledged before ordering. | NATO filtered view current. Clear; 1 min. |
| E003 | Day 1 08:00 | GM -> Russia / Russia-private | briefing | BRF-R-001 | Sent Russia only its zone, own status, routes, objective, and no opposing location. Russia acknowledged before ordering. | Russia filtered view current. Clear; 1 min. |
| E004 | Day 1 08:15 | NATO / GM-private | order | O-N-001 | Submitted a complete order: A2 company moves via A3 to C3, purpose seize the west side of Market Square, start immediately, avoid contact until confirmed, Hold if commander unreachable. | GM acknowledged and accepted; estimated 10:00 (A2-A3 open 30 min plus A3-C3 built 60 min). Timer started. Clear; 3 min. |
| E005 | Day 1 08:15 | Russia / GM-private | order | O-R-001 | Submitted a complete order: F3 company moves via E3/D3, purpose pressure Market Square, start immediately, do not pursue beyond D3, Hold if commander unreachable. | Accepted; estimated 10:15 (built movement aid). Timer started. Clear; 3 min. |
| E006 | Day 1 08:45 | Russia / GM-private | order returned | O-R-002 | Intentionally omitted the destination from a route-change order. GM asked one question, returned it, and did not start a timer. | O-R-002 returned; O-R-001 remained authoritative. Clear; 2 min. |
| E007 | Day 1 09:00 | Russia / GM-private | order | O-R-003 | Resubmitted the corrected route-change order: F3 to E3, purpose establish observation, route via F3-E3, limit Hold, no behavior. | Accepted at 09:02; replacement linked to O-R-001. Timer starts only at acceptance. Clear; 2 min. |
| E008 | Day 1 09:30 | NATO / GM-private | order | O-N-002 | Added bounded behavior to the accepted movement: trigger confirmed opposing presence in C3 or D3; action Hold in current sector and report; limits no commitment; expiry at 12:00 or replacement; unreachable fallback Hold. | Validated and linked. Trigger/action/limits/expiry/fallback complete. Clear; 3 min. |
| E009 | Day 1 09:30 | Russia / GM-private | order | O-R-004 | Replaced the route objective with a bounded route change from E3 toward D3 and linked it to O-R-003. | Replacement accepted; prior order remains auditable. Clear; 2 min. |
| E010 | Day 1 10:30 | GM -> NATO / NATO-private | report | R-N-001 | Released a suspected observation: movement noise near A3, source local observer, observed at 10:20, possibly stale by 30 min. No hidden unit location was released. | NATO marked it suspected, not confirmed. Russia did not receive it. Clear; 2 min. |
| E011 | Day 1 10:30 | GM -> Russia / Russia-private | report | R-R-001 | Released a separate reported observation: possible NATO movement near A3, source forward element, observed 10:20, stale after 30 min. | Russia received only its filtered report. No boundary leak. Clear; 2 min. |
| E012 | Day 1 11:30 | GM / GM-only then public | contact | C-001 | NATO's movement reached C3 and encountered a Russian presence. Paused O-N-001 at contact with 15 active minutes of routine movement remaining. Unrelated records continued. | Contact state created; neither hidden strength nor band released. Clear; 4 min. |
| E013 | Day 1 11:30 | GM -> both / filtered-private | contact | C-001 | Sent separate contact reports. NATO received confirmed opposing presence in C3; Russia received confirmed NATO presence in C3. Each report separated observation from estimated posture. | Response deadline 12:00, routine-contact 30 active minutes. Clear; 3 min. |
| E014 | Day 1 12:00 | NATO and Russia / private | status/order | C-001 | Both submitted position, posture, preparation, readiness, strength, reserve, and response. NATO chose Probe, preserve 60 strength, objective learn and hold C3. Russia chose Hold, commit 100, objective deny C3. | Both status submissions verified against the master record. Clear; 5 min. |
| E015 | Day 1 12:30 | GM -> affected roles / public rolls + protected GM state | resolution | C-001 | Frozen snapshot; read back intent; selected NATO favorable and Russia even bands from position, preparation, commitment, and hidden conditions. Hidden comparison and bands stayed GM-only. Visible rolls were NATO d6=5 and Russia d6=3. | Publicly visible rolls and result tiers only; no hidden band leak. Clear; 8 min. |
| E016 | Day 1 12:30 | GM / public + filtered | map update | MAP-002 | Interpreted NATO 5/favorable as strong and Russia 3/even as mixed. The adjacent result tiers produced a mixed exchange: NATO gained limited initiative and pressure, while Russia remained capable. C3 became contested; NATO moved to C3, Russia remained in D3. NATO readiness steady, Russia shaken. | O-N-001 remained paused-contact; no town control claimed. Clear; 5 min. |
| E017 | Day 1 13:30 | GM -> both / public + filtered | map update | MAP-003 | Recorded approach-pair check: Russia holds D3 but not C3, so Market Square pair is contested. No town control; approach occupation was not misreported as town control. | Control logic preserved. Clear; 3 min. |
| E018 | Day 1 15:00 | GM -> NATO / NATO-private | behavior/deadline | C-002 | Opened urgent response window for a threatened route at C3, due 15:30. NATO commander was simulated unreachable; reminder at 15:20; no response by 15:30. | Standing Hold behavior and last accepted limits used; no invented attack. Clear; 4 min. |
| E019 | Day 1 15:30 | GM / GM-only + public ruling | succession | RUL-001 | Simulated temporary absence for NATO. No superior was available, so a NATO same-side temporary commander assumed the role. Handoff contained NATO orders, status, earned reports, and pending decision only. | Temporary command began at 15:30; authority did not cross factions. Clear; 6 min. |
| E020 | Day 1 16:00 | Temporary NATO commander / NATO-private | order | O-N-003 | Temporary commander accepted the existing Hold/Probe limits and did not rewrite C-001 after its result. New order only requested reorganization in C3 for 60 active minutes, with fallback Hold. | O-N-003 accepted; C-001 closed as disengaged after the mixed exchange and subsequent hold. Clear; 3 min. |
| E021 | Day 1 16:00 | GM / GM-only | timer | T-001 | Started a deliberate withdrawal/route order that would cross the freeze: Russia D3 to E3 via E2, 120 active minutes remaining at the planned freeze checkpoint. | Timer active; no contact or resolution added. Clear; 2 min. |
| E022 | Day 1 22:00 | GM / public + redacted observer | pause/freeze | T-001 | Stopped active timers at the exact boundary. Recorded T-001 with 90 active minutes remaining after 30 minutes elapsed, current route D3-E2-E3, Russia shaken, and no new result during freeze. | Frozen 22:00-08:00. Remaining time preserved as 90 minutes. Clear; 5 min. |
| E023 | Day 2 08:00 | GM -> both / filtered-private | briefing/restart | BRF-N-002, BRF-R-002 | Restarted active window, delivered normal private handoffs, and resumed T-001 with exactly 90 active minutes. No overnight movement, combat, or information change was invented. | Restart state reconstructs from freeze record; clear. GM processing 5 min. |
| E024 | Day 2 08:00 | Observer / redacted-observer | closeout | OBS-001 | Froze the transcript and compared public events, redacted releases, order register, contact register, ruling log, timer record, and map snapshots. | All required event IDs and links present; no leak detected. Clear; 6 min. |

### Combat record and protected information

The visible record showed both commander-submitted statuses, their stated
intents, the two die results (NATO 5, Russia 3), the result tiers, and the
graduated consequences. The GM retained the situation bands and hidden
comparison in GM-only state. The visible result did not expose a hidden unit,
unreleased modifier, or the opposing side's private report.

### Temporary ruling

`RUL-001` recorded the temporary absence/succession handoff as a same-side
commander appointment because no superior or subordinate context was available
in the simulation. The handoff scope followed the published temporary-command
procedure and was symmetrical in information discipline. This was an
operations-test setup ruling, not a new combat or movement rule.

## Checkpoint results

| Checkpoint | Pass / fail / blocked | Evidence or linked event IDs |
|------------|------------------------|------------------------------|
| Role isolation and information boundaries | Pass | E002-E003, E010-E013, E015, E019; no boundary leaks or premature hidden reveals |
| Order lifecycle | Pass | E004-E009; returned order had no timer, corrected order linked to acceptance |
| Timing, freeze, and restart | Pass | E012, E018, E021-E023; 90 active minutes recorded before and after freeze |
| Standing behaviors and fallbacks | Pass | E008, E018-E020; trigger, action, limit, expiry, and unreachable fallback recorded |
| Contact and combat procedure | Pass | E012-E016; snapshot, intent, protected bands, visible rolls, result, consequences, and update present |
| Map, sector control, and victory logic | Pass | E016-E017; C3/D3 contested and no approach-pair claim of town control |
| GM workload and observer reconstruction | Pass | E001-E024; every required transition reconstructed from the redacted feed |

## Observer metrics

| Metric | Result | Notes |
|--------|--------|-------|
| Rule clarifications | 1 | E006 omitted destination; one clear question returned the order |
| Returned or reworked orders | 1 returned, 1 corrected | O-R-002 -> O-R-003; 2 minutes from return to acceptance |
| GM processing time | 83 minutes total recorded | Sum of per-event processing estimates; no unmeasured event processing was required |
| Timer/deadline errors | 0 | Contact pause, response expiry, freeze, and restart were linked |
| Information-boundary or confidence-label errors | 0 | Suspected/reported/confirmed labels preserved; 0 leaks |
| Transcript completeness errors | 0 | 24 events had IDs, time, actor, visibility, link, state, and clarity |
| Combat-resolution processing time | 8 minutes | E015 snapshot through visible result; no rework |
| Map/control errors | 0 | Approach occupation did not become town control; C3/D3 remained contested |
| Temporary rulings | 1 | RUL-001, same-side succession handoff; review before human test |
| Role dependency | 0 blocked events | Temporary commander fallback allowed the sequence to continue |

## What worked?

- Separate filtered briefings and release labels kept the four role contexts
  isolated while preserving a reconstructable public record.
- The incomplete-order lifecycle made it explicit that no timer starts before
  acceptance.
- Contact paused only the affected order, and the resolution sequence showed
  rolls without exposing the GM-only bands.
- The control-pair check prevented an approach position from being reported as
  town control.
- The freeze record carried the exact 90 active minutes into the next-day
  restart.
- The bounded behavior and temporary-command fallback prevented silence from
  becoming an invented attack order.

## What did not work?

- The packet does not provide a canonical machine-readable schema for the
  observer feed; this report used a manually enforced table. That is a
  recording aid gap, not a rules failure.
- The controlled simulation could not test actual channel permissions,
  notification delivery, or human response latency. Those remain human-test
  setup checks.

## Human player experience

Not applicable. This was an AI-assisted rules and operations test and makes no
claim about enjoyment, social dynamics, or whether decisions felt meaningful.

## Changes for the next version

| Change | Reason | Priority |
|--------|--------|----------|
| Use the new [observer event ledger template](observer-event-ledger-template.md) for the next run. | The dry run required a manually enforced record shape; the reusable schema now standardizes rows and closeout counts. | Medium |
| Select and name primary and backup same-side succession contacts before the human test. | The dry run used a simulated same-level handoff; concrete contacts and a handoff path must be prepared in advance. | High |
| Validate Discord permissions, notification delivery, and real human absence handoff in the human preflight. | The temporary channel simulation intentionally did not test integration or delivery. | High |

No Phase 3 rule was changed during the sequence. No minimal documentation fix
was required from a rules defect.

## Designer notes

Observed behavior supports the packet's order, contact, timing, information,
control, and absence procedures for this focused sequence. The observer-led
schema gap is operational documentation work, not evidence that a new game rule
is needed. The visible-roll requirement is compatible with protected hidden
bands when the result tiers and consequences are released without the bands.

## Decision

**Rules-ready for human test — historical snapshot only; superseded as current readiness evidence.**

The focused sequence completed with no blocked checkpoint, no information
boundary leak, no timer/restart error, and no combat or control-rule defect in
the recorded `cbf33f8` rules snapshot. Later rule revisions changed the
repository materially. This report therefore must not be cited as validation
of the current `main` ruleset. Current readiness depends on the present packet,
current rehearsals, and the final GM preflight.

## Open decisions

- Fill the ledger header and event rows for the human test.
- Name and confirm the primary and backup same-side succession contacts for
  each faction using the packet's selection order.
- Complete actual Discord channel and notification validation; this remains a
  human preflight requirement and was not claimed by this dry run.
