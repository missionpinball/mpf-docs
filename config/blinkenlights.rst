blinkenlights:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``blinkenlights:`` section of your config file is used
to define lights on your pinball machine that can be shared by
multiple different modes at the same time.  Blinkenlights work best with
RGB LEDs, because each mode that uses a blinkenlight can
specify a color that the blinkenlight should flash for that mode.
The blinkenlight will then flash each of its colors in a cycle according to
a given schedule.

Here's an example section:

.. code-block:: mpf-config

    #! lights:
    #!   l_left_ramp_arrow:
    #!     channels:
    #!       red:
    #!         number: 1
    #!       green:
    #!         number: 2
    #!       blue:
    #!         number: 3
    #!   l_right_ramp_arrow:
    #!     channels:
    #!       red:
    #!         number: 4
    #!       green:
    #!         number: 5
    #!       blue:
    #!         number: 6
    blinkenlights:
      blinkenlight_1:
        color_duration: 1s
        off_when_multiple: false
        light: l_left_ramp_arrow
        priority: 1000
      blinkenlight_2:
        cycle_duration: 1s
        off_when_multiple: false
        light: l_right_ramp_arrow
        priority: 1000

With the above configuration, two blinkenlights are configured: blinkenlight_1
and blinkenlight_2.  You can then use a
:doc:`blinkenlight_player </config/blinkenlight_player>`
to add or remove colors to these blinkenlights from within your modes.

The options are as follows:

.. config


Required settings
-----------------

The following sections are required in the ``blinkenlights:`` section of your
config:

light:
~~~~~~
Single value, type: string name of a :doc:`lights <lights>` device. Defaults
to empty.

This is the name of the light which this blinkenlight controls.

color_duration:
~~~~~~~~~~~~~~~
Time value. Defaults to empty.

Either ``color_duration`` or ``cycle_duration`` (see below) must be specified
for each blinkenlight, but not both.

This specifies the amount of time that each of the blinkenlight's colors will
be turned on.  For example, if this value is ``1s``, then each of the
blinkenlight's colors will be on for 1 second.

The more colors that are added to the blinkenlight when ``color_duration`` is
specified, the longer it will take to cycle through all the colors.  If you want
the blinkenlight's cycle to always last the same amount of time regardless of
how many colors the blinkenlight has, then use ``cycle_duration`` instead (see
below).

cycle_duration:
~~~~~~~~~~~~~~~
Time value. Defaults to empty.

Either ``cycle_duration`` or ``color_duration`` (see above) must be specified
for each blinkenlight, but not both.

This specifies the length of one cycle of the blinkenlight.  The blinkenlight
will show all of its colors in one cycle.  This includes the "off" color at the
end of the cycle, if applicable (see ``off_when_multiple`` below).  For example,
if this value is ``1s``, and the blinkenlight has 2 colors in its list, and
``off_when_multiple`` is ``false``, then each color will be displayed for 0.5
seconds. If ``off_when_multiple`` is ``true``, then the "off" color will count
as a color in the blinkenlight's cycle, and so the each color will only be
displayed for 1/3 of a second.

The more colors that are added to the blinkenlight when ``cycle_duration`` is
specified, the shorter each color will be displayed.  If you want each color to
be displayed for a certain length of time regardless of the number of colors,
then use ``color_duration`` instead (see above).

Optional settings
-----------------

The following sections are optional in the ``blinkenlights:`` section
of your config. (If you don't include them, the default will be used).

off_when_multiple:
~~~~~~~~~~~~~~~~~~
Boolean True/False or Yes/No. Default: ``False``.

This specifies whether or not to include an "off" color at the end of each
cycle when the blinkenlight has more than one color in its list.

For example, if the blinkenlight has 2 colors (red and green) and
``off_when_multiple`` is ``False`` (the default value), then the cycles will be
red, green, red, green. However, if ``off_when_multiple`` is ``True``, then the
cycles will be red, green, off, red, green, off.  The "off" color in this case
is treated as another color for the purposes of the ``color_duration`` and
``cycle_duration`` settings above.

A blinkenlight that only has 1 color in its list will be off at the end of its
cycle, regardless of whether ``off_when_multiple`` is ``True`` or ``False``.
For example, the cycles of a blinkenlight that has 1 color (red) will be red,
off, red, off.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The priority of the blinkenlight.  If there is a show that uses this
blinkenlight's light, and the show and the blinkenlight are happening at the
same time, then the light will be controlled by whichever one has the highest
priority.
