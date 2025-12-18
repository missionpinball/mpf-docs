---
title: "fast:net: Config Reference"
---

# fast:net: Config Reference

--8<-- "deeper_config_section.md"

| Valid in | |
|-----|:----:|
|[machine](../instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](../instructions/mode_config.md) config files|**NO** :no_entry_sign:|

## net: config reference

Within the `fast:` section of your machine-wide config, you configure the IO network in the subsection `net:`.

### port:

List of strings, default: `auto`

MPF will attempt to connect to the IO boards on this port. If many ports are given, MPF will try each until finding a valid connection.

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

Single value, integer number of milliseconds, default: `1000`

The watchdog timeout duration. The default 1000 represents 1 second.

### default_quick_debounce_open:

Single value, integer number of milliseconds, default: `2`

### default_quick_debounce_close:

Single value, integer number of milliseconds, default: `2`

### default_normal_debounce_open:

Single value, integer number of milliseconds, default: `4`

### default_normal_debounce_close:

Single value, integer number of milliseconds, default: `4`

### mute_unconfigured_switches:

* available MPF 0.57.4/0.80.0.dev12 * #TODO

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
