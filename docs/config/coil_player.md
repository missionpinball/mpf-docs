---
title: "coil_player:"
---

# coil_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `coils:` section of
    a step.

The `coil_player:` section of your config is where you configure
coil/solenoid/driver actions (pulse, enable, disable, etc.) based on
events. It's also used in shows (via the `coils:` section) to perform
coil actions in that show step.

Example from a config file:

``` yaml
coil_player:
  some_event: coil_1
  some_other_event:
    coil_2:
      action: enable
      hold_power: .5
```

In the example above, when the event called `some_event` is posted,
coil_1 will pulse. When the event `some_other_event` is posted, coil_2
will enable (be held on) at power level 0.5 (means 50% of maximum
power).

Note that the `some_event: coil_1` is entered in a different way than
the `some_other_event:`. The first one has a simple key/value pair,
whereas the second has a complete nested sub-configuration.

The first example shows the "express" config, while the second shows
the full config. (What's an "express config?" Details
[here](instructions/express_config.md).

The coil player's express config is the "pulse" action.

Example coil player from a show:

``` yaml
##! show: test
- time: 0
  coils:
    coil1: pulse
```

See [Coil player](../config_players/coil_player.md) for
details.

## Optional settings

The following sections are optional in the `coil_player:` section of
your config. (If you don't include them, the default will be used).

### action:

Single value, type: one of the following options: pulse, on, off,
enable, disable. Default: `pulse`

What action the coil should perform. Note that "on" and "enable" are
the same, and that "disable" and "off" are the same.

### hold_power:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

This setting lets you control how much power is sent to the coil when
it's "held" in the on position. This is an float value from 0-1 (i.e.
0% power to 100% power) which controls the relative power. If not set it
will use `default_hold_power` of the [coils:](coils.md).

### max_wait_ms:

Single value, type: `integer`. Defaults to empty.

The maximum time in ms which MPF might use to delay this pulse for power
management reasons. See
[Power Management in Software](../hardware/voltages_and_power/power_management.md) for details.

### pulse_ms:

Single value, type: `integer`. Defaults to empty.

The number of milliseconds you'd like this coil to pulse for. This
setting overrides the coil's *default_pulse_ms* setting. Note that this
setting only affects pulse actions. Make sure you are not exceeding the
coil's *max_pulse_ms* setting. If not set it will use
`default_pulse_ms` of the [coils:](coils.md).

### pulse_power:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

The power factor which controls how much power is applied during the
initial pulse phase of the coil's activation. (Note that not all
hardware platforms support variable pulse power.)

If not set it will use `default_pulse_power` of the
[coils:](coils.md).

## Related How To guides

* [Coil player](../config_players/coil_player.md)
* [Coils (Solenoids)](../mechs/coils/index.md)
* [Shakers](../mechs/shaker.md)
