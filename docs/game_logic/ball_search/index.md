---
title: Ball Search
---

# Ball Search


Related Config File Sections:

* [ball_devices:](../../config/ball_devices.md)
* [switches:](../../config/switches.md)
* [playfields:](../../config/playfields.md)
* [example ball_search](../examples/index.md)

!!! note

    Ball search is off by default in MPF because it might hurt users not
    expecting it. In a prototype game it might trigger quite frequently and
    coils can seriously injure humans. To turn it on follow
    [/events/flipper_cradle_release](configuring_ball_search.md).

MPF contains ball search functionality which is used to try to dislodge
a stuck ball if MPF thinks there's a ball loose on the playfield but it
hasn't hit any playfield switches in awhile and the player is not
holding the flipper button in.

Ball searching in MPF has multiple "rounds", with the early rounds
doing a simple search that doesn't screw anything up (like firing pop
bumpers and pulsing eject coils from ball devices that don't contain
any balls), but after a few rounds of that, if it still hasn't found
the ball, it can start to to things like resetting drop targets.

Eventually MPF will give up and mark the ball as lost and kick a new
ball into play.

Everything is fully configurable, including the timeouts, the order
devices are searched, the number of rounds, etc.

Ball search in MPF is fairly automatic. It's enabled when MPF thinks
that balls are on the playfield, and disabled when no balls are free.
(This means that even when a machine tilts, ball search is still active
until the balls drain, etc.)

## Related How To guides

* [/events/flipper_cradle_release](configuring_ball_search.md)

## Related Events

* [ball_search_failed](../../events/ball_search_failed.md)
* [ball_search_started](../../events/ball_search_started.md)
* [ball_search_stopped](../../events/ball_search_stopped.md)
* [flipper_cradle](../../events/flipper_cradle.md)
* [flipper_cradle_release](../../events/flipper_cradle_release.md)

* [How to configure Ball Search](configuring_ball_search.md)
