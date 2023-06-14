---
title: How to Connect Segment Displays as Lights to MPF
---

# How to Connect Segment Displays as Lights to MPF


Related Config File Sections:

* [hardware:](../config/hardware.md)
* [segment_displays:](../config/segment_displays.md)
* [lights:](../config/lights.md)
* [light_segment_displays:](../config/light_segment_displays.md)

MPF can map segment displays to arbitrary lights which can be controlled
via any hardware platform. You can select from multiple mappings (see
[platform_settings](../config/light_segment_displays.md) for details). Let us know if you need another mapping.

Video about segment displays:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jyf3jxGXnTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Hardware

### BCD Seven Segment

Segment displays are readily available at most electronics suppliers.
Most of them use some BCD encoder to save connectors. Those are easily
recognizable because they got less than 8 connectors. You can use any
driver or digital outputs on those. Be a bit careful with current driven
light controllers (i.e. the PD-LED) here. Those cannot be dimmed
currently (let us know if you need that).

### Parallel Seven Segment

Those are not as common as BCD segment displays but still available. You
can recognize them by more than 8 connectors. Make sure that your
display is not multiplexed or it will not work without an additional
controller chip. Those can be driven by any parallel LED controller (see
[LEDs](../mechs/lights/leds.md) for details). If you
use drivers you will probably need current limiting resistors. In most
cases BCD is simpler to use and will save you some outputs.

Those are also available as RGB. However, they often are multiplexed and
will not work without an additional chip.

### Serial Segment Displays

Additionally, there are serial segment displays which use chips such as
WS2811 internally. Those can also be used here using a serial LED
controller (see [LEDs](../mechs/lights/leds.md) for
details).

There is a [hackaday project for monochrome serial segment
displays](https://hackaday.com/2019/01/12/addressable-7-segment-displays-may-make-multiplexing-a-thing-of-the-past/).
Furthermore, there are also [full RGB serial segment
displays](https://www.rgbdigit.com/rgbdigit/). Both are controlled using
WS2811 controllers.

You can also buy WS2811 controller with PCB in China (bulk 100 pcs) for
about ten bucks solder your own display.

### Color and Brightness

There is no color or brightness support for segment displays in MPF yet.
Let us know if you need that. However, you can control both using normal
light shows.

## Config

This is an example:

``` mpf-config
hardware:
  segment_displays: light_segment_displays

lights:
  segment1_a:
    number: 1
  segment1_b:
    number: 2
  segment1_c:
    number: 3
  segment1_d:
    number: 4
  segment1_e:
    number: 5
  segment1_f:
    number: 6
  segment1_g:
    number: 7
  segment2_a:
    number: 8
  segment2_b:
    number: 9
  segment2_c:
    number: 10
  segment2_d:
    number: 11
  segment2_e:
    number: 12
  segment2_f:
    number: 13
  segment2_g:
    number: 14

segment_displays:
  display1:
    number: 1
    platform_settings:
      lights:
        - a: segment1_a
          b: segment1_b
          c: segment1_c
          d: segment1_d
          e: segment1_e
          f: segment1_f
          g: segment1_g
        - a: segment2_a
          b: segment2_b
          c: segment2_c
          d: segment2_d
          e: segment2_e
          f: segment2_f
          g: segment2_g
      type: 7segment
```

Here is another example for a monochrome serial 16-segment display using
a WS2811 controller on OPP:

``` mpf-config
hardware:
  segment_displays: light_segment_displays

lights:
  l_neoseg_0_0_a:
    start_channel: 0-0-60  #When using other RGB pixels in the chain before the display,
                           #             start_channel = 3 x start_pixel
                           #Using RGBW,  start_channel = 4 x start pixel
                           #Here, there are 20 RGB neopixels before the display
    type: w
    subtype: led
  l_neoseg_0_0_m:
    previous: l_neoseg_0_0_a
    type: w
    subtype: led
  l_neoseg_0_0_k:
    previous: l_neoseg_0_0_m
    type: w
    subtype: led
  l_neoseg_0_0_h:
    previous: l_neoseg_0_0_k
    type: w
    subtype: led
  l_neoseg_0_0_u:
    previous: l_neoseg_0_0_h
    type: w
    subtype: led
  l_neoseg_0_0_s:
    previous: l_neoseg_0_0_u
    type: w
    subtype: led
  l_neoseg_0_0_t:
    previous: l_neoseg_0_0_s
    type: w
    subtype: led
  l_neoseg_0_0_g:
    previous: l_neoseg_0_0_t
    type: w
    subtype: led
  l_neoseg_0_0_f:
    previous: l_neoseg_0_0_g
    type: w
    subtype: led

  l_neoseg_0_0_e:
    previous: l_neoseg_0_0_f
    type: w
    subtype: led
  l_neoseg_0_0_dp:
    previous: l_neoseg_0_0_e
    type: w
    subtype: led
  l_neoseg_0_0_d:
    previous: l_neoseg_0_0_dp
    type: w
    subtype: led
  l_neoseg_0_0_r:
    previous: l_neoseg_0_0_d
    type: w
    subtype: led
  l_neoseg_0_0_p:
    previous: l_neoseg_0_0_r
    type: w
    subtype: led
  l_neoseg_0_0_c:
    previous: l_neoseg_0_0_p
    type: w
    subtype: led
  l_neoseg_0_0_n:
    previous: l_neoseg_0_0_c
    type: w
    subtype: led
  l_neoseg_0_0_b:
    previous: l_neoseg_0_0_n
    type: w
    subtype: led
  l_neoseg_0_0_na:
    previous: l_neoseg_0_0_b
    type: w
    subtype: led

segment_displays:
  display1:
    number: 1
    platform_settings:
      lights:
        - a: l_neoseg_0_0_a
          b: l_neoseg_0_0_b
          c: l_neoseg_0_0_c
          d: l_neoseg_0_0_d
          e: l_neoseg_0_0_e
          f: l_neoseg_0_0_f
          g: l_neoseg_0_0_g
          h: l_neoseg_0_0_h
          k: l_neoseg_0_0_k
          m: l_neoseg_0_0_m
          n: l_neoseg_0_0_n
          p: l_neoseg_0_0_p
          r: l_neoseg_0_0_r
          s: l_neoseg_0_0_s
          t: l_neoseg_0_0_t
          u: l_neoseg_0_0_u
      type: 16segment
```

## What if it did not work?

Have a look at our
[hardware troubleshooting guide](troubleshooting_hardware.md).
