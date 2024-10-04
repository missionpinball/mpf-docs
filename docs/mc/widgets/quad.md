---
title: Quad Widget
---

# Quad Widget


The quad widget is used to draw solid polygons on a slide.

Here's an example:

``` mpf-mc-config
#config_version=5
slide_player:
  mc_ready:
    bezier_example:
      - type: quad
        points: 210, 110, 210, 150, 500, 200, 590, 190
        color: pink
      - type: quad
        points: 50, 550, 400, 400, 400, 100, 200, 200
        color: lime
```

Which results in the following:

![image](/docs/mc/images/quad.png)

## Settings

``` yaml
type: quad
points:
```

!!! note

    Quad widgets also have "common" widget settings for position, opacity,
    animations, color, style, etc. Those are not listed here, but are
    instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following quad widget settings may be
[animated](animation.md):
`color:`, `points:`, `opacity:`, `rotation:`, and `scale:`.

### type: quad

Tells MPF this is a quad widget.

### points:

A list of 8 values representing x,y coordinate pairs for the four
corners of the quad.

A list of the x,y coordinates of the corners. Note that to have a normal
four-cornered shape, the corners need to be in order. You can start with
any one and go clockwise or counter-clockwise, but if you enter the
corners in a mixed order like 1, 3, 2, 4 then it's possible your quad
will fold over itself and look weird.
