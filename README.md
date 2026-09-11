# Project Olive Drab

Project Olive Drab is a **real-time, roleplaying wargame** set in a fictionalized present-day global conflict. It is being designed as a human-moderated campaign first, using maps, written orders, communication channels, and game-master adjudication. A software version is a possible future direction, not part of the current project.

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

The repository is organized around game design rather than software development:

| Location | Purpose |
|----------|---------|
| `docs/game-design/` | The rules and design documents being developed |
| `docs/playtesting/` | Plans, reports, and lessons from test games |
| `docs/assets/` | Player-facing reference material |
| `.github/ISSUE_TEMPLATE/` | Templates for proposing ideas or reporting design problems |

Start with [`docs/game-design/00-project-brief.md`](docs/game-design/00-project-brief.md), then use [`docs/game-design/01-core-loop.md`](docs/game-design/01-core-loop.md) to define what players actually do during play.

The first prototype's commander and game master responsibilities are outlined in [`docs/game-design/04-game-master-and-player-roles.md`](docs/game-design/04-game-master-and-player-roles.md). The assembled live-test materials are indexed in [`docs/game-design/09-prototype-packet-index.md`](docs/game-design/09-prototype-packet-index.md), with a [`GM setup checklist`](docs/game-design/10-gm-setup-checklist.md) and [`commander role sheets`](docs/game-design/11-commander-role-sheets.md).

The initial scenario concept is documented in [`docs/game-design/05-first-prototype-scenario.md`](docs/game-design/05-first-prototype-scenario.md).

The repository-side pre-test materials are collected in the
[`pre-test tooling index`](docs/playtesting/pre-test-tooling-index.md). They
prepare a stable snapshot, solo GM rehearsal, operational templates, external
setup checks, onboarding, and post-test issue/revision decisions without
publishing a release or claiming a human test.

The prototype operating procedure is documented in [`docs/game-design/06-prototype-operating-procedure.md`](docs/game-design/06-prototype-operating-procedure.md), with timing aids in [`docs/game-design/07-timing-and-action-aids.md`](docs/game-design/07-timing-and-action-aids.md) and draft control conditions in [`docs/game-design/08-control-and-victory-conditions.md`](docs/game-design/08-control-and-victory-conditions.md).

See [`docs/project-roadmap.md`](docs/project-roadmap.md) for the project phases and the current design focus.

## Contributing and playtesting

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the documentation workflow, pull
request expectations, and how to record playtest findings. Use the repository's
issue forms for rules questions, playtest findings, documentation
inconsistencies, and focused design proposals. Keep player-identifying details
out of public reports.

## Design principles

1. **Human-moderated first** — Rules should work with people, maps, written orders, communication channels, and simple reference aids before any automated implementation is considered.
2. **Roles should matter** — Each role needs meaningful authority, information, and responsibilities.
3. **Decisions should have consequences** — The game should create difficult choices rather than reward a single obvious strategy.
4. **Rules should be teachable** — Complexity should support the experience, not obscure it.
5. **Test before polishing** — Playtesting is how we discover whether a rule works.

## Project status

Phase 3's first-test packet is assembled for live, supervised testing, but the
repository still contains documented rule-owner questions that are not silently
resolved by packet assembly, including #127 (formal withdrawal) and #146
(Reserve/commit terminology). Phase 4 AI rules-testing preparation is also
complete; the communication/order dry run and first focused human playtest are
still pending. External setup and human participation remain separate readiness
checks and are not implied by repository completion.
