---
title: How to configure LEDs (FAST Pinball)
---

# How to configure LEDs (FAST Pinball)


Related Config File Sections:

* [leds:](../../config/leds.md)
* [fast:](../../config/fast.md)

The FAST Nano Controller has a built-in 4-channel RGB LED controller
which can drive up to 64 RGB LEDs per channel. This controller uses
serially-controlled LEDs (where each LED element has a little serial
protocol decoder chip in it), allowing you to drive dozens of LEDs from
a single data wire. These LEDs are generally known as "WS2812" (or
similar). You can buy them from many different companies, and they're
what's sold as the "NeoPixel" brand of products from Adafruit. (They
have all different shapes and sizes.)

![image](/hardware/images/fast-nano.png)

Most of the settings in the [Lights](../../mechs/lights/index.md) documentation apply to LEDs connected to FAST Pinball
controllers, however there are a few FAST-specific things to know.

Overview video about serial LEDs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q9BG9T7Kj4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Channel and Number Syntax

--8<-- "light_channels_numbers.md"

FAST assumes RGB lights by default. For everything else (i.e. RGBW) you
have to use channels.

The FAST Nano supports 256 LEDs across four chains (listed as "CH 1" -
"CH 4" on the Nano). LEDs 0-63 are on chain 1, 64-127 on chain 2,
128-191 on chain 3 and 192-255 on chain 4 (please note that FAST
diagrams label these 4 headers as "channels" but we are using the term
"chains" to avoid confusion with the non-RGB "Channels" section
below).

### Light Numbers

FAST numbers use the format: `number`

This is as easy as it gets. Just provide the number of you LED in the
chain. Internally, FAST assumes three channels per LED (RGB/GRB
[WS2811/WS2812 LEDs](../../mechs/lights/ws2812.md)).

### Channels

FAST channels use the format: `number`-`index`

`number` is the same as above and `index` is a an index from 0 to 2.
This is because serial LEDs are traditionally RGB (or GRB) LEDs with
exactly three channels. However, this is not true for RGBW or similar
LEDs which do not work with this style of numbering. Luckily, you can
chain them instead and have MPF calculate the internal channels for you:

``` mpf-config
lights:
  led_0:
    start_channel: 0      # you could also use number: 0
    subtype: led
    type: rgb    # will use red: 0-0, green: 0-1, blue: 0-2
  led_1:
    previous: led_0
    subtype: led
    type: rgbw   # will use red: 1-0, green: 1-2, blue: 1-3, white: 2-0
  led_2:
    previous: led_1
    subtype: led
    type: rgbw   # will use red: 2-1, green: 2-2, blue: 3-0, white: 3-1
```

Remember that each chain from the Nano will handle up to 64 RGB LEDs. You likely will have more than just 64 LEDs in your machine resulting in multiple chains. When configuring the `start_channel` or `number` for subsequent chains, remember to identify the number of the first LED in that chain starting with the first number LED supported in that chain. For example, your first chain should start with LED_0 and your second chain with LED_64, the third with LED_128 and the fourth with LED_192, like this:

``` mpf-config
lights:
  led_0:
    start_channel: 0      # you could also use number: 0
    subtype: led
    type: rgb    # will use red: 0-0, green: 0-1, blue: 0-2
  led_1:
    previous: led_0
    subtype: led
    type: rgb   # will use red: 1-0, green: 1-2, blue: 1-3
  led_2:
    previous: led_1
    subtype: led
    type: rgb   # will use red: 2-0, green: 2-1, blue: 2-2

## beginning of second chain
  led_50:
    start_channel: 64      # even though you only used 3 LEDs on the first chain, this chain needs to start with '64' to signify this is the beginning of a new chain from the Nano board
    subtype: led
    type: rgb    # will use red: 64-0, green: 64-1, blue: 64-2
  led_51:
    previous: led_50
    subtype: led
    type: rgb   # will use red: 65-0, green: 65-1, blue: 65-2
  led_52:
    previous: led_51
    subtype: led
    type: rgb   # will use red: 66-0, green: 66-1, blue: 66-2
```

See [WS2811 and WS2812 LEDs in Pinball](../../mechs/lights/ws2812.md) for details.

## RGB LED buffering

Most computers have the ability to send LED updates to the FAST Pinball
controller faster than the controller can process them. If this happens,
then the LED command messages can get backlogged and it will appear that
you have a "delay" in your LEDs and/or you might get weird colors due
to corrupt messages.

To help combat this, there are two settings you can adjust:

``` mpf-config
mpf:
  default_light_hw_update_hz: 50
fast:
  rgb_buffer: 3
```

If you notice that your LEDs seem to be getting behind, you can adjust
the `default_led_hw_update_hz:` setting to be lower. (Frankly the 50hz
by default is too high and we should lower it to 30.) You can probably
drive 128 or so LEDs at 50Hz, but if you have more than that then you
might need to start playing with this number.

## Hardware LED fading

You can globally set the fade rate for LEDs connected to a FAST Pinball
controller via the `fast:hardware_led_fade_time:` setting. (This is
`0ms` by default, meaning it's disabled.)

See the [fast:](../../config/fast.md) section of the
config file reference for details.

## Color Correction

If you are using RGB LEDs, they might not be perfectly white when you
turn them on. They might be pinkish or blueish instead depending on the
brand of the LED. To a certain extend this is normal/expected and you
can compensate for it by configuring
[color_correction profiles in light_settings](../../config/light_settings.md).

## What if it did not work?

Have a look at our
[FAST troubleshooting guide](../../troubleshooting/index.md).
