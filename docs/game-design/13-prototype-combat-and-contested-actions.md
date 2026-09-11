# Prototype Combat and Contested Actions

This is the minimum contact procedure for the first live Brackenford test. It is
a GM-run, infantry-only, and deliberately abstract. It is not the final real-time
combat system: it does not model weapons, ranges, casualties, formations, or
continuous fire. It tests whether commanders make useful choices when contact
interrupts a timed order and information arrives imperfectly.

## What this procedure tracks

The GM tracks each involved force with five simple states:

- **Position:** current sector, route, and whether the force is in contact.
- **Posture:** moving, probing, holding, attacking, withdrawing, or reorganizing.
- **Preparation:** unprepared, ready, or fortified. Preparation describes time
  spent making a position usable; it is not a permanent bonus.
- **Strength:** fresh, pressured, depleted, or broken. The authoritative strength
  state belongs to each involved **Unit/force marker**. A company-wide summary may
  be recorded separately for narrative context, but it never replaces the
  subordinate-unit strength records used for adjudication.
- **Control and options:** which sectors are controlled or contested, and which
  routes, reserves, or withdrawals remain available.

The GM may also record **readiness** as steady, shaken, or recovering. Readiness
is separate from strength: a force can be intact but shaken, or depleted but
steady. Do not invent numerical modifiers for these states.

Commanders maintain and submit their own current force-status record for an
engagement. It should identify the **Unit** and state position, posture,
preparation, readiness, strength, reserve or commitment, and any active order or
behaviors. This is a commander report, not an automatic state change. The GM
checks it against the authoritative log, map, reports, and observed outcomes
before accepting any correction. Repeat the status record separately for each
involved unit when a commander has more than one unit in the engagement.

## Contact triggers

For each trigger below, pause the active routine timer for **every affected unit** and create a contact record:

1. A force enters a sector containing an opposing force it did not know was
   there.
2. A force observes an opposing force closely enough that movement, control, or
   the current order could be affected.
3. Opposing forces attempt to occupy, pass through, withdraw from, or establish a
   position in the same sector or an immediately relevant adjacent sector.
4. A route, objective, or control pair becomes contested.
5. A commander declares an **Attack**, **Probe**, **Hold**, or **Withdraw** against
   an opposing force.

A distant or uncertain sighting is an information event, not automatically an
engagement. The GM sends a report and continues the timer unless the sighting
changes what the unit can safely do. The GM records the sighting and the reason
for treating it as an information event or as a contact trigger, using the
existing temporary-ruling/record standard when the packet does not otherwise
cover the case. Contact is about a decision being required, not about a marker
merely being nearby.

## Pause and engagement state

When a trigger occurs, the GM records the exact time, current sector, last
accepted order, remaining routine time, and what each side knows. The active order
for **each affected unit** enters **paused—contact**. No movement or preparation
completes while the GM is establishing the engagement, but unrelated orders
continue.

The engagement has three states:

- **Contact:** opposing presence is suspected or confirmed and both sides may
  still choose a response.
- **Engaged:** the GM has received the available responses and resolves the
  current exchange.
- **Disengaged:** opposing forces no longer remain in the same or otherwise
  contested position, or one side has withdrawn, been forced out, or broken;
  the GM resumes, replaces, or closes the paused order after recording the new
  posture and any changed control.

Contact does not mean combat must happen. A commander may choose **Hold, Probe,
Attack, Prepare, Reserve/commit, or Withdraw** from the established decision menu.
If only one side can reasonably act before the other, the GM uses the response
deadline and the last standing instruction rather than waiting indefinitely.

For disengagement after a response exchange, the GM may mark the engagement
**Disengaged** only when the opposing forces no longer share a sector or an
actively contested position and neither side has an **Attack** or **Probe** response
still being executed. A **Withdraw** response counts as disengagement only after
the withdrawal has separated the opposing forces or otherwise ended the contest.
**Hold** or **Prepare** alone does not end contact while the opposing forces still
share or actively contest a position.

An accepted movement or position order may include one or more behaviors that
act when specified conditions occur, allowing play to continue while a commander
is away. Use the behavior rules in the operating procedure. The GM validates the
triggers, expiry conditions, limits, and fallbacks before allowing those behaviors
to act; a triggered behavior that creates contact enters this same paused
engagement state.

## Information and report flow

The GM sends each commander a separate contact report as soon as that side could
receive it. Use the existing confidence labels:

```text
Contact ID:
Unit(s) involved:
Time observed:
Sector or route:
Source:
Observed:
Estimated opposing posture/strength:
Confidence: confirmed / reported / suspected
Decision needed by:
```

The report must distinguish what was seen from what was inferred. A commander
may receive a suspected strength or posture estimate even when the master record
has a different truth. The GM releases later results only when the side could
learn them through its surviving force, observation, or a report.

The GM updates the master map first. Public control changes, friendly status,
and released reports then go to the relevant filtered views. The opposing
marker is not revealed merely because an engagement exists.

