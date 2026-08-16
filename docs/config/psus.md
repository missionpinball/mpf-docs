---
title: "psus: Config Reference"
---

# psus: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `psus:` section of your config is where you power supply units. See
[Voltages and Power in Pinball Machines](../hardware/voltages_and_power/index.md) for
details about voltages in pinball machines and some electric details.
Then specify to which PSU your [coils:](coils.md) are connected. This is used for power management. In some
cases, MPF ,ay deliberately delay coil pulses to prevent too many coils
from firing and drawing to much current from your PSU.
[Ball devices](ball_devices.md) and
[drop target](drop_targets.md) do this by
default to ensure more consistent pulses.

## Optional settings

The following sections are optional in the `psus:` section of your
config. (If you don't include them, the default will be used).

### max_amps:

Single value, type: `integer`. Defaults to empty.

Maximum ampers which can be provided by this PSU. Currently not used.

### release_wait_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `10`

Time to wait after a coil pulse.

### voltage:

Single value, type: `integer`. Defaults to empty.

Voltage of your PSU. Only informal.

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

Currently unused.

## Related How To guides

* [Power Management in Software](../hardware/voltages_and_power/power_management.md)
