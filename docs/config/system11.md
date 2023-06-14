---
title: system11:
---

# system11:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `system11:` section of your config is where your system11 machine.
This is usually used together with the
[snux platform](../hardware/snux.md) or
[apc platform](../hardware/apc/index.md).

## Required settings

The following sections are required in the `system11:` section of your
config:

### ac_relay_driver:

Single value, type: string name of a [coils:](coils.md) device. Defaults to empty.

The driver to use to drive the AC relay which switches between A and C
side drivers.

## Optional settings

The following sections are optional in the `system11:` section of your
config. (If you don't include them, the default will be used).

### ac_relay_debounce_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

--8<-- "todo.md"

### ac_relay_delay_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `75ms`

Delay when switching between A and C side.

### ac_relay_switch:

Single value, type: string name of a
[switches:](switches.md) device. Defaults to
empty.

--8<-- "todo.md"

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

--8<-- "todo.md"

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### platform:

Single value, type: `string`. Defaults to empty.

Upstream platform for hardware. System 11 is a virtual platform which
drives coils on another underlying platform which can be configured
here.

### prefer_a_side_event:

Single event. The device will add an handler for this event. Default:
`game_ended`

Event to trigger A-side preference. This is triggered at game end by
default to reduce stress on the AC-relay during attract.

### prefer_c_side_event:

Single event. The device will add an handler for this event. Default:
`game_will_start`

Event to trigger C-side preference. This is triggered at game start by
default to increase response times.

### queue_c_side_while_preferred:

Single value, type: `boolean` (`true`/`false`). Default: `true`

--8<-- "todo.md"

## Related How To guides

* [Snux System 11 Driver Board](../hardware/snux.md)
* [Arduino Pinball Controller](../hardware/apc/index.md)
