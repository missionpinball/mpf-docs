---
title: flipper_cradle_release
---

# flipper_cradle_release


--8<-- "event.md"

Posted when one of the flipper buttons that has previously been active
for more than 3 seconds has been released.

If the player pushes in one flipper button for more than 3 seconds, and
then the second one and holds it in for more than 3 seconds, this event
won't be posted until both buttons have been released.

Note that in order for this event to work, you have to add
`left_flipper` as a tag to the switch for your left flipper, and
`right_flipper` to your right flipper.

See [timed_switches:](../config/timed_switches.md) for details.

--8<-- "event_no_keywords_notice.md"
