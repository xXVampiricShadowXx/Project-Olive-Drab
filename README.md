# Project Olive Drab

Project Olive Drab is a **real-time, roleplaying wargame** set in a fictionalized present-day global conflict. It is being designed as a human-moderated campaign first, using maps, written orders, communication channels, and game-master adjudication. A software version is a possible future direction, not part of the current project.

## Start here

**New player? [Learn to play](docs/learn/index.md)** gives you exactly three
ordered public pages, then a clear stopping point. The first test is one
infantry company per side in fictional Brackenford, Day 1 only, 08:00-22:00.
Your GM provides the private briefing and confirms readiness before play.

| Your role | Start |
|---|---|
| Commander | [Player learning route](docs/learn/index.md) |
| Game master (GM) | [Prepare, set up, rehearse, then go/no-go](docs/gm/index.md) |
| Observer (optional, playtest-only) | [Observer route](docs/learn/index.md#other-roles) |
| Contributor or returning reader | [Documentation catalog](docs/index.md) |

**Prototype, not a validated game or software release.** The first-test packet
and AI rehearsal preparation are assembled; human validation and external
setup remain pending. Discord, notifications, and map setup issues
[#14](https://github.com/xXVampiricShadowXx/Project-Olive-Drab/issues/14),
[#15](https://github.com/xXVampiricShadowXx/Project-Olive-Drab/issues/15), and
[#16](https://github.com/xXVampiricShadowXx/Project-Olive-Drab/issues/16)
remain open. The static renderer is a **proposed map method**, not a confirmed
platform. Learning summaries add no rules; the linked repository governing
sections remain authoritative. See [project status](#project-status).

## The broader game

The game combines:

- Real-time decision-making instead of traditional turns.
- Military command with civilian, diplomatic, and economic leadership.
- Multiple map scales, from a local conflict to a Europe-wide campaign.
- Roleplaying, where players have authority, information, and objectives that may not be shared by everyone else.

## Current concept

The first planned setting is a Europe-focused WW3 scenario involving NATO and Russia. The setting, factions, and events should remain playable and respectful: the game is about difficult decisions and consequences, not about celebrating real-world violence.

### Player roles

- **Civilian government roles** — Set national priorities, make economic and diplomatic decisions, and issue strategic direction.
- **Military command roles** — The full game supports command at every tier of the authoritative hierarchy: Combatant Command/equivalent region or theater → Army Group/Front → Field Army → Corps → Division → Brigade → Regiment → Battalion → Company/equivalent → Staff/Echelon → Platoon → Section → Squad → Fireteam/Crew.
  - At any selected military command tier, the commander directs the immediate subordinate tier using the project's hierarchy and unit model.
  - **First human test:** only the Company → Echelon slice is player-controlled, with one company commander per side; this is a test slice, not the limit of the game's command architecture.

## Where to work

The repository is organized around audiences and game design rather than
software development. These are lookup routes, not extra required player reading:

| Location | Purpose |
|----------|---------|
| [`docs/learn/`](docs/learn/index.md) | Finite first-test player learning |
| [`docs/reference/`](docs/reference/prototype/index.md) | Governing rules, map, scenario, timing and contact; live aids |
| [`docs/gm/`](docs/gm/index.md) | Setup, readiness, rehearsal, and operational tooling |
| [`docs/templates/`](docs/templates/operational-records.md) | Blank forms; filled private records stay outside the repository |
| [`docs/project/`](docs/project/game-concept.md) | Project brief, core loop, roadmap, feedback, and optional snapshot preparation |
| [`docs/decisions/`](docs/decisions/rule-owner-decisions.md) | Recorded clarifications and design notes |
| [`docs/history/`](docs/index.md) | Test evidence, fictional examples, and optional solo/AI rehearsal |
| `.github/ISSUE_TEMPLATE/` | Templates for proposing ideas or reporting design problems |

Use the [catalog](docs/index.md) to find roles, scenario, map, operating procedure,
timing, control conditions, commander sheets, briefing templates, and the
assembled packet inventory. The [GM route](docs/gm/index.md) gathers pre-test
tooling without implying a release or completed human test.
See the [roadmap](docs/project/roadmap.md) for phases and current design focus.

## Contributing and playtesting

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the documentation workflow, pull
request expectations, and how to record playtest findings. Use the repository's
issue forms for rules questions, playtest findings, documentation
inconsistencies, and focused design proposals. Keep player-identifying details
out of public reports.

[Code of conduct](CODE_OF_CONDUCT.md) · [Security policy](SECURITY.md) ·
[License](LICENSE.md)

## Design principles

1. **Human-moderated first** — Rules should work with people, maps, written orders, communication channels, and simple reference aids before any automated implementation is considered.
2. **Roles should matter** — Each role needs meaningful authority, information, and responsibilities.
3. **Decisions should have consequences** — The game should create difficult choices rather than reward a single obvious strategy.
4. **Rules should be teachable** — Complexity should support the experience, not obscure it.
5. **Test before polishing** — Playtesting is how we discover whether a rule works.

## Project status

Phase 3's first-test packet is assembled for live, supervised testing. The four
audited rule-owner clarifications are incorporated in the current packet through
the merged [audit-cleanup pull request](https://github.com/xXVampiricShadowXx/Project-Olive-Drab/pull/168)
and recorded in the [Rule-Owner Decisions](docs/decisions/rule-owner-decisions.md)
page. Phase 4 AI rules-testing preparation is also complete; human-playtest
validation, including the communication/order dry run and first focused human
playtest, is still pending. External setup and human participation remain
separate readiness checks and are not implied by repository completion.

Development tooling for this repository uses AI assistance for technical
work such as repository setup and code; see
[CONTRIBUTING.md](CONTRIBUTING.md#use-of-ai-tools) for what that does and
does not cover.
