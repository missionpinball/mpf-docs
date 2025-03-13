---
title: Matrix Lights (Bulbs)
---

# Matrix Lights (Bulbs)


Related Config File Sections:

* [lights:](../../config/lights.md)

Some hardware platforms support lamps in a matrix. Those lights are
usually bulbs and single color (white). Each of them is assigned to a
unique column/row combination and driven sequentially by the platform.

Video about wiring of lights:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/C9GzkMduEKY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Hardware

[TODO: Add a picture of bulbs in a matrix](../../about/help.md)

There are various types of bulbs in pinball machines depending on when
they were made. In EM and early SS #44 and #47 bulbs were used. Later SS
machines used #555 bulbs (or the vibration resistant variant #444 or the
#259 substitute). Those bulbs are rated at 6.3V but typically driven at
12V in a matrix or using AC voltages in older machines. Newer machines
(pre LED) use #906 bulbs which are rated at 13.5V.

## Config

Details differ by platform but the syntax for the number of such a light
is usually `column:row` or `column:row` (see
your platform for details). The config looks like this:

``` mpf-config
lights:
  my_matrix_light:
    number: 2:10      # or 2/10
```

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for LEDs is `device.lights.(name)`.

* *color*
* *corrected_color*

Related How To guides:

* [Tutorial step 17: Add lights (or LEDs)](../../tutorial/17_add_lights_leds.md)
