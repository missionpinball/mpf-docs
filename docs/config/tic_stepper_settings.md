---
title: "tic_stepper_settings:"
---

# tic_stepper_settings:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

If you use the
[Pololu Tic Stepper Controller](../hardware/pololu_tic.md) you can use the following settings in `platform_settings` of
your steppers.

## Optional settings

The following sections are optional in the `tic_stepper_settings:`
section of your config. (If you don't include them, the default will be
used).

### current_limit:

Single value, type: `integer`. Default: `192`

--8<-- "todo.md"

### max_acceleration:

Single value, type: `integer`. Default: `40000`

--8<-- "todo.md"

### max_deceleration:

Single value, type: `integer`. Default: `40000`

--8<-- "todo.md"

### max_speed:

Single value, type: `integer`. Default: `2000000`

--8<-- "todo.md"

### poll_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `100ms`

How often should MPF poll the state of your steppers? This is used to
check for completion of movements. There should be no need to modify
this.

### starting_speed:

Single value, type: `integer`. Default: `0`

--8<-- "todo.md"

### step_mode:

Single value, type: `integer`. Default: `1`

--8<-- "todo.md"

## Related How To guides

* [How to use Pololu Tic in MPF](../hardware/pololu_tic.md)