## Commander decision menu

For each engagement, a commander chooses one primary response and may state one
limit or fallback:

| Response | Meaning and tradeoff |
|---|---|
| **Hold** | Keep the current sector and posture; preserve strength and information, but concede initiative. |
| **Probe** | Commit limited strength to learn or pressure; preserve a reserve, but risk losing time and position. |
| **Attack** | Commit the main force to gain position or control; may create a decisive advantage, but risks strength and readiness. |
| **Prepare** | Stay in place and improve the position; gains a better future option, but gives the opponent time. |
| **Reserve/commit** | Keep a named portion uncommitted or commit it now; preserves flexibility or increases immediate pressure. |
| **Withdraw** | Leave by a stated route or sector; preserve future options, but give up position or control and may expose the retreat. |

The commander should state the objective (delay, seize, hold, learn, preserve,
or disengage), the intended posture, and the maximum acceptable commitment. A
standing instruction may cover a predictable response, such as “Hold unless
Withdraw is the only way to avoid becoming broken.”

## Flexible attention and response deadlines

The GM sets a response-by time based on the situation, not on continuous
attendance:

- **Routine contact:** 30 active minutes.
- **Immediate close contact or threatened withdrawal route:** 15 active
  minutes.
- **A planned attack or deliberate probe:** use the next decision point stated
  in the contact report; if no specific decision point is stated, use 30 active
  minutes from the time the report is delivered.

For the broader multi-day prototype, the deadline pauses at 22:00 and resumes
at 08:00 with the other active timers. For the **first human test**, Day 1 ends
at the 22:00 final control-state check; the deadline terminates with session
closure and does not implicitly resume on a later scenario day. The GM sends one
reminder when practical. A commander may answer early, give a standing
instruction, or request one extension before the deadline. An extension is
recorded and cannot be used to gain information after the original deadline.

If the deadline expires during an active window, use the unit's last accepted
limits and fallback. If none exists, the GM chooses **Hold** for a unit in a
defensible position, **Withdraw** along the safest available route for a unit
in an untenable position, or **Reserve/commit** only as needed to prevent an
immediate unresolved overlap. Record why; do not treat silence as an attack order.

## Transparent GM resolution sequence

Resolve one exchange in this order and show the sequence to the commanders
after hidden information has been protected:

1. **Freeze the snapshot.** Request each commander's current force-status
   submission. Check both submissions against the authoritative log, then record
   time, sectors, posture, preparation, strength, readiness, control, available
   reserves, routes, active behaviors, and each side's knowledge. Unverified
   self-reported changes remain unconfirmed.
2. **Confirm intent.** Read back each response, objective, commitment, and limit.
   Ask one clarification only if the order cannot be executed safely.
3. **Set the comparison.** Combine the verified portions of both sides'
   status submissions with position/terrain, preparation, commitment, readiness,
   strength, information, and hidden conditions. Identify the single clearest
   immediate advantage and the single clearest countervailing advantage, using
   only verified or deliberately hidden conditions that actually affect this
   exchange. Do not stack multiple speculative advantages or treat an unverified
   self-report as fact.
4. **Choose the uncertainty band.** Start at **even**. Shift one side to
   **favorable** only when its single clearest immediate advantage remains after
   considering the clearest countervailing advantage. Shift the other side to
   **unfavorable** in that same case. If the advantages balance, no single factor
   is clearly decisive, or the GM cannot explain the difference from the recorded
   snapshot, keep both sides **even**. The band describes the situation before
   the resolution aid; it is not a hidden arithmetic bonus.
5. **Use the simple resolution aid.** Roll one six-sided die for each side and
   show each roll to every player directly affected by the outcome. The GM may
   keep hidden information, the comparison, and any unrevealed situation band or
   modifier under GM control; do not reveal those merely to make the roll
   transparent. Add no arithmetic modifier to the visible die. Interpret the
   result with the side's band: 1–2 is a poor result, 3–4 a mixed result, and
   5–6 a strong result; an unfavorable band treats one step worse and a
   favorable band treats one step better, capped at poor/strong.
6. **Compare results and intent.** Map the pair of result categories to one
   existing outcome relationship:
   
   - **Strong vs. poor:** clear edge for the strong-result side.
   - **Strong vs. mixed:** narrow edge for the strong-result side.
   - **Mixed vs. poor:** narrow edge for the mixed-result side.
   - **Matching results (poor/poor, mixed/mixed, or strong/strong):** equal or
     mixed exchange.
   
   Apply the same mapping symmetrically when the other side has the stronger
   result. Use the declared objective and existing response limits to select an
   outcome within that mapped relationship; do not invent a new relationship.
7. **Apply graduated consequences.** Choose one primary consequence and up to
   two linked consequences from the outcome table. Do not eliminate an involved
   force unless the snapshot and prior consequences make continued operation
   implausible.
8. **Update the map and timers.** Mark position, control, posture, strength,
   readiness, preparation, commitment, and any remaining order time for each
   affected unit. Resume a paused order only if its objective and route still
   make sense; otherwise close it and request a new order.
