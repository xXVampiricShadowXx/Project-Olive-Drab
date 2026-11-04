# Operational Templates

Copy these tables into the GM's private working document. They are recording
aids, not additional rules. Use `N/A` rather than leaving a field ambiguous.

## Order register

| Order ID | Day/time received | Side/issuer | Unit | Required fields complete | Status | Timer/deadline | Linked report/contact | GM note |
|---|---|---|---|---|---|---|---|---|
| O-001 |  |  |  | yes / no | draft / submitted / acknowledged / returned / accepted / in progress / paused—contact / resolved / cancelled / superseded |  |  |  |

The `Unit` field names the specific subordinate organizational element receiving
the order. Use the same unit identity when later records refer to that order.

Use the status that matches the current lifecycle state in the operating
procedure. A superseded order is closed because a newer accepted operational
order replaced it; a cancelled order is explicitly ended without being replaced
by another active order. `Paused—contact` records an interruption that is handled
by the prototype contact procedure.

## GM event log

| Event ID | Day/time | Actor | Type | Visibility | Source ID | Observed fact | Rule/section | State before | State after | Correction/open question |
|---|---|---|---|---|---|---|---|---|---|---|
| E001 |  |  |  |  |  |  |  |  |  |  |

## Contact and combat resolution

| Contact ID | Trigger/location | Affected unit(s) | Affected order(s) | Response-by | Side A response | Side B response | Procedure used | Result | Reports released | Map/control update |
|---|---|---|---|---|---|---|---|---|---|---|
| C-001 |  |  |  |  |  |  |  |  |  |  |

The `Affected unit(s)` field names the specific subordinate organizational
elements involved in the contact. Use one or more unit identities when the
contact involves multiple subordinate units.

## Hidden-information release

| Release ID | Source ID | Recipient | Information | Confidence | Visibility | Why earned | Time released | GM initials |
|---|---|---|---|---|---|---|---|---|
| H-001 |  |  |  | confirmed / reported / suspected |  |  |  |  |

## Timer and freeze tracking

| Timer ID | Order/contact | Started | Paused | Resumed | Expired/cancelled | Active time remaining | Freeze/restart note |
|---|---|---|---|---|---|---|---|
| T-001 |  |  |  |  |  |  |  |

## Temporary-command handoff

| Handoff ID | Side/role | Commanded organization | Absence start/end | Primary/backup | Information transferred | Information withheld | Pending decisions | Return/closeout |
|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  |  |  |  |

The `Commanded organization` field identifies the absent commander's organization
at the command level being played. For the first human test this is the company;
in broader hierarchical play it can be an echelon, platoon, section, or squad
organization as applicable.

## Daily briefing and end-of-day summary

```text
Scenario day:
Active window and local time zone:
Public clock/status:
Public map/control update:
Orders or reports awaiting action:
Private handoff for [side]:
Standing behaviors active/cancelled:
Contacts and response deadlines:
Pause, safety, or accessibility note:
Freeze time:
Timers paused with remaining active time:
Map/register snapshots saved:
Next restart:
GM:
```
