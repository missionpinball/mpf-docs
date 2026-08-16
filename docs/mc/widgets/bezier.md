---
title: Bezier Curve Widget
---

# Bezier Curve Widget


The bezier widget is used to draw a curved line on a
[slide](../slides/index.md). (Note
that if you want to draw a straight line, you can use the
[Line Widget](line.md).)

Here's an example:

TODO This example just shows a blank slide in MPF 0.50?

``` yaml
#config_version=5
slide_player:
  mc_ready:
    bezier_example:
      - type: bezier
        points: 10, 10, 150, 450, 300, 100, 790, 590
        color: lime
        thickness: 5
        cap: square
      - type: bezier
        points: 0, 600, 400, 400, 400, 0
        color: pink
        close: true
        joint: miter
        thickness: 10
```

Which results in the following:

![image](../images/bezier.png)

## Settings

``` yaml
type: bezier
points:
thickness:
cap:
joint:
cap_precision:
joint_precision:
close:
precision:
```

!!! note

    Bezier widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following bezier widget settings may be
[animated](animation.md):
`color:`, `thickness:`, `opacity:`, `points:`, `rotation:`, and
`scale:`.

### type: bezier

Tells MPF that this is a bezier curve widget. This setting is required
when using bezier curve widgets.

### points:

A list of points which make up the bezier curve, expressed in x/y pairs
(so the number of items here has to be even).

The first pair is the starting point. The last pair is the ending point.
Each pair in between is a point the curve will pass through.

For example:

``` yaml
points: 10, 10, 200, 50, 300, 200
```

This would draw a bezier curve starting at (10,10) and ending at
(300,200), with a center point at (200, 50).

### thickness:

The thickness of the line. You'll probably have to play with different
settings to get it right. The default is `1.0`, so `2.0` is twice as
thick as the default, `0.5` is half as thick, etc.

### cap:

Determine the cap of the line, defaults to 'round'. Can be one of
'square' or 'round'

### joint:

Determine the join of the line, defaults to 'round'. Can be one of
'none', 'round', 'bevel', 'miter'.

### cap_precision:

Integer, defaults to 10.

Number of segments for drawing the "round" joint, defaults to 10. The
joint_precision must be at least 1.

### joint_precision:

Integer, defaults to 10.

Number of segments for drawing the "round" joint, defaults to 10. The
joint_precision must be at least 1.

### close:

Boolean (True/False), default is `False`.

If `True`, the line will be closed.

### precision:

Integer, defaults to 180.

The number of individual segments that will be drawn between each pair
of points.

## Examples

The example config files section of the documentation contains
[examples of bezier widgets](../../examples/index.md).
