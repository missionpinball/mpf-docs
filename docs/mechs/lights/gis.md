---
title: GI (general illumination)
---

# GI (general illumination)


Related Config File Sections:

* [lights:](../../config/lights.md)
* [light_player:](../../config/light_player.md)
* [coils:](../../config/coils.md)

MPF includes support for GI (general illumination) light strings which
are common in existing Williams and Stern machines. You can specify GI
strings which you can then enable, disable, or (if the hardware supports
it) dim. Typically, there are one to four GI strings.

!!! note

    In MPF 0.50 GIs became [lights:](../../config/lights.md)
    with `subtype` gi. They behave like any other lights in MPF.

## Hardware

[TODO: Add a picture of a GI string](../../about/help.md)
[TODO: Add a picture of GI LEDs](../../about/help.md)

GI Strings are actually kind of complex. Many of them are AC (even in
WPC machines), and some Williams WPC machines include triacs (kind of
like a transistor for AC) and "zero cross" AC waveform detection
circuits so they can sync their dimming commands with the AC current
wave. Later Williams WPC machines split their GI into non-dimmable
(which used still used AC) and switched their dimmable to DC. Some
machines also have "enable" relays that must be activated first before
certain GI strings will work. In general those bulbs are the same models
as used for inserts (#44 and #47 for EM and early SS; #444/#555/#249 for
later SS; #906 for later machines).

GI string might also be
[connected to a driver](coils_as_lights.md)
and not part of a light matrix. In recent machines LEDs are used but
still driven in strings.

Video about wiring of lights:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/C9GzkMduEKY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Config

MPF hides all this complexity from you. You just define your GI strings
in your machine [lights:](../../config/lights.md) section
and then you can enable, disable, and dim the dimmable ones as you wish.

This is an example for a [light](../../config/lights.md) with `subtype: gi`:

``` mpf-config
lights:
  gi_string_left:
    number: 3    # number depends on your platform
    subtype: gi
```

In modern machines (such as Spike) your GIs might just be handled as
lights. The details depend on your hardware platform and are outlined in
the platform documentation.

This is an example for a [light](../../config/lights.md) in Spike:

``` mpf-config
lights:
  gi_string_left:
    number: 3    # number depends on your platform
    subtype: led  # might be matrix in some platforms
```

In some cases GIs are connected to normal drivers on your driver board
(e.g. on a PD-16 on the P3-Roc). If that is the case you should
configure them as [coils](../../config/coils.md).
Then add them as [light](../../config/lights.md)
with `platform: drivers`:

``` mpf-config
coils:
  gi_string_left:
    number: A1-B1-3    # number depends on your platform
    allow_enable: true  # this will allow 100% enable without pwm
lights:
  gi_string_left:
    number: gi_string_left  # map this light to a driver
    platform: drivers
```

Alternatively, you could also use
[coil_player](../../config/coil_player.md) but
this gives you the convinience of being able to use GIs in normal light
shows.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for lights is `device.lights.<name>`.

*color*

:   The color of this string. If you set it to brightness values all
    color channels will have the same value. Brightness 100 (of 255)
    will be hex 64 and color 646464.

## Related How To guides

See the documentation of your platform on how to configure GIs.

Platform related How To

* [P/P3-Roc leds](../../hardware/multimorphic/leds.md)
* [P/P3-Roc matrix light](../../hardware/multimorphic/lights.md)
* [FAST leds](../../hardware/fast/leds.md)
* [FAST matrix light](../../hardware/fast/lights.md)
* [OPP leds](../../hardware/opp/leds.md)
* [OPP matrix light](../../hardware/opp/lights.md)----

## Related Events

None
