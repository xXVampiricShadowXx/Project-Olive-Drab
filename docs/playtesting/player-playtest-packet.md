# Player Playtest Packet

A plain-language guide to everything you need to know before the **first
supervised human playtest** of Olive Drab. It covers three audiences:
**Commanders** (NATO and Russia), the **GM**, and optional **Observers**.

> **This packet adds no rules.** Every summary below restates and links an
> existing document. If anything here seems to differ from the linked source,
> **the source wins**. Human-playtest validation of the packet remains
> **pending**: no human test has been completed yet.

The repository does not provide a Discord server, shared map, notification
service, or player roster. Those are set up outside the repository by the GM
and are not assumed to exist ([manifest: known
limitations](human-playtest-packet-manifest.md#known-limitations)).

## Start here

| You are... | Read first | Then |
|---|---|---|
| **Commander** (NATO or Russia) | [Everyone](#1-everyone-read-this) and [Commanders](#2-commanders) below | Your private role sheet and briefing from the GM; keep the [quick reference](../assets/quick-reference.md) open during play |
| **GM** | [Everyone](#1-everyone-read-this) and [GM](#3-game-master-gm) below | The full [prototype packet index](../game-design/09-prototype-packet-index.md) in its read order, then the [readiness guide](human-playtest-readiness-guide.md) |
| **Observer** (optional) | [Everyone](#1-everyone-read-this) and [Observers](#4-observers-optional) below | The [observer event ledger template](observer-event-ledger-template.md) |

New to the project? The short [participant onboarding
packet](participant-onboarding-packet.md) and the [first human test quick
start](../game-design/19-first-human-test-quick-start.md) are good companions.

---

## 1. Everyone: read this

### What the test is

- A **fictionalized**, live-supervised, infantry-only wargame around the town
  of **Brackenford**. It is not a statement about real nations, current
  events, or real military capability
  ([participant briefing](consent-safety-participant-briefing.md);
  [scenario](../game-design/05-first-prototype-scenario.md#boundaries)).
- **People:** one NATO company commander, one Russia company commander, and
  one neutral GM. An observer is optional and is not a required fourth
  participant ([readiness guide §1](human-playtest-readiness-guide.md#1-people-roles-and-contact)).
- **Forces:** each commander directs one infantry company represented by 1–4
  echelon force markers; the count is recorded at setup and stays fixed
  ([scenario](../game-design/05-first-prototype-scenario.md#initial-sides)).
- **Objective:** secure and hold the town through the end of Day 1 under the
  published control rule
  ([control and victory](../game-design/08-control-and-victory-conditions.md#primary-result-for-the-first-human-test)).
- **What it tests:** communication, command decisions, timing, and the GM
  record ([onboarding packet](participant-onboarding-packet.md)).

### What the test is not

- Not a balance verdict; the first test does not require one
  ([onboarding packet](participant-onboarding-packet.md#what-feedback-is-useful)).
- Not a full combat simulation. There are no vehicles, artillery, air
  support, cyberwarfare, national politics, or detailed equipment
  ([packet boundaries](../game-design/09-prototype-packet-index.md#packet-boundaries)).
- Not a multi-day campaign. The broader seven-day clock and overnight freeze
  exist for later tests and rehearsal only
  ([operating procedure: campaign clock](../game-design/06-prototype-operating-procedure.md#campaign-clock)).
- Not a release. The packet is a preparation package
  ([manifest](human-playtest-packet-manifest.md#packet-identity)).

### The time window: Day 1, 08:00–22:00

- The test runs **Day 1, 08:00–22:00** on the shared scenario clock, in the
  shared local time zone. No calendar dates are part of the rules
  ([operating procedure](../game-design/06-prototype-operating-procedure.md#campaign-clock)).
- Scenario time runs at the same rate as real time: one real-time minute equals
  one scenario-clock minute. The overnight freeze pauses actions and timers, not
  the progress of scenario time
  ([campaign clock](../game-design/06-prototype-operating-procedure.md#campaign-clock)).
- The clock stays live during that window, but **your attention can be
  flexible**: check in briefly or stay for long stretches. The GM keeps
  processing accepted orders while you are away
  ([operating procedure](../game-design/06-prototype-operating-procedure.md#command-hierarchy-and-unit-terminology)).
- At **22:00** the GM performs the **final control-state check** and the
  session closes. Orders and response deadlines do **not** carry into a
  second day ([quick reference](../assets/quick-reference.md#active-day-procedure)).

### Consent, safety, pause, and withdrawal

From the [consent and safety briefing](consent-safety-participant-briefing.md#consent-and-real-life-priority):

- **Participation is voluntary.** You may pause, take a break, withdraw, or
  ask for a change **without giving a personal reason**.
- **Real life always comes first.** Illness, work, caregiving, emergencies,
  accessibility needs, or private obligations are enough reason to pause or
  leave.
- Use the agreed **pause/hiatus signal**, or contact the GM by the safest
  available route.
- The GM records only the game consequence (for example, `commander
  unavailable`), never your personal circumstances.
- A pause is not a failure and needs no apology. It must not create an in-game
  advantage or disadvantage
  ([roleplay layer: safety](../game-design/17-prototype-roleplay-layer.md#safety-and-consent-expectations)).
- Roleplay is optional. You may decline a prompt, fade to black, summarize, or
  ask for a neutral presentation
  ([roleplay layer: safety](../game-design/17-prototype-roleplay-layer.md#safety-and-consent-expectations)).
- The GM may pause, suspend, place the game on hiatus, adjust, or end play at
  their discretion, consulting players where practical, and preserves the
  game state ([briefing template](../game-design/14-initial-scenario-briefing-template.md#established-rules-do-not-rewrite-at-briefing)).
- The GM decides when play resumes after discussing it with the players to
  confirm everyone is ready
  ([consent and real-life priority](consent-safety-participant-briefing.md#consent-and-real-life-priority)).

Before starting, the GM asks each participant for a simple confirmation. It is
not a waiver and should not include personal information
([participant briefing: before starting](consent-safety-participant-briefing.md#before-starting)):

```text
I understand the fictional scope, information boundaries, pause/withdrawal
option, and real-life priority rule. I know how to contact the GM privately.
```

### Channels and conduct

The test plans to use a Discord server set up by the GM. Until the GM confirms
it, treat it as **not yet available**. The planned structure is
([communication and chain of command](../game-design/06-prototype-operating-procedure.md#communication-and-chain-of-command);
[readiness guide §2](human-playtest-readiness-guide.md#2-discord-roles-channels-and-permissions)):

| Channel | Who | Used for |
|---|---|---|
| Group channel | Both commanders and GM | Public updates, non-sensitive game talk, rules procedure |
| Side-private channel | One commander and GM | Orders, reports, private status |
| Opposing-contact path | Only with GM approval and GM visibility | Any contact with the other commander |

Conduct basics:

- **Keep game talk in game channels.** Personal direct messages are never an
  order, report, ruling, map update, or notification
  ([readiness guide §2](human-playtest-readiness-guide.md#2-discord-roles-channels-and-permissions)).
- **Use a display or role name.** Do not share personal, health, political,
  or real-world operational information
  ([onboarding packet](participant-onboarding-packet.md#before-play)).
- **Do not share** another side's private reports, hidden map, or GM-only
  conditions, or post screenshots or transcripts outside the agreed group
  without removing private and identifying details
  ([participant briefing: information boundaries](consent-safety-participant-briefing.md#information-boundaries)).
- **Keep player knowledge and character knowledge apart.** You can always say,
  "My commander does not know that"
  ([roleplay layer](../game-design/17-prototype-roleplay-layer.md#information-and-roleplay-boundaries)).

### What feedback is useful

Report **what happened** separately from **what you think should change**
([onboarding packet](participant-onboarding-packet.md#what-feedback-is-useful)).
Useful topics include:

- confusing order fields or missed notifications;
- unclear authority or timing friction;
- decisions that felt meaningful (or did not);
- role gaps, accessibility concerns, or safety concerns.

Findings are routed through the [feedback, issue, and revision
framework](feedback-issue-revision-framework.md) and recorded in the
[playtest report template](playtest-report-template.md). Remove names and
personal details before anything is shared outside the group.

---

## 2. Commanders

This section is the same for both sides. Your **side-specific** strengths,
limitations, starting zone, readiness, and private notes come only from your
**private role sheet and private briefing** from the GM
([commander role sheets](../game-design/11-commander-role-sheets.md);
[private side briefing](../game-design/14-initial-scenario-briefing-template.md#private-side-briefing)).
Do not share that private material with the other side.

### Your role and authority

From [what commanders do](../game-design/04-game-master-and-player-roles.md#what-commanders-do)
and [shared commander instructions](../game-design/11-commander-role-sheets.md#shared-commander-instructions):

- You command **one infantry company** and directly control its **1–4 echelon
  units**. Each unit is one **force marker** on the map.
- You choose **priorities, routes, formations, positions, and timing** within
  the published objective.
- You **cannot** see the master map, and you may not treat a suspicion as a
  confirmed fact.
- You use the reference aids for **predictable, uncontested** actions. The GM
  handles contact, contest, hidden information, and edge cases
  ([division of calculations](../game-design/04-game-master-and-player-roles.md#division-of-calculations)).
- Before play, spend about five minutes on a light commander identity (name,
  style, motivation, one strength, one complication). It shapes how you play,
  **not** the rules or results
  ([minimum commander creation](../game-design/17-prototype-roleplay-layer.md#minimum-commander-creation)).

### Writing and sending orders

Send orders to the GM in your designated game channel using **every standard
field** ([minimum order form](../game-design/06-prototype-operating-procedure.md#minimum-order-form);
[order card](../game-design/11-commander-role-sheets.md#order-card)):

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

Tips drawn from the [order lifecycle](../game-design/06-prototype-operating-procedure.md#order-lifecycle):

- **One purpose per order**, addressed to one specific unit. The GM may assign
  the Order ID if you leave it blank.
- The lifecycle is **draft → submitted → acknowledged → accepted or returned →
  in progress → resolved**.
- **Acknowledged is not accepted.** An incomplete or contradictory order is
  returned with one clear question, and its **timer does not start** until you
  resubmit.
- **One active operational order per unit.** A new accepted order for that
  unit replaces the old one, including its behaviors, unless the GM records a
  non-conflicting concurrent action.
- You may clarify an order before it starts. **A changed objective is a new
  order**, and you cannot rewrite an action after learning its result
  ([fairness and continuity](../game-design/06-prototype-operating-procedure.md#fairness-and-continuity-rules)).

#### Standing behaviors (for when you step away)

You may attach behaviors to a movement or position order so a unit can act
while you are away. The listed behaviors are **Continue, Prepare, Observe and
report, Hold, Probe, Withdraw, and Engage**. Original behaviors need GM
approval before acceptance. Each behavior must state
([behaviors and standing orders](../game-design/06-prototype-operating-procedure.md#behaviors-and-standing-orders)):

```text
Trigger:
Action:
Limits:
Expiry or cancel condition:
If commander cannot be reached:
```

The GM validates every trigger. **Silence never authorizes an unlisted attack
or unlimited commitment.**

#### Asking the GM a question

Use the labelled question format on your role sheet
([questions for the GM](../game-design/11-commander-role-sheets.md#questions-for-the-gm)).

### Timing basics

Use the movement and routine-action tables in the
[timing aid](../game-design/07-timing-and-action-aids.md#movement-aid) and
[quick reference](../assets/quick-reference.md#common-actions--their-effects).
In short:

- Times apply to **each ordered unit** moving along a known, uncontested route.
- For multi-sector routes, **add each sector's time**, then round up to the
  next 15-minute multiple if needed. Do not use one terrain value for the
  whole route when sectors differ.
- Weather and visibility adjustments are listed in
  [conditions and adjustments](../game-design/07-timing-and-action-aids.md#conditions-and-adjustments).
- Times say **how long an uncontested attempt takes**, not that it succeeds.
- You calculate route time, expected completion, and whether an order reaches
  22:00. You **do not** calculate hidden enemy positions, combat outcomes,
  surprise, or disputed control
  ([what commanders calculate](../game-design/07-timing-and-action-aids.md#what-commanders-calculate)).

### Reading the map and sectors

From [town map and terrain sectors](../game-design/12-town-map-and-terrain-sectors.md#map-identity-and-conventions):

- Brackenford is a **6-by-5 grid**: columns `A`–`F` (west to east), rows
  `1`–`5` (north to south). Each cell is a **named sector**, not a precise spot.
- **Adjacent** means sharing an edge. Diagonal moves go through an
  edge-sharing sector.
- The four map edges are the **named approaches** and the only off-map entry
  or exit points.
- Each sector has a **terrain category** that sets its movement time
  ([terrain table](../game-design/12-town-map-and-terrain-sectors.md#named-sectors-and-terrain-categories)).
- You see **your own** forces, public terrain, public control updates, and what
  your side has earned. Mark guesses as **suspected**; they never overwrite a
  confirmed marker ([information layers](../game-design/12-town-map-and-terrain-sectors.md#information-layers)).
- Reports use three confidence labels: **confirmed**, **reported**,
  **suspected** ([reports and map updates](../game-design/06-prototype-operating-procedure.md#reports-and-map-updates)).

Your permitted starting zone is private and comes in your private briefing.

### Contact and combat (summary)

The full procedure is in [prototype combat and contested
actions](../game-design/13-prototype-combat-and-contested-actions.md). What you
need to know:

- **Contact pauses** the active order for each affected unit; unrelated orders
  continue ([pause and engagement state](../game-design/13-prototype-combat-and-contested-actions.md#pause-and-engagement-state)).
  A distant or uncertain sighting may just be a report
  ([contact triggers](../game-design/13-prototype-combat-and-contested-actions.md#contact-triggers)).
- You get a **separate contact report** with a Contact ID and a **decision
  needed by** time ([information and report flow](../game-design/13-prototype-combat-and-contested-actions.md#information-and-report-flow)).
- Choose one response: **Hold, Probe, Attack, Prepare, Reserve/commit, or
  Withdraw**, and state your objective, posture, and maximum commitment
  ([decision menu](../game-design/13-prototype-combat-and-contested-actions.md#commander-decision-menu)).
- When asked, submit your **engagement status** for each involved unit. The GM
  checks it against the record; it is a claim, not an automatic change
  ([engagement status submission](../game-design/11-commander-role-sheets.md#engagement-status-submission)).
- If your deadline passes, the GM uses your last accepted limits and fallback.
  Silence is never treated as an attack order
  ([response deadlines](../game-design/13-prototype-combat-and-contested-actions.md#flexible-attention-and-response-deadlines)).
- The GM resolves the exchange in a transparent sequence. You **see the dice
  rolls** that affect you, but not hidden facts or unrevealed situation bands
  ([resolution sequence](../game-design/13-prototype-combat-and-contested-actions.md#transparent-gm-resolution-sequence)).
- Consequences are graduated (time, position, readiness, strength, control,
  future options). A **broken** force cannot attack or contest a sector; a
  **depleted** force needs a recorded reorganization period before a
  deliberate attack ([outcome guide](../game-design/13-prototype-combat-and-contested-actions.md#outcome-guide)).

### Control and victory

From [control and victory conditions](../game-design/08-control-and-victory-conditions.md#control-state):

- **Town control** needs a credible infantry presence in **both central
  control pairs**: Market Square (`C3`/`D3`) and Town Hall Quarter
  (`C4`/`D4`), with no opposing eligible force marker contesting a required
  sector.
- **Broken** or formally **withdrawn** markers do not count as present;
  **depleted** or **shaken** markers still count.
- Mill Road Junction (`C2`/`D2`) and Station Street (`E3`/`F3`) are useful
  approach and observation positions, but **do not** give town control.
- Submitting an order, observing, or damaging an enemy marker does not by
  itself give control. Control changes when the GM resolves the action and
  updates the master map.
- **At 22:00** ([first-test result](../game-design/08-control-and-victory-conditions.md#primary-result-for-the-first-human-test)):
  town **controlled** = that side wins the primary objective; **contested** =
  draw on the primary objective; **uncontrolled** = neither side wins it.
- Both secondary conditions (Preservation and Evacuation) are in play and
  published before the first order. After the game ends, the GM determines
  whether either side achieved either of them; they never override the
  primary objective
  ([secondary conditions](../game-design/08-control-and-victory-conditions.md#optional-secondary-conditions-for-testing)).
- **Information discipline** is not a victory condition. It is a standing
  expectation throughout play. The GM records breaches and decides whether
  any consequence applies; no penalty is required, and optional examples are
  provided
  ([consequences for breaches](../game-design/08-control-and-victory-conditions.md#consequences-for-breaches)).
- The victory test is published before the first order
  ([fairness safeguards](../game-design/08-control-and-victory-conditions.md#fairness-safeguards)).

### Absence and succession

- Brief check-ins and missed response windows do **not** by themselves trigger
  succession. Urgent decisions fall back to your last accepted order and
  recorded fallback ([urgent decisions](../game-design/06-prototype-operating-procedure.md#urgent-decisions-and-response-windows)).
- In the two-player game (one commander per side), succession and temporary
  command do not apply, and no succession contacts are required. If a side has
  additional eligible commanders, the GM uses the succession order; temporary
  command **never crosses sides**, and a temporary commander receives only your
  role's earned information
  ([temporary command](../game-design/06-prototype-operating-procedure.md#temporary-command-and-player-absence)).
- When a temporary commander applies and you return, you get the normal role
  handoff, **not** retroactive knowledge.

### Commander before-you-start checklist

- [ ] I have read [Everyone](#1-everyone-read-this) and this section.
- [ ] I have given the GM my consent confirmation and know the pause/hiatus
      signal.
- [ ] I know my channels and that personal DMs are not part of the game.
- [ ] I have my private role sheet and private briefing, and I confirmed
      receipt to the GM
      ([private side briefing](../game-design/14-initial-scenario-briefing-template.md#private-side-briefing)).
- [ ] I proposed my force-marker placement within my zone, and the GM
      recorded approval.
- [ ] I completed the five-minute commander identity and shared it with the GM.
- [ ] I have the order card, status card, and
      [quick reference](../assets/quick-reference.md) handy.
- [ ] I know the control rule and that the session ends at **Day 1, 22:00**.
- [ ] I took part in the [communication and order dry
      run](../game-design/15-communication-and-order-dry-run.md).

---

## 3. Game Master (GM)

You are **neutral**, keep the authoritative record, and do not play to win
([what the game master does](../game-design/04-game-master-and-player-roles.md#what-the-game-master-does)).
Results come from the scenario rules, aids, dice, or clearly stated judgment
calls, not invention.

### Preflight and go/no-go

Run these in order before accepting the first operational order
([packet index: before play](../game-design/09-prototype-packet-index.md#before-play);
[quick start](../game-design/19-first-human-test-quick-start.md#run-the-existing-packet)):

1. Prepare the session with the [GM setup checklist](../game-design/10-gm-setup-checklist.md),
   including recording each side's echelon count **before** marker placement.
2. Complete the [readiness guide](human-playtest-readiness-guide.md): people,
   Discord channels and permissions, the shared map and filtered views,
   records, consent, and the clock.
3. Deliver the [initial scenario briefing](../game-design/14-initial-scenario-briefing-template.md).
4. Run the [communication and order dry run](../game-design/15-communication-and-order-dry-run.md)
   (and, if used, the separate [communication rehearsal](human-communication-order-rehearsal.md)).
5. Pass the [final GM preflight](../game-design/16-final-gm-preflight-readiness-checklist.md).

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
- [ ] Observer (if any) can read every game channel and record but cannot post.
- [ ] Combat sequence, outcome guide, response-window aid, and decision log
      ready.

---

## 4. Observers (optional)

An observer is a **playtest-only support and audit role**. You watch and
document the playtest; do not post in the game unless a commander or GM
interacts with you. You are not a required participant and do **not** direct
either side. There are no observers in the final actual game
([participant briefing](consent-safety-participant-briefing.md#what-participation-means);
[readiness guide §1](human-playtest-readiness-guide.md#1-people-roles-and-contact)).

### What you see

- **Everything.** You have read-only access to every game channel and record,
  including both sides' private channels, the GM records, and the master
  map, so you can audit the whole playtest ([readiness guide §2](human-playtest-readiness-guide.md#2-discord-roles-channels-and-permissions);
  [observer ledger](observer-event-ledger-template.md)).

### The ledger

Use the [observer event ledger template](observer-event-ledger-template.md):

- Fill in the [header](observer-event-ledger-template.md#header), including
  the packet version and rules commit.
- Add **one append-only row per operational event** with a sequential `E###`
  ID. Write `N/A` for fields that do not apply.
- Keep **observed fact** separate from **inference**, and use the confidence
  labels.
- **Never overwrite.** To fix a mistake, add a correction row that links to
  the original.
- At the end, complete the [closeout counts](observer-event-ledger-template.md#closeout-counts).

### Privacy

- **Never reveal** one side's private information, the master map, or GM-only
  notes to either commander, during play or before closeout.
- Keep your ledger access-controlled; it may contain private information
  ([observer ledger](observer-event-ledger-template.md)).
- Do not record personal details or why someone paused or withdrew
  ([redacted observer copies](gm-private-records-and-data-handling.md#redacted-observer-copies);
  [onboarding packet](participant-onboarding-packet.md#consent-and-exit)).

### What not to do

- Do not direct either side, and do not pass any side information it has not
  earned.
- Do not overwrite ledger entries; add a correction row instead.
- Do not share screenshots or transcripts outside the agreed group without
  removing private and identifying information
  ([participant briefing: information boundaries](consent-safety-participant-briefing.md#information-boundaries)).
- Do not use personal DMs for anything related to the game.

---

## 5. Glossary

| Term | Meaning | Source |
|---|---|---|
| **Active window** | 08:00–22:00 on the scenario clock, when orders resolve | [Operating procedure](../game-design/06-prototype-operating-procedure.md#campaign-clock) |
| **Acknowledged** | GM confirms an order is legible; not approval | [Order lifecycle](../game-design/06-prototype-operating-procedure.md#order-lifecycle) |
| **Accepted / returned** | Complete order starts processing / incomplete order goes back with one question | [Order lifecycle](../game-design/06-prototype-operating-procedure.md#order-lifecycle) |
| **Behavior (standing order)** | A trigger-based instruction attached to an order for when you are away | [Behaviors](../game-design/06-prototype-operating-procedure.md#behaviors-and-standing-orders) |
| **Broken / depleted / pressured / fresh** | Strength states for a unit | [Combat: what this tracks](../game-design/13-prototype-combat-and-contested-actions.md#what-this-procedure-tracks) |
| **Steady / shaken / recovering** | Readiness states, separate from strength | [Combat: what this tracks](../game-design/13-prototype-combat-and-contested-actions.md#what-this-procedure-tracks) |
| **Confirmed / reported / suspected** | Confidence labels for information | [Reports and map updates](../game-design/06-prototype-operating-procedure.md#reports-and-map-updates) |
| **Contact** | A situation that pauses an order and needs a decision | [Contact triggers](../game-design/13-prototype-combat-and-contested-actions.md#contact-triggers) |
| **Control pair** | Two sectors that must both be held: `C3`/`D3` and `C4`/`D4` | [Control state](../game-design/08-control-and-victory-conditions.md#control-state) |
| **Controlled / contested / uncontrolled** | The three town control states | [Control state](../game-design/08-control-and-victory-conditions.md#control-state) |
| **Echelon** | The company's immediate subordinate unit (1–4 per company) | [Scenario](../game-design/05-first-prototype-scenario.md#initial-sides) |
| **Filtered view** | A commander's map showing only their own and earned information | [Information layers](../game-design/12-town-map-and-terrain-sectors.md#information-layers) |
| **Force marker** | The map representation of one subordinate unit | [Map conventions](../game-design/12-town-map-and-terrain-sectors.md#map-identity-and-conventions) |
| **Formal withdrawal** | A successful Withdraw order that exits the map through a named approach | [Broader result and withdrawal](../game-design/08-control-and-victory-conditions.md#primary-result-for-the-broader-prototype) |
| **Master map** | The GM's authoritative map; commanders never see it | [Map and fog of war](../game-design/04-game-master-and-player-roles.md#map-and-fog-of-war) |
| **Response-by time** | Deadline for answering an urgent decision or contact | [Response deadlines](../game-design/13-prototype-combat-and-contested-actions.md#flexible-attention-and-response-deadlines) |
| **Sector** | One named cell on the 6-by-5 Brackenford grid | [Map conventions](../game-design/12-town-map-and-terrain-sectors.md#map-identity-and-conventions) |
| **Temporary ruling** | A recorded, symmetrical GM decision for an uncovered case | [Disputed rulings](../game-design/04-game-master-and-player-roles.md#fairness-and-disputed-rulings) |
| **Unit** | A subordinate element under the current commander's control | [Command hierarchy](../game-design/06-prototype-operating-procedure.md#command-hierarchy-and-unit-terminology) |

## 6. Where the full rule lives

| Topic | Authoritative source |
|---|---|
| Full packet and read order | [Prototype packet index](../game-design/09-prototype-packet-index.md) |
| Test scope and acceptance | [First human test quick start](../game-design/19-first-human-test-quick-start.md) |
| Roles and authority | [Game master and player roles](../game-design/04-game-master-and-player-roles.md) |
| Scenario and sides | [First prototype scenario](../game-design/05-first-prototype-scenario.md) |
| Clock, orders, reports, succession | [Prototype operating procedure](../game-design/06-prototype-operating-procedure.md) |
| Movement and action times | [Timing and action aids](../game-design/07-timing-and-action-aids.md) |
| Control and victory | [Control and victory conditions](../game-design/08-control-and-victory-conditions.md) |
| GM setup | [GM setup checklist](../game-design/10-gm-setup-checklist.md) |
| Commander sheets (private sections) | [Commander role sheets](../game-design/11-commander-role-sheets.md) |
| Map, terrain, information layers | [Town map and terrain sectors](../game-design/12-town-map-and-terrain-sectors.md) |
| Contact and combat | [Prototype combat and contested actions](../game-design/13-prototype-combat-and-contested-actions.md) |
| Briefings | [Initial scenario briefing template](../game-design/14-initial-scenario-briefing-template.md) |
| Dry run | [Communication and order dry run](../game-design/15-communication-and-order-dry-run.md) |
| Go/no-go | [Final GM preflight](../game-design/16-final-gm-preflight-readiness-checklist.md) |
| Roleplay and safety | [Prototype roleplay layer](../game-design/17-prototype-roleplay-layer.md) |
| Recorded clarifications | [Rule-owner decisions](../game-design/18-open-rule-owner-decisions.md) |
| One-page aid | [Quick reference](../assets/quick-reference.md) |
| Consent and safety | [Consent, safety, and participant briefing](consent-safety-participant-briefing.md) |
| Packet files and external setup | [Human playtest packet manifest](human-playtest-packet-manifest.md) |
| Readiness gate | [Human playtest readiness guide](human-playtest-readiness-guide.md) |
| Private records | [GM-only records and data handling](gm-private-records-and-data-handling.md) |
| Observer record | [Observer event ledger template](observer-event-ledger-template.md) |
| Report | [Playtest report template](playtest-report-template.md) |
