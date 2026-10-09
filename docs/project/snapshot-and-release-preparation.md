# Optional snapshot and release administration

This is optional project administration, outside the
[first-test GM preparation route](../gm/index.md#prepare-in-this-order).
It preserves both the snapshot procedure and later release guidance;
neither authorizes a tag or release now. The project owner's explicit
request and the conditions below still apply.

## Release preparation

This is a preparation guide only. Do not publish a release for the first human
playtest unless the project owner explicitly requests it. For the repository
snapshot and go/no-go record, use the more detailed [stable prototype snapshot
procedure](#snapshot-preparation).

### Release preparation: Before tagging

1. Confirm the readiness package is merged into `main` and record the exact
   commit SHA used by the GM.
2. Confirm the packet manifest, readiness guide, communication rehearsal,
   participant briefing, observer ledger, and report template are present.
3. Confirm all external setup remains accurately marked as complete, pending,
   or blocked; do not infer Discord, map, roster, or player completion from
   repository changes.
4. Run the final GM preflight and record `GO` with the packet version, map
   version, time zone, and first order ID.

### Release preparation: Suggested tag metadata

If a release is later requested, use a tag that identifies the packet rather
than implying rules maturity, for example `human-playtest-0.1`. The release
notes should link to the [packet manifest](human-playtest-packet-manifest.md),
state that this is a supervised prototype, list known limitations, and state
that no Phase 3 mechanics were expanded.

The release should include the commit SHA, map version, report template, and
observer ledger used by the GM. A release is not a substitute for the
authoritative record or external setup checklist.
## Snapshot preparation

This is a preparation guide, not a release. A repository snapshot/tag is allowed only
after the focused readiness PR has merged into `main`, the merged commit has
passed validation, and the project owner has requested the human-test snapshot.
Do not publish a GitHub release.

### Snapshot preparation: Snapshot procedure

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

### Snapshot preparation: Suggested identity

```text
Packet version: human-playtest-0.1
Snapshot name: olive-drab-human-playtest-0.1
Rules authority: <main commit SHA>
Status: supervised prototype snapshot; external human-test readiness is recorded separately
Map authority: Brackenford map v1.0
```

If requested after merge, create an annotated repository tag named
`prototype-v0.1-human-test-snapshot` on the exact merged `main` commit. This is
a repository tag, not a published release, and the tag name does not by itself
claim that external human-test setup is complete. Record the commit SHA, packet
manifest, map version, observer ledger, and report template alongside the tag.
State that the packet is provisional, infantry-only, and does not expand Phase
3 mechanics.

### Snapshot preparation: Go/no-go record

```text
Snapshot commit:
Documentation check:
Packet files present: yes / no
External setup status: complete / pending / blocked
GM authorization:
First accepted order ID:
```
