---
title: Display Widget
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../../gmc/index.md)

# Display Widget


* [Effects](effects.md)

The display widget is used to show the contents of a display on a slide
[slide](../../slides/index.md) or
another display (think of this like a picture-in-picture kind of thing).
To attempt to clear up any confusion, there are two types of displays: a
[display](../display/index.md) which
is basically an in-memory target for for slides and widgets, and a
display widget (this help topic) which enables the graphical display of
the previously mentioned type of display within its boundaries (it is
the actual visual output of the logical display).

Here's an example:

``` yaml
#config_version=5
displays:
  window:
    height: 600
    width: 800
  my_frame:
    width: 400
    height: 300
    default: true

slides:
  base_slide:
    widgets:
      - type: display
        source_display: my_frame
        width: 400
        height: 300
        x: 300
        y: 200
      - type: text
        text: this is the base slide
        x: 600
        y: 400
  frame_slide:
    widgets:
      - type: text
        text: this is a slide in the frame
    background_color: red
slide_player:
  mc_ready.1:
    base_slide:
      target: window
  mc_ready.2: frame_slide
```

And the result:

![image](../../images/slide_frame.png)

## Settings

``` yaml
type: display
source_display:
width:
height:
effects:
```

!!! note

    Display widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](../common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](../styles.md), rather than you having to set every setting on every
widget.

The following display widget settings may be
[animated](../animation.md):
`x:` `y:`, and `pos:`.

## source_display:

The name of the logical display to show on the screen within the widget
boundaries. This name is available as a `target:` name is other areas of
your configs when you want to target a slide the specified display.

More information on display targets is
[here](../../slides/display_targets.md).

## width:

The width of the frame in pixels.

## height:

The height of the frame in pixels.

## effects:

A list of effects to apply to the display contents. These effects
perform image processing to the source image and can be used to get an
old school "DMD look" or "color DMD look" to your display as well as
other special effects. For more information on effects, please review
the [effects](effects.md) documentation.

An example of a display widget with a dmd effect:

``` yaml
#config_version=5
#! displays:
#!   window:
#!     height: 200
#!     width: 600
#!   dmd:
#!     width: 400
#!     height: 300
#!     default: true
slides:
  base_slide:
    - type: display
      source_display: dmd
      width: 640
      height: 160
      effects:
        - type: dmd
          dot_color: ff5500
#! slide_player:
#!   mc_ready:
#!     base_slide:
#!       target: window
```
