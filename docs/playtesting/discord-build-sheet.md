# Discord Build Sheet (Refs #14)

This is a setup script for the human GM and server owner, not evidence that a
server exists. The [operating procedure](../game-design/06-prototype-operating-procedure.md)
and [readiness guide](human-playtest-readiness-guide.md) govern communication and
information release. Discord delivers messages; the GM's time-stamped registers
remain authoritative. Use the first-test roles only: GM, NATO commander, Russia
commander, and optional Observer. No superior or subordinate player role exists
in the three-person prototype. Never use personal direct messages for orders,
reports, rulings, map updates, or game notifications.

## Choose the container and build it

1. **Dedicated server:** The user uses Discord desktop's **Add a Server >
   Create My Own** to create a game-only server, then keeps unrelated members
   out. The server owner/setup administrator must be the GM, not a commander
   or Observer: privileged access bypasses channel denies. Record the server
   choice in issue #14, without
   invite links or personal identifiers.
2. **Existing server:** The user uses the existing server and reserves one
   game-only `Brackenford Game` category. Audit every participant's other
   roles, including moderation roles and `Administrator`: another role or
   server-wide privilege may defeat a game-channel restriction. The server
   owner/setup administrator must be the GM, not a commander or Observer.
   If that cannot be arranged, this variant is **NO-GO**; use an isolated
   server/platform with a privileged GM owner and retest. Do not put the
   master map in a generally shared server channel. Record the decision in
   issue #14.
3. In either variant, open **Server Settings > Roles > Create Role**. Create
   `GM`, `NATO commander`, `Russia commander`, and `Observer` only if used.
   On each role's **Permissions** tab, keep game-role server-wide privileges
   minimal: leave `Administrator` and the management permissions in the matrix
   disabled. On the `NATO commander` and `Russia commander` roles' **Display**
   tab, turn on **Allow anyone to @mention this role** so the GM can ping a
   commander without any mass-mention permission.
   Save changes and assign each participant only their intended game role
   through the role's **Manage Members** tab. Audit all additional roles and
   application/bot principals; record role names in
   [external setup](external-setup-and-notification-checklist.md).
4. From the channel list's **Create Channel > Create Category**, create
   `Brackenford Game`. In **Edit Category > Permissions**, deny
   `View Channels` for `@everyone`; explicitly grant only the game roles
   their intended access to each child channel. Keep game-role server-level
   permissions minimal. Do not rely on a channel's synced category permissions
   for a private channel; edit each channel's permissions and re-check after
   any category resync, role change, or bot addition during setup.
   **Permissions are frozen at game start:** finish and verify every role
   and channel permission before the first order, then make no permission,
   role, or channel changes until the playtest ends. If a permission fault
   is discovered during play, the GM records it and may pause under the
   real-life/pause procedure; any correction is recorded as a deviation and
   retested before play resumes. No role except the
   server owner/setup administrator needs `Manage Channels` or `Manage Roles`.
5. Within that category, use **Create Channel > Text** to add `#group`
   (non-sensitive procedure and public updates), `#nato-private` (NATO and GM orders/reports),
   `#russia-private` (Russia and GM orders/reports),
   `#opposing-contact` (GM-approved, GM-visible relay),
   `#public-redacted-feed` (optional Observer's curated public transcript),
   `#observer-response` (optional, GM-visible interaction only),
   `#gm-orders-reports`, and `#gm-map-record` (GM-only records). Set the
   per-channel access levels below via **Edit Channel > Permissions >
   Add Roles or Members**. Save each override, including an explicit denial
   for every role assigned `No access`; inspect whether the channel is unsynced.
   Create `#observer-response` only if an Observer participates. Keep it
   hidden from both commanders. Observer has standing `Text reply`
   access there for the whole playtest, but by conduct rule posts only to
   answer a question the GM has placed in that channel; the GM logs each
   question and reply and handles any unprompted post as a conduct matter,
   not by changing permissions. A commander
   asks through `#group` only when the question
   is non-sensitive, or through their own private channel otherwise; the
   GM relays only the permitted question and any redacted response. Never
   paste a live opposing private report into the Observer channel.
   Keep the feed even without an Observer only if useful to the GM; do not
   assign another audience to it. Store the master map and private register
   links only in GM-only locations, with a separate backup per the
   [private-records guide](gm-private-records-and-data-handling.md).
6. The GM posts public updates in `#group`. For an opposing contact request,
   the requesting commander writes to their own private channel; the GM
   approves or declines it there, and relays only approved text into
   `#opposing-contact`, with both commanders able to read and the GM able to
   review the entire exchange. Replies return through the same private-to-GM
   route. Do not use DMs, private threads, or unlogged voice for this route.
   A higher player's permission applies only if a higher player-controlled
   role actually exists in a later arrangement; do not invent one here.
7. For a response-by reminder, the GM sends the deadline in the relevant
   private channel and pings only that commander's game role (not `@everyone`
   or `@here`). Because the commander roles are mentionable (step 3), the
   GM's ordinary `Post` access is enough; no role, including GM, is granted
   **Mention @everyone, @here, and All Roles**. Confirm delivery to
   the intended recipient. Record delivery time and the
   response-by time in the relevant register. Test the primary game-channel
   notification and the separately agreed `<backup contact method>` with a
   harmless reminder; never publish the backup address or personal details.
   If a role mention cannot deliver, use a tested, GM-approved notification
   route and record the blocker/workaround before go/no-go.

