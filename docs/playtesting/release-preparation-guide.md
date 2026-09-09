# Playtest Tag and Release Preparation

This is a preparation guide only. Do not publish a release for the first human
playtest unless the project owner explicitly requests it.

## Before tagging

1. Confirm the readiness package is merged into `main` and record the exact
   commit SHA used by the GM.
2. Confirm the packet manifest, readiness guide, communication rehearsal,
   participant briefing, observer ledger, and report template are present.
3. Confirm all external setup remains accurately marked as complete, pending,
   or blocked; do not infer Discord, map, roster, or player completion from
   repository changes.
4. Run the final GM preflight and record `GO` with the packet version, map
   version, time zone, and first order ID.

## Suggested tag metadata

If a release is later requested, use a tag that identifies the packet rather
than implying rules maturity, for example `human-playtest-0.1`. The release
notes should link to the [packet manifest](human-playtest-packet-manifest.md),
state that this is a supervised prototype, list known limitations, and state
that no Phase 3 mechanics were expanded.

The release should include the commit SHA, map version, report template, and
observer ledger used by the GM. A release is not a substitute for the
authoritative record or external setup checklist.
