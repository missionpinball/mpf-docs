---
title: Ball Saves
---

# Ball Saves


Related Config File Sections:

* [ball_saves:](../../config/ball_saves.md)

MPF uses *ball saves* to automatically re-serve a ball that has drained.
(Essentially this means the ball drain doesn't count.)

Ball saves are typically used in several scenarios:

* Give the player their ball back if they drain right after their ball
    starts.
* Give the player their ball back if there's a particularly wicked
    shot that tends to drain which the game designers feel bad about.
    (You should avoid this if possible, and instead, as Lyman Sheets
    would say, "Fix your f-ing game layout!")
* Use to make a timed mode where the player has unlimited drains.
* Etc.

You can configure ball saves to have various start and stop events and
timers, and you can configure multiple ones in different modes that do
different things.

This is an example:

``` yaml
ball_saves:
  random_ball_save:
    active_time](5s
    hurry_up_time)
center_post

## Related Events

* [ball_save_(name)_enabled](../../events/ball_save_ball_save_enabled.md)
* [ball_save_(name)_disabled](../../events/ball_save_ball_save_disabled.md)
* [ball_save_(name)_timer_start](../../events/ball_save_ball_save_timer_start.md)
* [ball_save_(name)_hurry_up](../../events/ball_save_ball_save_hurry_up.md)
* [ball_save_(name)_grace_period](../../events/ball_save_ball_save_grace_period.md)
* [ball_save_(name)_saving_ball](../../events/ball_save_ball_save_saving_ball.md)
