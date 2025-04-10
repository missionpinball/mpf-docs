---
title: Triangle widget
---

# Triangle widget


The triangle widget is used to draw triangles on a
[slide](../slides/index.md).

Here's an example:

``` yaml
#config_version=5
slide_player:
  mc_ready:
    triangle_example:
      - type: triangle
        color: blue
        points: 0, 0, 100, 0, 100, 100
      - type: triangle
        points: 400, 400, 300, 200, 600, 500
        color: red
      - type: triangle
        points: 200, 500, 100, 400, 300, 400
```

The example above results in the following:

![image](../images/triangle.png)

## Settings

``` yaml
type: triangle
points:
```

!!! note

    Triangle widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following triangle widget settings may be
[animated](animation.md):
`color:`, `points:`, `opacity:`, `rotation:`, and `scale:`.

### type: triangle

Tells MPF that this is a triangle widget.

### points:

A list of six numbers which are the the x,y coordinates for each of the
three corners. For example, `points: 400, 300, 200, 300, 400, 200` would
be a triangle with one corner at (400, 300), another corner at (200,
300), and the final corner at (400, 200).
