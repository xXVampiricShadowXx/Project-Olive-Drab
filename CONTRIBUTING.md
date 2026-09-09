# Contributing to Project Olive Drab

Thank you for helping develop Project Olive Drab. This repository is a
documentation-first design project for a human-moderated, real-time,
roleplaying wargame.

## Before opening an issue or pull request

1. Read the [README](README.md) and the [project roadmap](docs/project-roadmap.md).
2. Search existing issues and pull requests so related discussion stays together.
3. Keep proposals small enough to test or review in one focused change.
4. Do not present an untested rule as settled. Mark assumptions and open questions
   clearly.

Use the issue forms for a rules question, playtest finding, documentation
inconsistency, or feature/design proposal. Use a pull request for a concrete
documentation or configuration change.

## Design and documentation changes

- Put rules and design material in `docs/game-design/`.
- Put playtest plans, reports, and observations in `docs/playtesting/`.
- Update the relevant index or roadmap entry when adding a document.
- Use descriptive filenames and relative Markdown links.
- Preserve the distinction between authoritative rules, provisional procedures,
  and observed playtest results.
- Keep real-world conflict references fictionalized and respectful. Do not add
  hateful, harassing, or celebratory depictions of violence.

## Playtest findings

Record the scenario, rules version, participants or roles, observed event, and
the effect on play. Separate observation from interpretation and proposed
changes. A finding can be useful even when it does not yet justify a rule
change.

## Pull requests

Pull requests should:

- Explain the design or documentation problem being addressed.
- Link related issues or playtest reports.
- Identify any changed assumptions, rules, links, or workflows.
- Keep unrelated cleanup out of the change.
- Include updated indexes or references when needed.

Before requesting review, run the repository's available validation commands and
`git diff --check`. Review rendered Markdown links and check that templates and
workflow YAML remain valid.

## Review expectations

Reviewers focus on clarity, testability, internal consistency, accessibility,
and whether a change preserves the intended human-moderated experience.
Discussion should be specific and constructive. Maintainers may ask for a
smaller experiment or a playtest before accepting a broad rules change.

## Security and private concerns

Do not report private or sensitive information in a public issue. See
[SECURITY.md](SECURITY.md) for reporting security concerns.
