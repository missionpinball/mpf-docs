Display Widget Effects
======================

Effects are used to apply a variety of fancy graphical effects to the contents of a display widget.  The most commonly
used effects are ``dmd`` and ``color_dmd`` which create the look of hardware DMDs (in version of MPF prior to 0.50,
these were previously their own widget types). Multiple effects may be combined in a chain, however, effects can be
CPU/GPU intensive!

Required settings
-----------------

The following sections are required for the ``effects`` setting of the display widget:

type:
^^^^^
Single value, type: one of the options listed below.

The ``type:`` setting controls which effect will be loaded to process the display widget output.
Here is the list of available effect types (the settings for each type are found below):

- ``anti_aliasing`` applies a very basic anti-aliasing
- ``color_channel_mix`` swaps color channels
- ``color_dmd`` creates an RGB DMD look
- ``colorize`` applies a color tint
- ``dmd`` creates a monochrome DMD look
- ``dot_filter`` creates a dot filter to look like individual round dots/pixels (similar to a DMD)
- ``flip_vertical`` vertically flips the contents
- ``gain`` applies a gain (brightness) adjustment
- ``gamma`` applies a gamma correction
- ``glow`` applies a pulsing glow effect
- ``horizontal_blur`` Gaussian blurs horizontally
- ``invert_colors`` inverts the colors
- ``monochrome`` converts the image to monochrome/grayscale
- ``pixelate`` pixelates the image
- ``reduce`` reduces the number of bits per color channel (reducing the number of resulting colors)
- ``scanlines`` displays flickering scanlines (like an old CRT)
- ``vertical_blur`` Gaussian blurs vertically


Settings for *anti-aliasing* effect:
------------------------------------

The ``anti-aliasing`` effect does not have any settings.


Settings for *color_channel_mix* effect:
----------------------------------------

order:
^^^^^^
List, type: ``int``. Default: ``[1, 2, 0]``

The new sorted order of the rgb channels. The list must contain an arrangement of the list ``[0, 1, 2]``.


Settings for *color_dmd* effect:
--------------------------------

dot_filter:
^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Enables the "dot" look. Setting this to ``False`` means that the color DMD will not have dots.

dots_x:
^^^^^^^
Single value, type: ``int``. Default: ``128``

The number of DMD dots in the x direction.

dots_y:
^^^^^^^
Single value, type: ``int``. Default: ``32``

The number of DMD dots in the y direction.

blur:
^^^^^
Single value, type: ``float``. Default: ``0.1``

This is the radius of the "glow" of the pixels (when using ``dot_filter: True``). This is expressed
as a decimal relative to the size of the pixels. The default is ``0.1`` which means there's a 10%
glow radius.

dot_size:
^^^^^^^^^
Single value, type: ``float``. Default: ``0.7``

The size of the individual "dots", expressed as a decimal relative to what their full size would
be. A value of ``1.0`` will mean that each pixel will fill 100% of the space (e.g. no space in
between), and it won't really look like separate pixels.

background_color:
^^^^^^^^^^^^^^^^^
Single value, type: ``kivycolor``. Default: ``191919ff``