9. **Report and set the next window.** Send each side its result, known
   consequences, confidence, and next decision-by time. Preserve hidden facts
   for later reports.

The dice are an uncertainty aid, not the whole decision. Impacted players see
the resolution rolls, but not necessarily the hidden facts that shaped the
comparison or situation bands. Commander choices, map position, preparation,
commitment, information quality, and consequences must be visible in the record
when the affected side could know them.

### Status submission and behavior record

For each engagement, the GM retains:

```text
Side:
Unit:
Commander-submitted status:
Authoritative status at snapshot:
Verified changes:
Unverified claims:
Active behaviors and triggers:
Behavior actions/limits:
Expiry or cancel conditions:
Unreachable fallbacks:
```

Repeat the behavior fields for each attached behavior as needed. The GM remains
neutral: both commanders use the same verification standard, and neither
self-reported strength, readiness, preparation, position, or commitment becomes
authoritative until supported by the log, map, reports, or observed outcome.

## Outcome guide

Use the deterministic result relationship and the declared objective to select a
result. A less severe outcome may be used only when a recorded snapshot condition
makes the typical outcome inconsistent with an existing tracked state or the
declared limit, and the GM must record that reason.

| Result relationship | Typical outcome |
|---|---|
| Clear edge for one side | The advantaged side achieves its objective or gains the initiative. The other side gives ground, loses readiness, or becomes depleted. |
| Narrow edge | The advantaged side gains position, information, or control pressure, but the opposing force remains capable of responding. |
| Equal or mixed exchange | Both sides remain in contact or one side holds while both pay a time/readiness cost. No automatic capture. |

Possible consequences include:

- **Time:** add 15–60 active minutes, or leave the paused order incomplete.
- **Position:** advance one sector, hold, give ground one sector, or lose a
  route. Do not create halfway positions.
- **Readiness:** steady, shaken, or recovering after a reorganization period.
- **Strength:** fresh, pressured, depleted, or broken. A depleted force must
  withdraw or reorganize before another deliberate attack. The reorganization
  period must be recorded in the affected unit's order/timer record before a
  new deliberate attack begins; use an existing applicable action timing aid,
  or record a temporary ruling when no existing timing aid covers the action.
- **Control:** a sector or control pair becomes controlled, contested, or
  uncontrolled under the existing control rules.
- **Future options:** a reserve is committed, a route is exposed or blocked, a
  withdrawal remains possible, or a new observation/report opportunity is
  created.

After an exchange, a force that is **broken** cannot attack or contest a sector;
it must withdraw or otherwise cease contesting the situation under the scenario's
GM ruling. A **depleted** force can hold or withdraw but needs a recorded
reorganization period before a deliberate attack. These are prototype states,
not casualty tables.

## Withdrawal and disengagement

A withdrawal is an order, not an automatic escape. The commander names a route,
destination, and limit (preserve strength, delay, or avoid further contact).
The GM compares the withdrawal against the opponent's posture and the route's
terrain. A successful withdrawal resumes the movement aid after the engagement
and normally gives up the contested sector.

A **pressured withdrawal** uses the existing result relationship and applies the
least severe existing consequence that still matches the recorded snapshot and
the commander's limit. Apply consequences in this order only as needed:

1. Give ground one additional sector when the named route and current position
   allow it and doing so matches the declared withdrawal limit.
2. If that is not appropriate, reduce readiness one existing step (for example,
   steady to shaken) when the force can absorb that change.
3. If neither position nor readiness can account for the pressure, add the
   existing minimum time consequence of 15 active minutes to the withdrawal or
   remaining paused order.

Do not select a consequence merely for variety; the GM records why the chosen
existing consequence follows from the snapshot and withdrawal limit. A failed
withdrawal leaves the force engaged and may make it depleted or broken.

A withdrawal counts as disengagement only after the opposing forces are no longer
in the same or actively contested position. A failed withdrawal does not
establish disengagement.

When both sides choose **Hold** or **Prepare** while still sharing or actively
contesting a position, the engagement remains active. When both sides choose
**Hold**, **Prepare**, or **Withdraw** and the opposing forces have separated so
that no active contest remains, the GM marks the engagement **Disengaged** and
records the new posture and any changed control. The last accepted orders resume
only after the GM records the new posture and any changed control.

## Prototype boundaries and review questions

This procedure intentionally omits detailed weapons, casualty counts, morale
tests, reinforcements, artillery, vehicles, air support, and simultaneous
real-time micro-orders. The GM must not add those systems during the first test.

After the test, review whether:

- position, posture, preparation, and commitment changed commander choices;
- uncertainty produced useful reports rather than arbitrary surprises;
- mixed results created recoverable setbacks;
- response windows worked for players with flexible attention;
- the GM could resolve an exchange and update both filtered maps without
  excessive delay; and
- combat changed the time, control, strength, readiness, or future options that
  mattered to the town-control objective.
