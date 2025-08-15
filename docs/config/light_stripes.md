---
title: "light_stripes: Config Reference"
---

# light_stripes: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

A `light_stripes` will create `count` leds for you starting the number
at `number_start`. If you need a prefix or suffix for the number you
can use `number_template`. All settings in `led_template` will be
applied to all LEDs. The only difference between
[led_stripes](light_stripes.md) and
[light_rings](light_rings.md) is how
the x/y coordinates are computed.

In order to access single light in your strip you can use the following syntax schema `(light_strip_name)_light_(light_number)`. Where `(light_strip_name)` is the name you have choosen for your light strip and `(light_number)` is the number of the light in the stip, keep in mind the numbering starts with 0 and not 1.

## Required settings

The following sections are required in the `light_stripes:` section of
your config:

### count:

Single value, type: `integer`. Defaults to empty.

The integer value for how many LEDs are in the stripe.

### light_template:

Single value, type: [lights:](lights.md).
Defaults to empty.

This is a list of sub-settings (indented) that are regular settings from
the [../about/help_us_to_write_it](lights.md) section of your machine
config. Any settings that are valid there are valid here, and they're
applied to all the LEDs in the stripe.

## Optional settings

The following sections are optional in the `light_stripes:` section of
your config. (If you don't include them, the default will be used).

### direction:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

The angle (in degrees, 0-360) the this LED stripe is positioned on the
playfield. This is used for the calculation of x/y positions of
individual LEDs only.

### distance:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

The distance between individual LEDs (in relative size to the x/y
coordinates of the `start_x:` and `start_y:` positions. This is used for
the calculation of x/y positions of individual LEDs only.

### number_start:

Single value, type: `integer`. Default: `0`

The integer value for the number for the first LED in the stripe. (MPF
assumes that all the LEDs in the stripe are numbered sequentially.)

### number_template:

Single value, type: `string`. Defaults to empty.

MPF automatically configures the LEDs in a stripe. The first one uses
the `number_start:` value, and then it counts up from there up through
the `count:` value.

However, many hardware numbers for LEDs are not just vanilla numbers,
rather they also include a board number or channel or something like
that. The `number_template:` is where you specify what that number value
looks like. Just use braces `{}` for the part you want replaced by a
number.

The example config with a number template of `7-{}` with a number start
of 200 and a count of 5 will create 5 LEDs with the numbers 7-200,
7-201, 7-202, 7-203, and 7-204.

### previous:

Single value, type: `string` name of a [lights:](lights.md) device. Defaults to empty.

--8<-- "todo.md"

### start_channel:

Single value, type: `string`. Defaults to empty.

--8<-- "todo.md"

### start_x:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

The "x" position of the first LED. (This is not used in MPF yet.)

### start_y:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

The "y" position of the first LED.

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


## Related How To guides

--8<-- "todo.md"
