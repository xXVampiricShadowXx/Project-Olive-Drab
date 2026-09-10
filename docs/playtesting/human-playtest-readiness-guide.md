# Human Playtest Readiness Guide

This guide turns the existing GM packet into a human-facing readiness gate. It
does not change the Phase 3 rules. The GM owns the final go/no-go decision and
the authoritative record.

## 1. People, roles, and contact

- [ ] Confirm one neutral GM, one NATO commander, one Russia commander, and one
  observer. Record preferred display names only; no personal details are
  required.
- [ ] Record the shared local time zone and the scenario start/end as scenario
  day and time on the shared clock. The prototype does not require exact
  calendar dates.
- [ ] Record the notification method, backup notification method, and who
  checks response deadlines. Test both methods.
- [ ] Name a primary and backup same-side succession contact for each
  commander. Record role, contact route, handoff start/end, and that the
  contact receives only the absent role's earned information.
- [ ] Confirm the real-life pause/hiatus signal and who may invoke it. A
  pause, suspension, hiatus, adjustment, or end is allowed when real life
  requires it; the GM preserves the state and records the restart or closure.
- [ ] Confirm a player may withdraw without explaining personal circumstances.
  The GM records only the operational consequence needed for continuity.

## 2. Discord roles, channels, and permissions

Create a game-only server or game-only channel structure. Personal direct
messages are never an order, report, ruling, map update, or notification.

| Role or channel | Required access |
|---|---|
| GM | All game channels, master record, master map, and private views |
| Observer | Public transcript and redacted feed; no live opposing private state |
| NATO commander | Group channel, NATO private channel, and permitted same-side path |
| Russia commander | Group channel, Russia private channel, and permitted same-side path |
| Group channel | Both commanders and GM; public updates and non-sensitive procedure |
| NATO private | NATO commander and GM; no Russia access |
| Russia private | Russia commander and GM; no NATO access |
| Opposing-contact path | GM approval and GM visibility in the first prototype; superior permission applies only when a higher player-controlled role exists |
| GM record channels/files | GM only, with an explicit backup location |

- [ ] Test read, post, and attachment permissions with harmless messages.
- [ ] Verify that no commander can view the master map, opposing private
  reports, hidden starting zone, or GM-only conditions.
- [ ] Verify notifications and the backup notification route, including a
  response-by reminder.
- [ ] Record channel names and the result in the dry-run completion fields.

## 3. Shared map and filtered views

- [ ] Reproduce the authoritative six-column by five-row Brackenford map,
  labels, approaches, terrain, and control pairs exactly.
- [ ] Create one GM master view containing all forces, hidden conditions,
  orders, control, and map version.
- [ ] Create filtered NATO and Russia views with public terrain, own status,
  earned information, and clearly labelled suspected positions only.
- [ ] Verify that hidden markers and stale private reports cannot leak through
  layers, links, exports, or screen sharing.
- [ ] Record the map version, snapshot method, and backup location.

## 4. Records and scenario briefing

- [ ] Prepare sequential order, report, contact, map, ruling, and event IDs.
- [ ] Prepare the observer ledger, master clock log, order/report registers,
  decision log, and dated map snapshots.
- [ ] Read the [GM-only records and data handling
  guide](gm-private-records-and-data-handling.md); record the access-controlled
  working location, separate backup, redaction check, restore check, and
  retention/deletion date without putting those links or details in the
  repository.
- [ ] Complete the public and private briefing templates, including map links,
  weather, visibility, starting zones, approved placement, and first deadline.
- [ ] Publish the objective and control rule before accepting the first order.
- [ ] Explain the 22:00 freeze, 08:00 restart, response windows, standing
  behavior fields, and that silence never authorizes an unlisted attack.
- [ ] Complete the separate [communication rehearsal](human-communication-order-rehearsal.md).

## 5. Consent, safety, and real-life priority

Before role assignment, deliver the [participant briefing](consent-safety-participant-briefing.md).
Confirm privately, without requiring disclosure, that each participant can:

- opt out, pause, take a break, or withdraw at any time;
- keep personal identity, health, schedule, and other private details private;
- decline roleplay content or request a lower-intensity presentation; and
- ask the GM to stop or change the activity for a real-life safety concern.

The fictionalized setting is not a statement about real nations or current
events. Keep tactical information inside the game record and do not request
real operational, political, or personal information.

## 6. Seven-day clock and continuity

- [ ] Record the scenario start at Day 1, 08:00 in the shared local time zone.
- [ ] At each 22:00 boundary, stop timers, record remaining active time, save
  the state, and publish the end-of-day note.
- [ ] At each 08:00 restart, deliver private handoffs and resume the recorded
  remaining time without recalculation.
- [ ] For a full-day-or-longer absence, activate the named same-side primary,
  then backup, using the existing succession order. Do not transfer a player
  across factions or grant unearned information.
- [ ] Preserve the state during a pause or hiatus. Restart only after the GM
  confirms the participants and records the restart time.
- [ ] Before a pause, hiatus, or overnight freeze, save a labelled snapshot.
  On restart, verify the snapshot ID, active timers, pending deadlines, and
  information boundaries before resuming. If the session ends, record closure
  and apply the agreed retention/deletion date.

## Final go/no-go

The GM records `GO` only when every blocking item above is checked or a
temporary workaround is written and accepted by both commanders. Record:

```text
Readiness result: GO / NO-GO
Packet version and commit:
Scenario start and local time zone:
Unresolved blocker:
Temporary workaround and expiry:
Both commanders agree: yes / no
GM authorization time:
First accepted order ID:
```

If the result is `NO-GO`, do not reveal the scenario clock or start a timer.
