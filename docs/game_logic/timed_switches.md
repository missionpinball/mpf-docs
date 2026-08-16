---
title: Timed Switches
---

# Timed Switches


Related Config File Sections:

* [timed_switches:](../config/timed_switches.md)

MPF includes functionality to manage "timed_switches" which are
scenarios when a single switch is continuously active (or inactive,
depending on the settings) for a set period of time.

A classic example of this is the flipper "cradling" where a player
holds a flipper button in for a few seconds. In almost all modern
machines, this is used to trigger a "player info" screen that shows
the player's score, how much bonus they have built up, high scores,
etc.

Flipper cradling is also used to reset (and pause) the ball search
timer, since a player could be holding a ball and drinking a beer,
meaning no switch hits will happen, but the ball search should not
start.

In fact MPF's default config file (which is automatically used in all
games) includes a `timed_switches:` section for flipper cradling and
automatically creates *flipper_cradle* and *flipper_cradle_release*
events (as long as you tag your flipper switches with *left_flipper* and
*right_flipper*).

Note that timed switches are similar to, but not the same as
[combo switches](combo_switches.md).

## Monitorable Properties

For
[dynamic values](../config/instructions/dynamic_values.md) and
[conditional events](../events/overview/conditional.md), the prefix for timed switches is
`device.timed_switches.](name) todo
[Help us to write it](../about/help.md)

## Related Events

* [(timed_switch_name)_active](../events/timed_switch_active.md)
* [(timed_switch_name)_released](../events/timed_switch_released.md)