The background color of the display (the color of the pixels when they're "off"). Note: this is a
color with alpha channel value.

gain:
^^^^^
Single value, type: ``float``. Default: ``1.0``

A numeric multiplier that will be applied to every color channel of every pixel in this
color DMD widget (brightness).

For example, if you set ``gain: 1.2``, then a pixel on this color DMD's source display
that has a color of (100, 100, 100) will be drawn with the color (120, 120, 120). (Each
element multiplied by 1.2). Note that values above 255 will be capped at 255.

The default is 1.0 which means that the original colors are unchanged. You can play with
this to act as a "poor man's" brightness control, but values too far above or below 1.0
will probably look weird.

shades:
^^^^^^^
Single value, type: ``int``. Default: ``0``

This is the number of shades each color channel will be reduced to. The default is ``0``
which disables it and uses the full 256 shades per color channel, meaning the color DMD
widget will use have 256 shades each of red, green, and
blue. (In other words, the default is standard 24-bit color for a total of 16.7m colors.)

Note that this setting can produce weird results depending on your source content. If
you want an old school look, you might have better luck creating your videos and
graphics with fewer colors and then not setting the shades option here.

Also note if you want to use full color (no shade reduction), it's better to set this
to ``0`` and not ``256`` since 0 will disable this processing which will be less
overhead.


Settings for *colorize* effect:
-------------------------------

tint_color:
^^^^^^^^^^^
Single value, type: ``kivycolor``. Default: ``ff66ff00``

The color to tint the pixels in the display.


Settings for *dmd* effect:
--------------------------

dot_filter:
^^^^^^^^^^^
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Enables the "dot" look. Setting this to ``False`` means that the DMD will not have dots.

dots_x:
^^^^^^^
Single value, type: ``int``. Default: ``128``

The number of DMD dots in the x direction.

dots_y:
^^^^^^^
Single value, type: ``int``. Default: ``32``

The number of DMD dots in the y direction.

blur:
^^^^^
Single value, type: ``float``. Default: ``0.1``

This is the radius of the "glow" of the pixels (when using ``dot_filter: True``). This is expressed
as a decimal relative to the size of the pixels. The default is ``0.1`` which means there's a 10%
glow radius.

dot_size:
^^^^^^^^^
Single value, type: ``float``. Default: ``0.7``

The size of the individual "dots", expressed as a decimal relative to what their full size would
be. A value of ``1.0`` will mean that each pixel will fill 100% of the space (e.g. no space in
between), and it won't really look like separate pixels.

background_color:
^^^^^^^^^^^^^^^^^
Single value, type: ``kivycolor``. Default: ``191919ff``

The background color of the display (the color of the pixels when they're "off"). Note: this is a
color with alpha channel value.

gain:
^^^^^
Single value, type: ``float``. Default: ``1.0``

A numeric multiplier that will be applied to every color channel of every pixel in this
color DMD widget (brightness).

For example, if you set ``gain: 1.2``, then a pixel on this color DMD's source display
that has a color of (100, 100, 100) will be drawn with the color (120, 120, 120). (Each
element multiplied by 1.2). Note that values above 255 will be capped at 255.

The default is 1.0 which means that the original colors are unchanged. You can play with
this to act as a "poor man's" brightness control, but values too far above or below 1.0
will probably look weird.

shades:
^^^^^^^
Single value, type: ``int``. Default: ``0``

This is the number of shades each color channel will be reduced to. The default is ``0``
which disables it and uses the full 256 shades per color channel, meaning the color DMD
widget will use have 256 shades each of red, green, and
blue. (In other words, the default is standard 24-bit color for a total of 16.7m colors.)

Note that this setting can produce weird results depending on your source content. If
you want an old school look, you might have better luck creating your videos and
graphics with fewer colors and then not setting the shades option here.

Also note if you want to use full color (no shade reduction), it's better to set this
to ``0`` and not ``256`` since 0 will disable this processing which will be less
overhead.

luminosity:
^^^^^^^^^^^
List, type: ``float``. Default ``[.299, .587, .114]``

This defines the luminosity factor for each color channel. The value for each channel
must be between 0.0 and 1.0.

dot_color:
^^^^^^^^^^
Single value, type: ``kivycolor``. Default: ``ff5500``

The color of the dots in the DMD.  Defaults to classic DMD orange.


Settings for *dot_filter* effect:
---------------------------------

dots_x:
^^^^^^^
Single value, type: ``int``. Default: ``128``

The number of dots in the x direction.

dots_y:
^^^^^^^
Single value, type: ``int``. Default: ``32``

The number of dots in the y direction.

blur:
^^^^^
Single value, type: ``float``. Default: ``0.1``

This is the radius of the "glow" of the pixels. This is expressed as a decimal relative to the
size of the pixels. The default is ``0.1`` which means there's a 10% glow radius.

dot_size:
^^^^^^^^^
Single value, type: ``float``. Default: ``0.7``

The size of the individual "dots", expressed as a decimal relative to what their full size would
be. A value of ``1.0`` will mean that each pixel will fill 100% of the space (e.g. no space in
between), and it won't really look like separate pixels.

background_color:
^^^^^^^^^^^^^^^^^
Single value, type: ``kivycolor``. Default: ``191919ff``

The background color of the display (the color of the pixels when they're "off"). Note: this is a
color with alpha channel value.


Settings for *flip_vertical* effect:
------------------------------------

The ``flip_vertical`` effect does not have any settings.


Settings for *gain* effect:
---------------------------

gain:
^^^^^
Single value, type: ``float``. Default: ``1.0``

A numeric multiplier that will be applied to every color channel of every pixel in the
display widget (brightness).

For example, if you set ``gain: 1.2``, then a pixel on this display that has a color of
(100, 100, 100) will be drawn with the color (120, 120, 120). (Each element multiplied
by 1.2). Note that values above 255 will be capped at 255.

The default is 1.0 which means that the original colors are unchanged. You can play with
this to act as a "poor man's" brightness control, but values too far above or below 1.0
will probably look weird.


Settings for *gamma* effect:
----------------------------

gamma:
^^^^^^
Single value, type: ``float``. Default: ``1.0``

Sets the gamma factor of the effect.

Settings for *glow* effect:
----------------------------

blur_size:
^^^^^^^^^^
Single value, type: ``float``. Default: ``0.5``

The blur width in pixels

intensity:
^^^^^^^^^^
Single value, type: ``float``. Default: ``0.5``

The base intensity of the glow effect

glow_amplitude:
^^^^^^^^^^^^^^^
Single value, type: ``float``. Default: ``1.0``

The amplitude of the pulsing glow.  Set to 0 if you want to disable the pulse.

glow_speed:
^^^^^^^^^^^
Single value, type: ``float``. Default: ``1.0``

The frequency of the glow effect in Hz.


Settings for *horizontal_blur* effect:
--------------------------------------

size:
^^^^^
Single value, type: ``float``. Default: ``4.0``

The blur width in pixels.


Settings for *invert_colors* effect:
------------------------------------

The ``invert_colors`` effect does not have any settings.


Settings for *monochrome* effect:
---------------------------------

luminosity:
^^^^^^^^^^^
List, type: ``float``. Default ``[.299, .587, .114]``

This defines the luminosity factor for each color channel. The value for each channel
must be between 0.0 and 1.0.


Settings for *pixelate* effect:
-------------------------------

pixel_size:
^^^^^^^^^^^
Single value, type: ``int``. Default: ``10``

Sets the size of a new 'pixel' in the effect, in terms of number of 'real' pixels.


Settings for *reduce* effect:
-----------------------------

shades:
^^^^^^^
Single value, type: ``int``. Default: ``16``

This is the number of shades each color channel will be reduced to. Note that this setting
can produce weird results depending on your source content. If you want an old school look,
you might have better luck creating your videos and graphics with fewer colors and then not
setting the shades option here.


Settings for *scanlines* effect:
--------------------------------

The ``scanlines`` effect does not have any settings.


Settings for *vertical_blur* effect:
------------------------------------

size:
^^^^^
Single value, type: ``float``. Default: ``4.0``

The blur width in pixels.
