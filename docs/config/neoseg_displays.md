---
title: neoseg_displays:
---

# neoseg_displays:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `neoseg_displays:` section of your config is where you...

--8<-- "todo.md"

## Required settings

The following sections are required in the `neoseg_displays:` section of
your config:

### light_template:

Single value, type: [lights:](lights.md).
Defaults to empty.

--8<-- "todo.md"

## Optional settings

The following sections are optional in the `neoseg_displays:` section of
your config. (If you don't include them, the default will be used).

### number_start:

Single value, type: `integer`. Default: `0`

--8<-- "todo.md"

### number_template:

Single value, type: `string`. Defaults to empty.

--8<-- "todo.md"

### previous:

Single value, type: string name of a [lights:](lights.md) device. Defaults to empty.

--8<-- "todo.md"

### size:

Single value, type: one of the following options: 2digit, 8digit.
Default: `8digit`

--8<-- "todo.md"

### start_channel:

Single value, type: `string`. Defaults to empty.

--8<-- "todo.md"

### start_x:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

--8<-- "todo.md"

### start_y:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

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

--8<-- "todo.md"

## Related How To guides

--8<-- "todo.md"
