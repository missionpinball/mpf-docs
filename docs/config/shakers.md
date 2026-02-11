---
title: "shakers: Config Reference"
---

# shakers: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `shakers:` section of your config is where you specify any shaker
devices in your machine, as well as configuring the control events 
that will cause the shakers to activate.

Note that most platforms use `coils:` instead, along with `coil_player:`;
only the FAST 1313 EXP board supports the shaker config definition described on this page.

Here's an example `shakers:` section with a shaker defined - *my_shaker*, as well as two shaking event options, `mid_shaker` and `hi_shaker`:

``` yaml
fast:
  exp:
    boards:
      1313board:
        model: FP-EXP-1313

shakers:
  my_shaker:
    number: 1313board-1
    control_events:
      mid_shaker:
        duration: 500ms
        power: 0.25
      hi_shaker:
        duration: 2s
        power: 0.75
```

For each shaker in your `shakers:` section, the following settings apply:

## Required settings

The following sections are required in the `shakers:` section of your
config:

### number:

Single value, type: `string`. Defaults to empty.

This is the number of the shaker which specifies which driver output the
shaker is physically connected to. The exact format used here will depend
on which control system you're using and how the shaker is connected.
In practice with the FAST 1313, it will be the board name, and then `-1` as the
1313 only supports a single controlled output.

See the [How to configure "number:" settings](../hardware/numbers.md) guide for details.

## Optional settings

The following sections are optional in the `servos:` section of your
config. (If you don't include them, the default will be used).

### default_power:

Single value, type: `number` (will be converted to floating point).
Default: `0.0`

The default power used if a control event does not otherwise specify one.

### platform:

Single value, type: `string`. Defaults to empty.

Name of the platform this shaker is connected to. The default value of
`None` means the default hardware platform will be used. You only need
to change this if you have multiple different hardware platforms in use
and this coil is not connected to the default platform.

See the [Mixing-and-Matching hardware platforms](../hardware/platform.md) guide for
details.

### platform_settings:

Single value, type: `dict`. Defaults to empty.

Dict of platform specific settings. Consult your platform documentation
for those settings.

### control_events:

Dict of one (or more) values, each is a type:
`shaker_pulse_settings:`, described below. Defaults to empty.

Control events to manage the behavior of the motor. 

### shaker_pulse_settings:
    action: single|enum(pulse,stop)|pulse
    power: single|float|None
    duration: single|template_secs|None

#### action:

Single value, type: one of the following options: `pulse`, `stop`.
Default: `pulse`

Whether this control event should cause a pulse of power to the driver or should stop any current power.

#### power:

Single value, type: `number` (will be converted to floating point).
Default: `None`

What power setting to use for the shaker when the event is received. If unset, the `default_power` value will be used.

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

* [Shakers](../mechs/shaker.md)
