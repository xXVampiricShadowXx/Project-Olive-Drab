# Communication and Order-Submission Dry Run

Run this rehearsal after the initial briefing and before the first live order.
The dry run verifies delivery, permissions, timestamps, and fallbacks; it does
not create an operational result or reveal hidden information.

## Established rules

- The Discord group channel carries non-sensitive game communication, public
  updates, and rules procedure.
- Private channels must be role-based and GM-visible. They support the
  superior/subordinate communication paths used by the scenario.
- **For the first prototype, opposing-player contact requires GM approval and GM
  visibility. A superior's permission is required only when a higher
  player-controlled role actually exists.**
- Personal direct messages are not part of the game record.
- Every order uses the standard fields and one purpose per order.
- The GM acknowledges receipt, returns incomplete or contradictory orders for
  one clear question, and starts a timer only after acceptance.
- A changed objective is a new order. A clarification does not rewrite a
  resolved result.
- Standing behaviors require a trigger, action, limits, expiry or cancel
  condition, and unreachable fallback.
- **First human test:** urgent decisions have a response-by time, but the
  deadline terminates with the Day 1 22:00 final control-state check; it does
  not pause and resume on a later scenario day.
- **Broader multi-day prototype:** urgent decision deadlines may pause at 22:00
  and resume at 08:00 with the active timers when the scenario actually
  continues into another day. Expiry uses the last accepted limits and fallback.
- Contact reports separate observation from inference and use confirmed,
  reported, or suspected confidence labels.
- Real life always takes precedence. At the GM's discretion, consulting players
  where practical, the GM may pause, suspend, place the game on hiatus, otherwise
  adjust play, or end a session. The GM records and preserves the game state and
  resumes only when appropriate.

## GM completion fields

```text
Discord server:
Group channel:
NATO commander channel:
Russia commander channel:
NATO superior/subordinate path:
Russia superior/subordinate path:
Approved opposing-contact channel/procedure:
Order register:
Report register:
Contact register:
Decision/ruling log:
Notification method:
Backup notification method:
Response-window reminder owner:
```

The GM records channel permissions and verifies that no commander can see the
master map, the opposing side's private reports, hidden starting zones, or
GM-only conditions.

## Dry-run checklist

### 1. Channel and visibility test

- [ ] GM posts a harmless public test message in the group channel.
- [ ] Both commanders can read the group message.
- [ ] GM sends a harmless private test message to each commander.
- [ ] Each commander can read and reply only in the channels appropriate to the
      role-based communication chain.
- [ ] GM can review every private game message and the approved opposing-contact
      path.
- [ ] Personal chat is explicitly excluded from orders, reports, map updates,
      and rulings.
- [ ] GM records the channel names and permission result in the setup record.

### 2. Complete order test

- [ ] Each commander drafts a harmless movement or position order with all
      standard fields.
- [ ] Commander submits it in the recorded order channel.
- [ ] GM records arrival time and assigns a sequential Order ID.
- [ ] GM acknowledges receipt without implying acceptance.
- [ ] GM accepts the complete order and records start time, route, conditions,
      and expected completion.
- [ ] Commander confirms the accepted interpretation.
- [ ] GM demonstrates where the order status and remaining time are recorded.

### 3. Incomplete-order test

- [ ] Commander submits a harmless order with one required field omitted.
- [ ] GM returns it with one clear question and does not start its timer.
- [ ] Commander resubmits the corrected order.
- [ ] GM records the new acceptance and confirms that the timer starts only then.

### 4. Behavior and flexible-attention test

- [ ] Commander submits a harmless accepted order with a listed behavior.
- [ ] The behavior states trigger, action, limits, expiry/cancel condition, and
      unreachable fallback.
- [ ] GM explains how the trigger will be validated and what remains hidden.
- [ ] GM simulates an unreachable commander and records the fallback without
      creating an attack or unlimited commitment.
- [ ] GM cancels or replaces the behavior through a new accepted order and
      records which behavior changed.

### 5. Report, contact, and response-window test

- [ ] GM sends a harmless report with source, observed fact, confidence, and
      possible staleness.
- [ ] Each commander identifies what is observed versus inferred.
- [ ] GM simulates contact, pauses the affected order, and issues separate
      contact reports.
- [ ] Each report includes a Contact ID and response-by time.
- [ ] Commanders submit a harmless response with objective, posture,
      commitment, and limit.
- [ ] GM demonstrates the force-status submission and transparent resolution
      sequence using the prototype combat procedure.
- [ ] GM shows both resolution rolls to affected players without exposing hidden
      information or unrevealed situation bands.
- [ ] GM records the result, consequences, map update, and next decision window.

### 6. Freeze and restart test

- [ ] GM simulates an order and response window crossing 22:00.
- [ ] GM records remaining active time and current conditions at the freeze.
- [ ] GM confirms that no new operational result resolves during 22:00–08:00.
- [ ] GM resumes the recorded remaining time at 08:00 without recalculating it.
- [ ] GM demonstrates the morning private briefing and commander receipt
      confirmation.
- [ ] GM labels this freeze/restart evidence as **broader multi-day prototype
      procedure**, not first-human-test behavior. For the first human test, the
      simulated Day 1 response deadline ends at the 22:00 final control-state
      check instead of resuming on another day.

### 7. Real-life pause and hiatus test

- [ ] GM announces the real-life priority rule and the agreed pause/hiatus signal.
- [ ] GM demonstrates pausing, suspending, placing the game on hiatus, adjusting
      play, or ending a session at the GM's discretion, consulting players where
      practical.
- [ ] GM records and preserves the current game state, including affected timers
      and response windows.
- [ ] GM confirms that play resumes only when appropriate and records the restart
      time and any handoff.

## Dry-run sign-off

```text
Dry run completed at scenario day/time:
GM:
NATO commander:
Russia commander:
Unresolved communication issue:
Temporary workaround recorded:
Ready for final GM preflight: yes / no
```

An unresolved channel or recording failure is a preflight blocker. Do not
substitute personal chat or an invisible private exchange for a missing game
channel.
