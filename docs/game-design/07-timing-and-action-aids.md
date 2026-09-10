# Timing and Action Aids

The prototype uses a small number of consistent timing bands instead of detailed simulation. Players may resolve predictable actions with these aids; the game master resolves uncertainty, opposition, and exceptions.

## Timing principles

An action timer runs only during the active window. The timer pauses at 22:00 and resumes at 08:00 with the same remaining time. The game master may pause a timer while waiting for a clarification only when the order cannot be interpreted safely; the pause and reason are recorded.

Estimate the base time first, then apply one clear condition adjustment. Do not stack several speculative penalties. If an action is contested or its outcome is uncertain, stop the routine timer and adjudicate it.

## Movement aid

The following bands are a starting aid for one infantry company moving as a formed unit along a known route. They express elapsed active time, not distance precision.

| Route condition | Base time for one map sector | Guidance |
|---|---:|---|
| Road or open ground | 30 minutes | Route is known and uncontested |
| Broken ground, woods, or scattered buildings | 45 minutes | Formation remains coherent |
| Dense town, steep ground, or difficult crossing | 60 minutes | Includes deliberate movement through obstacles |
| Unknown route or forced detour | Add 30 minutes | Game master confirms the new route |

For a route spanning multiple sectors, **add the applicable base time for each sector traversed** and then round the total up to the next 15-minute mark. Do not choose one terrain category for the entire route when sectors differ. An unknown route or forced detour adds 30 minutes after the GM confirms the revised route. A commander may choose a slower deliberate movement, but the order must say so.

## Routine action aid

| Routine action | Active time | Completion condition |
|---|---:|---|
| Change formation or facing | 15 minutes | Unit is not under direct pressure |
| Establish a temporary position | 30 minutes | Unit remains in place and has a defensible position |
| Observe one adjacent sector | 15 minutes | Visibility and terrain permit observation |
| Search a town sector | 30 minutes | Unit can enter and inspect without opposition |
| Resupply from an established friendly point | 30 minutes | Supply point is accessible and uncontested |
| Withdraw one sector | Use the movement aid | Route is available |

These times are not promises that an action succeeds. They only describe how long an uncontested attempt takes. Contact, fire, blocked routes, or a change in conditions moves the action to game-master adjudication.

## Conditions and adjustments

The game master chooses the smallest adjustment that describes the situation:

- **Poor visibility:** add 15 minutes to movement or observation, and reduce what can be confirmed.
- **Heavy rain or comparable weather:** add 15 minutes to movement and preparation.
- **Night:** no action resolves because the prototype is frozen.
- **Readiness or supply problem:** pause the routine timer and request a ruling; do not invent a numerical penalty.
- **Enemy contact:** stop the timer, create a contact record, and use the prototype contact procedure.

Terrain and weather should be visible on the commander reference when they are known. Hidden conditions are communicated through reports or revealed by the game master when they affect an action.

## What commanders calculate

Commanders may calculate:

- A route's estimated active time from the movement table.
- The next expected completion time.
- Whether the order crosses the 22:00 freeze.
- Which known terrain or weather condition is being applied.

Commanders do not calculate hidden enemy positions, combat outcomes, surprise, or disputed control. Those belong to the game master.

## What the game master records

For every timed order, record:

```text
Order ID:
Start time:
Base time:
Adjustment:
Expected completion:
Remaining at freeze:
Interruptions or contact:
Result:
```

For a contact, also record the Contact ID, response-by time, paused order,
posture, preparation, commitment, result pair, consequences, and next decision
window. Use active time for response windows; pause them at 22:00.

At the end of a frozen window, the game master resumes the recorded remaining time rather than recalculating from memory. If conditions changed overnight in a way that the prototype rules do not cover, record a temporary ruling before resuming and use it symmetrically.
