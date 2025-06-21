---
title: "lights:"
---

# lights:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `lights:` section of your config is where you configure physical
lights for your hardware platform.

!!! note

    As of MPF 0.50, all lights have been combined into this single `lights`
    configuration. If you are using 0.33 or earlier, please see
    [matrix_lights:](matrix_lights.md) for incandescent
    bulbs and [leds:](leds.md) for LEDs.

## Concepts

MPF supports white, single-color or multi-color lights. Traditional GIs
are single white. Similar, single-color red lights are possible (i.e.
red inserts). RGBW lights are possible as well. They maintain an
additional white channel for better color reproduction.

To support all those different kinds of lights with a single interface
for various hardware generations MPF abstracts two concepts: Light
numbers and channel numbers.

### Light Numbers

Configuring the `number` of a light is often the simplest way.
Internally, your hardware platform will turn this into one or multiple
channels (see below) depending on the `subtype` configured. For
instance, if lights are usually RGB the platform will parse the number
into three channels.

This is an example:

``` yaml
lights:
  my_led:
    number: 7   # might also be 8-7 or 8-1-0 depending on your platform
```

This is often the easiest way to start and will work in most cases.

### Channel Numbers

Channel numbers can be configured in `channels` and describe the number
for a single light channel each. This channel number is then used when
the talking to the hardware. For single-color or white light this can be
the same as `number`. However, for some serial LED platforms this might
be also `number * 3` or a more complex conversion.

This is an example:

``` yaml
lights:
  rainbow_star:
    type: rgb
    channels:
      red:
        number: 9-29
      green:
        number: 9-30
      blue:
        number: 9-40     # this light is not sequential to the previous
```

This syntax allows the greatest flexibility but is also the most verbose
one.

You can either use `channels` to arbitrarily map channels to colors or
you can use `start_channel` + `type` (color order) to define the first
channel and then map colors sequentially to the following channels as
defined in the color order. Instead of `start_channel` you can also
chain lights by configuring the `previous` light and let MPF (with help
by the hardware platform) figure out the channel number.

This is an example:

``` yaml
lights:
  rainbow_star:    # this will use red: 9-29, green: 9-30 and blue: 9-31
    type: rgb
    start_channel: 9-29

  rainbow_star2:   # this will use red: 9-33, green: 9-32 and blue: 9-34
    type: grb      # notice the changed order here
    previous: rainbow_star
```

This syntax covers almost all practical cases and is beneficial with
serial LEDs as the above channels syntax is very verbose. It allows the
service mode to disable broken LEDs if they were removed from a serial
chain. Numbers will then be recalculated omitting disabled LEDs. The
syntax also works for parallel LEDs and other types of lights.

See the
[documentation page of your hardware platform](../hardware/index.md) for more details about numbers and channels.

## Optional settings

