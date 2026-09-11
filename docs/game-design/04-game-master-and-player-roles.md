# Game Master and Player Roles

This document defines the intended division of responsibility for the first prototype. It is a starting point for testing, not a final authority structure.

## First prototype roles

The **first human test** has the smallest complete player arrangement currently being tested:

- One infantry company commander for Side A.
- One infantry company commander for Side B.
- One game master.

Each commander controls one company of roughly 100–200 troops. The numbers are an abstraction for play, not a requirement to model every individual soldier.

The first test's company-command arrangement is intentionally a bounded slice of the broader game architecture. Later scenarios may place players at other echelons and add subordinate or superior player roles without changing the basic distinction between a commander and the subordinate units they control.

## What commanders do

Commanders should spend most of their time making decisions and roleplaying their responsibilities. Use the [prototype roleplay layer](14-prototype-roleplay-layer.md) for lightweight identity, relationship, NPC, and safety guidance; it does not add hidden mechanical advantages.

They are responsible for:

- Understanding their orders, objectives, and available information.
- Choosing priorities and issuing clear orders to subordinate units.
- Choosing routes, formations, positions, and timing.
- Tracking their own organization's known status.
- Using quick-reference aids to resolve routine movement and other uncontested actions.
- Reporting what their organization observes and what it needs.
- Accepting that incomplete information and delayed reports are part of the game.

For the **first human test**, “commander” refers to the company commander and their immediate subordinate echelon units. In a future hierarchical test, the same responsibilities apply at the selected command level, with the commander's immediate subordinate units receiving the relevant orders.

Commanders should not need to calculate detailed combat mathematics for every action. If a routine action requires a long calculation, the reference aid is too complicated for the first prototype.

## What the game master does

The game master is neutral. They do not secretly favor either side or play to win.

The game master is responsible for:

- Preparing the scenario, map, objectives, starting information, and hidden information.
- Maintaining the authoritative master map, including the true location and status of all forces.
- Providing each commander with a filtered map or map view showing only their side's forces and information they have obtained.
- Explaining the rules and keeping the real-time session moving.
- Maintaining the authoritative record of time, locations, conditions, and events.
- Confirming routine actions when necessary.
- Adjudicating contested actions and engagements using the agreed resolution system.
- Applying battle conditions such as terrain, weather, visibility, surprise, readiness, and supply.
- Controlling opposing forces or events that are not directly assigned to a player.
- Delivering reports according to what each side could reasonably know.
- Resolving unusual situations consistently and explaining rulings clearly.
- Moderating fair play, including preventing players from using information their role has not received.
- Recording unresolved questions for later review rather than stopping the game for every edge case.

The game master should not invent outcomes arbitrarily. Results should come from the scenario rules, reference tables, dice, cards, or clearly stated judgment calls.

## Map and fog of war

The master map is the source of truth. Commanders should not be expected to see it directly during play.

For the first prototype:

- Each commander sees their own organization's known position and status.
- Enemy forces are hidden unless revealed by direct observation, an engagement, a scenario briefing, or another explicitly allowed source.
- The game master decides what a commander can observe based on distance, terrain, visibility, movement, and other scenario conditions.
- A commander may record beliefs or suspected enemy locations, but suspicions are not treated as confirmed facts.
- The game master updates each side's map or information sheet separately.

This can be implemented with separate paper maps, screens, folders, or an agreed physical barrier. The exact presentation can change; the separation of information should remain consistent.

## Full-game hierarchical play

The full game uses the complete organizational hierarchy shown in the authoritative project hierarchy chart. From highest to lowest, the supported tiers are:

**Combatant Command (or equivalent region/theater) → Army Group/Front (or equivalent) → Field Army → Corps → Division → Brigade → Regiment → Battalion → Company (or equivalent) → Staff/Echelon → Platoon → Section → Squad → Fireteam/Crew.**

Every tier in this chain is part of the intended playable architecture. At any selected command tier, a player commands that organization and may direct its immediate subordinate tier using the same command, order, status, map-marker, and information-boundary principles defined elsewhere in the prototype documentation. “Unit” remains context-dependent: it means the immediate subordinate organizational element under the current commander's control.

The full hierarchy does not require every higher-tier organization to use the same fixed subordinate count. Higher formations retain the constituent-unit ranges and equivalents represented by the authoritative hierarchy chart. The rigid game structure beginning at Company is intentionally defined separately: a company contains **1–4 echelons**; each echelon contains **2 platoons**; each platoon contains **2 sections**; each section contains **2 squads**; and each squad contains **2 fireteams**. This fixed Company → Echelon → Platoon → Section → Squad → Fireteam/Crew chain is the project's repeatable game abstraction for the lower hierarchy.

The **first human test uses only the Company → Echelon slice** of that full architecture: one company commander per side directs the company's 1–4 echelon subordinate units. Platoon, section, squad, fireteam/crew, and every higher command tier remain part of the full game and may be used in later tests without redefining the underlying hierarchy.

This is a deliberate game abstraction. Real military terminology and organization vary among countries; the project hierarchy fixes its own supported tiers and the lower-level repeatable relationships so player authority and map representation remain consistent.

## Future information systems

Intelligence analysis, counter-intelligence, cyberwarfare, and similar systems are planned expansion areas. They should not be required for the first prototype.

When those systems are added, they should answer clear questions such as:

- What information can a side collect?
- How long does collection take?
- What resources must be committed?
- How reliable is the information?
- How can an opponent deceive, disrupt, or protect against it?

These systems should deepen the command decisions without replacing the basic observation and fog-of-war rules.

## Division of calculations

The default principle is:

> Players handle predictable, uncontested actions. The game master handles uncertainty, conflict, and hidden information.

| Situation | Default responsibility |
|-----------|------------------------|
| Moving along a known route with no opposition | Commander uses a movement reference |
| Changing formation or preparing a position | Commander uses a routine action aid |
| Enemy contact, ambush, or contested movement | Game master adjudicates |
| Combat or attempted capture of an objective | Game master adjudicates |
| Weather or terrain modifier already listed on the reference aid | Commander applies it |
| Unusual weather, damaged route, unclear information, or edge case | Game master decides using the stated principles |
| Information available only to one side | Game master controls and communicates it |

## Proposed decision aids

The first prototype should use simple physical aids rather than open-ended arithmetic:

- A movement table with a small number of terrain categories.
- Condition cards or tokens for weather and visibility.
- A short list of routine action times.
- A combat worksheet or outcome table used by the game master.
- A visible game clock and private notes for hidden information.
- A standard order form so commanders state who is acting, what they are doing, where, and with what objective.

The goal is not to remove judgment. The goal is to reserve judgment for the parts of the game where uncertainty and conflict are interesting.

## Fairness and disputed rulings

The game master makes the ruling during live play so the real-time game can continue. A commander may ask for the ruling to be recorded for review after the session, but should not be able to repeatedly reopen a decision during the scenario.

If the rules do not cover a situation, the game master should:

1. State the temporary ruling and the factor it is based on.
2. Apply the same ruling to equivalent situations for both sides.
3. Record the gap for the post-game rules review.
