light_stripes:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

A "led_stripe" will create "count" leds for you starting the number at "number_start".
If you need a prefix or suffix for the number you can use "number_template". All settings
in "led_template" will be applied to all LEDs. The only difference between
:doc:`led_stripes </config/light_stripes>`  and :doc:`light_rings </config/light_rings>`
is how the x/y coordinates are computed.

Here's an example:

.. literalinclude:: /mpf_examples/light/config/light_groups.yaml
   :language: yaml

.. config


Required settings
-----------------

The following sections are required in the ``light_stripes:`` section of your config:

count:
~~~~~~
Single value, type: ``integer``. Defaults to empty.

The integer value for how many LEDs are in the stripe.

light_template:
~~~~~~~~~~~~~~~
Single value, type: :doc:`lights <lights>`. Defaults to empty.

This is a list of sub-settings (indented) that are regular settings from the
:doc:`lights` section of your machine config. Any settings that are valid there
are valid here, and they're applied to all the LEDs in the stripe.

number_start:
~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

The integer value for the number for the first LED in the stripe. (MPF assumes
that all the LEDs in the stripe are numbered sequentially.)


Optional settings
-----------------

The following sections are optional in the ``light_stripes:`` section of your config. (If you don't include them, the default will be used).

direction:
~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

The angle (in degrees, 0-360) the this LED stripe is positioned on the
playfield. This is used for the calculation of x/y positions of individual
LEDs only.

distance:
~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

The distance between individual LEDs (in relative size to the x/y coordinates
of the ``start_x:`` and ``start_y:`` positions. This is used for
the calculation of x/y positions of individual LEDs only.

number_template:
~~~~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

MPF automatically configures the LEDs in a stripe. The first one uses the
``number_start:`` value, and then it counts up from there up through the
``count:`` value.

However, many hardware numbers for LEDs are not just vanilla numbers, rather
they also include a board number or channel or something like that. The
``number_template:`` is where you specify what that number value looks like.
Just use braces ``{}`` for the part you want replaced by a number.

The example config with a number template of ``7-{}`` with a number start of
200 and a count of 5 will create 5 LEDs with the numbers 7-200, 7-201, 7-202,
7-203, and 7-204.

start_x:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

The "x" position of the first LED. (This is not used in MPF yet.)

start_y:
~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

The "y" position of the first LED.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Unused.


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
