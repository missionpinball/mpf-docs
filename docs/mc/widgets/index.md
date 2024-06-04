---
title: Widgets
---

!!! warning "MPF-MC is being deprecated"

    This instruction page is for the legacy MPF-MC for MPF versions 0.57 and prior. For users of MPF 0.80 and later, please refer to the [Godot Media Controller (GMC) Documentation](../../gmc/index.md)

# Widgets


If a slide is a blank canvas, then "widgets" are the things you put on
that blank canvas, like text, images, shapes, videos, etc. Here's an
example of a slide (on the window display) showing how it's made up of
different types of widgets.

![image](/mc/images/widget_examples.jpg)

Widgets have properties like size and position, and some widgets include
additional properties depending on what type of widget they are. (Text
widget have font properties, video widgets have properties controlling
video playback, etc.)

You can control the stacking order of widgets on a slide (also called
the "layer" or "z-order"), to specify which widget should be on top
of another if they're overlapping.

You can specify all the widgets that are on a slide when you define that
slide, and/or you can add widgets later to existing slides or remove
certain widgets from slides while keeping others there.

You can even create a library of reusable "named" widgets which you
can use again and again on many slides.

You can specify widget "styles" which are default properties that are
inherited by all widgets based on that style. (So, for example, you
could specify a set of styles for text widgets called "title",
"default" and "small" that control the font name, font size, color,
and spacing for widgets using that style.

Individual widget properties can also be animated, meaning you can
change the size, position, opacity, etc. of a widget over time. You can
animate multiple properties of a widget at the same time or in a
sequence (or both), and you can specify which MPF events trigger
animation sequences to start and stop.

In this section of the documentation, we'll look at all the different
types of widgets (and their properties and settings), then look at how
you position and animate them, how to use widget styles, and how you can
create the reusable widgets.

You can test slides and widgets interactively using
[Interactive MC (iMC)](../../tools/imc.md).

* [Types of widgets](types.md)
* [Showing widgets on a slide](adding_widgets.md)
* [Positioning widgets on slides](positioning.md)
* [Animating widgets](animation.md)
* [Animation "easing"](easing.md)
* [Widget styles](styles.md)
* [Opacity & transparency](opacity.md)
* [Fonts](fonts.md)
* [Bitmap Fonts](bitmap_fonts.md)
* [Creating reusable "named" widgets](reusable_widgets.md)
* [Expiring & removing widgets](expire.md)
* [Widget keys](keys.md)
* [Layers, overlap, & z-order](layers.md)
