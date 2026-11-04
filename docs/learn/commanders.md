# 3. Commander guide

**Non-authoritative summary:** linked governing sections win; this page adds
no rules. Read after [essentials](essentials.md) and
[consent and safety](consent-and-safety.md).

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

An **order** tells one unit what to attempt; **acceptance** means the GM has
approved it for processing, not guaranteed success. A **standing behavior**
is an instruction triggered by a stated situation while you are away.

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
  returned with one clear question. Resubmit it; its timer starts only after
  the GM accepts the order.
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

Example of the distinction: a fictional "Hold" instruction does not authorize
an attack because its commander is absent. Use approved triggers, limits, and
fallbacks, not assumptions about silence.

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

For example, `C3` identifies a sector, not an exact coordinate. A guess about
an opponent there stays **suspected**, not confirmed.

### Contact and combat (summary)

A **contact** needs a GM decision rather than routine timing alone.
**Strength** (fresh, pressured, depleted, broken) and **readiness**
(steady, shaken, recovering) are separate states; see
[tracked states](../reference/prototype/contact-and-combat.md#what-this-procedure-tracks).

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

- [ ] I have read the three public learning pages, including this one.
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

**STOP: public learning is complete.** Finish these operational handoffs with
the GM; do not read all GM/admin/history pages. The
[quick reference](../reference/quick-reference.md) and
[glossary](../reference/glossary.md) are optional live lookups.
