# GM preparation and packet catalog

This is the GM route, not required player reading. Players use the
[finite learning route](../learn/index.md); optional Observers use the
[Observer guide](../templates/observer-guide.md).
This navigation adds no rules: the
[governing prototype sources](../reference/prototype/index.md) remain
authoritative. Issues #14, #15, and #16 remain open external prerequisites;
the static renderer is proposed and human verification is pending.

## Prepare in this order

1. Confirm [first-test scope and acceptance](test-scope-and-acceptance.md).
   Deliver the [consent and safety briefing](../learn/consent-and-safety.md)
   before role assignment.
   Use the [GM overview](overview.md) as a non-authoritative orientation.
2. Prepare the governing sources and forms in the
   [packet catalog](#packet-manifest-required-repository-files). Establish
   [private records, backup, and retention](private-records.md) before
   creating working files or channels.
3. Work through [session and table setup](setup-and-readiness.md#setup-checklist)
   and the [readiness checks](setup-and-readiness.md#readiness-guide).
   Use [external checks](setup-and-readiness.md#external-checks),
   the [Discord build sheet](discord-build-sheet.md), the
   [map build sheet](shared-map-build-sheet.md), and the
   [collaborative agenda](collaborative-setup.md) at the relevant setup step.
4. Repeat the [consent and safety briefing](../learn/consent-and-safety.md)
   before the first order, then complete and deliver the
   [scenario briefings](../templates/scenario-briefing.md) and private
   [commander sheets](../templates/commander-role-sheets.md).
5. Complete the [communication dry run and human rehearsal](communication-rehearsal.md).
   Multi-day freeze/restart and succession exercises remain conditional,
   not extra evidence required for the first one-day test.
6. Record the [final preflight decision](setup-and-readiness.md#final-preflight).
   Do not accept an operational order until every blocking item is checked
   or a recorded temporary workaround is accepted by both commanders.
   On NO-GO, do not reveal the scenario clock or start a timer.

After authorization, use the setup checklist's
[live-play and closeout tasks](setup-and-readiness.md#setup-checklist-4-start-the-first-active-day)
and the governing [active-window workflow](../reference/prototype/operating-procedure.md#game-master-active-window-workflow).
The following catalogs identify materials and their uses; they are not
additional reading orders or separate readiness decisions.

## Packet manifest

Use this manifest to reproduce the first supervised human playtest without
silently changing the Phase 3 rules. It identifies the exact repository files
that form the packet and the external setup that still has to be completed.

### Packet manifest: Packet identity

```text
Packet version: human-playtest-0.1
Rules authority: Phase 3 prototype packet on the selected playtest commit
Scenario: Brackenford, Day 1 only for first human test
Map authority: Brackenford sector specification, map v1.0
Clock: scenario time runs 1:1 with real time; Day 1, 08:00-22:00 active; first human session ends at 22:00
Status: preparation package; not a release
```

The GM records the commit SHA used at the top of the briefing, observer
ledger, and report. The packet version is a document identifier, not a change
to any rule.

### Packet manifest: Required repository files

Prepare and use these materials at the recorded commit as needed for the
tasks above. The catalog is not a cover-to-cover player reading requirement:

| Area | File | Authority or use |
|---|---|---|
| Packet index | [Prototype packet index](../game-design/09-prototype-packet-index.md) | Complete reading order and materials |
| Rules and clock | [Prototype operating procedure](../game-design/06-prototype-operating-procedure.md) | Orders, communication, continuity, succession |
| Map | [Town map and terrain sectors](../game-design/12-town-map-and-terrain-sectors.md) | Authoritative sectors, terrain, views, and control pairs |
| Timing | [Timing and action aids](../game-design/07-timing-and-action-aids.md) | Routine movement and action timing |
| Control | [Control and victory conditions](../game-design/08-control-and-victory-conditions.md) | Published result test |
| Contact | [Prototype combat and contested actions](../game-design/13-prototype-combat-and-contested-actions.md) | Infantry-only contact resolution |
| Roles | [Commander role sheets](../game-design/11-commander-role-sheets.md) | Private commander instructions |
| Briefing | [Initial scenario briefing](../game-design/14-initial-scenario-briefing-template.md) | Public and private briefing fields |
| Rehearsal | [Communication and order dry run](../game-design/15-communication-and-order-dry-run.md) | Pre-play channel and order test |
| Go/no-go | [Final GM preflight](../game-design/16-final-gm-preflight-readiness-checklist.md) | Blocking readiness gate |
| Safety and roleplay | [Prototype roleplay layer](../game-design/17-prototype-roleplay-layer.md) | Bounded fictional roleplay |
| Quick reference | [Quick reference](../assets/quick-reference.md) | Live reference aid |
| Observer record | [Observer event ledger](observer-event-ledger-template.md) | Append-only event and closeout record when an observer is used |
| Report | [Playtest report template](playtest-report-template.md) | Rules and human-specific results |
| Private records | [GM-only records and data handling](gm-private-records-and-data-handling.md) | Access, redaction, backup, and retention boundaries |
| Participant guide | [Player playtest packet](player-playtest-packet.md) | Plain-language, role-by-role summary of the files above; adds no rules |

The [Phase 4 AI packet](phase-4-ai-rules-operations-playtest.md) and its
dry-run report are validation context only. They do not replace a human
session or prove that external channels, notifications, or player experience
work.

### Packet manifest: Known limitations

- The first human test remains infantry-only and uses the six-by-five Brackenford
  sector map; no Phase 3 mechanics are expanded here.
- The first human session is one active scenario day, Day 1 from 08:00 through
  22:00. The broader seven-day continuity procedure remains documented but is
  not required evidence for this first test.
- The repository does not provide a Discord server, shared map, notification
  service, player roster, or backup contacts.
- The AI dry run used simulated channels and did not validate Discord
  permissions, delivery latency, human response behavior, or enjoyment.
- Exact calendar dates are intentionally not part of the scenario rules.
- The GM must record any uncovered edge case as a temporary, symmetrical ruling;
  do not improvise a new mechanic during play.

### Packet manifest: External setup still required

Before the final go/no-go, the GM and participants must complete the
[readiness guide](human-playtest-readiness-guide.md), including:

- a shared local time zone and the Day 1 08:00–22:00 first-test window;
- a Discord server with the documented roles, channels, permissions, and
  GM-visible opposing-contact path (use the [Discord build
  sheet](discord-build-sheet.md));
- a shared map with one GM master view and filtered NATO and Russia views
  (use the [shared map build sheet](shared-map-build-sheet.md));
- primary and backup same-side succession contacts only when a side has
  additional eligible commanders; none are required in the two-player
  arrangement;
- the scenario briefing, consent/safety briefing, and communication rehearsal;
- authoritative registers, backup location, and pause/hiatus procedure;
- an observer and observer ledger only when an optional observer is actually used.

Use the [collaborative setup session agenda](collaborative-setup-session-agenda.md)
to record the user-led decisions and Dev/QA checks; it does not replace the
GM's final readiness decision.

The GM must also establish the private working-record location, backup, and
retention period before the first order. This is a repository guide, not proof
that any account, channel, map, backup, or participant arrangement exists.

Completion of these items must be recorded by the GM. This manifest does not
claim that any external setup or player action has happened.
## Preparation tooling

This index is the repository-side preparation package for the first human
playtest. It makes the existing Phase 3 packet runnable and auditable without
adding mechanics. **For the first human test, Day 1 runs 08:00–22:00 and ends
with the final control-state check.** The broader prototype remains a fictional,
infantry-only seven-day scenario with 08:00–22:00 active windows and
22:00–08:00 overnight freezes; that broader schedule is exercised separately
in solo/AI rehearsal and later multi-day tests.

### Preparation tooling: Task catalog

| Material | When to use it |
|---|---|
| [External setup and notification checks](setup-and-readiness.md#external-checks) | During platform setup; real human checks remain required |
| [Participant onboarding](../learn/essentials.md) | Player orientation, on the separate learning route |
| [Operational templates](../templates/operational-records.md) | Prepare reusable registers and forms |
| [GM-only records and data handling](private-records.md) | Before creating private records |
| [First-test scope and post-test decision framework](test-scope-and-acceptance.md) | Select the first-test boundary and record the post-test decision |
| [Feedback, issue, and revision framework](../project/feedback-and-revisions.md) | After collecting test evidence |
| [Filled fictional example packet](../history/examples/filled-fictional-example-packet.md) | Optional reference example, not live data |
| [Solo GM seven-day rehearsal](../history/rehearsals/solo-gm-seven-day-rehearsal.md) | Optional broader-prototype rehearsal, not first-test evidence |
| [Stable prototype snapshot and tag preparation](../project/snapshot-and-release-preparation.md) | Optional administration, not a first-test prerequisite or permission to release |

These documents complement, and do not replace, the [prototype packet
index](../game-design/09-prototype-packet-index.md), [readiness
guide](human-playtest-readiness-guide.md), [communication rehearsal](human-communication-order-rehearsal.md),
[observer ledger](observer-event-ledger-template.md), or [playtest report
template](playtest-report-template.md).

For the user-led external setup tracked in issues #14 and #15, use the
[Discord build sheet](discord-build-sheet.md), [shared map build
sheet](shared-map-build-sheet.md), and [collaborative setup
agenda](collaborative-setup-session-agenda.md). They prepare checks, not
external services or human sign-off.

### Preparation tooling: Repository versus external completion

Repository changes can prepare documents, IDs, checklists, examples, and
rehearsals. They cannot create or verify a Discord account, shared map access,
notification delivery, participant consent, accessibility needs, or human
enjoyment. The GM must mark those items separately and must not claim a human
test occurred until real participants complete it.

Real-life priority, consent, privacy, the right to pause or withdraw, and the
fictional framing apply to every rehearsal and test.

New players use the [learning route](../learn/index.md); they do not need
this GM preparation catalog. The GM uses the route above and reads the
private-records guide before creating any working files or channels.
