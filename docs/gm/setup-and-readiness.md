# GM setup, readiness, and final authorization

Use the [GM preparation route](index.md#prepare-in-this-order) to navigate
this combined checklist. These sections have different purposes:
[setup](#setup-checklist) prepares and operates the session;
[external checks](#external-checks) test actual services;
[readiness](#readiness-guide) checks people, safety, and evidence; and
[final preflight](#final-preflight) records the GM's authorization.
They add no mechanics and do not replace the
[governing rules](../reference/prototype/index.md).
Issues #14, #15, and #16 remain open; repository preparation is not human
verification. Record private completion fields only in the GM's protected
working records, never as filled examples in this repository.

## Setup checklist

Use this checklist before and during the first live, supervised prototype. The GM is neutral and maintains the authoritative record; the checklist does not authorize hidden advantages or unscheduled rules.

### Setup checklist: 1. Confirm the session

- [ ] Confirm two commanders and one GM. For each side with additional eligible
      commanders, confirm a temporary-command contact; no succession contacts
      are required in the two-player arrangement.
- [ ] Confirm the shared local time zone and active window: 08:00–22:00.
- [ ] Confirm that the first human test uses Day 1 only; the broader prototype also supports a seven-day scenario clock with a frozen window from 22:00–08:00 when multiple days are run.
- [ ] Confirm one group channel for non-sensitive game communication and public updates.
- [ ] Confirm the role-based chain: players communicate through available superiors and subordinates; the GM can review all game communication.
- [ ] Confirm that opposing-player contact requires GM approval and GM visibility; a superior's permission is required only when a higher player-controlled role actually exists.
- [ ] Confirm the selected Discord server is used for game communication and is separate from personal chat; the shared map may use another tool.
- [ ] Explain that the 08:00–22:00 clock remains live while player attention may be brief or extended.
- [ ] Define how urgent decisions receive response-by times, notifications, and recorded fallback handling.
- [ ] Confirm that full-day-or-longer unavailability uses the separate temporary-command and succession procedure when additional eligible commanders are present.
- [ ] Explain that the game is fictional, infantry-only, and about decisions rather than real-world claims.
- [ ] Complete the five-minute commander identity prompts and confirm each player's roleplay boundaries from the [prototype roleplay layer](17-prototype-roleplay-layer.md).
- [ ] Explain the table safety rule: any participant may pause for a real-world safety concern; the GM records the pause and decides when play resumes after discussing it with the players to confirm everyone is ready.
- [ ] Explain the real-life priority rule: real life always takes precedence. At the GM's discretion, consulting players where practical, the GM may pause, suspend, place the game on hiatus, otherwise adjust play, or end a session. The GM records and preserves the game state and decides when play resumes after discussing it with the players to confirm everyone is ready.

### Setup checklist: 2. Prepare the table

- [ ] Name and label every town sector, approach, road, open area, broken ground, and difficult feature on the town-scale map.
- [ ] Prepare one hidden master map showing all starting forces, routes, control states, and scenario conditions.
- [ ] Prepare one filtered map or status sheet for each commander showing only their starting information.
- [ ] Place each company's markers and record the company's starting strength/readiness summary plus each marker's starting location and current order.
- [ ] Before marker placement, record the actual number of echelons used by each company for this test; keep those counts fixed for the session.
- [ ] Define balanced but asymmetric hidden starting zones and the readiness condition for each side.
- [ ] Give each commander only their own permitted zone and readiness information.
- [ ] Review each commander's proposed force-marker placement and require revision if it creates an unfair immediate advantage, such as placing all of the company's subordinate-unit markers directly on the objective.
- [ ] Record approved starting locations and readiness privately on the master map before revealing the scenario clock.
- [ ] Choose the starting weather and visibility; write the choice in the master log.
- [ ] Publish the primary objective, the three control states (controlled, contested, and uncontrolled), and both secondary conditions (Preservation and Evacuation) to both commanders before the first order.
- [ ] Put the movement aid, routine action aid, order form, report format, and victory conditions where they can be used.
- [ ] Put the prototype contact procedure, contact register, and response-window aid where they can be used.
- [ ] Confirm that every player directly impacted by a combat or contested-action outcome can see the resolution roll; keep hidden information and unrevealed situation bands or modifiers under GM control.
- [ ] Explain standing behaviors, approve any original behavior before acceptance, and require a trigger, action, limits, expiry/cancel condition, and unreachable fallback.

### Setup checklist: 3. Open the authoritative records

Create a master record with these fields:

```text
Scenario date:
Local time zone:
Current day and time:
Weather and visibility:
NATO echelon count:
Russia echelon count:
Public control state:
Order register location:
Report register location:
Master-map version:
Open rulings/questions:
```

Give each order, report, map update, and ruling a sequential ID. Record the source, time, affected side, and whether information is public, private, confirmed, reported, or suspected.

### Setup checklist: 4. Start the first active day

- [ ] Announce Day 1, the current time, weather, visibility, and public control state.
- [ ] For a first human test, confirm that the session ends after the Day 1 final control-state check at 22:00.
- [ ] If a multi-day prototype test is being run later, reconcile each order paused overnight using its recorded remaining time.
- [ ] Give each commander a private briefing with friendly status, known reports, current orders, pending decisions, and the next deadline.
- [ ] Confirm each commander received the briefing before accepting a new order.
- [ ] Start the visible active-window timer.

### Setup checklist: 5. Run live play

- [ ] Time-stamp orders in arrival order and acknowledge or return incomplete orders promptly.
- [ ] Start routine timers only after an order is accepted.
- [ ] Let commanders resolve predictable, uncontested actions with the timing aid.
- [ ] Stop a routine timer when contact, opposition, a blocked route, or uncertain control appears.
- [ ] Validate any triggered behavior against its accepted trigger, limits, expiry, and fallback before executing it.
- [ ] Create a contact record, send separate reports, and set a response-by time.
- [ ] Request each commander's current force-status submission; verify it against the authoritative log and observed outcomes before changing the master state.
- [ ] Adjudicate contested movement, combat, observation, and capture using the transparent prototype contact sequence.
- [ ] Show the resolution roll to every directly impacted player without exposing hidden information or unrevealed GM assessments.
- [ ] Record posture, preparation, commitment, result pair, and graduated consequences before updating the map.
- [ ] Update the master map first, then send only the appropriate filtered update to each side.
- [ ] Send reports when the relevant side could reasonably receive them, including confidence and possible staleness.
- [ ] Give urgent requests a response-by time; if it expires, use the recorded standing instruction or fallback and log the decision.
- [ ] State and record a temporary ruling when the packet does not cover an edge case; apply it symmetrically.

### Setup checklist: 6. Close the first active day

- [ ] At 22:00, stop all timers and record remaining time and current conditions.
- [ ] Resolve only actions completed by the exact deadline.
- [ ] Publish the public end-of-day note and any control changes.
- [ ] Save the order register, report register, decisions log, and dated master-map snapshot.
- [ ] Confirm that the first human session has ended after the final control-state check.
- [ ] For a later multi-day test, confirm the next 08:00 restart time and any player handoffs.

### Setup checklist: 7. End the scenario

- [ ] For the first human test, apply the Day 1 primary result after the final control-state check.
- [ ] For a broader seven-day test, at the end of Day 7's active window, stop timers and resolve actions completed by the exact deadline.
- [ ] Record the final master-map state and control state.
- [ ] Apply the published primary result, then determine whether either side achieved any of the secondary conditions.
- [ ] Send both commanders the same public result and their final private status.
- [ ] Preserve the logs and list unresolved questions for the playtest report.
## Final preflight

Use this as the final go/no-go gate after the initial briefing and communication
dry run. The GM should not accept the first operational order until every
blocking item is checked or a temporary workaround is recorded and accepted by
both commanders.

### Final preflight: Established rules to verify

- [ ] The first human test is one scenario day (Day 1); the broader prototype remains compatible with seven scenario days for later multi-day tests.
- [ ] The shared clock is 08:00–22:00 active; 22:00–08:00 is frozen only when a multi-day prototype test continues overnight.
- [ ] Everyone understands that real life always takes precedence. At the GM's
      discretion, consulting players where practical, the GM may pause, suspend,
      place the game on hiatus, otherwise adjust play, or end a session. The GM
      records and preserves the game state and decides when play resumes after
      discussing it with the players to confirm everyone is ready.
- [ ] Flexible player attention is supported; accepted orders continue during
      brief absences, subject to response windows and fallbacks.
- [ ] The sides are one NATO infantry company and one Russian infantry company,
      with one commander per side and one neutral GM.
- [ ] The selected NATO and Russia echelon counts are recorded before marker placement and remain fixed for this test.
- [ ] Brackenford's authoritative map, named sectors, approaches, and control
      pairs are available.
- [ ] Town control is understood as both central control pairs held without
      opposing contest.
- [ ] Standing behaviors and the order lifecycle are understood.
- [ ] The prototype combat and contested-action procedure is available and will
      be used for contact, not an invented detailed combat system.
- [ ] The scope excludes vehicles, artillery, air support, cyberwarfare,
      national politics, and detailed equipment.

### Final preflight: GM completion fields

```text
Scenario label (no calendar date):
Shared local time zone:
Starting scenario day/time:
GM:
NATO commander:
Russia commander:
NATO echelon count:
Russia echelon count:
Temporary-command contacts (if applicable; otherwise N/A):
Weather and visibility:
Master map version/link:
NATO filtered map/link:
Russia filtered map/link:
Order register/link:
Report register/link:
Contact register/link:
Decision/ruling log/link:
Backup location:
Real-life pause/hiatus procedure:
```

### Final preflight: Blocking readiness checks

#### Final preflight: People and authority

- [ ] Both commanders understand their authority and information limits.
- [ ] In the two-player arrangement, succession and temporary command do not
      apply and no succession contacts are required. If a side has additional
      eligible commanders, the GM has named primary and backup same-side
      succession contacts, recorded the selection tier and handoff path, and
      confirmed that each contact will receive only the absent role's earned
      information.
- [ ] The GM has explained the real-life priority rule, GM discretion,
      pause/hiatus recording, game-state preservation, and that the GM decides
      when play resumes after discussing readiness with the players.
- [ ] Both commanders have received and acknowledged their private briefing.

#### Final preflight: Map and hidden information

- [ ] The digital Brackenford map matches the authoritative ASCII specification.
- [ ] The GM master map contains all forces, hidden zones, conditions, control,
      routes, and map version information.
- [ ] Each filtered view contains only public terrain, earned information, and
      that commander's friendly information.
- [ ] Hidden starting zones are balanced but asymmetric, and neither force starts
      in a central control pair.
- [ ] Each commander has proposed placement and the GM has recorded approval.
- [ ] Weather, visibility, strength, readiness, and starting conditions are
      recorded before the clock starts.

#### Final preflight: Communication and records

- [ ] The Discord group channel and role-based GM-visible channels passed the
      dry run.
- [ ] Orders, reports, contacts, rulings, and map updates have sequential IDs.
- [ ] The GM can timestamp submissions and preserve the authoritative record.
- [ ] Notification and backup notification methods are tested.
- [ ] No required game action depends on personal chat.

#### Final preflight: Rules and aids

- [ ] The order form, timing aid, control rule, report format, and commander
      status form are available to everyone who needs them.
- [ ] The GM has the combat sequence, outcome guide, and contact response-window
      aid ready.
- [ ] The GM has confirmed that the first human test ends with the Day 1 final
      control-state check at 22:00. For a later multi-day test, the GM also knows
      how 22:00 freezes timers and how 08:00 resumes them.
- [ ] Standing behaviors have been reviewed for trigger, action, limits, expiry,
      and unreachable fallback.
- [ ] Any temporary ruling needed before play is written, neutral, and
      symmetrical.

### Final preflight: Go/no-go decision

```text
Readiness result: GO / NO-GO
Packet version and commit:
Scenario start: Day 1, 08:00
First-test end: Day 1, 22:00
Scenario local time zone:
Blocking item(s), if any:
Temporary workaround and expiry:
Both commanders agree to proceed: yes / no
GM authorization time (scenario day/time):
First accepted order ID:
```

If the result is **NO-GO**, record the blocker and do not start a timer or
reveal the scenario clock. If the result is **GO**, publish the public briefing,
send the private briefings, and accept the first order through the normal order
lifecycle.
## External checks

Complete this with the actual GM and participants. Repository preparation does
not prove any item below is complete.

### External checks: Discord

- [ ] Create a game-only server or isolated channel group.
- [ ] Add GM, NATO commander, and Russia commander roles. If an observer participates, add the observer role as an optional support role.
- [ ] Create group, NATO-private, Russia-private, approved opposing-contact, and
  GM-record channels.
- [ ] Set read, post, attachment, history, and mention permissions for each
  role; test with harmless messages.
- [ ] If an observer participates, confirm the observer can read every game
  channel and record (read-only audit access) and cannot post in those
  channels. The only posting exception is a text-only reply to a GM-placed
  question in `#observer-response`; observers are playtest-only.
- [ ] Confirm personal direct messages are not part of the record.
- [ ] Freeze all role and channel permissions before the first order; make no
  permission changes until the playtest ends.
- [ ] Test primary and backup notification methods and response-by reminders.

### External checks: Shared map

- [ ] Reproduce Brackenford labels, sectors, approaches, and control pairs from
  the authoritative map document.
- [ ] Treat the repository-built static PNG renderer as the **proposed**
  #15 method only; the platform choice remains pending user confirmation and
  human leak testing.
- [ ] The GM machine is the user's PC with Python 3.12.10 available as
  `py -3`; Pillow is not installed yet. Install it with
  `py -3 -m pip install -r requirements-map.txt` from the repository root.
  Copy the fictional fixture to `%USERPROFILE%\OliveDrabPrivate\game.toml`
  outside the repository and replace **all test content** before real use.
  From the repository root, complete an unaided `--check` and real render
  using the concrete commands in the
  [build sheet](shared-map-build-sheet.md).
- [ ] Keep the private game TOML, master snapshots, and backup outside the
  repository and Discord. Write `updated_at` and `released_at` with the
  shared local time-zone offset (for example, `-07:00`). Confirm the exact
  Discord text-channel names match the renderer's posting manifest.
- [ ] Render a GM-master PNG and separate filtered NATO and Russia PNGs with
  captions; the master is for `#gm-map-record` only.
- [ ] Test renderer inclusion and filtering with fictional markers: each
  side PNG and caption contains only public and earned side-visible data,
  never opposing live markers, hidden zones, GM notes, `source_id`, opposing
  `marker_id`, or master descriptions. Verify the side PNG shows friendly
  `cite` and opposing `release_id` and `released_at`, with list entries
  tagged OWN or OPP; the text caption repeats only those own and released
  record lines under a confidence legend, then the released descriptions.
  Verify NATO `release_id` values use `R-N-###` and Russia values use
  `R-R-###`, each counting only its own side's releases so neither exposes
  the other's release count.
  Downscale each side PNG to 400px wide and confirm the marker list is
  readable. Moving a live marker must not silently update
  an older released report.
- [ ] Test Discord permissions with each actual commander account: each sees
  only its own private channel, not the opposing channel or
  `#gm-map-record`. If used, the Observer has read-only audit access to all
  needed channels and cannot post there; only text replies to GM-placed
  questions in `#observer-response` are allowed.
- [ ] Inspect generated PNGs and captions against the manifest: side,
  version, banner, filename, and channel must agree. Inspect superseded
  Discord posts for leaks and distinguish newer versions; neither posts nor
  `#gm-map-record` serve as the private master backup.
- [ ] Test screen sharing of a filtered view without exposing the master,
  other side, thumbnails, notifications, or private paths.
- [ ] With each commander's actual account, verify that a phone displays
  that side's PNG legibly and cannot see the opposing side or master channel.
- [ ] Use the [build-sheet pre-post checklist](shared-map-build-sheet.md)
  for one-file/one-channel posting, and stop all further posts on a
  wrong-channel incident until the GM ruling is recorded. Deletion is not
  a fix; corrected re-posts require a new version.
- [ ] Record map version, exact channel names, access list, snapshot method,
  private backup location, restore result, and leak-test results.

### External checks: Record and notification check

```text
Discord/server:
Map platform:
Shared local time zone:
Primary notification:
Backup notification:
Response-deadline test result:
Map access test result:
Permissions blocker/workaround:
Observer used: yes / no
GM sign-off:
```

Never paste real personal contact details into public repository files.
## Readiness guide

This guide turns the existing GM packet into a human-facing readiness gate. It
does not change the Phase 3 rules. The GM owns the final go/no-go decision and
the authoritative record.

### Readiness guide: 1. People, roles, and contact

- [ ] Confirm one neutral GM, one NATO commander, and one Russia commander. These three roles are the defined minimum first-test arrangement.
- [ ] If an observer is available, optionally assign one for the playtest only. The observer watches and documents, does not count as a required fourth participant, and is not part of the final actual game. Use the limited GM-placed question and text-only `#observer-response` reply path described in [External checks: Discord](#external-checks-discord); no posting in other game channels.
- [ ] Record preferred display names only; no personal details are required.
- [ ] Record the shared local time zone and the first human test start/end as
  scenario day and time on the shared clock: Day 1, 08:00 through 22:00. The
  prototype does not require exact calendar dates.
- [ ] Record the notification method, backup notification method, and who
  checks response deadlines. Test both methods.
- [ ] If a side has additional eligible commanders, name a primary and backup
  same-side succession contact. Record role, contact route, handoff start/end,
  and that the contact receives only the absent role's earned information. In
  the two-player arrangement, succession and temporary command do not apply and
  no succession contacts are required.
- [ ] Confirm the real-life pause/hiatus signal and who may invoke it. A
  pause, suspension, hiatus, adjustment, or end is allowed when real life
  requires it; the GM preserves the state, discusses readiness with the players,
  decides when play resumes, and records the restart or closure.
- [ ] Confirm a player may withdraw without explaining personal circumstances.
  The GM records only the operational consequence needed for continuity.

### Readiness guide: 2. Discord roles, channels, and permissions

Create a game-only server or game-only channel structure. Personal direct
messages are never an order, report, ruling, map update, or notification.
Use the [Discord build sheet](discord-build-sheet.md) for UI steps, the
permission matrix, and the human verification script; the
[collaborative setup agenda](collaborative-setup-session-agenda.md) assigns
the live setup and review actions.

| Role or channel | Required access |
|---|---|
| GM | All game channels, master record, master map, and private views |
| Observer | Read-only access to every game channel and record, including both private side channels, GM records and the master map, as a playtest auditor; never reveals private or GM-only information to either commander; playtest-only watch/document role; only text replies to GM-placed questions in `#observer-response` |
| NATO commander | Group channel, NATO private channel, and permitted same-side path |
| Russia commander | Group channel, Russia private channel, and permitted same-side path |
| Group channel | Both commanders and GM; public updates and non-sensitive procedure |
| NATO private | NATO commander and GM; no Russia access |
| Russia private | Russia commander and GM; no NATO access |
| Opposing-contact path | GM approval and GM visibility in the first prototype; superior permission applies only when a higher player-controlled role exists |
| GM record channels/files | GM only, with an explicit backup location |

- [ ] Complete the permission tests and freeze in
  [External checks: Discord](#external-checks-discord), including harmless
  messages and files and the limited Observer reply exception. The
  [Discord build sheet](discord-build-sheet.md#human-permission-and-delivery-rehearsal)
  also requires actual-account and privileged-owner/administrator checks;
  GM preview alone is not verification.
- [ ] Verify that no commander can view the master map, opposing private
  reports, hidden starting zone, or GM-only conditions.
- [ ] Complete the primary/backup notification and response-by reminder test
  in [External checks: Discord](#external-checks-discord).
- [ ] Record channel names and the result in the dry-run completion fields.

### Readiness guide: 3. Shared map and filtered views

Use the [shared map build sheet](shared-map-build-sheet.md) for the exact
source transcription, filtered-view and leak checks, and snapshot fields.

- [ ] Reproduce the authoritative six-column by five-row Brackenford map,
  labels, approaches, terrain, and control pairs exactly.
- [ ] Create one GM master view containing all forces, hidden conditions,
  orders, control, and map version.
- [ ] Create filtered NATO and Russia views with public terrain, own status,
  earned information, and clearly labelled suspected positions only.
- [ ] Verify that hidden markers and stale private reports cannot leak through
  layers, links, exports, or screen sharing.
- [ ] Record the map version, snapshot method, and backup location.

### Readiness guide: 4. Records and scenario briefing

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
- [ ] Explain the active-day end at 22:00, response windows, standing behavior
  fields, and that silence never authorizes an unlisted attack. The overnight
  freeze and next-day restart are broader prototype procedures, not required
  first-test steps.
- [ ] Complete the separate [communication rehearsal](human-communication-order-rehearsal.md).

### Readiness guide: 5. Consent, safety, and real-life priority

Before role assignment, deliver the [participant briefing](consent-safety-participant-briefing.md).
Confirm privately, without requiring disclosure, that each participant can:

- opt out, pause, take a break, or withdraw at any time;
- keep personal identity, health, schedule, and other private details private;
- decline roleplay content or request a lower-intensity presentation; and
- ask the GM to stop or change the activity for a real-life safety concern.

The fictionalized setting is not a statement about real nations or current
events. Keep tactical information inside the game record and do not request
real operational, political, or personal information.

### Readiness guide: 6. First-test clock and continuity

- [ ] Record the first human test start at Day 1, 08:00 in the shared local
  time zone.
- [ ] Run the active test window through Day 1, 22:00 and perform the final
  control-state check before closing the session.
- [ ] If the session reaches a real-life pause before 22:00, preserve the state
  and record the restart/closure according to the pause procedure.
- [ ] Do not extend the first human test into additional scenario days solely
  to satisfy the broader seven-day prototype schedule.
- [ ] For longer rehearsal only, use the existing 22:00 freeze and 08:00
  restart. Use same-side succession only when additional eligible commanders
  are present; it does not apply to the two-player arrangement.

### Readiness guide: Final go/no-go

The GM records `GO` only when every blocking item above is checked or a
temporary workaround is written and accepted by both commanders. Use the
single [final preflight decision record](#final-preflight-gono-go-decision),
which includes the packet version/commit, shared zone, Day 1 start/end,
unresolved blocking items, workaround/expiry, both commanders' agreement,
GM authorization time, and first accepted order ID.
If the result is `NO-GO`, do not reveal the scenario clock or start a timer.
