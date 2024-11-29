---
title: Flashers
---

# Flashers


Related Config File Sections:

* [coils:](../../config/coils.md)
* [coil_player:](../../config/coil_player.md)
* [lights:](../../config/lights.md)
* [light_player:](../../config/light_player.md)
* [flasher_player:](../../config/flasher_player.md)

MPF includes support for flashers, which are essentially just really
bright lights that are controlled via high-power driver transistors
instead of low-power lighting circuitry.

![image](/docs/mechs/images/flasher1.jpg)

![image](/docs/mechs/images/flasher2.jpg)

MPF's flasher devices are only used in older machines (WPC, Stern SAM,
System 11) since modern LED-based machines typically use regular LED
devices (or combinations of them) as flashers. (So basically a
"flasher" in MPF is any single-color light that's connected to a
driver output rather than a light output.

## Hardware

\#89 and \#906 bulbs are commonly used as flashers in pinball machines.
Those are rated at 13V but typically driven at higher voltages for only
a very short amount of time. Turning them on permanently will burn
quickly in most machines.

Video about wiring of lights:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/C9GzkMduEKY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Config

Starting with MPF 0.50 flashers and lights have been unified. Depending
on your platform flashers might be [lights:](../../config/lights.md) or [coils:](../../config/coils.md). In most
cases they are configured as [coil](../../config/coils.md):

``` mpf-config
coils:
  flasher_coil_4:
    number: 4
    allow_enable: true
```

Then add them as [light](../../config/lights.md):

``` mpf-config
#! coils:
#!   flasher_coil_4:
#!     number: 4
#!     allow_enable: true
lights:
  flasher_4:
    number: flasher_coil_4
    platform: drivers
```

Now you can use them in [flasher_player:](../../config/flasher_player.md) (or also in [light_player:](../../config/light_player.md) if you want to enable the flasher permanently).

``` mpf-config
flasher_player:
  flash:
    flasher_01: 100ms
```

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for lights is `device.lights.(name)`.

*color*

The color of this string. If you set it to brightness values all color channels will have the same value. Brightness 100 (of 255) will be hex 64 and color 646464.

## Related How To guides

See the documentation of your platform on how to configure GIs.

Platform related How To

* [P/P3-Roc leds](../../hardware/multimorphic/leds.md)
* [P/P3-Roc matrix light](../../hardware/multimorphic/lights.md)
* [FAST leds](../../hardware/fast/leds.md)
* [FAST matrix light](../../hardware/fast/lights.md)
* [OPP leds](../../hardware/opp/leds.md)
* [OPP matrix light](../../hardware/opp/lights.md)----
