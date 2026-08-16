---
title: OPP LEDs
---

# OPP LEDs


Related Config File Sections:

* [lights:](../../config/lights.md)

OPP hardware can directly drive LED strips. This features is currently
being developed. Documentation will be added as the feature becomes more
mature.

LEDs work similar to matrix lights (chain 0, board 1, LED 1):

``` yaml
lights:
  some_led:
    number: 0-1-1
    subtype: led
    type: rgb
```

Note, counting starts always with 0, so LED 1 in aboves example is the
2nd LED of the strip.

Overview video about serial LEDs:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q9BG9T7Kj4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Channel and Number Syntax

--8<-- "light_channels_numbers.md"

OPP assumes RGB lights by default. For everything else (i.e. RGBW) you
have to use channels.

### Light Numbers

OPP numbers use the format: `serial_chain`-`card_num`-`index`

`chain_serial` is only relevant if you got multiple chains connected via
USB. See [Connecting OPP to your computer](connecting.md) for details about
chains. If you only got one chain you can omit this part and your format
becomes `card_num`-`index`.

`card_num` is the index of the board on the chain. As the first board
is always at addr `0x20` you can calculate the
addr using `0x20` + card_num. If you only got
one board you can omit the board and your format becomes just `index`.

For instance, `0-0-0` for the first RGB LED on chain `0` on card `0x20`.
In this case you can also use `0-0` or `0` (channel `0-2`). `0-0-1` or
`0-1` or `1` is the second LED on the chain (channels `3-5`).

`3-2-6` is the 6th LED on board 2 (addr `0x22`) of chain `3` (channels
`18-20`).

### Channels

OPP channels use the format: `serial_chain`-`card_num`-`internal_index`

This is mostly the same as numbers above except that
`internal_index = 3 * index`. This is because serial LEDs are
traditionally RGB (or GRB) LEDs with exactly three channels. However,
this is not true for RGBW or similar LEDs which do not work with this
style of numbering. Luckily, you can chain them instead and have MPF
calculate the internal channels for you:

``` yaml
lights:
  led_0:
    start_channel: 0-0-0
    subtype: led
    type: rgb    # will use red: 0-0-0, green: 0-0-1, blue: 0-0-2
  led_1:
    previous: led_0
    subtype: led
    type: rgbw   # will use red: 0-0-3, green: 0-0-4, blue: 0-0-5, white: 0-0-6
  led_2:
    previous: led_1
    subtype: led
    type: rgbw   # will use red: 0-0-7, green: 0-0-8, blue: 0-0-9, white: 0-0-10
```

See [WS2811 and WS2812 LEDs in Pinball](../../mechs/lights/ws2812.md) for details.

## What if it did not work?

Have a look at our
[OPP troubleshooting guide](../../troubleshooting/index.md).
