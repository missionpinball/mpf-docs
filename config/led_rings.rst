led_rings
=========

*Config File Section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

A "led_rings" will create "count" leds for you starting the number at
"number_start". If you need a prefix or suffix for the number you can use
"number_template". All settings in "led_template" will be applied to all LEDs.
The only difference between :doc:`led_stripes </config/led_stripes>`  and
:doc:`led_rings </config/led_rings>` is how the x/y coordinates are computed.

Here's an example:

.. literalinclude:: /example_configs/led/config/led_groups.yaml
   :language: yaml


number_start:
~~~~~~~~~~~~~
The integer value for the number for the first LED in the ring. (MPF assumes
that all the LEDs in the ring are numbered sequentially.)

count:
~~~~~~
The integer value for how many LEDs are in the ring.

number_template:
~~~~~~~~~~~~~~~~
MPF automatically configures the LEDs in a ring. The first one uses the
``number_start:`` value, and then it counts up from there up through the
``count:`` value.

However, many hardware numbers for LEDs are not just vanilla numbers, rather
they also include a board number or channel or something like that. The
``number_template:`` is where you specify what that number value looks like.
Just use braces ``{}`` for the part you want replaced by a number.

The example config with a number template of ``7-{}`` with a number start of
200 and a count of 5 will create 5 LEDs with the numbers 7-200, 7-201, 7-202,
7-203, and 7-204.

center_x:
~~~~~~~~~
The "x" position of the center of the ring. (This is not used in MPF yet.)

center_y:
~~~~~~~~~
The "y" position of the center of the ring.

start_angle:
~~~~~~~~~~~~
The angle (in degrees, 0-360) of the first LED in the right. This is used for
the calculation of x/y positions of individual LEDs only.

radius:
~~~~~~~
The radius of the ring (in relative size to the x/y coordinates of the
``center_x:`` and ``center_y:`` positions. This is used for
the calculation of x/y positions of individual LEDs only.

led_template:
~~~~~~~~~~~~~
This is a list of sub-settings (indented) that are regular settings from the
:doc:`leds` section of your machine config. Any settings that are valid there
are valid here, and they're applied to all the LEDs in the ring.
