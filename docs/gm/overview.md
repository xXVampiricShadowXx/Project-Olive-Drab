# GM overview

This is a **non-authoritative summary**, not another preparation checklist.
Use the [single GM preparation route](index.md#prepare-in-this-order).
The exact governing sections linked below take precedence; this overview
does not establish new rules or certify external readiness.

## 3. Game Master (GM)

You are **neutral**, keep the authoritative record, and do not play to win
([what the game master does](../game-design/04-game-master-and-player-roles.md#what-the-game-master-does)).
Results come from the scenario rules, aids, dice, or clearly stated judgment
calls, not invention.

### Preflight and go/no-go

The [GM preparation route](index.md#prepare-in-this-order) sequences these
tasks before accepting the first operational order
([packet index: before play](../game-design/09-prototype-packet-index.md#before-play);
[quick start](../game-design/19-first-human-test-quick-start.md#run-the-existing-packet)):

Use that route for setup, readiness, briefing, the dry run and human rehearsal,
and final preflight; it replaces the repeated run order here. Record each
side's echelon count **before** marker placement
([table setup](setup-and-readiness.md#setup-checklist-2-prepare-the-table)).

Record **GO** only when every blocking item is checked or a written temporary
workaround is accepted by both commanders. On **NO-GO**, do not reveal the
scenario clock or start a timer
([go/no-go decision](../game-design/16-final-gm-preflight-readiness-checklist.md#gono-go-decision)).

External items such as Discord, the shared map, and the roster are not
provided by the repository. Mark them complete only when they actually exist
([external setup](human-playtest-packet-manifest.md#external-setup-still-required)).

### What to brief, and when

| When | What | Source |
|---|---|---|
| Before role assignment, and again before the first order | Consent, safety, and participant briefing; collect each confirmation | [Participant briefing](consent-safety-participant-briefing.md) |
| Before the first active window | Five-minute commander identity prompts and roleplay boundaries | [Roleplay layer](../game-design/17-prototype-roleplay-layer.md#minimum-commander-creation) |
| Before marker placement | Each side's private zone and readiness; review and record placement | [Starting zones](../game-design/05-first-prototype-scenario.md#starting-zones-and-readiness) |
| Before the first order | Public briefing script and announcement | [Public briefing script](../game-design/14-initial-scenario-briefing-template.md#public-briefing-script) |
| Before the first order | Each side's private briefing; commander confirms receipt | [Private side briefing](../game-design/14-initial-scenario-briefing-template.md#private-side-briefing) |
| Before the first order | Primary objective and control rule, plus both secondary conditions, published to both commanders | [Fairness safeguards](../game-design/08-control-and-victory-conditions.md#fairness-safeguards) |
| With the first order | The standard order fields, unchanged | [First-order reminder](../game-design/14-initial-scenario-briefing-template.md#first-order-reminder) |

Never expose the master map, the opposing starting zone, GM-only conditions,
or unearned information in a briefing.

### During play and at 22:00

- Follow the [active-window workflow](../game-design/06-prototype-operating-procedure.md#game-master-active-window-workflow):
  time-stamp, acknowledge or return, start timers only on acceptance, validate
  behaviors, adjudicate contact, update the **master map first**, then send
  filtered updates.
- At 22:00, follow the [end-of-scenario
  procedure](../game-design/08-control-and-victory-conditions.md#end-of-scenario-procedure):
  stop timers, resolve only what completed by the deadline, record the final
  map, check the result, send both sides the same public result and their
  private status, and preserve the logs.

### Records and data handling

From the [GM-only records and data handling guide](gm-private-records-and-data-handling.md):

- Keep the master map, hidden information, all registers, and snapshots in an
  **access-controlled working location** with a separate backup.
- Record only what continuity needs. Use display or role names. Do **not**
  record diagnoses, reasons for withdrawal, private conversations, or
  unrelated identifying details.
- **Never** put GM-only records, private briefings, hidden maps, contact
  details, or access links in the repository, issues, PRs, commits, public
  channels, or the curated public feed.
- The observer (if any) has read-only audit access to these records. When
  sharing records beyond the GM and observer, build a redacted copy, label it
  `observer-redacted`, and recheck before sharing.
- Snapshot before a pause, after a major ruling, and at closeout. Delete or
  destroy records after the agreed review period.
- If private information may have leaked: stop sharing, preserve the event ID,
  restrict access, and record the incident without copying the exposed content.

### Rulings for uncovered edge cases

When the packet does not cover a situation
([fairness and disputed rulings](../game-design/04-game-master-and-player-roles.md#fairness-and-disputed-rulings)):

1. State the **temporary** ruling and the factor it is based on.
2. Apply it **symmetrically** to equivalent situations for both sides.
3. Record the gap for post-game review.

Also:

- If an ambiguous case could change the result, state your interpretation
  **before** resolving it
  ([fairness safeguards](../game-design/08-control-and-victory-conditions.md#fairness-safeguards)).
- A commander may ask for a ruling to be recorded for review, but rulings are
  not reopened during live play, and a challenge does not pause the clock.
- **Do not improvise a new mechanic** during play
  ([manifest: known limitations](human-playtest-packet-manifest.md#known-limitations)).
- Do not grant roleplay-based hidden advantages, rerolls, shorter timers, or
  extra forces ([roleplay and rules](../game-design/17-prototype-roleplay-layer.md#roleplay-and-rules)).

### GM checklist

This is an evidence cross-check, not a second preparation route or
independent authorization form. Record the decision in the
[single final preflight record](setup-and-readiness.md#final-preflight-gono-go-decision).

- [ ] Commit SHA recorded at the top of the briefing, observer ledger, and
      report ([packet identity](human-playtest-packet-manifest.md#packet-identity)).
- [ ] Shared local time zone and Day 1, 08:00–22:00 recorded.
- [ ] Echelon counts recorded before marker placement.
- [ ] If either side has additional eligible commanders, primary and backup
      same-side succession contacts are recorded. No succession contacts are
      required in the two-player arrangement.
- [ ] Discord channels and permissions, shared map, and filtered views
      actually exist and have been tested.
- [ ] Private working record, backup, and retention period set **before** the
      first order.
- [ ] Consent confirmations collected; pause/hiatus signal agreed.
- [ ] Public and private briefings delivered and receipts confirmed.
- [ ] Dry run passed; final preflight result is **GO**.
- [ ] Observer (if any) can read every game channel and record but cannot post
      there; only text replies to GM-placed questions in `#observer-response`
      are allowed under the [Discord permission matrix](discord-build-sheet.md#permission-matrix).
- [ ] Combat sequence, outcome guide, response-window aid, and decision log
      ready.

---
