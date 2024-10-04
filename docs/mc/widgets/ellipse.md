---
title: Ellipse Widget
---

# Ellipse Widget


The ellipse widget is used to draw a solid ellipse (including circles)
on a [slide](../slides/index.md).

It can also be used to draw "wedges" (pie slices) or ellipses with
sections missing (like Pac Man).

Note that ellipses are always solid. If you want an elliptical outline,
use the [Bezier Curve Widget](bezier.md).

Here's an example:

``` mpf-mc-config
#config_version=5
slide_player:
  mc_ready:
    ellipse_example:
      - type: ellipse
        x: 200
        y: 200
        width: 200
        height: 200
        color: blue
        angle_start: 0
        angle_end: 90
      - type: ellipse
        x: 400
        y: 300
        width: 400
        height: 200
        color: yellow
        segments: 8
      - type: ellipse
        x: 600
        y: 500
        width: 400
        height: 300
        color: red
        angle_start: 200
        angle_end: 300
      - type: ellipse
        x: 700
        y: 200
        width: 90
        height: 300
        color: lime
```

And the result:

![image](../images/ellipse.png)

## Settings

``` yaml
width:
height:
segments:
angle_start:
angle_end:
```

!!! note

    Ellipse widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following ellipse widget settings may be
[animated](animation.md):
`x:`, `y:`, `width:`, `position:`, `height:`, `size:`, `color:`,
`angle_start:`, `angle_end:`, `opacity:`, `rotation:`, and `scale:`.

### type: ellipse

Tells MPF that this is an ellipse widget. This setting is required when
using ellipse widgets.

### width:

The width (in pixels) of this ellipse. This setting is required.

The `width:` and `height:` settings set the bounding box that the
ellipse will be drawn in. If you want a circle, set the width and height
to be the same.

### height:

The height (in pixels) of this ellipse. This setting is required.

### segments:

The number of segments that will make up the ellipse. More segments will
create a smoother edge, but depending on the size of your display and
the size of the ellipse, you might not see much of a difference.

The default is `180`.

### angle_start:

The angle, between 0-360, where the ellipse will start. The default is
`0`.

### angle_end:

The angle, between 0-360, where the ellipse will start. The default is
`360`.

Note that a start angle of 0 and an end angle of 360 will create a
complete solid ellipse.
