---
title: Ball Holds
---

# Ball Holds


Related Config File Sections:

* [ball_holds:](../config/ball_holds.md)

MPF's *ball holds* are used to temporarily hold a ball that has entered
a [Ball Devices](../mechs/ball_devices/index.md) while
something else happens.

The most common use cases are to hold a ball while you play a show, or
while a video mode is going on. Ball holds do not affect the balls in
play count, and if all other balls drain while a ball hold is in
progress, the players ball does not end.

Ball holds are *not* used to lock balls for multiball. (See the
[multiball_locks](multiballs/multiball_locks.md) device for that).

You can have lots of different ball holds in your game, typically
configured per mode.

Video about ball locks and multiballs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2mFkgIlksC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Monitorable Properties

For
[dynamic values](../config/instructions/dynamic_values.md) and
[conditional events](../events/overview/conditional.md), the prefix for ball holds is `device.ball_holds.(name)`.

### *balls_held*:

The number of balls this ball hold is currently holding

### *enabled*:

Boolean (true/false) which shows whether this ball hold is enabled.

## Related How To guides

* [Using ball_holds for a mystery award](../cookbook/mystery_award.md)

## Related Events

* [ball_hold_(name)_held_ball](../events/ball_hold_ball_hold_held_ball.md)
* [ball_hold_(name)_full](../events/ball_hold_ball_hold_full.md)
* [ball_hold_(name)_balls_released](../events/ball_hold_ball_hold_balls_released.md)
