---
title: Lights
---

# Lights


Related Config File Sections:

* [lights:](../../config/lights.md)
* [light_settings:](../../config/light_settings.md)
* [light_player:](../../config/light_player.md)

In MPF 0.50 all LEDs, matrix lights and GIs are configured as
[lights:](../../config/lights.md). See
[/tutorial/17_add_lights_leds](lights_versus_leds.md) for details.

There are multiple types of lights (read those for specific details):

* [/tutorial/17_add_lights_leds](leds.md)
* [/tutorial/17_add_lights_leds](gis.md)
* [/tutorial/17_add_lights_leds](matrix_lights.md)
* [/tutorial/17_add_lights_leds](flashers.md)
* [/tutorial/17_add_lights_leds](coils_as_lights.md)

![image](/mechs/images/lights_vs_leds.jpg)

This is an example of for a light:

``` mpf-config
lights:
  my_led:
    number](7   # the exact number format depends on your platform
```

For WS2812 LEDs use `type)
* [Capitalization
    doesn't matter in the config file, e.g. `LightSalmon` or
    `lightsalmon` are equally good

In the `light_player` section you can either define the color as value
of the specified LED, which turns that LED immediately to the given
color. Or you can specifiy a `color` and a `fade` value, then the color
will transition to the new value in the specified time. In the config
file this is configured for key 5, see `led_fade` in the `light_player`
section.

In the `light_player` section after each event you can specify one or
multiple lights. In the section `led_off` both LEDs are specified, hence
both are turned off when the event `led_off` is sent.

Note that the defined lights have tags, here the tag value is `group1`.
In the `light_player` section you can either address a single LED by its
name or you can use a group name to address all LEDs in that group. When
you press key 4 then LED 1, 2, and 3 are switched to green. A few notes
on above example:

* It is kept as simple as possible to learn by example.
* Keep in mind that numbering starts with 0, so LED 1 and 2 in above
    config are your 2nd and 3rd LED of the strip
* If you use a WS2812 strip then the green and red channel are
    swapped. Which means that if you see a red light when pressing
    button 4, then you have a WS2812 strip. In order to get this fixed
    change the type value in the config file from `rgb` to `grb`.
* After you run that example and understand how it works, then change
    the type of `led_strip_0_led_2` to `ggg`. Now run the setup again
    and press key 4. The first LED will still show green, but the second
    LED will show white. That is because you told the configuration that
    that LED has only green channels so it turns all of them on when you
    want to show green, but in fact the other channels show red and
    blue. Depending on what you do, this might be helpful to know.
* The above example uses NEO0 of the Cobra controller, if you want to
    use NEO1 you have to change the number value in the lights section
    of your config file, the first 0 has to be a 1 in this case.
* Note that in the definition of `led_strip_0_led_3` the hardware
    addess is not specified (unlike led_strip_0_1 and led_strip_0_2.
    Instead what is specified is what the previous LED is. That is handy
    in case you need to add a new LED somewhere in your chain. Instead
    of changing all hardware addresses you can just change the one
    `previous` tag.

## Fully working Example 2 - light_stripes

From a hardware perspective the same remarks as in the example above are
true. This example will show a fully working example using the parameter
`light_stripes` (yes written with an e). The adavantage of this
paramater is that you are able to define a full serial LED light strip
with a few lines of config. See as well the corresponding config file
section [light_stripes:](../../config/light_stripes.md)

``` mpf-config
#config_version=5

hardware:
 platform](opp
 driverboards)
