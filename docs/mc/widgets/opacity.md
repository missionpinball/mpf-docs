---
title: Widget Opacity & Transparency
---

# Widget Opacity & Transparency


All widgets in MPF can have "opacity" settings which control how
transparent they are. 100% opacity is the default, where nothing would
show through that widget. 0% opacity means that the widget is completely
transparent and would not show up at all. 50% means it's about half-way
in between, etc.

Here's an example. (This example is from the
[MC Demo](../../examples/mc_demo.md) which
you can download and run to see it in action.)

![image](/docs/mc/images/opacity_example.png)

## Specifying opacity by opacity: setting

Every widget type has an optional setting called `opacity:` which you
can use to set the opacity of that widget. This is a value from 0.0 to
1.0, with `0` meaning 0% opacity (completely transparent and not visible
at all), `1.0` meaning 100% opacity (the default), `0.25` meaning 25%,
etc.

Note that you can animate the opacity setting to cause a widget to blink
or flash. This is easier than adding and removing the widget over and
over, as with this method the widget stays put, it's just alternating
between visible and invisible. See the [How to animate display widgets](animation.md) guide for details.

You can apply opacity settings to all widget types, including images and
videos. (The opacity setting will affect the opacity for every pixel in
the image or video. If you just want an image with transparent parts,
then you would use a PNG or GIF with alpha settings instead.)

## Specifying opacity by color

For widget types that accept `color:` settings (text and the various
shape widgets), you can specify a transparency level as part of the
color by adding a fourth byte to the color hex value. (If your color
value is only six characters, MPF automatically adds `ff` (fully opaque)
to the end.

For example, regular red with 100% opacity would be:

    color: ff0000

Or it would also be (this is the same as the prior example):

    color: ff0000ff

If you wanted red with 50% opacity, you could enter:

    color: ff000080

There's not really any difference between setting the opacity at the
`color:` setting versus the `opacity:` setting. The opacity setting is
nice because it's applicable to all widget types (including those
without color settings), and it's animatable. But the color setting is
nice because you can set the opacity and color at the same time. It
really doesn't matter.
