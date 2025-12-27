---
title: "fast:net: Config Reference"
---

# fast:net: Config Reference

--8<-- "deeper_config_section.md"

| Valid in | |
|-----|:----:|
|[machine](../instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](../instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Within the [`fast:`](../fast.md) section of your machine-wide config, you configure the IO network in the subsection `net:`.

### port:

List of one (or more) values, each is a type: `string`. Defaults to `auto`.

A comma-separated list of the serial port names your FAST controller uses.

### io_loop:

Dict of string board names to dicts of IO board properties. Defaults to empty.

Each item defines its own name and has two sub-properties, `model` and `order`.
There is a hard limit of 9 boards in the IO loop.
Note that the Playfield Interchange board is pass-through, and is not listed in the IO loop.

Example:

```yaml
fast:
  net:
    controller: neuron
    io_loop:
      my_io_board:
        model: FP-I/O-0804
        order: 1
      my_second_favorite_board:
        model: FP-I/O-0024
        order: 2
```

#### model:

The product number of the IO board. E.G. `FP-I/O-0804`

#### order:

The board number in the IO loop, starting from 1.

### baud:

Single value, int, default: `921600`

The connection baud rate.

### controller:

Single value, string, one of: `neuron`, `nano`, `sys11`, `wpc89`, `wpc95`

The FAST Pinball controller type.

### watchdog:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Default: `1000`

The FAST controllers include a "watchdog" timer. A watchdog is a timer
that is continuously counting down towards zero, and if it ever hits
zero, the controller shuts off all the power to the drivers. The idea is
that every time MPF runs a game loop (so, 30 times a second or
whatever), MPF tells the FAST controller to reset the watchdog timer. So
this timer is constantly getting reset and never hits zero.

But if MPF crashes or loses communication with the FAST controller, then
this watchdog timer won\'t be reset. When it hits zero, the FAST
controller will kill the power to the drivers. This should prevent an
MPF crash from burning up driver or somehow damaging your hardware in
another way.

You can set the watchdog timer to whatever you want. (This is
essentially the max time a driver could be stuck "on" if MPF crashes.)
The default is 1 second which is probably fine for almost everyone, and
you don\'t have to include this section in your config if you want to
use the default.

### default_quick_debounce_open:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Defaults to empty.

Specifies the default value for the debounce time for switches that are
configured with `debounce: quick` when they open.

Even though this is listed as a required setting, this entry is in the
`mpfconfig.yaml` file, (with a value of `2ms`), so you don\'t have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch\'s config.

### default_quick_debounce_close:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Defaults to empty.

Specifies the default value for the debounce time for switches that are
configured with `debounce: quick` when they close.

Even though this is listed as a required setting, this entry is in the
`mpfconfig.yaml` file, (with a value of `2ms`), so you don\'t have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch\'s config.

### default_normal_debounce_open:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Defaults to empty.

Specifies the default value for the debounce time for switches that are
configured with `debounce: normal` when they open.

Even though this is listed as a required setting, this entry is in the
`mpfconfig.yaml` file, (with a value of `10ms`), so you don\'t have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch\'s config.

### default_normal_debounce_close:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Defaults to empty.

Specifies the default value for the debounce time for switches that are
configured with `debounce: normal` when they close.

Even though this is listed as a required setting, this entry is in the
`mpfconfig.yaml` file, (with a value of `10ms`), so you don\'t have to
enter it here unless you want to override that.

Also, keep in mind that this setting is only a default. You can override
it for any switch in that switch\'s config.

### mute_unconfigured_switches:

* available MPF 0.57.4/0.80.0.dev12 *

Single value, boolean, default: `false`

Before this change, FAST Switches were configured with mode `00`, meaning they did not report if unconfigured.
With the release of this config setting, switch inputs on the IO board will default to mode `01`, meaning they do report to MPF even if no switch device is configured.
In production mode, or if this setting is set to `true`, unregistered switches will NOT report to MPF on state change.

### gi_hz:

Single value, int, default: `30`

Lights using the light subtype `gi` will use this for their hz setting if unspecified.

### lamp_hz:

Single value, int, default: `30`

Lights using the light subtype `matrix` will use this for their hz setting if unspecified.

## FAST Docs:

For more information, see the [FAST Net Interface MPF Config page](https://fastpinball.com/mpf/config/net/).
