---
title: Image Widget
---

# Image Widget


The image widget is used to display an image on a
[slide](../slides/index.md). It's
also used to display animated images, which can either be animated GIFs
or a folder or zip file of sequentially-numbered images (of any type).

Image types that support alpha channels (like PNGs) are supported.

## Settings

!!! note

    Image widgets also have "common" widget settings for position,
    opacity, animations, color, style, etc. Those are not listed here, but
    are instead covered in
    [common widget settings](common_settings.md) page.

Also remember that all widget settings can be controlled via
[widget styles](styles.md), rather than you having to set every setting on every
widget.

The following image widget settings may be
[animated](animation.md):
`x:`, `y:`, `color:`, `rotation:`, `scale:`, `fps:`, `current_frame:`,
and `opacity:`.

### type: image

Single value, type: `string`.

Tells MPF that this is an image widget

### image:

Single value, type: `string` name of a
[image](../../assets/images.md).

The name of the image asset this widget will show. Details on image
assets are [here](../../assets/images.md).

### mag_filter: 

!!! info ""

    New in MPF 0.57.5, requires MPF-MC 0.57.2

Single value, type: `string` (linear or nearest). Default: `linear'

Sets the magnification (enlarging) scaling method for the image.  
By default linear scaling with smooth appearance. 
nearest results in pixelated appearance.

### min_filter:

!!! info ""

    New in MPF 0.57.5, requires MPF-MC 0.57.2

Single value, type: `string` (linear or nearest). Default: `linear'

Sets the minimizing (shrinking) scaling method for the image.  
By default linear scaling with smooth appearance. 
nearest results in pixelated appearance.

For mag_filter and min_filter, the differences between the scaling algorithms can be seen in this image:
![open menu](../images/image_filter.png)


### fps:

Single value, type: `integer`. Default: `10`.

For animated images, sets how fast it plays (frames per second).

### loops:

Single value, type: `integer`. Default: `-1`.

The number of times an animated image will loop. Set to `-1` for
unlimited. Note this is now consistent in 0.50 with other areas of MPF.
In earlier versions of MPF this setting used `0` to specify unlimited
loops.

### auto_play:

Single value, type: `boolean` (Yes/No or True/False). Default: `True`

If the image is an animated image, configures whether it plays
automatically when it's loaded.

This is good for looping images, but if you have an image you want to
play at a specific point, you probably want to set this to no and play
it from specific events via the widget player.

### start_frame:

Single value, type: `integer`. Default: `0`.

Which start frame to use for animated images.

### persist_frame:

Single value, type: `boolean` (`true`/`false`). Default: `false`

When true, the animated image widget will remember the frame the it was
on when it was last used, and restore that frame when the widget is next
used.

By default, an animated image will reset itself each time it is added to
a slide.
