---
title: Rectangle Widget
---

# Rectangle Widget


The rectangle widget is used to draw a rectangle (or rounded rectangle)
on a slide. Remember that a square is just a rectangle whose height and
width are the same.

Here's an example:

``` mpf-mc-config
#config_version=5
slide_player:
  mc_ready:
    rectangle_example:
      - type: rectangle
        x: 200
        y: 200
        width: 200
        height: 200
        color: pink
      - type: rectangle
        x: 400
        y: 300
        width: 400
        height: 200
        corner_radius: 50
        corner_segments: 3
        color: yellow
      - type: rectangle
        x: 600
        y: 500
        width: 400
        height: 300
        corner_radius: 75
        color: red
```

Which results in the following:

![image](/docs/mc/images/rectangle.png)

## Settings

``` yaml
type: rectangle
width:
height:
corner_radius:
corner_segments:
```

!!! note

    Rectangle widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following rectangle widget settings may be
[animated](animation.md):
`x:`, `y:`, `width:`, `height:`, `color:`, `corner_radius:`, `opacity:`,
`rotation:`, and `scale:`.

### width:

The width of the rectangle, in pixels.

### height:

The height of the rectangle, in pixels.

### corner_radius:

Number value of the radius of the corners (in pixels). Default is `0`
which means sharp square corners.

### corner_segments:

For rectangles with rounded corners (where `corner_radius:` is greater
than 1), how many individual segments should make up the corner. The
more segments, the smoother the corner is.

Default is `10`.
