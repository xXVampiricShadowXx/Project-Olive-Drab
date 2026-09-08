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
- **Military roles** — Translate political direction into operations at the appropriate command level.
  - Corps Commander — Used on the largest maps.
  - Army Commander — The default highest military rank.
  - Division Commander — The base military rank.
  - Brigade Commander — Used on the smallest maps.

## Where to work

The repository is organized around game design rather than software development:

| Location | Purpose |
|----------|---------|
| `docs/game-design/` | The rules and design documents being developed |
| `docs/playtesting/` | Plans, reports, and lessons from test games |
| `docs/assets/` | Player-facing reference material |
| `.github/ISSUE_TEMPLATE/` | Templates for proposing ideas or reporting design problems |

Start with [`docs/game-design/00-project-brief.md`](docs/game-design/00-project-brief.md), then use [`docs/game-design/01-core-loop.md`](docs/game-design/01-core-loop.md) to define what players actually do during play.

The first prototype's commander and game master responsibilities are outlined in [`docs/game-design/04-game-master-and-player-roles.md`](docs/game-design/04-game-master-and-player-roles.md).

The initial scenario concept is documented in [`docs/game-design/05-first-prototype-scenario.md`](docs/game-design/05-first-prototype-scenario.md).

See [`docs/project-roadmap.md`](docs/project-roadmap.md) for the project phases and the current design focus.

## Design principles

1. **Human-moderated first** — Rules should work with people, maps, written orders, communication channels, and simple reference aids before any automated implementation is considered.
2. **Roles should matter** — Each role needs meaningful authority, information, and responsibilities.
3. **Decisions should have consequences** — The game should create difficult choices rather than reward a single obvious strategy.
4. **Rules should be teachable** — Complexity should support the experience, not obscure it.
5. **Test before polishing** — Playtesting is how we discover whether a rule works.

## Project status

This project is in the **concept and rules-foundation phase**. Nothing is considered final yet. Ideas should be recorded, tested, and revised openly.
