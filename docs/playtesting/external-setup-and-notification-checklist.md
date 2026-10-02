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
  `py -3 -m pip install -r requirements-map.txt` from the repository root.
  Copy the fictional fixture to `%USERPROFILE%\OliveDrabPrivate\game.toml`
  outside the repository and replace **all test content** before real use.
  From the repository root, complete an unaided `--check` and real render
  using the concrete commands in the
  [build sheet](shared-map-build-sheet.md).
- [ ] Keep the private game TOML, master snapshots, and backup outside the
  repository and Discord. Write `updated_at` and `released_at` with the
  shared local time-zone offset (for example, `-07:00`). Confirm the exact
  Discord text-channel names match the renderer's posting manifest.
- [ ] Render a GM-master PNG and separate filtered NATO and Russia PNGs with
  captions; the master is for `#gm-map-record` only.
- [ ] Test renderer inclusion and filtering with fictional markers: each
  side PNG and caption contains only public and earned side-visible data,
  never opposing live markers, hidden zones, GM notes, `source_id`, opposing
  `marker_id`, or master descriptions. Verify the side PNG shows friendly
  `cite` and opposing `release_id` and `released_at`; the text caption lists
  released descriptions only. Moving a live marker must not silently update
  an older released report.
- [ ] Test Discord permissions with each actual commander account: each sees
  only its own private channel, not the opposing channel or
  `#gm-map-record`. If used, the Observer has read-only audit access to all
  needed channels and cannot post.
- [ ] Inspect generated PNGs and captions against the manifest: side,
  version, banner, filename, and channel must agree. Inspect superseded
  Discord posts for leaks and distinguish newer versions; neither posts nor
  `#gm-map-record` serve as the private master backup.
- [ ] Test screen sharing of a filtered view without exposing the master,
  other side, thumbnails, notifications, or private paths.
- [ ] With each commander's actual account, verify that a phone displays
  that side's PNG legibly and cannot see the opposing side or master channel.
- [ ] Use the [build-sheet pre-post checklist](shared-map-build-sheet.md)
  for one-file/one-channel posting, and stop all further posts on a
  wrong-channel incident until the GM ruling is recorded. Deletion is not
  a fix; corrected re-posts require a new version.
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