## Permission matrix

Apply each access level to the named role **on each channel**. The access
levels (`No access`, `Read-only`, `Text reply`, `Post`) are this sheet's
shorthand, not Discord settings: each one is a bundle of the real Discord
permission switches listed in the second table. `@everyone` uses
`No access` everywhere, including the category; `Observer` is optional.
`A` means Allow and `D` means Deny; set explicit denies on each
private channel rather than relying on an absent allow. `Manage Roles` is a
server-level role permission, not a text-channel switch; it remains denied on
all game roles. Server owner/administrator access is an exception that must be
audited separately.

| Channel | @everyone | GM | NATO commander | Russia commander | Observer |
|---|---|---|---|---|---|
| `#group` | No access | Post | Post | Post | No access |
| `#nato-private` | No access | Post | Post | No access | No access |
| `#russia-private` | No access | Post | No access | Post | No access |
| `#opposing-contact` | No access | Post | Read-only | Read-only | No access |
| `#public-redacted-feed` | No access | Post | Read-only | Read-only | Read-only |
| `#gm-orders-reports` | No access | Post | No access | No access | No access |
| `#gm-map-record` | No access | Post | No access | No access | No access |
| `#observer-response` (only if Observer used) | No access | Post | No access | No access | Text reply (answers GM-placed questions only) |

| Discord permission (real setting name) | No access | Read-only | Text reply (Observer only) | Post |
|---|:---:|:---:|:---:|:---:|
| View Channels | D | A | A | A |
| Send Messages | D | D | A | A |
| Send Messages in Threads | D | D | D | D |
| Create Public Threads | D | D | D | D |
| Create Private Threads | D | D | D | D |
| Read Message History | D | A | A | A |
| Attach Files | D | D | D | A |
| Embed Links | D | D | D | A |
| Add Reactions | D | D | D | D |
| Mention @everyone, @here, and All Roles | D | D | D | D |
| Manage Messages | D | D | D | D |
| Manage Channels | D | D | D | D |
| Manage Roles (server-level role setting) | D | D | D | D |
| Manage Threads | D | D | D | D |
| Use Application Commands | D | D | D | D |

