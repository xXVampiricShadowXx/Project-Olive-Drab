# Quick Reference Sheet

This is an optional live aid, not additional required learning or a rule source.
**The exact governing sections linked below win if this summary differs.**
Keep it available during play; use the [glossary](glossary.md) for terminology.

## Active-Day Procedure
Source: [campaign clock](prototype/operating-procedure.md#campaign-clock)
and [order lifecycle](prototype/operating-procedure.md#order-lifecycle).

Scenario time advances at the same rate as real time: one real-time minute
equals one scenario-clock minute. During the overnight freeze, scenario time
proceeds to 08:00, but no action resolves and action timers do not count down.

1. Draft and submit a clear order.
2. Wait for game-master acknowledgment and **acceptance**; revise if returned.
3. After the GM accepts the order, the GM starts and records the timer. Track expected completion and report observations.
4. **First human test:** Day 1 ends after the 22:00 final control-state check. Orders and response deadlines do not carry into a second scenario day.
5. **Broader multi-day prototype:** at 22:00, pause timers and record remaining time; resume at 08:00 with the GM briefing and recorded remaining time.

## Force Markers At A Glance
Source: [map conventions](prototype/map-and-terrain.md#map-identity-and-conventions).

| Force marker | Status | Location | Current order | Expected completion |
|------|--------|----------|---------------|---------------------|
|      |        |          |               |                     |

## Common Actions & Their Effects
Source: [movement aid](prototype/timing.md#movement-aid) and
[routine actions](prototype/timing.md#routine-action-aid).

| Action | Active time |
|--------|-------------|
| Move one road/open sector | 30 min |
| Move one broken/woods sector | 45 min |
| Move one built/difficult-crossing sector | 60 min |
| Change formation or facing | 15 min |
| Establish a temporary position | 30 min |
| Observe one adjacent sector | 15 min |

For routes spanning multiple sectors, add the applicable movement time for each
sector. If the total is not already a multiple of 15 minutes, round it up to the
next 15-minute multiple. A total already on a 15-minute multiple remains unchanged.
Do not use one terrain value for the whole route when sectors differ.

## Contact Quick Reference
Sources: [triggers](prototype/contact-and-combat.md#contact-triggers),
[pause](prototype/contact-and-combat.md#pause-and-engagement-state),
[resolution](prototype/contact-and-combat.md#transparent-gm-resolution-sequence),
[status card](../templates/commander-role-sheets.md#engagement-status-submission),
[behaviors](prototype/operating-procedure.md#behaviors-and-standing-orders),
and [reports](prototype/operating-procedure.md#reports-and-map-updates).

- Stop affected units' routine timers when enemy contact, a blocked route, or a contested objective occurs; unrelated orders continue. A distant or uncertain sighting may only need a report.
- Create a contact record and send each commander a separate report with a response-by time.
- Accepted movement or position orders may include a GM-approved behavior: trigger, action, limits, expiry/cancel condition, and unreachable fallback.
- Commander choices: Hold, Probe, Attack, Prepare, Reserve/commit, or Withdraw.
- Resolve: snapshot → confirm intent → compare situation → choose band → roll 1d6 each → apply graduated consequences → update map → report.
- Show every roll that directly affects a player to that player; keep hidden positions, modifiers, and other unrevealed situation bands private.
- Before resolution, commanders submit current position, posture, preparation, readiness, strength, and commitment; the GM verifies claims against the authoritative record.
- Choices and position matter; the dice are an uncertainty aid, not a complete combat result.
- Reports use **confirmed**, **reported**, or **suspected**.

## Terrain Modifiers
Source: [conditions and adjustments](prototype/timing.md#conditions-and-adjustments).

| Condition | Effect |
|-----------|--------|
| Poor visibility | Add 15 min; reduce confirmation |
| Heavy rain | Add 15 min to movement/preparation |
| Night (22:00–08:00) | Freeze; no action resolves in the broader multi-day prototype |

---

*Print this out or have it available during play!*
