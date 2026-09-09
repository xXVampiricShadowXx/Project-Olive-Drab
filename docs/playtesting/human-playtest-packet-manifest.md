# Human Playtest Packet Manifest

Use this manifest to reproduce the first supervised human playtest without
silently changing the Phase 3 rules. It identifies the exact repository files
that form the packet and the external setup that still has to be completed.

## Packet identity

```text
Packet version: human-playtest-0.1
Rules authority: Phase 3 prototype packet on the selected playtest commit
Scenario: Brackenford, seven scenario days
Map authority: Brackenford sector specification, map v1.0
Clock: 08:00-22:00 active; 22:00-08:00 frozen
Status: preparation package; not a release
```

The GM records the commit SHA used at the top of the briefing, observer
ledger, and report. The packet version is a document identifier, not a change
to any rule.

## Required repository files

Read and use these files at the recorded commit:

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
| Safety and roleplay | [Prototype roleplay layer](../game-design/14-prototype-roleplay-layer.md) | Bounded fictional roleplay |
| Quick reference | [Quick reference](../assets/quick-reference.md) | Live reference aid |
| Observer record | [Observer event ledger](observer-event-ledger-template.md) | Append-only event and closeout record |
| Report | [Playtest report template](playtest-report-template.md) | Rules and human-specific results |
| Private records | [GM-only records and data handling](gm-private-records-and-data-handling.md) | Access, redaction, backup, and retention boundaries |

The [Phase 4 AI packet](phase-4-ai-rules-operations-playtest.md) and its
dry-run report are validation context only. They do not replace a human
session or prove that external channels, notifications, or player experience
work.

## Known limitations

- The first test remains infantry-only and uses the six-by-five Brackenford
  sector map; no Phase 3 mechanics are expanded here.
- The repository does not provide a Discord server, shared map, notification
  service, player roster, or backup contacts.
- The AI dry run used simulated channels and did not validate Discord
  permissions, delivery latency, human response behavior, or enjoyment.
- Exact calendar dates are intentionally not part of the scenario rules.
- The GM must record any uncovered edge case as a temporary, symmetrical ruling;
  do not improvise a new mechanic during play.

## External setup still required

Before the final go/no-go, the GM and participants must complete the
[readiness guide](human-playtest-readiness-guide.md), including:

- a shared local time zone, seven-day calendar window, and notification plan;
- a Discord server with the documented roles, channels, permissions, and
  GM-visible opposing-contact path;
- a shared map with one GM master view and filtered NATO and Russia views;
- primary and backup same-side succession contacts for each commander;
- the scenario briefing, consent/safety briefing, and communication rehearsal;
- an observer, authoritative registers, backup location, and pause/hiatus
  procedure.

The GM must also establish the private working-record location, backup, and
retention period before the first order. This is a repository guide, not proof
that any account, channel, map, backup, or participant arrangement exists.

Completion of these items must be recorded by the GM. This manifest does not
claim that any external setup or player action has happened.