The following sections are optional in the `lights:` section of your
config. (If you don't include them, the default will be used).

### channels:

Single value, type: dict. Defaults to empty.

Instead of a single `number` address for a light, you can enter channels
corresponding to the multi-color channels of an RGB or RGBW LED. Each
channel entry can contain any of the `lights` parameters listed on this
page, but at least `number` is required.

``` yaml
lights:
  rainbow_star:
    type: rgb
    channels:
      red:
        number: 9-29
      green:
        number: 9-30
      blue:
        number: 9-31
```

Note that a light must have either `channels` or `number` defined, but
cannot have both. See [LEDs](../mechs/lights/leds.md)
for more details about how to configure channels for different types of
LEDs.

### color_correction_profile:

Single value, type: `string`. Defaults to empty.

If provided, a color correction profile will be applied to all color
settings this light receives. By order of operations, the light will be
set to the requested color first and then the color correction profile
will be applied on top.

### default_on_color:

Single value, type: `color` (*color name*, *hex*, or list of values
*0*-*255*). Default: `ffffff`

For multi-color LEDs, the color defined here will be used when the light
is enabled via "on" (as opposed to being enabled with a specific
color). Not intended for single-color lights.

Color values may be a hex string (e.g. `22FFCC`), a list of
RGB values (e.g. `\[50, 128, 206\]`), or a color name (e.g.
`turquoise`). MPF knows 140+ standard web color names, and
you can define your own custom colors in the
[named_colors:](named_colors.md) section of your
config.

### fade_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

When this light receives instructions to change color, it can
interpolate from its current value to the new value over a fade time. If
no value is provided, the machine default will be used. If this light is
part of a show that defines a fade time, the show's value will
supercede this light's setting.

### number:

Single value, type: `string`. Defaults to empty.

This is the number of the light which specifies which output the
hardware bulb or LED is physically connected to. The exact format used
here will depend on which control system you're using and how the light
is connected.

See the [How to configure "number:" settings](../hardware/numbers.md) guide for
details.

Note that a light must have either `channels` or `number` defined, but
cannot have both.

### platform:

Single value, type: `string`. Defaults to empty.

Name of the platform this LED is connected to. The default value of
`None` means the default hardware platform will be used. You only need
to change this if you have multiple different hardware platforms in use
and this coil is not connected to the default platform.

See the [Mixing-and-Matching hardware platforms](../hardware/platform.md) guide for
details.

There is a special platform `drivers` which will reference a driver
which has to be configured in the `number` setting. It can be used if
you got a light which is connected to a driver in your platform. That
might be the case for [GIs](../mechs/lights/gis.md) for example. This is an example for a driver as light:

``` yaml
coils:
  light_connected_to_a_driver:
    number: 42           # number depends on your platform
    allow_enable: true   # this will allow 100% enable without pwm
lights:
  light_on_a_driver:
    number: light_connected_to_a_driver    # map this light to a driver
    platform: drivers
```

### platform_settings:

Single value, type: dict. Defaults to empty.

Platform-specific light settings. Consult your platform documentation
for details.

### previous:

Single value, type: `string` name of a [lights:](lights.md) device. Defaults to empty.

Instead of specifying the number for each light in a chain you can also
use the previous setting. To do this only specify the number of the
first light in the chain and then link all consequent light using the
previous setting:

``` yaml
lights:
  led_0:
    number: 0
    subtype: led
    type: rgb
  led_1:
    previous: led_0
    subtype: led
    type: rgbw
  led_2:
    previous: led_1
    subtype: led
    type: rgbw
```

MPF will then calculate the number based on the light of the previous
light. Make sure MPF knows how many channel each light has (i.e. by
specifying the type parameter). This is not supported in all platforms
but in most of them.

### start_channel:

Single value, type: `string`. Defaults to empty.

In most platforms MPF will calculate the internal address of a light and
how many channels it has using the number parameter. If you got unusual
types of lights (such as RGBW LEDs) you can instead provide this
internal address and the number of channels (i.e. using type). This is
an example:

``` yaml
lights:
  led_0:
    start_channel: 0-0
    subtype: led
    type: rgbw
```

Consult the manual of your platform for details.

### subtype:

Single value, type: `string`. Defaults to empty.

If you hardware platform supports multiple types of lights you need to
set a `subtype` to tell your platform how to address this light (to
prevent `number` collisions). Typical values are `led`, `matrix` or
`gi`. Consult your platform documentation for details.

### type:

Single value, type: `string`. Defaults to empty.

Default value is `rgb`.

This describes the channel order of an LED. Can be 1 to many channels
(if supported by hardware). Valid channels: r (red), g (green), b
(blue), w (white=minimum of red, green and blue), + (always on), -
(always off).

When using serial LEDs (e.g. with FAST or Fadecandy), use
`rgb` for WS2812 and `grb` for WS2811 LEDs.

### x:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

This is used for display_light_player to determine the position of this
light on the playfield and use it as a huge display.

### y:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

This is used for display_light_player to determine the position of this
light on the playfield and use it as a huge display.

### z:

Single value, type: `number` (will be converted to floating point).
Defaults to empty.

Currently not used anywhere.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

If `True`, this light will log its configuration and color changes to
the debug log.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of the light in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Lights can be referenced by their tags in light_players. Typical tags
are `gi` for all GIs or `playfield_inserts` for
all inserts on the playfield.

## Related How To guides

* [Lights](../mechs/lights/index.md)
