---
title: Points Widget
---

# Points Widget


The points widget is used to draw points (individual square points) on a
slide.

Here's an example:

``` mpf-mc-config
#config_version=5
slide_player:
  mc_ready:
    points_example:
      - type: points
        points: 50, 50, 75, 50, 100, 50
        pointsize: 2
        color: lime
      - type: points
        points: 400, 300
        pointsize: 3
        color: pink
```

Which results in the following:

![image](/docs/mc/images/points.png)

## Settings

``` yaml
type: points
points:
pointsize:
```

!!! note

    Points widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following points widget settings may be
[animated](animation.md):
`color:`, `points:`, `pointsize:`, `opacity:`, `rotation:`, and
`scale:`.

### type: points

### points:

A list of the x,y coordinates of pairs of points.

### pointsize:

Floating-point number, default is `1.0`.

The distance from the center of the point to the edge, so a value of 1.0
makes a point that's two pixels wide. (This is kind of like the radius,
though points are square so it's not technically the radius. Probably
there's some fancy math name for it.)
