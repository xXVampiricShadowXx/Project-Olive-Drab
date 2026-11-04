# GM-Only Records and Data Handling

Use this guide with the [readiness guide](human-playtest-readiness-guide.md)
and [operational templates](operational-templates.md). It adds no rules. It
defines where sensitive game and participant information belongs during a
supervised test.

## Keep in the GM-only working record

Store only what is needed to run, pause, resume, hand off, or audit the game:

- the master map, hidden starting zones, hidden conditions, and unearned
  opposing information;
- orders, reports, contacts, rulings, timers, event IDs, and state snapshots;
- role assignments, succession tier, handoff status, and notification outcomes;
- a minimal availability or accessibility note only when it changes operations,
  such as `commander unavailable` or `pause requested`.

Do not record diagnoses, reasons for withdrawal, private conversations, exact
home or work details, or unrelated identifying information. The GM should use
display names or role names and collect no more personal data than continuity
requires.

## Where not to store it

Do not put GM-only records, private briefings, hidden maps, personal contact
details, or participant circumstances in:

- the public repository, issues, pull requests, or commit messages;
- the curated public feed, public channels, shared map layers, exports, or screen
  shares;
- personal direct messages as the authoritative record; or
- unprotected downloads, screenshots, or third-party tools not approved for the
  test.

The GM chooses an access-controlled working location. If an observer
participates, they get read-only audit access to these records and must not
reveal their contents to either commander.

## Redacted observer copies

The observer can read the full record during the playtest. Make a redacted
copy only when the observer ledger or record is shared beyond the GM and
observer, such as in a post-game report. Create that copy from the authoritative record, not by forwarding the
GM file. Remove hidden positions, unearned reports, private briefings,
succession contact routes, personal details, and any note that reveals why a
participant paused or withdrew. Keep event IDs, timestamps, public outcomes,
and the minimum operational fact needed to explain the visible timeline.
Label the copy `observer-redacted` and recheck it before sharing or exporting.

## Backups and retention

- Keep one access-controlled backup of the GM record in a separate approved
  location; record its location in the preflight checklist without publishing
  the link.
- Snapshot before a pause or hiatus, at each overnight freeze, after a major
  ruling, and at closeout. Record the snapshot ID and restore check.
- Retain the authoritative record and redacted observer copy only for the
  agreed review period, then delete or securely destroy them unless a
  participant has explicitly agreed to a longer, documented retention period.
- Delete temporary exports, downloads, and duplicate copies when the session
  closes. Never put credentials or access links in the repository.

If a file or channel may have exposed private information, stop sharing,
preserve the relevant event ID, restrict access, and record the incident for
the GM and project maintainer without copying the exposed content into a
public report.