The GM uses `Post` to place curated copies in the feed; commanders and
Observer cannot post there. `Text reply` is Observer's fixed text-only access in
`#observer-response` for the whole playtest; Observer uses it only to answer a
GM-placed question. Role pings work because the two commander roles have
**Allow anyone to @mention this role** turned on; nobody can use `@everyone`
or `@here`. Disable application integrations/bots with extra
access or test them as separate principals. Discord permission overrides and
role stacking can change effective access, so the matrix is not a substitute
for a live test. See Discord's [channel permission
guide](https://support.discord.com/hc/en-us/articles/10543994968087-Channel-Permissions-Settings-101)
and [permission setup FAQ](https://support.discord.com/hc/en-us/articles/206029707-Setting-Up-Permissions-FAQ).

## Human permission and delivery rehearsal

The user and GM run this with harmless fictional text and a harmless file (no
real orders, placements, private links, or personal data). In Discord desktop,
open **Server Settings > Roles**, choose each role's **Display** tab and
select **View Server As Role**; select combined roles in the preview bar to
audit stacked privileges, then **Disable** the preview. Have the actual
participants check from their own accounts: role preview does not prove
delivery, attachment behavior, notification receipt, or stacked-role safety.
Repeat for any participant holding more than one role and after any setup
change to permission overrides; complete this rehearsal before game start,
because permissions do not change during play. Inspect the actual server owner and every administrator
identity separately: **PASS** only if these privileged identities are GM-only,
never a commander or Observer, and no other moderator/bot can expose game
records. Role preview cannot simulate owner/administrator bypass. For every row below,
record actual `PASS` or `FAIL`, channel name, role, and a redacted observation
in the [readiness guide section 2](human-playtest-readiness-guide.md) dry-run
completion fields, [communication rehearsal](human-communication-order-rehearsal.md)
step 1, or issue #14 comments; never post participant handles, contact
addresses, tokens, invite links, private reports, or screenshots of hidden
state. `FAIL` is a readiness blocker until corrected and retested or an
accepted temporary workaround is recorded. The role-preview control is
documented in Discord's [View Server As Role
guide](https://support.discord.com/hc/en-us/articles/360055709773-View-Server-As-Role-Permission-Guide).

| Check (repeat for each named channel/role) | Expected PASS | Expected FAIL to verify |
|---|---|---|
| `@everyone` in each of the seven core channels (plus optional `#observer-response`) | Cannot see, read history, post, or attach | Any channel or history visible, or posting succeeds |
| GM in each core and optional channel | Can see/read, post harmless text and attach harmless file | Any required channel or action inaccessible |
| NATO in `#group`, `#nato-private` | Can see/read, post harmless text and attach harmless file | Missing expected access or failed post/attachment |
| NATO in `#opposing-contact`, `#public-redacted-feed` | Can see/read but cannot post, attach, react, create or post in threads, or run commands | Any write/attachment/reaction/thread/command succeeds |
| NATO in `#russia-private`, both GM records and optional observer response | Cannot see/read/post/attach or get a working channel link | Any content or action accessible |
| Russia in `#group`, `#russia-private` | Can see/read, post harmless text and attach harmless file | Missing expected access or failed post/attachment |
| Russia in `#opposing-contact`, `#public-redacted-feed` | Can see/read but cannot post, attach, react, create or post in threads, or run commands | Any write/attachment/reaction/thread/command succeeds |
| Russia in `#nato-private`, both GM records and optional observer response | Cannot see/read/post/attach or get a working channel link | Any content or action accessible |
| Observer (if used) in `#public-redacted-feed` | Sees only curated public/redacted text and history; cannot post, attach, react, thread, or run commands | Missing feed or any write action succeeds |
| Observer (if used) in all six other core channels | Cannot see/read/post/attach or follow a channel link | Any private or live group content accessible |
| Observer in `#observer-response` (if used) | Reads the GM's permitted question and can reply with text only, visible to GM; cannot attach, react, thread, or see private opposing content | Attachment or other write action succeeds, a commander can see the channel, or any private opposing content is visible |
| Server owner/setup administrator and other privileged identities | Owner/admin is GM-only; other moderators/bots cannot access or leak private game content | Commander/Observer is owner/admin, or privileged third party exposes records: NO-GO until isolated and retested |
| Each game role, including GM, in every accessible channel | Cannot use `@everyone`/`@here`, manage messages/channels/roles/threads, or create private/public threads | Any such privilege succeeds |
| GM pings a commander role in that commander's private channel | Role mention delivers a notification to that commander only | Mention fails or another participant is notified |
| Opposing contact, with both commanders | Private request visible only to requester and GM; only GM can approve and post relay; both read approved relay; Observer cannot see it | Direct unapproved post, missing GM record, or private request exposed |
| Each commander's role-ping deadline and `<backup contact method>` | Intended commander receives harmless reminder by both tested routes; GM records delivery and response-by time | No delivery, wrong audience, or unrecorded backup route |

Do not mark issue #14 or the final preflight complete from this build sheet.
The human GM must record the actual names, permissions, notification results,
backup route, and sign-off after the rehearsal.
