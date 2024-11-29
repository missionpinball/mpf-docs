---
title: Line Widget
---

# Line Widget


The line widget is used to draw a straight line on a
[slide](../slides/index.md). (Note
that if you want to draw a curved line, you can use the
[Bezier Curve Widget](bezier.md).)

Here's an example:

``` mpf-mc-config
#config_version=5
slide_player:
  mc_ready:
    line_example:
      - type: line
        points: 0, 300, 800, 300
      - type: line
        points: 0, 100, 800, 100
      - type: line
        points: 400, 95, 400, 0
        color: red
        thickness: 5
        cap: square
      - type: line
        points: 100, 500, 150, 550, 200, 450
        color: lime
        thickness: 2
      - type: line
        points: 500, 150, 600, 350, 650, 200
        color: blue
        close: true
        thickness: 3
```

And the results:

![image](../images/line.png)

## Settings

``` yaml
type: line
points:
thickness:
cap:
joint:
cap_precision:
joint_precision:
close:
```

!!! note

    Line widgets also have "common" widget settings for position, opacity,
    animations, color, style, etc. Those are not listed here, but are
    instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following line widget settings may be
[animated](animation.md):
`color:`, `thickness:`, `opacity:`, `points:`, `rotation:`, and
`scale:`.

### type: line

Tells MPF that this is a line widget. This setting is required when
using line curve widgets.

### points:

A list of point pairs which make up the line, expressed in x/y pairs (so
the number of items here has to be even).

For example:

    points: 10, 10, 200, 50, 300, 200

This would draw a line starting at (10,10) and going to (200, 50), and
then from there, going to (300,200). If you just want a single straight
line, then you would enter 4 values here: the x/y of the start and the
x/y of the end.

### thickness:

The thickness of the line. You'll probably have to play with different
settings to get it right. The default is `1.0`, so `2.0` is twice as
thick as the default, `0.5` is half as thick, etc.

### cap:

Determine the cap of the line, defaults to 'round'. Can be one of
'none', 'square' or 'round'.

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

## Examples

The example config files section of the documentation contains
[examples of line widgets](../../examples/index.md).
