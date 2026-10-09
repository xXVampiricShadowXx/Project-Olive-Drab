# Game concept and core loop

This project background preserves the broader design vision separately from
the [finite player learning route](../learn/index.md) and the
[governing first-test sources](../reference/prototype/index.md).
Future architecture and open design questions below are not additional
first-test mechanics or preparation requirements.

## Project brief

This document is the starting point for the game design. It describes what Olive Drab is trying to be before individual rules are written.

### Project brief: One-sentence pitch

Project Olive Drab is a real-time, roleplaying wargame where commanders coordinate during a fictional modern conflict while dealing with incomplete information, limited resources, and competing objectives.

### Project brief: What kind of game is this?

- **Medium:** Human-moderated, live campaign using maps, written orders, and agreed communication methods.
- **Players:** Multiple players, divided among opposing factions and command roles.
- **Time model:** Real time, with a clock driving pressure and coordination.
- **Setting:** A fictionalized present-day conflict, initially focused on Europe.
- **Experience:** Leadership, communication, uncertainty, logistics, and consequential decisions.

### Project brief: What this project is not yet

- It is not a video game or software project.
- It is not a historically exact simulation.
- It is not a finished ruleset.
- It is not a promise to reproduce every detail of modern warfare.

### Project brief: Design goals

The game should make players feel:

1. Pressured by time without making thoughtful planning impossible.
2. Responsible for a role with a distinct perspective and authority.
3. Uncertain about what is happening outside their immediate knowledge.
4. Able to succeed through different approaches, not only tactical destruction.
5. That communication, preparation, and political choices matter as much as combat.

### Project brief: Success criteria for an early prototype

An early paper prototype is successful if:

- Players can understand their role and immediate objective quickly.
- The game creates meaningful decisions within the first 15 minutes.
- Players have reasons to communicate across role boundaries.
- The real-time structure creates tension without causing confusion.
- A playtest produces specific observations that can improve the next version.

### Project brief: Initial prototype targets

These are working assumptions for the first complete prototype. They are deliberately narrow so that we can test the game's central experience before expanding it.

- **Minimum group:** 3 people — one commander for each opposing side and one game master.
- **Additional players:** New commanders can be added as the scenario's scale and command structure expand. There is no fixed theoretical maximum; the practical limit is how many players the game master can support clearly.
- **First human test:** One infantry company commander per side, one company vs. one company, representing roughly 100–200 troops per side, with one game master. This is the initial playable slice, not the ceiling of the game architecture.
- **First map:** A small town and its surrounding terrain, rather than an entire country or theater.
- **First scenario:** A small, fictionalized near-future NATO-Russia crisis around a town, using asymmetric company forces without attempting to simulate real national militaries in detail.
- **First human-test duration:** One scenario day, 08:00–22:00, ending after the Day 1 final control-state check.
- **Broader prototype schedule:** A real-time week with daytime play active and nighttime play frozen. The broader schedule is exercised separately in solo/AI rehearsal and later multi-day tests; it is not a first-human-test requirement.
- **Prototype participation:** Players act together during the active window under game-master supervision. Short breaks are allowed, and the absence procedure covers players who cannot attend.
- **Primary experience:** Making real-time command decisions while accounting for terrain, weather, distance, logistics, uncertainty, and communication.
- **Game master:** Resolves engagements and hidden information, controls scenario events, interprets unusual situations, moderates fair play, and keeps the game moving.
- **Information model:** The game master maintains the authoritative map. Each commander sees their own forces and only the enemy information their side has legitimately obtained.
- **Future systems:** Intelligence analysis, counter-intelligence, cyberwarfare, and broader information operations are expansion systems, not requirements for the first prototype.
- **Long-term hierarchical architecture:** The game supports commanders at different organizational echelons, from fireteam/crew level through larger formations and theater-level commands. Each commander controls their immediate subordinate units using the same hierarchical command model; the first human test exercises only the company-command slice of that architecture.

