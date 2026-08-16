---
title: MyPinballs Segment Display Controller
---

# MyPinballs Segment Display Controller

--8<-- "hardware_platform.md"

Related Config File Sections:

* [Hardware](../../config/hardware.md)
* [mypinballs](../../config/mypinballs.md)
* [segment_displays](../../config/segment_displays.md)
* [segment_display_player](../../config/segment_display_player.md)

Those segment displays are controlled by a very simple serial protocol.
Two variants exist: The original MyPinball controller which can controll
existing segments and the TNA segment displays sold by PBL which
includes four segments. Both can be controlled using this platform.

Video about segment displays:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jyf3jxGXnTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mypinballs Segment Displays Controller

MyPinballs sells segment display controller which can be used with MPF
to control existing Bally/Stern segment displays (or replacement
displays). See the [Direct-wiring MyPinballs to 3rd-Party Segment Displays](wiring.md) section for
details about how to wire those. Connect it to your PC using USB and
control up to six segment displays.

Config looks like this:

``` yaml
hardware:
  segment_displays: mypinballs
mypinballs:
  port: /dev/ttyUSB0
segment_displays:
  display1:
    number: 1
  display2:
    number: 2
  display3:
    number: 3
  display4:
    number: 4
  display5:
    number: 5
  display6:
    number: 6
```

You can configure your serial port in `port`. See
[segment_display](../../mc/displays/alpha_numeric.md) for more informations about how to drive segment display in
your game.

## Total Nuclear Annihilation Remake Serial Score Display Assembly

Alternative, PBL sells TNA segment displays which use the same serial
protocol. The board is ready-made with four segment displays and a
controller which can be controlled by MPF via USB.

Part number:

* PBL-600-0473-00

Config looks like this:

``` yaml
hardware:
  segment_displays: mypinballs
mypinballs:
  port: /dev/ttyUSB0
segment_displays:
  display1:
    number: 1
  display2:
    number: 2
  display3:
    number: 3
  display4:
    number: 4
```

You can configure your serial port in `port`. See
[segment_display](../../mc/displays/alpha_numeric.md) for more informations about how to drive segment display in
your game.

See [Scotts description of the display for
details](https://www.scottdanesi.com/?p=4220).

* [Wiring 3rd-Party Segment Displays](wiring.md)

## What if it did not work?

Have a look at our [hardware troubleshooting guide](../troubleshooting_hardware/index.md).
