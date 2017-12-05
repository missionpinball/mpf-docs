lights:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``lights:`` section of your config is where you configure physical lights for your 
hardware platform. 

.. note::
   As of MPF 0.50, all lights have been combined into this single
   ``lights`` configuration. If you are using 0.33 or earlier, please see
   :doc:`/config/matrix_lights` for incandescent bulbs and :doc:`/config/leds` for LEDs.

Required settings
-----------------

The following sections are required in the ``lights:`` section of your config:

channels:
~~~~~~~~~
List of ``lights`` settings for multi-color LEDs. Default: ``None``

Instead of a single ``number`` address for a light, you can enter channels 
corresponding to the multi-color channels of an RGB or RGBW LED. Each channel entry can
contain any of the ``lights`` parameters listed on this page, but at least ``number`` is required.

.. code-block:: yaml
  
  lights:
    rainbow_star:
      type: rgb
      channels:
        red:
          number: 9-29
        green:
          number: 9-30
        blue:
          number: 9-31

Note that a light must have either ``channels`` or ``number`` defined, but cannot have both.

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the light which specifies which output the
hardware bulb or LED is physically connected to. The exact format used here will
depend on which control system you're using and how the light is connected.

See the :doc:`/hardware/numbers` guide for details.

Note that a light must have either ``channels`` or ``number`` defined, but cannot have both.


Optional settings
-----------------

The following sections are optional in the ``lights:`` section of your config. (If you don't include them, the default will be used).


color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

If provided, a color correction profile will be applied to all color settings this light receives.
By order of operations, the light will be set to the requested color first and then the color
correction profile will be applied on top.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

If ``True``, this light will log its configuration and color changes to the debug log.

default_on_color:
~~~~~~~~~~~~~~~~~
Single value, type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Default: ``ffffff``

For multi-color LEDs, the color defined here will be used when the light is enabled via "on" 
(as opposed to being enabled with a specific color). Not intended for single-color lights.

default_fade_ms:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

When this light receives instructions to change color, it can interpolate from its current value to the 
new value over a fade time. If no value is provided, the machine default will be used. If this light is
part of a show that defines a fade time, the show's value will supercede this light's setting.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this LED is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Lights can be referenced by their tags in light_players.
Typical tags are `gi` for all GIs or `playfield_inserts` for all inserts on the playfield.

type:
~~~~~
Single value, type: ``string`` (case-insensitive). Default: ``rgb``

This describes the channel order of an LED. Can be 1 to many channels (if supported by hardware). 
Valid channels: r (red), g (green), b (blue), w (white=minimum of red, green and blue), 
+ (always on), - (always off).

When using serial LEDs (e.g. with FAST or Fadecandy), use `rgb` for WS2812 and `grb` for WS2811 LEDs.

x:
~~
Single value, type: ``integer``. Default: ``None``

This is used for display_light_player to determine the position of this light on the playfield and
use it as a huge display.

y:
~~
Single value, type: ``integer``. Default: ``None``

This is used for display_light_player to determine the position of this light on the playfield and
use it as a huge display.

z:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   *No longer used?*