The initial prototype targets above are provisional and should be revisited after the first few playtests. The full-game hierarchy and its defined command tiers are documented separately and are not provisional merely because the first-test scope is narrow.

### Project brief: Resolved prototype decisions

The first prototype packet resolves the initial implementation questions:

- The GM uses the timing aid for movement and routine actions, while the GM
  adjudicates contact, combat, and unusual situations.
- Commanders submit orders through the role-based Discord channels; the GM
  acknowledges, accepts, tracks, and records them.
- The GM maintains the authoritative master map and filtered commander views.
- The active window is 08:00–22:00, the nighttime window is frozen, and the
  shared clock uses one local time zone.
- Player attention may be intermittent. Accepted orders and GM-validated
  standing behaviors continue under their recorded limits, with response
  windows, fallbacks, and temporary command covering longer absences.
- **Scope boundary:** The first human test is intentionally company-vs-company. The broader hierarchical game architecture may use different player command echelons and subordinate-unit representations without changing that first-test scope.

### Project brief: Remaining questions

These questions remain for later playtests or expansion:

- How many players can the smallest complete game support beyond the minimum of
  three, and what is the shortest satisfying session?
- How should intelligence and counter-intelligence interact with fog of war in
  later versions?
- How are victory and non-military success measured beyond the first town-control
  objective?
- What level of abstraction is appropriate for units, geography, and logistics
  as the game expands?
## Core game loop

The core loop is the repeated pattern of activity players perform during a game. It should be defined before writing detailed unit statistics or equipment lists.

### Core game loop: Draft loop

1. **Receive information** — Commanders receive their side's filtered map view and learn what their role can currently see or what reports they have received.
2. **Interpret the situation** — Commanders decide what matters and what remains uncertain.
3. **Issue orders** — Commanders give instructions through the game's communication structure.
4. **Estimate and track time** — Players use simple reference aids to estimate routine actions. The game master confirms unusual or contested timings using factors such as distance, terrain, weather, opposition, and unit condition.
5. **Act** — Forces move, engage, defend, gather information, or perform other permitted actions while the daytime real-time clock continues. During the prototype's nighttime freeze, no new actions resolve.
6. **Resolve consequences** — The game master applies the rules, adjudicates unusual situations, and updates the hidden and public state of the scenario.
7. **Report and adapt** — The game master provides appropriate information; commanders revise plans and respond to new developments.

### Core game loop: Questions for the first paper prototype

Keep the first prototype small enough to answer these questions:

- Does the clock create useful pressure?
- Do players need one another, or can everyone act alone?
- Are orders clear enough to execute without constant rule lookups?
- Does limited information create interesting uncertainty?
- Can a player tell what a good decision looks like even when it fails?
- Can the game master make consistent rulings without slowing the game down?
- Do terrain and weather meaningfully change the time and risk of an action?
- Can commanders resolve routine actions themselves with a reference card or table?
- Does each commander receive enough information to make decisions without accidentally seeing the master map?
- Can all players act together during the active window without the game master becoming overwhelmed?
- Does freezing the game overnight preserve tension while allowing the group to pause between live sessions?

### Core game loop: Boundaries for version 0.1

The first human test should use:

- One small town-scale map with surrounding terrain.
- Two opposing sides.
- One infantry company per side.
- One commander per side.
- One game master.
- A bounded scenario with a clear beginning and end; the Brackenford first human test uses Day 1 only, while the broader prototype supports a seven-day scenario clock.
- Simple resolution methods, using components already available at home.
- A quick-reference aid for movement and other routine actions.
- Agreed communication channels and an order-submission procedure.
- A shared local-time schedule for active and frozen periods.

Do not begin by modeling every country, weapon system, historical event, or detailed military specialization. Those details can be added after the core loop proves enjoyable; the project's supported command hierarchy is defined separately from this first-test scope.
