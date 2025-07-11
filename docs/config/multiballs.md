---
title: "multiballs: Config Reference"
---

# multiballs: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `multiballs:` section of your config is where you can configure
multiball devices. Multiball devices are "abstract" devices in that
they're more of a concept rather than a physical device on the
playfield. The multiball "device" is used to start multiball. This
section can be used in your machine-wide config files. This section can
be used in mode-specific config files.

Here's an example which contains several different multiball configs.
(In the real world, you'd probably only have one multiball for each
mode.)

``` yaml
#! switches:
#!   s_ball1:
#!     number:
#! coils:
#!   c_eject:
#!     number:
#! ball_devices:
#!   bd_lock:
#!     eject_coil: c_eject
#!     ball_switches: s_ball1
multiballs:
  add_a_ball:
    ball_count: 1
    ball_count_type: add
    shoot_again: 30s
    enable_events: mb4_enable
    disable_events: mb4_disable
    start_events: mb4_start
    stop_events: mb4_stop
  quick_2_ball:
    ball_count: 2
    ball_count_type: total
    shoot_again: 20s
    start_events: mb11_start
    ball_locks: bd_lock
  release_all_locked_balls:
    ball_count: current_player.lock_mb6_locked_balls
    ball_count_type: add
    shoot_again: 20s
    start_events: mb12_start
    ball_locks: bd_lock
  quick_add_2_ball:
    ball_count: 2
    ball_count_type: add
    shoot_again: 0
    start_events: mb6_start
    ball_locks: bd_lock
  full_ball_save:
    ball_count: 2
    shoot_again: 30s
    hurry_up_time: 10s
    grace_period: 5s
    add_a_ball_events: add_ball
    add_a_ball_shoot_again: 20s
    add_a_ball_hurry_up_time: 5s
    add_a_ball_grace_period: 10s
    start_events: mb20_start
```

## Required settings

The following sections are required in the `multiballs:` section of your
config:

### ball_count:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)). Defaults to empty.

The number of balls this multiball should eject (and maintain during
shoot again period). This is a template so you can use
[dynamic values](instructions/dynamic_values.md) to calculate this during runtime.

## Optional settings

The following sections are optional in the `multiballs:` section of your
config. (If you don't include them, the default will be used).

### add_a_ball_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, will add one ball into play. Posting
an event multiple times will add one ball for each time the event is
posted.

This is useful for "add-a-ball" functionality (which you can combine
with a counter and/or conditional events if you want to cap how many
total balls can be added into play).

### add_a_ball_grace_period:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `0`

The "secret" time (in MPF time string format) the ball save is still
active after any shows or effects that are triggered end. This is added
onto the add_a_ball_shoot_again.

### add_a_ball_hurry_up_time:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `0`

The time before the add-a-ball ball save ends (in MPF time string
format) that will cause the [multiball_(name)\_hurry_up](../events/multiball_multiball_hurry_up.md) event to be
posted. Use this to change the script for the light or trigger other effect.

### add_a_ball_shoot_again:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `5s`

Specifies a time period for "shoot again" when an add-a-ball event is
posted. This is a sort of automatic ball save for multiballs. The timer
will start when this multiball starts, and any balls that drain during
this time will be re-added into play.

### ball_count_type:

Single value, type: one of the following options: add, total. Default:
`total`

Set this to either `total` or `add`. Default is `total`.

This setting controls the behavior of how the multiball calculates the
number of balls it should add into play. Adjusting this setting is
useful when you have multiple (or stacked) multiballs and you want to
control how the combined counts work.

#### *total*:

Means the `ball_count:` setting will provide a target for the total
number of balls that should be in play when this multiball starts.
So if this multiball has a `ball_count: 3`, and it starts when 2
balls are live on the playfield, then this multiball will only add 1
more ball to bring the total to 3.

#### *add*:

Means that the `ball_count:` setting will specify the number of
balls that are added into play on top of whatever number of balls
are already in play. So if this multiball is set to `ball_count: 2`
and there are already 2 balls in play, then this multiball will add
2 more balls for a total of 4 balls live.

### ball_locks:

List of one (or more) values, each is a type: string name of a
[ball_devices:](ball_devices.md) device.
Defaults to empty.

Use those devices first when ejecting balls to the playfield on
multiball start. On start all balls from all locks will be ejected
(maybe more than ball_count). If there are not enough balls in the lock
more balls will be requested to the source_playfield.

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, disable this multiball. When disabled,
the other events (like start and add a ball) do not work. If this
multiball is in a mode config, then it will also be disabled when the
mode it's in stops.

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, enable this multiball. Note that
enabling a multiball is not the same as starting it, but the other
events (like to start the multiball or, or add a ball, etc.) do not work
unless this multiball is enabled.

Note that if you do not add any `enable_events:` (which is the default),
this multiball will be automatically enabled when the mode it's in
starts.

### grace_period:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `0`

The "secret" time (in MPF time string format) the ball save is still
active after any shows or effects that are triggered end. This is added
onto the shoot_again.

### hurry_up_time:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `0`

The time before the ball save ends (in MPF time string format) that will
cause the [multiball_(name)\_hurry_up](../events/multiball_multiball_hurry_up.md) event to be posted. Use this
to change the script for the light or trigger other effect.

### replace_balls_in_play:

Single value, type: `boolean` (`true`/`false`). Default: `false`

This setting controls whether the multiball should include existing
balls in play when counting the number of balls to add to the playfield.
Specifically for machines which physically lock multiple balls, this
setting should be used in tandem with balls-to-replace from
[multiball_locks:](multiball_locks.md) to accurately
populate the multiball when it starts.

See
[How to create a multiball with a traditional ball lock](../game_logic/multiballs/multiball_with_traditional_ball_lock.md) for detailed instructions on using this setting.

### reset_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `machine_reset_phase_3, ball_starting`

Event(s) that reset this multiball, which means they disable it as well
as disabling shoot again and resetting the ball add counts to 0.

### shoot_again:

Single value, type: `time string (ms) or template`
([Instructions for entering time strings](instructions/time_strings.md) and
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `10s`

Specifies a time period for "shoot again" which is a sort of automatic
ball save for multiballs. The timer will start when this multiball
starts, and any balls that drain during this time will be re-added into
play.

### source_playfield:

Single value, type: `string` name of a
[ball_devices:](ball_devices.md) device.
Default: `playfield`

The name of the playfield (from the `playfields:` section of your
machine config that this multiball will add balls to. You don't have to
worry about this unless you have multiple playfields that you're
managing separately (which is rare, usually only in head-to-head type
games).

### start_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, start the multiball. Note that these
events will only have an effect if this multiball is enabled.

### start_or_add_a_ball_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, will either start the multiball, or,
if it's started, will add another ball.

### stop_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, stop the multiball. If there are
multiball balls on the playfield, there's nothing that can be done
about that (unless you want to disable the flippers). However stopping
the multiball will cut off the "shoot again" period.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the
[documentation on the debug setting](instructions/debug.md) for details.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this device in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Unused.

## Related How To guides

* [Multiballs](../game_logic/multiballs/index.md)
