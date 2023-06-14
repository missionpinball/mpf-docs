---
title: ball_routings:
---

# ball_routings:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `ball_routings:` section of your config is where you...

--8<-- "todo.md"

## Required settings

The following sections are required in the `ball_routings:` section of
your config:

### source_devices:

List of one (or more) values, each is a type: string name of a
[ball_devices:](ball_devices.md) device.
Defaults to empty.

--8<-- "todo.md"

### target_device:

Single value, type: string name of a
[ball_devices:](ball_devices.md) device.
Defaults to empty.

--8<-- "todo.md"

## Optional settings

The following sections are optional in the `ball_routings:` section of
your config. (If you don't include them, the default will be used).

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

--8<-- "todo.md"

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

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
