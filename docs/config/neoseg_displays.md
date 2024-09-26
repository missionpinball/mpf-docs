---
title: "neoseg_displays:"
---

# neoseg_displays:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `neoseg_displays:` section of your config is where you set the hardware specific settings for this type of segment display. It is
only needed if you use a [Cobra serial segment display](../hardware/opp/cobrapin/cobrapin_serial_segment_displays.md). For any other
segment display hardware this setting is not needed.

## Required settings

The following sections are required in the `neoseg_displays:` section of
your config:

### light_template:

Single value, type: [lights:](lights.md).
Defaults to empty. Used to specify the light you have, though neoseg displays come in different
colors each segment is considered a single color segment, use color white in any case.

```
light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_orange
```

See as well these examples in the [Cobra serial segment display](../hardware/opp/cobrapin/cobrapin_serial_segment_displays.md) section.

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

Make sure to set the right size depending on what hardware you have.

### start_channel:

Single value, type: `string`. Defaults to empty.

The start channel for the first display would be either `0-0-0` or `1-0-0`, depending what neo seg connection you use on your Cobra pin. The start channel of the next hardware is
easily computed, for each digit you need 15 channels (14 segments plus the integrated dot). If your first segment has 8 digits you need 120 channels from 0 to 119, thus the next
display would have as start channel either `0-0-120` or `1-0-120`.

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
