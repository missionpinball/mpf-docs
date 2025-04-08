---
title: "blinkenlights:"
---

# blinkenlights:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `blinkenlights:` section of your config file is used to define
lights on your pinball machine that can be shared by multiple different
modes at the same time. Blinkenlights work best with RGB LEDs, because
each mode that uses a blinkenlight can specify a color that the
blinkenlight should flash for that mode. The blinkenlight will then
flash each of its colors in a cycle according to a given schedule.

Here's an example section:

``` yaml
#! lights:
#!   l_left_ramp_arrow:
#!     channels:
#!       red:
#!         number: 1
#!       green:
#!         number: 2
#!       blue:
#!         number: 3
#!   l_right_ramp_arrow:
#!     channels:
#!       red:
#!         number: 4
#!       green:
#!         number: 5
#!       blue:
#!         number: 6
blinkenlights:
  blinkenlight_1:
    color_duration: 1s
    off_when_multiple: false
    light: l_left_ramp_arrow
    priority: 1000
  blinkenlight_2:
    cycle_duration: 1s
    off_when_multiple: false
    light: l_right_ramp_arrow
    priority: 1000
```

With the above configuration, two blinkenlights are configured:
blinkenlight_1 and blinkenlight_2. You can then use a
[blinkenlight_player](blinkenlight_player.md) to add or remove colors to these blinkenlights from within
your modes.

The options are as follows:

## Optional settings

The following sections are optional in the `blinkenlights:` section of
your config. (If you don't include them, the default will be used).

### color_duration:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Either `color_duration` or `cycle_duration` (see below) must be
specified for each blinkenlight, but not both.

This specifies the amount of time that each of the blinkenlight's
colors will be turned on. For example, if this value is `1s`, then each
of the blinkenlight's colors will be on for 1 second.

The more colors that are added to the blinkenlight when `color_duration`
is specified, the longer it will take to cycle through all the colors.
If you want the blinkenlight's cycle to always last the same amount of
time regardless of how many colors the blinkenlight has, then use
`cycle_duration` instead (see below).

### cycle_duration:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Either `cycle_duration` or `color_duration` (see above) must be
specified for each blinkenlight, but not both.

This specifies the length of one cycle of the blinkenlight. The
blinkenlight will show all of its colors in one cycle. This includes the
"off" color at the end of the cycle, if applicable (see
`off_when_multiple` below). For example, if this value is `1s`, and the
blinkenlight has 2 colors in its list, and `off_when_multiple` is
`false`, then each color will be displayed for 0.5 seconds. If
`off_when_multiple` is `true`, then the "off" color will count as a
color in the blinkenlight's cycle, and so the each color will only be
displayed for 1/3 of a second.

The more colors that are added to the blinkenlight when `cycle_duration`
is specified, the shorter each color will be displayed. If you want each
color to be displayed for a certain length of time regardless of the
number of colors, then use `color_duration` instead (see above).

### light:

Single value, type: string name of a [lights:](lights.md) device. Defaults to empty.

This is the name of the light which this blinkenlight controls.

### off_when_multiple:

Single value, type: `boolean` (`true`/`false`). Default: `false`

This specifies whether or not to include an "off" color at the end of
each cycle when the blinkenlight has more than one color in its list.

For example, if the blinkenlight has 2 colors (red and green) and
`off_when_multiple` is `False` (the default value), then the cycles will
be red, green, red, green. However, if `off_when_multiple` is `True`,
then the cycles will be red, green, off, red, green, off. The "off"
color in this case is treated as another color for the purposes of the
`color_duration` and `cycle_duration` settings above.

A blinkenlight that only has 1 color in its list will be off at the end
of its cycle, regardless of whether `off_when_multiple` is `True` or
`False`. For example, the cycles of a blinkenlight that has 1 color
(red) will be red, off, red, off.

### priority:

Single value, type: `integer`. Default: `0`

The priority of the blinkenlight. If there is a show that uses this
blinkenlight's light, and the show and the blinkenlight are happening
at the same time, then the light will be controlled by whichever one has
the highest priority.

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

* [Blinkenlight player](../config_players/blinkenlight_player.md)
