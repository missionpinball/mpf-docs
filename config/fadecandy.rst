fadecandy:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``fadecandy:`` section of your config is where you configure your fadecandy
hardware platform.
Usually you can leave this at the defaults.
See :doc:`/hardware/fadecandy/index` for more details.

From the `fadecandy documentation <https://github.com/scanlime/fadecandy>`_:

Fadecandy internally represents colors with 16 bits of precision per channel,
or 48 bits per pixel. Why 48-bit color? In combination with our dithering
algorithm, this gives a lot more color resolution. It's especially helpful near
the low end of the brightness range, where stair-stepping and color popping
artifacts can be most apparent.

Each pixel goes through the following processing steps in Fadecandy:

 * 8 bit per channel framebuffer values are expanded to 16 bits per channel
 * We interpolate smoothly from the old framebuffer values to the new
   framebuffer values
 * This interpolated 16-bit value goes through the color LUT, which itself is
   linearly interpolated
 * The final 16-bit value is fed into our temporal dithering algorithm, which
   results in an 8-bit color
 * These 8-bit colors are converted to the format needed by OctoWS2811's DMA
   engine
 * In hardware, the converted colors are streamed out to eight LED strings in
   parallel

The color lookup tables can be used to implement gamma correction, brightness
and contrast, and white point correction. Each channel (RGB) has a 257 entry
table. Each entry is a 16-bit intensity. Entry 0 corresponds to the 16-bit
color 0x0000, entry 1 corresponds to 0x0100, etc. The 257th entry corresponds
to 0x10000, which is just past the end of the 16-bit intensity space.

Since MPF cannot do any better we suggest that you use this instead of our
software color correction (which is limited to 8-bit resolution here).

.. config


Optional settings
-----------------

The following sections are optional in the ``fadecandy:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

dithering:
~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Enabled temporal dithering for 16bit color precision.
You want to leave this enabled since it looks much nicer (especially at low
brightness).

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

gamma:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``2.5``

Specifies the `gamma correction <http://en.wikipedia.org/wiki/Gamma_correction>`_ value for the lights.
The default is 2.5.

keyframe_interpolation:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whatever the fadecandy should fade between keyframes.
You usually want to leave this at true since it looks much nicer.

linear_cutoff:
~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

This is best explained by quoting the FadeCandy documentation:
By default, brightness curves are entirely nonlinear. By setting
linearCutoff to a nonzero value, though, a linear area may be defined
at the bottom of the brightness curve. The linear section, near zero,
avoids creating very low output values that will cause distracting
flicker when dithered. This isn't a problem when the lights are viewed
indirectly such that the flicker is below the threshold of perception,
but in cases where the flicker is a problem this linear section can
eliminate it entirely at the cost of some dynamic range. To enable the
linear section, set linearCutoff to some nonzero value. A good
starting point is 1/256.0, corresponding to the lowest 8-bit PWM level.

linear_slope:
~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

Specifies the slope (output / input) of the linear section of the
brightness curve for the lights. The default is 1.0.

whitepoint:
~~~~~~~~~~~
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``1.0, 1.0, 1.0``

Specifies the white point (or white balance) of your lights. Enter it as
a list of three floating point values that correspond to the red,
blue, and green light segments. These values are treated as multipliers
to all incoming color commands. The default of `1.0, 1.0, 1.0` means
that no white point adjustment is used. `1.0, 1.0, 0.8` would set the
blue segment to be at 80% brightness while red and green are 100%,
etc.

You can use this to affect the overall brightness of lights (e.g. ``0.8, 0.8, 0.8``
would be 80% brightness as every color would be multiplied by 0.8). You can
also use this to affect the "tint" (lowering the blue, for example).


Related How To guides
---------------------

* :doc:`/hardware/fadecandy/index`
