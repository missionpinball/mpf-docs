DMD Widget
==========

The DMD widget is used to render a :doc:`display </displays/display/index>` on a
:doc:`slide </displays/slides/index>` which looks like a classic monochrome DMD.

You can use the DMD widget to get an old school "DMD look" on your LCD display.

You can set the color of the dots to be whatever you want. (Default is orange, but you
can make them red or purple or whatever.)

The DMD widget is almost identical to the :doc:`/displays/widgets/color_dmd/index` widget
except the DMD widget has the additional options to do the color reduction.

Note that the DMD Widget really is unrelated to whether you have a
:doc:`physical DMD </displays/display/physical_mono_dmd>` in your machine. (Though
if you do have a physical DMD, you can add a DMD widget to a slide in your
on-screen window to see the DMD when you're running your machine in virtual mode.)

Settings
--------

::

   type: dmd
   width:
   height:
   source_display:
   luminosity:
   pixel_color:
   gain:
   dark_color:
   shades:
   dot_filter:
   pixel_size:
   blur:
   bg_color:

type: dmd
~~~~~~~~~

.. note:: DMD widgets also have "common" widget settings for position, opacity,
   animations, style, etc. Those are not listed here, but are instead covered in
   :doc:`common widget settings </displays/widgets/common_settings>` page.

Also remember that all widget settings can be controlled via
:doc:`widget styles </displays/widgets/styles>`, rather than
you having to set every setting on every widget.

width:
~~~~~~

The width (in pixels) that the DMD will be drawn on the slide. Note that this
does *not* control how many pixels (or dots) are in the DMD, rather, it's how big it
is on the slide. (The number of dots on the DMD is controlled via the source display's
width setting.)

For example, you might have a window that's 1024x768, and a source DMD display that's
128x32.

If you set ``width: 896`` for your DMD widget, that means it will be 896 pixels
wide in your 1024 window, and each drawn "dot" in the display will be 7 pixels wide in
the window (896 / 128 = 7).

This setting is required.


height:
~~~~~~~

The height that the DMD will be drawn on the slide. See the "width:" setting above
for details.


source_display:
~~~~~~~~~~~~~~~

The name of the display (from your ``displays:`` section) that will be the source for
the content of this DMD widget. The default is ``dmd``, which means you would need
to have a display called "dmd" in the ``displays:`` section of your machine config.

luminosity:
~~~~~~~~~~~

In MPF, all display content is full color, but the DMD widget displays a range of
monochrome colors to simulate a classic DMD. So MPF has to first reduce the color
content to grayscale which is controlled by this setting.

Luminosity is a list of three decimal values that are the multipliers
which are applied to each color change in the source content.
used to reduce the full color

The default is:

::

   luminosity: .299, .587, .184

which means that it converts each pixel to a grayscale color which is 29.9% of the red,
58.7% of the green, and 18.4% of the blue. (The reason these are not simply 1/3 of
each color is because the human eye perceives the brightness of each color channel
differently, so if it was a straight 1/3rd each then the resulting grayscale image
would appear muddy.)

You can change these values form the default if you want to play with different settings,
or just do not include a ``luminosity:`` setting to use the defaults.

pixel_color:
~~~~~~~~~~~~

Controls what color the pixels will be of this DMD widget. The default is ``ff5500`` which
is a classic DMD orange.

This is essentially the color that becomes the "full on" pixel color, and then
darker shades of it are proportional based on the grayscale conversion that was done
previously.

gain:
~~~~~

A numeric multiplier that will be applied to every color channel of every pixel in this
DMD widget.

For example, if you set ``gain: 1.2``, then a pixel on this DMD's source display
that has a color of (100, 100, 100) will be drawn with the color (120, 120, 120). (Each
element multiplied by 1.2).

Note that values above 255 will be capped at 255.

The default is 1.0 which means that the original colors are unchanged. You can play with
this to act as a "poor man's" brightness control, but values too far above or below 1.0
will probably look weird.

This is applied after the ``luminosity:`` and ``pixel_color:`` processing and can help you tweak the look of
the DMD widget.

dark_color:
~~~~~~~~~~~

Note: This feature is not currently implemented. TODO

This is the color of the pixels when they're "off" (black). Default is ``221100``.


shades:
~~~~~~~

This is the number of shades each color channel will be reduced to. The default is ``16``
which means that the DMD widget will use have 16 levels of brightness between black and
the ``pixel_color:`` you specified.

Set it to ``0`` if you want to disable it and keep the original range of shades.

Note that this setting can produce weird results depending on your source content. If
you want an old school look, you might have better luck creating your videos and
graphics with fewer colors and then not setting the shades option here.

dot_filter:
~~~~~~~~~~~

Enabled the "dot" look. Setting this to False means that the DMD will not have
dots. Default is ``True``.

pixel_size:
~~~~~~~~~~~

The size of the individual "dots", expressed as a decimal relative to what their
full size would be. A value of ``1.0`` will mean that each pixel will fill 100% of the
space (e.g. no space in between), and it won't really look like separate pixels.

The default is ``0.5``.

You can play with this setting (and the ``blur:`` setting below) to get a look that
you like.

blur:
~~~~~

This is the radius of the "glow" of the pixels (when using ``dot_filter: true``). This
is expressed as a decimal relative to the size of the pixels. The default is ``0.1``
which means there's a 10% glow radius.

This will be in addition to the ``pixel_size:``, so the defaults...

::

   pixel_size: 0.5
   blur: 0.1

...would result in the pixel being 50% of the space, the glow being 20% (10% on each side),
leaving 30% for spacing in between the pixels.

bg_color:
~~~~~~~~~

The background color which is used for the spaces in-between the pixels when you
have ``dot_filter: true``. Default is ``191919ff`` which is a dark gray color that's
fully opaque.

If you set the alpha channel to be transparent (like ``19191900``), then the dots will
appear "on top" of whatever else is on the slide behind the DMD widget.

Examples
--------

The example config files section of the documentation contains
:doc:`examples of DMD widgets </examples/dmd/index>`.

More examples are in the :doc:`/displays/display/adding_dot_look_to_lcd` guide.
