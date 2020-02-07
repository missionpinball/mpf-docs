light_settings:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

+------------------------------------------------------------------------------+
| Related Tutorial                                                             |
+==============================================================================+
| :doc:`/mechs/lights/index`                                                   |
+------------------------------------------------------------------------------+

.. overview

The ``light_settings:`` section of your config is where you configure default
settings for lights in your machine.

If you are using LEDs in your machine you probably want to set
``default_fade_ms`` to make them look softer. Otherwise, they will turn on
and off very sharply and might look flickery. For instance, Stern uses a value
of about 40ms for LEDs on modern machines:

.. code-block:: mpf-config

   light_settings:
     default_fade_ms: 40

Depending on your hardware your color might look a bit off by default.
Different color channels might achive different brightnesses and white might
look pinkish or blueish for example.
You can set a color_correction_profile to compensate for that:

.. code-block:: mpf-config

   light_settings:
     default_color_correction_profile: correction_profile_less_red
     color_correction_profiles:
       correction_profile_less_red:
         whitepoint: [0.9, 1.0, 1.0]
         gamma: 2.5
         linear_slope: 1.0
         linear_cutoff: 0.0

Human perception is also not linear. Therefore, ``linear_slope`` is used to
translate perceived brightness to brightness (you can configure that). If you
see flickering at very low brightnesses you can increase ``linear_cutoff`` to
compensate for that (see below for details).

You can also define more than one profile and configure them per
:doc:`light </config/lights>` in the ``color_correction_profile`` setting.
This might be useful if you use different types of lights in your machine:

.. code-block:: mpf-config

   light_settings:
     default_color_correction_profile: correction_profile_less_red
     color_correction_profiles:
       correction_profile_less_red:
         whitepoint: [0.9, 1.0, 1.0]
         gamma: 2.5
         linear_slope: 1.0
         linear_cutoff: 0.0
       correction_profile_less_blue:
         whitepoint: [1.0, 1.0, 0.9]
         gamma: 2.5
         linear_slope: 0.8
         linear_cutoff: 0.1
   lights:
     special_led:
       number: 42
       color_correction_profile: correction_profile_less_blue

Please note, that some hardware platforms (such as the
:doc:`fadecandy </hardware/fadecandy/index>`) support color correction in
hardware.
If possible, we advice you to use the hardware correction because it gives
you more dynamic range (since they use 16bit values internally).


Optional settings
-----------------

The following sections are optional in the ``light_settings:`` section of your config. (If you don't include them, the default will be used).

color_correction_profiles:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: dict. Default: ``None``

The ``color_correction_profile:`` section of your config is where you configure
named color correction profiles which you can then apply to lights. You could
create a single profile here which you use for all of them, or create different
ones for different groups of lights.

The following sections are optional in the ``color_correction_profile:`` section of your config. (If you don't include them, the default will be used).

gamma:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``2.5``

Specifies the `gamma correction <http://en.wikipedia.org/wiki/Gamma_correction>`_ value for the lights.
The default is 2.5.

linear_cutoff:
^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

Specifies the slope (output / input) of the linear section of the
brightness curve for the lights. The default is 1.0.

whitepoint:
^^^^^^^^^^^
List of three values, each is a type: ``number`` (will be converted to floating point).
Default: ``1.0, 1.0, 1.0``

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

default_color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

The name of the color correction profile that applies to an light by default if
that light doesn't have a profile configured for it.

default_fade_ms:
~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

This is the default *fade_ms* that will be applied to individual lights
that don't have fade_ms settings configured. If you configure an
individual light's *fade_ms*, it will override this setting.

