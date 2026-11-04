# Feedback, Issue, and Revision Framework

Use the [playtest report template](playtest-report-template.md) for the
complete record. This framework turns an observation into a traceable issue
without silently changing a rule.

## Capture and classify

1. Record the observed fact, event/order IDs, visibility, and confidence.
2. Separate player experience, GM operations, rules clarity, and setup failures.
3. Mark severity: blocking, high-friction, confusing, or polish.
4. State whether the issue is a documentation correction, a temporary ruling,
   or a proposed design change.
5. Remove names and personal details before sharing externally.

## Issue routing

Use the repository's existing issue forms:

- [Playtest finding](../../.github/ISSUE_TEMPLATE/playtest_finding.yml) for
  observed test evidence.
- [Documentation inconsistency](../../.github/ISSUE_TEMPLATE/documentation_inconsistency.yml)
  for conflicting or missing instructions.
- [Rules question](../../.github/ISSUE_TEMPLATE/rules_question.yml) for
  unresolved interpretation.
- [Feature/design proposal](../../.github/ISSUE_TEMPLATE/feature_design_proposal.yml)
  only when evidence supports a deliberate rules or experience change.

Link the issue from the report and preserve the original event record. Do not
use an issue to disclose hidden positions or personal participant information.

## Revision gate

The GM or design owner reviews each issue and chooses `document`, `rehearse
again`, `revise`, `defer`, or `close as expected behavior`. Any rules revision
must name its affected documents, explain the evidence, preserve consent and
real-life priority, and receive a fresh rehearsal before the next human test.
Do not add mechanics merely to resolve a one-off edge case.
