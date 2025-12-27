---
title: "fast:exp: Config Reference"
---

# fast:exp: Config Reference

--8<-- "deeper_config_section.md"

| Valid in | |
|-----|:----:|
|[machine](../instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](../instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Within the [`fast:`](../fast.md) section of your machine-wide config, you configure the EXP processor in the subsection `exp:`, and sometimes in `exp_int:`.

### port:

List of one (or more) values, each is a type: `string`. Defaults to `auto`.

A comma-separated list of the serial port names your FAST controller uses.

### baud:

Single value, int, default: `921600`

The connection baud rate.

### boards:

Dict of string board names to dicts of EXP board properties. Defaults to empty.

Example:

```yaml
fast:
  exp:
    port: auto
    boards:
      neuron:
        model: FP-EXP-2000
      playfield_0081:
        model: FP-EXP-0081
```

#### model:

The product number of the IO board. E.G. `FP-EXP-0081`

#### ignore_led_errors:

Single value, boolean, default: `false`

If false, LED hex communication decode errors will be raised as errors when encountered from this board.
If you encounter instability due to these errors, set this to true to silently ignore them.

## Using exp_int

If using a Raspberry Pi connected directly to the Neuron controller, the LED headers on the Neuron will not be available on the normal EXP interface.
In order to access these Neuron LED headers, you must define a parallel structure to the existing `exp:` configuration, and move the Neuron definition over to it.

Example:

```yaml
fast:
  exp:
    boards:
      playfield_0081:
        model: FP-EXP-0081
  exp_int:
    boards:
      neuron:
        model: FP-EXP-2000
```

## FAST Docs:

For more information, see the [FAST EXP Interface MPF Config page](https://fastpinball.com/mpf/config/exp/).
