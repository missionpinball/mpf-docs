---
title: "smart_virtual:"
---

# smart_virtual:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `smart_virtual:` section of your config is where you configure the
[smart virtual platform](../hardware/virtual/smart_virtual.md).

## Optional settings

The following sections are optional in the `smart_virtual:` section of
your config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

File level for the console log for this platform.

### simulate_manual_plunger:

Single value, type: `boolean` (`true`/`false`). Default: `false`

When `simulate_manual_plunger` is set to `True` the smart_virtual
platform will automatically plunge balls in devices with mechanical
eject after `simulate_manual_plunger_timeout` ms.

### simulate_manual_plunger_timeout:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `10s`

When `simulate_manual_plunger` is set to `True` the smart_virtual
platform will automatically plunge balls in devices with mechanical
eject after `simulate_manual_plunger_timeout` ms.

## Related How To guides

* [The "Smart Virtual" Platform](../hardware/virtual/smart_virtual.md)
