# Filled Fictional Example Packet

Everything in this document is fictional and illustrative. It is not a
scenario result, a rules change, or evidence from a human participant.

## Packet header

```text
Packet version: human-playtest-0.1
Snapshot commit: 0000000 (fictional placeholder)
Scenario: Brackenford, Day 2
Map version: Brackenford v1.0
GM: Morgan Vale (fictional)
NATO commander: Alex Reed (fictional)
Russia commander: Ilya Petrov (fictional)
```

## Order lifecycle and report

```text
O-NATO-004 received 09:10; complete
Intent: hold Mill Road Junction and observe the east approach
Route/action: move one element from C2 to D2, then report
Trigger/limit: do not initiate contact; stop if contact is reported
Standing behavior: return to C2 if the element cannot report by 10:00
Accepted 09:12; timer recorded; resolved 09:42
R-NATO-004 released 09:45; confirmed own position, suspected movement east
```

The GM records the report as `confirmed` for the own position and `suspected`
for movement. The suspected movement is not released as a confirmed enemy
position.

## Contact and combat

```text
C-002 10:03: contact at East Road, affecting O-NATO-004
Response-by 10:15; affected order paused; other orders continue
NATO response: hold and observe
Russia response: withdraw from contact area
GM resolution: contested action procedure applied; no new mechanic
R-C-002 10:18: both sides receive only their earned result
```

## Standing behavior

The trigger is “cannot report by 10:00,” the action is “return to C2,” the
limit is “do not initiate contact,” the expiry is the end of Day 2, and the
unreachable fallback is “hold current position.” `O-NATO-005` cancels it at
11:00. The GM records the cancellation and does not leave the old behavior
active.

## Temporary-command absence handoff

At 13:00, Alex Reed is unavailable. The GM activates the same-side primary
contact, Sam Cole (fictional), and provides current NATO orders, earned NATO
reports, pending decisions, and the public map. The GM withholds Russia-private
reports and hidden master-map state. At 15:00, Sam returns control to Alex Reed
and the GM records the end time. No faction changes.

## Map control and end-of-day freeze

At 21:40, the master map shows NATO control pressure at Mill Road Junction and
Russia control pressure at Station Street. The GM records each control pair
using the published sector-control test; the filtered views show only
information each side has earned. These approach positions do not by themselves
establish town control.

At 22:00, `T-002` records 18 minutes remaining on `O-NATO-006`. The GM stops
the timer, saves the map snapshot, and publishes:

```text
Day 2 end: active results frozen at 22:00.
O-NATO-006 has 18 active minutes remaining.
Restart: Day 3, 08:00, same local time zone.
```

At Day 3, 08:00, the GM records `T-002 resumed with 18 minutes`; no overnight
movement or result is inferred. This example demonstrates record shape only.
