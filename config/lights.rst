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

Here is a minimal example:

.. code-block:: mpf-config

  lights:
    my_led:
      number: 7


Optional settings
-----------------

The following sections are optional in the ``lights:`` section of your config. (If you don't include them, the default will be used).

channels:
~~~~~~~~~
Single value, type: dict.

Instead of a single ``number`` address for a light, you can enter channels
corresponding to the multi-color channels of an RGB or RGBW LED. Each channel entry can
contain any of the ``lights`` parameters listed on this page, but at least ``number`` is required.

.. code-block:: mpf-config

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
See :doc:`/mechs/lights/leds` for more details about how to configure channels
for different types of LEDs.

color_correction_profile:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``.

If provided, a color correction profile will be applied to all color settings this light receives.
By order of operations, the light will be set to the requested color first and then the color
correction profile will be applied on top.

default_on_color:
~~~~~~~~~~~~~~~~~
Single value, type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Default: ``ffffff``

For multi-color LEDs, the color defined here will be used when the light is enabled via "on"
(as opposed to being enabled with a specific color). Not intended for single-color lights.

Color values may be a hex string (e.g. `22FFCC`), a list of RGB values (e.g. `[50, 128, 206]`),
or a color name (e.g. `turquoise`). MPF knows 140+ standard web color names, and you can define your
own custom colors in the :doc:`/config/named_colors` section of your config. 

fade_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) .

When this light receives instructions to change color, it can interpolate from its current value to the
new value over a fade time. If no value is provided, the machine default will be used. If this light is
part of a show that defines a fade time, the show's value will supercede this light's setting.

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the light which specifies which output the
hardware bulb or LED is physically connected to. The exact format used here will
depend on which control system you're using and how the light is connected.

See the :doc:`/hardware/numbers` guide for details.

Note that a light must have either ``channels`` or ``number`` defined, but cannot have both.

platform:
~~~~~~~~~
Single value, type: ``string``.

Name of the platform this LED is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

There is a special platform ``drivers`` which will reference a driver which
has to be configured in the ``number`` setting.
It can be used if you got a light which is connected to a driver in your
platform.
That might be the case for :doc:`GIs </mechs/lights/gis>` for example.
This is an example for a driver as light:

.. code-block:: mpf-config

  coils:
    light_connected_to_a_driver:
      number: 42           # number depends on your platform
      allow_enable: True   # this will allow 100% enable without pwm

  lights:     
    light_on_a_driver:
      number: light_connected_to_a_driver    # map this light to a driver
      platform: drivers

platform_settings:
~~~~~~~~~~~~~~~~~~
Single value, type: dict.

Platform-specific light settings.
Consult your platform documentation for details.

subtype:
~~~~~~~~
Single value, type: ``string``.

If you hardware platform supports multiple types of lights you need to set
a ``subtype`` to tell your platform how to address this light (to prevent
``number`` collisions).
Typical values are ``led``, ``matrix`` or ``gi``.
Consult your platform documentation for details.

type:
~~~~~
Single value, type: ``string``.

Default value is ``rgb``.

This describes the channel order of an LED. Can be 1 to many channels (if supported by hardware).
Valid channels: r (red), g (green), b (blue), w (white=minimum of red, green and blue),
+ (always on), - (always off).

When using serial LEDs (e.g. with FAST or Fadecandy), use `rgb` for WS2812 and `grb` for WS2811 LEDs.

x:
~~
Single value, type: ``number`` (will be converted to floating point).

This is used for display_light_player to determine the position of this light on the playfield and
use it as a huge display.

y:
~~
Single value, type: ``number`` (will be converted to floating point).

This is used for display_light_player to determine the position of this light on the playfield and
use it as a huge display.

z:
~~
Single value, type: ``number`` (will be converted to floating point).

Currently not used anywhere.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

If ``True``, this light will log its configuration and color changes to the debug log.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of the light in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``.

Lights can be referenced by their tags in light_players.
Typical tags are `gi` for all GIs or `playfield_inserts` for all inserts on the playfield.


