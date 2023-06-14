---
title: "hardware_sound_systems:"
---

# hardware_sound_systems:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `hardware_sound_systems:` section of your config is where you
configure external sound systems. For instance, this is used in the
[LISY platform](../hardware/lisy/index.md).

## Optional settings

The following sections are optional in the `hardware_sound_systems:`
section of your config. (If you don't include them, the default will be
used).

### platform:

Single value, type: `string`. Defaults to empty.

Overwrite the default platform.

### platform_settings:

Single value, type: dict. Defaults to empty.

--8<-- "todo.md"

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

Not used.

## Related How To guides

* [Arduino Pinball Controller](../hardware/apc/index.md)
* [How to use MPF with the LISY platform](../hardware/lisy/index.md)
