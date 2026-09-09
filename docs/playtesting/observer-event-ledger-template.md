# Observer Event Ledger Template

Use one append-only row per operational event. The observer may receive the
public transcript and a redacted feed only; the GM keeps the complete master
state. Do not put unreleased opposing positions, hidden situation bands, or
private reports into the observer copy.

Copy the header and table for each scenario day. If a field does not apply,
write `N/A`; do not leave whether it was considered ambiguous.

## Header

```text
Test packet version:
Phase 3 rules version/commit:
Scenario label:
Scenario day/time window:
Map version:
GM:
NATO commander:
Russia commander:
Observer:
Channel implementation: actual channels / controlled simulation
```

## Canonical event row

| Field | Entry |
|---|---|
| Event ID | Sequential `E###` |
| Scenario day/time | Day and scenario clock time |
| Wall-clock timestamp | Optional; use only if needed to audit processing |
| Actor/role | GM, NATO, Russia, temporary commander, or observer |
| Event type | briefing / order / report / contact / ruling / timer / map update / pause / resolution / succession |
| Visibility | public / NATO-private / Russia-private / GM-only / redacted-observer |
| Source or linked ID | Order, report, contact, map, timer, ruling, or correction ID |
| Observed fact | What the role or observer directly received or recorded |
| Inference | Interpretation, if any; otherwise `N/A` |
| Confidence | confirmed / reported / suspected / not applicable |
| Rule or section used | Exact packet document and section, or `temporary ruling` |
| State before | Relevant clock, order, position, control, or response state |
| Action or decision | The submitted, accepted, returned, released, or adjudicated action |
| State after | Resulting authoritative or released state |
| GM processing time | Minutes from input or trigger to acknowledgment/update |
| Observer clarity | clear / ambiguous / absent |
| Open question or correction link | Linked issue, correction, or `none` |

## Reusable ledger

| Event ID | Day/time | Actor/visibility | Type | Linked ID | Observed fact | Inference | Confidence | Rule/section | State before | Action/decision | State after | GM min | Clarity | Open question/correction |
|---|---|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| E001 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E002 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E003 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E004 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E005 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E006 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E007 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E008 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E009 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| E010 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Add rows rather than overwriting them. If an entry is wrong, add a correction
row with a link to the original event and preserve the original text.

## Closeout counts

| Metric | Count/result | Linked event IDs or note |
|---|---:|---|
| Events recorded |  |  |
| Clarifications |  |  |
| Returned/reworked orders |  |  |
| Timer starts/pauses/resumes/expiries |  |  |
| Information-boundary leaks |  |  |
| Confidence-label errors |  |  |
| Missing required fields |  |  |
| Temporary rulings |  |  |
| Events blocked by role handoff |  |  |
