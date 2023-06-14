---
title: Using Coil Drivers as Lights
---

# Using Coil Drivers as Lights


Related Config File Sections:

* [lights:](../../config/lights.md)
* [light_player](../../config/light_player.md)
* [coils:](../../config/coils.md)
* [coil_player:](../../config/coil_player.md)

Sometimes you will find lights on a (coil) driver. There are various
reasons for this and MPF supports it. You can either use
[coil_player:](../../config/coil_player.md) to control those
lights but it will be different from normal lights (and light shows).
Alternatively, you can map the coils to a light (recommended). To map a
coil as light you can use the following config:

``` mpf-config
coils:
  your_light_coil:
    number: 42                 # number depends on your platform
    allow_enable: true        # this will allow 100% enable without pwm
lights:
  your_light_on_a_coil:
    number: your_light_coil     # map this light to a driver
    platform: drivers
```

This is sometimes done for [GIs](gis.md) and [Flashers](flashers.md).
