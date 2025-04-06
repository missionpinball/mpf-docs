---
title: Multiballs
---

# Multiballs


Related Config File Sections:

* [multiballs:](../../config/multiballs.md)
* [multiball_locks:](../../config/multiball_locks.md)


MPF includes a *multiball* feature which can be used to automatically
start and stop multiballs.

Each multiball in MPF has a separate name. There are several different
types of multiballs (run until a single ball is left, timed multiballs,
etc.) Multiballs can also be configured with multiball saves so that
(for example) any balls lost in the first 15 seconds of a multiball are
automatically re-launched back into play.

MPF also supports stacking of multiple multiballs at the same time.

Balls can be locked for multiball with the related
[Multiball Locks](multiball_locks.md) config section.

Video about ball locks and multiballs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2mFkgIlksC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Common Issues

Why does MPF wait about 10s when adding balls to the playfield from the
trough during a multiball?

When MPF adds a ball to the playfield the launcher waits until the
ball is confirmed to be on the playfield. For the first ball this
happens when a playfield switch is hit after the eject. However, this
will not work with more than one ball on the playfield (e.g. during a
multiball). In this case, the launcher will wait until its eject
timeout passed (`eject timeouts in ball_devices </config/ball_devices>`) which defaults to 10s.
Therefore, you need to tune `eject_timeouts` of your launcher to fix this issue.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for multiballs is `device.multiballs.(name)`.

### *balls_added_live*:

Numeric value of how many balls this multiball added into play.

### *balls_live_target*:

Numeric value of how many balls this multiball is attempting to keep in play.

### *enabled*:

Boolean (true/false) as to whether this multiball is enabled.

### *shoot_again*:

Boolean (true/false) as to whether this multiball is in "shoot
again" mode which means it's attempting to keep live.

## Related How To guides

* [Multiball locks](multiball_locks.md)
* [Multiball with a traditional ball lock](multiball_with_traditional_ball_lock.md)
* [Multiball with a virtual ball lock](multiball_with_virtual_ball_lock.md)
* [Multiball with multiple lock devices](multiball_with_multiple_lock_devices.md)
* [Add a ball multiball](add_a_ball_multiball.md)

## Related Events

* [multiball_(name)\_started](../../events/multiball_multiball_started.md)
* [multiball_(name)\_hurry_up](../../events/multiball_multiball_hurry_up.md)
* [multiball_(name)\_grace_period](../../events/multiball_multiball_grace_period.md)
* [multiball_(name)\_shoot_again](../../events/multiball_multiball_shoot_again.md)
* [multiball_(name)\_lost_ball](../../events/multiball_multiball_lost_ball.md)
* [multiball_(name)\_shoot_again_ended](../../events/multiball_multiball_shoot_again_ended.md)
* [multiball_(name)\_ended](../../events/multiball_multiball_ended.md)
* [ball_save_(multiball_name)\_timer_start](../../events/ball_save_multiball_timer_start.md)
* [ball_save_(multiball_name)\_add_a_ball_timer_start](../../events/ball_save_multiball_add_a_ball_timer_start.md)
