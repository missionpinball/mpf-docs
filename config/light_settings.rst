light_settings:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

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

.. config


Optional settings
-----------------

The following sections are optional in the ``light_settings:`` section of your config. (If you don't include them, the default will be used).

color_correction_profiles:
~~~~~~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : :doc:`color_correction_profile <color_correction_profile>`

The ``color_correction_profile:`` section of your config is where you configure
named color correction profiles which you can then apply to lights. You could
create a single profile here which you use for all of them, or create different
ones for different groups of lights.

default_color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

The name of the color correction profile that applies to an light by default if
that light doesn't have a profile configured for it.

default_fade_ms:
~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

This is the default *fade_ms* that will be applied to individual lights
that don't have fade_ms settings configured. If you configure an
individual light's *fade_ms*, it will override this setting.


Related How To guides
---------------------

* :doc:`lights`
