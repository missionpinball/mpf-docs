---
title: "digital_score_reels: Config Reference"
---

# digital_score_reels: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `digital_score_reels:` section of your config is where you...

--8<-- "todo.md"

## Optional settings

The following sections are optional in the `digital_score_reels:`
section of your config. (If you don't include them, the default will be
used).

### frames:

!!! question "Is this a thing?"

    Need to investigate if this is still how this works? As of June 2023.

--8<-- "todo.md"

### include_player_number:

Single value, type: `boolean` (`true`/`false`). Default: `False`

--8<-- "todo.md"

### reel_count:

Single value, type: `number` (can be integer or floating point).
Default: `0`

--8<-- "todo.md"

### start_value:

Single value, type: `string`. Default: `0`

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
