led_settings:
=============

*Config file section*

* Valid in machine config files: **YES**
* Valid in mode config files: **NO**

.. overview

The ``led_settings:`` section of your config is where you configure settings
for RGB LEDs in your machine.


Optional settings
-----------------

The following sections are optional in the ``led_settings:`` section of your config. (If you don't include them, the default will be used).

color_correction_profiles:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: dict. Default: ``None``

The ``color_correction_profile:`` section of your config is where you configure
named color correction profiles which you can then apply to RGB LEDs. You could
create a single profile here which you use for all of them, or create different
ones for different groups of LEDs.

The following sections are optional in the ``color_correction_profile:`` section of your config. (If you don't include them, the default will be used).

gamma:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``2.5``

Specifies the `gamma correction <http://en.wikipedia.org/wiki/Gamma_correction>`_ value for the LEDs. The default is
2.5. This setting currently only affects LEDs connected to a FadeCandy
LED controller.

linear_cutoff:
^^^^^^^^^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

This is best explained by quoting the FadeCandy documentation:
By default, brightness curves are entirely nonlinear. By setting
linearCutoff to a nonzero value, though, a linear area may be defined
at the bottom of the brightness curve. The linear section, near zero,
avoids creating very low output values that will cause distracting
flicker when dithered. This isn't a problem when the LEDs are viewed
indirectly such that the flicker is below the threshold of perception,
but in cases where the flicker is a problem this linear section can
eliminate it entirely at the cost of some dynamic range. To enable the
linear section, set linearCutoff to some nonzero value. A good
starting point is 1/256.0, corresponding to the lowest 8-bit PWM level.

This setting currently only affects LEDs
connected to a FadeCandy LED controller.

linear_slope:
^^^^^^^^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

Specifies the slope (output / input) of the linear section of the
brightness curve for the LEDs. The default is 1.0. This setting
currently only affects LEDs connected to a FadeCandy LED controller.

whitepoint:
^^^^^^^^^^^
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``1.0, 1.0, 1.0``

Specifies the white point (or white balance) of your LEDs. Enter it as
a list of three floating point values that correspond to the red,
blue, and green LED segments. These values are treated as multipliers
to all incoming color commands. The default of `1.0, 1.0, 1.0` means
that no white point adjustment is used. `1.0, 1.0, 0.8` would set the
blue segment to be at 80% brightness while red and green are 100%,
etc.

You can use this to affect the overall brightness of LEDs (e.g. ``0.8, 0.8, 0.8``
would be 80% brightness as every color would be multiplied by 0.8). You can
also use this to affect the "tint" (lowering the blue, for example).

default_color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

The name of the color correction profile that applies to an LED by default if
that LED doesn't have a profile configured for it.

default_led_fade_ms:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

This is the default *fade_ms* that will be applied to individual RGB
LEDs that don't have fade_ms settings configured. If you configure an
individual LED's *fade_ms*, it will override this setting.

.. todo:: Verify platforms this works on.


