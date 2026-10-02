# External Setup and Notification Checklist

Complete this with the actual GM and participants. Repository preparation does
not prove any item below is complete.

## Discord

- [ ] Create a game-only server or isolated channel group.
- [ ] Add GM, NATO commander, and Russia commander roles. If an observer participates, add the observer role as an optional support role.
- [ ] Create group, NATO-private, Russia-private, approved opposing-contact, and
  GM-record channels.
- [ ] Set read, post, attachment, history, and mention permissions for each
  role; test with harmless messages.
- [ ] If an observer participates, confirm the observer can read every game
  channel and record (read-only audit access) and cannot post in game channels unless a commander or GM
  interacts with them; observers are playtest-only.
- [ ] Confirm personal direct messages are not part of the record.
- [ ] Freeze all role and channel permissions before the first order; make no
  permission changes until the playtest ends.
- [ ] Test primary and backup notification methods and response-by reminders.

## Shared map

- [ ] Reproduce Brackenford labels, sectors, approaches, and control pairs from
  the authoritative map document.
- [ ] Treat the repository-built static PNG renderer as the **proposed**
  #15 method only; the platform choice remains pending user confirmation and
  human leak testing.
- [ ] The GM machine is the user's PC with Python 3.12.10 available as
  `py -3`; Pillow is not installed yet. Install it with
  `py -3 -m pip install -r requirements-map.txt`, then complete an unaided
  dry run using `py -3 scripts/render_map.py GAME.toml --out DIR --check`
  and a real render to confirm the renderer works on that machine.
- [ ] Keep the private `GAME.toml` and master snapshots outside the repository
  and Discord. Confirm the actual Discord text-channel names for the NATO,
  Russia, and GM records destinations before posting.
- [ ] Create one GM master view and filtered NATO and Russia views.
- [ ] Test that hidden markers, layers, links, exports, and screen sharing do
  not leak opposing private information; commanders can view only their own
  private channel, while an Observer (if used) has read-only access to all
  channels.
- [ ] Confirm that players can read the PNGs on a phone and that each commander
  account sees only its own side's channel.
- [ ] Record map version, exact channel names, access list, snapshot method,
  private backup location, restore result, and leak-test results.

## Record and notification check

```text
Discord/server:
Map platform:
Shared local time zone:
Primary notification:
Backup notification:
Response-deadline test result:
Map access test result:
Permissions blocker/workaround:
Observer used: yes / no
GM sign-off:
```

Never paste real personal contact details into public repository files.
