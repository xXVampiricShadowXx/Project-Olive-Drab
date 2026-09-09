# Stable Prototype Snapshot and Tag Preparation

This is a preparation guide, not a release. A repository tag is allowed only
after the focused readiness PR has merged into `main`, the merged commit has
passed validation, and the project owner has requested the human-test
snapshot. Do not publish a GitHub release.

## Snapshot procedure

1. Start from the merge commit on `main` that contains the complete pre-test
   toolkit.
2. Run the repository's existing documentation checks and record the result.
3. Confirm that the [packet manifest](human-playtest-packet-manifest.md),
   readiness guide, communication rehearsal, participant briefing, observer
   ledger, and report template are present.
4. Record the exact commit SHA, map version, packet version, and rules authority
   in the GM briefing, event ledger, and report.
5. Save a read-only copy of the packet files used by the GM. Do not edit the
   snapshot during play; record corrections as event-log rows or issues.
6. Confirm all external setup fields are marked `complete`, `pending`, or
   `blocked`; repository work is not evidence that an external item is complete.

## Suggested identity

```text
Packet version: human-playtest-0.1
Snapshot name: olive-drab-human-playtest-0.1
Rules authority: <main commit SHA>
Map authority: Brackenford map v1.0
Status: supervised prototype preparation; not a release
```

If requested after merge, create an annotated repository tag named
`prototype-v0.1-human-test-ready` on the exact merged `main` commit. This is a
repository tag, not a published release. Record the commit SHA, packet
manifest, map version, observer ledger, and report template alongside the tag.
State that the packet is provisional, infantry-only, and does not expand Phase
3 mechanics.

## Go/no-go record

```text
Snapshot commit:
Documentation check:
Packet files present: yes / no
External setup status: complete / pending / blocked
GM authorization:
First accepted order ID:
```
