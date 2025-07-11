---
title: "steppers: Config Reference"
---

# steppers: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `steppers:` section of your config is where you configure steppers.

This is an example:

``` yaml
# main config
p_roc:
  use_separate_thread: true
  pd_led_boards:
    6:
      use_stepper_0: true
      stepper_speed: 1352400000  # Determine empiricall. Increasing slows pulsesrate
switches:
  s_stepper_home:
    number: 4/0/5
steppers:
  ramp_diverter:
    number: 6-0
    homing_mode: switch
    homing_switch: s_stepper_home
    homing_direction: clockwise
    pos_min: 0 # Default. (Neg values are behind home)
    pos_max: 100 # Default
    reset_events: machine_reset_phase_3, ball_starting, ball_will_end
    reset_position: 0 # Default
    debug: true
    named_positions:
      2: move_to_2
      25: move_to_25
      45: move_to_45
##! mode: base
# base mode
timers:
  test_diverter:
    start_value: 0
    end_value: 6
    start_running: true
    restart_on_complete: true
event_player:
  timer_test_diverter_tick{device.timers.test_diverter.ticks==1}: move_to_2
  timer_test_diverter_tick{device.timers.test_diverter.ticks==3}: move_to_25
  timer_test_diverter_tick{device.timers.test_diverter.ticks==5}: move_to_45
```

## Required settings

The following sections are required in the `steppers:` section of your
config:

### number:

Single value, type: `string`. Defaults to empty.

This is the number of the stepper which specifies which stepper the it
is physically connected to. The exact format used here will depend on
which control system you're using and how the stepper is connected.

See the [How to configure "number:" settings](../hardware/numbers.md) guide for
details.

## Optional settings

The following sections are optional in the `steppers:` section of your
config. (If you don't include them, the default will be used).

### ball_search_max:

Single value, type: `integer`. Default: `1`

The maximum position to use during ball search for this stepper. During
ball search the stepper will move between `ball_search_min` and
`ball_search_max`.

### ball_search_min:

Single value, type: `integer`. Default: `0`

The minimum position to use during ball search for this stepper. During
ball search the stepper will move between `ball_search_min` and
`ball_search_max`.

### ball_search_wait:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `5s`

How long should the stepper wait after moving to `ball_search_min`
before moving to `ball_search_max`.

### homing_direction:

Single value, type: one of the following options: clockwise,
counterclockwise. Default: `clockwise`

In which direction should the stepper move to reach the home position?

### homing_mode:

Single value, type: one of the following options: hardware, switch.
Default: `hardware`

Some controllers support `hardware` homing which should be preferred.
However, you can also define a `homing_switch` which will be used to
determine whether the stepper is at the home position.

### homing_switch:

Single value, type: `string` name of a
[switches:](switches.md) device. Defaults to
empty.

Switch to check if the stepper is at the home position when
`homing_mode` is set to `switch`.

### include_in_ball_search:

Single value, type: `boolean` (`true`/`false`). Default: `true`

Set to true to enable ball search on this stepper.

### named_positions:

One or more sub-entries. Each in the format of `number` (will be
converted to floating point) : `string`

This is a sub-section mapping of stepper positions to MPF event names.
For example:

``` yaml
#! steppers:
#!   my_stepper:
#!     number: 1
    named_positions:
      0: move_home
      999: move_to_999
      -500: move_to_-500 # Negative positions are behind home
```

The values in this `named_positions:` list represent MPF events that,
when posted, tell this stepper to move to a certain position. So in the
example above, when the *move_to_999* event is posted, this stepper will
move to position 999.

### platform:

Single value, type: `string`. Defaults to empty.

Name of the platform this stepper is connected to. The default value of
`None` means the default hardware platform will be used. You only need
to change this if you have multiple different hardware platforms in use
and this stepper is not connected to the default platform.

See the [Mixing-and-Matching hardware platforms](../hardware/platform.md) guide for
details.

### platform_settings:

Single value, type: `dict`. Defaults to empty.

Platform specific stepper settings for this stepper. Check the
[documentation of your platform](../hardware/platform.md) for details.

### pos_max:

Single value, type: `integer`. Default: `1000`

Maximum possible position.

### pos_min:

Single value, type: `integer`. Default: `0`

Minimum possible position. Negative values are left of the home
position.

### relative_positions:

One or more sub-entries. Each in the format of `number` (will be
converted to floating point) : `string`

This is a sub-section mapping of relative stepper increments to MPF event names (as opposed to absolute rotational positions).
For example:

``` yaml
#! steppers:
#!   my_stepper:
#!     number: 1
    relative_positions:
      50: advance_50 # positive values move the stepper in the direction of the `homing_direction`
      -50: move_back_50 # Negative positions move the stepper opposite of the `homing_direction`
```

The values in this `relative_positions:` list represent MPF events that,
when posted, tell this stepper to increment a certain number of "steps". So, in the
example above, when the *advance_50* event is posted, this stepper will
advance 50 steps or increments from where it is currently. Positive relative positions always advance in the direction that is defined in `homing_direction`. Negative relative positions move in the opposite direction.

### reset_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default:
`machine_reset_phase_3, ball_starting, ball_will_end, service_mode_entered`

Events to reset the position of the stepper.

### reset_position:

Single value, type: `integer`. Default: `0`

Reset position for this stepper. Usually this is the home position.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

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

Not used currently.

## Related How To guides

* [Stepper Motors](../mechs/steppers.md)
