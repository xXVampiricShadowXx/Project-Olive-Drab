# Collaborative Playtest Setup Session Agenda

This is a joint preparation session, not the human playtest or a declaration
of readiness. The user operates the Discord and map interfaces; Dev/QA
reviews the resulting structure against the [readiness
guide](human-playtest-readiness-guide.md), [operating
procedure](../game-design/06-prototype-operating-procedure.md), and
[map authority](../game-design/12-town-map-and-terrain-sectors.md). No real
account, server, map, or contact route is created by these repository docs.

## Decisions to record before building

- [ ] Dedicated game-only server or isolated category in an existing server?
  Record the choice and any inherited-role audit in issue #14.
- [ ] Which map platform and separate-view/access arrangement? Compare the
  [map build sheet](shared-map-build-sheet.md) options without a default;
  record the choice and constraints in issue #15.
- [ ] Optional Observer participating? Record yes/no in [external
  setup](external-setup-and-notification-checklist.md) and issue #14.
- [ ] Which primary game-channel notification and `<backup contact method>`
  will the user test? Record methods privately with the GM and results (not
  addresses) in readiness guide section 1/2 and issue #14.
- [ ] Where will the GM store access-controlled records and a separate
  backup? Record location fields privately in the
  [final preflight](../game-design/16-final-gm-preflight-readiness-checklist.md)
  and map method/result in issue #15; do not put links in public comments.

## Ordered live agenda

| Step | User action in external UI | Dev/QA check | Record result |
|---|---|---|---|
| 1. Confirm choices and boundaries | Choose the server variant, optional Observer and map platform; identify the GM and permission tester by role only. | Check choices against the decision list and that the GM controls release; no invented superior/subordinate role. | Issue #14 (server/observer), issue #15 (map), readiness guide sections 1–3. |
| 2. Build Discord roles and category | Create the game roles and `Brackenford Game` category; deny `@everyone` category visibility; audit existing roles. | Compare both variants and the role baseline with the [Discord build sheet](discord-build-sheet.md). | Issue #14; readiness guide section 2 channel names. |
| 3. Build channels and permissions | Create group, private, GM-only, curated feed and opposing-contact channels; apply each matrix profile. | Check every role/channel intersection, including Observer and inherited/admin privileges; no personal DMs in the game record. | Issue #14; readiness guide section 2 dry-run fields. |
| 4. Exercise communications | Use View Server As Role and actual-account harmless posts/files; test GM-approved relay, role-ping deadline and `<backup contact method>`. | Compare each PASS/FAIL to the Discord verification script; check GM receipt and redaction without collecting personal data. | Issue #14; [communication rehearsal](human-communication-order-rehearsal.md) step 1 and readiness guide section 2. |
| 5. Build Brackenford base | Copy the 6-by-5 grid, terrain, approaches, river, crossings and control pairs from doc 12. | Check all 30 cells and public features against source ASCII/table, not an inferred redraw. | Issue #15; readiness guide section 3. |
| 6. Filter and test map views | Create GM master plus NATO and Russia views; use fictional markers to test links, layers, exports, history and screen sharing. | Compare each test's PASS/FAIL and information boundary with the [map build sheet](shared-map-build-sheet.md); do not view or post live hidden placements publicly. | Issue #15; readiness guide section 3 map access test. |
| 7. Record recoverability | Enter map version, dated snapshot method, separate backup location and restore result in private GM records. | Check fields in final preflight and verify no private URL or hidden state is posted in issues. | Issue #15; final GM preflight `Master map version/link`, filtered map links and `Backup location`. |
| 8. Close the setup rehearsal | Leave unresolved failures as blockers; user/GM decides whether to retest or document a temporary workaround for both commanders' acceptance. | Check [final go/no-go](human-playtest-readiness-guide.md) fields are not marked `GO` merely because docs exist; communicate open questions without making mechanics decisions. | Issues #14/#15 for each outstanding result; readiness guide `Unresolved blocker`, `Temporary workaround and expiry`, `Both commanders agree`, and `GM authorization time` only when actually decided. |

Roster, succession, and consent (issue #16) remain with the user and are
outside this setup session. Do not mark #14, #15, or #16 complete from the
agenda; the human permission, notification, access and delivery checks are
still pending. If a setup choice seems to require a new mechanic, record an
open question for the user rather than changing the rules.
