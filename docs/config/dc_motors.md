---
title: "dc_motors: Config Reference"
---

# dc_motors: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `dc_motors:` section of your config is where you specify any DC motor
devices in your machine, as well as configuring the control events 
that will cause the dc_motors to activate.

Note that most platforms use `coils:` instead, along with `coil_player:`;
at initial release, only the FAST 0051 EXP board supports the dc_motor config definition described on this page.

Here's an example `dc_motors:` section with a dc_motor defined - *my_dc_motor*, as well as two shaking event options, `mid_dc_motor` and `hi_dc_motor`:

``` yaml
fast:
  exp:
    boards:
      0051board:
        model: FP-EXP-0051

dc_motors:
  my_dc_motor:
    number: 0051board-1
    control_events:
      mid_dc_motor:
        # action: pulse # pulse is default
        duration: 500ms
        power: 0.25
      hi_dc_motor:
        action: pulse
        duration: 500ms
        power: 0.25
      stop_dc_motor:
        action: stop
```

For each dc_motor in your `dc_motors:` section, the following settings apply:

## Required settings

The following sections are required in the `dc_motors:` section of your
config:

### number:

Single value, type: `string`. Defaults to empty.

This is the number of the dc_motor which specifies which driver output the
dc_motor is physically connected to. The exact format used here will depend
on which control system you're using and how the dc_motor is connected.
In practice with the FAST 0051, it will be the board name, and then `-1` or `-2`
as the 051 supports two motor outputs.

See the [How to configure "number:" settings](../hardware/numbers.md) guide for details.

## Optional settings

The following sections are optional in the `dc_motors:` section of your
config. (If you don't include them, the default will be used).

### default_power:

Single value, type: `number` (will be converted to floating point).
Default: `0.0`

The default power used if a control event does not otherwise specify one.

### platform:

Single value, type: `string`. Defaults to empty.

Name of the platform this dc_motor is connected to. The default value of
`None` means the default hardware platform will be used. You only need
to change this if you have multiple different hardware platforms in use
and this coil is not connected to the default platform.

See the [Mixing-and-Matching hardware platforms](../hardware/platform.md) guide for details.

### platform_settings:

Single value, type: `dict`. Defaults to empty.

Dict of platform specific settings. Consult your platform documentation for those settings.

### control_events:

Dict of one (or more) values, each is a type:
`dc_motors_pulse_settings:`, described below. Defaults to empty.

Control events to manage the behavior of the motor. 

### dc_motor_pulse_settings:
    action: single|enum(pulse,stop)|pulse
    power: single|float|None
    duration: single|template_secs|None

#### action:

Single value, type: one of the following options: `pulse`, `reverse_pulse`, `stop`.
Default: `pulse`

Whether this control event should cause a pulse of power to the driver, pulse in reverse, or should stop any current power (coasting).

#### power:

Single value, type: `number` (will be converted to floating point).
Default: `None`

What power setting to use for the dc_motor when the event is received. If unset, the `default_power` value will be used.

#### duration:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `None`

What duration to pulse the power for when the control event is received.


### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Enables more detailed debug information to be added to the log (when
verbose logging is enabled).

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to empty.

Tags work like tags for any device. Nothing special here.

## Related How To guides

* [dc_motors](../mechs/dc_motors.md)
