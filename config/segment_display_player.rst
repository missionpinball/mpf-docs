segment_display_player:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``segment_displays:`` section of a step.

.. overview

The ``segment_display_player:`` section of your config is a :doc:`/config_players/index`
which controls :doc:`segment_displays`.
See :doc:`/displays/display/alpha_numeric` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``segment_display_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: add, remove, flash, no_flash, flash_match, flash_mask, set_color. Default: ``add``

* ``add`` - Add a text to the segment_display.
* ``remove`` - Remove a text from the segment_display by key. If a ``transition_out:`` setting is used, then that
  transition will be started.
* ``no_flash`` - Stop flashing this segment display.
* ``flash`` - Flash this segment display.
* ``flash_match`` - Flash the last two characters of the segment display.
* ``flash_mask`` - Use the ``flash_mask`` parameter value to determine which characters of the segment display to
  flash.
* ``set_color`` - Set the color(s) of the characters in the segment display (for platforms that support it).

color:
~~~~~~
List of one (or more) values, each is a type: ``color`` (*color name*, *hex*, or list of values *0*-*255*). Defaults to empty.

The color for each character in the display (if the platform supports it). If a single color is supplied,
all characters in the display will be set to that color. See :doc:`/config/instructions/colors` for more
information on specifying colors in config files.

expire:
~~~~~~~
Single value, type: ms_or_token. Defaults to empty.

Only used with ``action`` ``add``. Text will be removed after ``expire`` ms.

flash_mask:
~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Only used with the ``flash_mask`` action (or with ``add`` when the ``flashing`` parameter is set to ``mask``.
Determines which characters of the segment display will be flashed. Each character of the flash mask string
represents a character in the display. Character positions with an ``F`` character (must be upper-case) will
be flashed while positions containing any other character will not flash. For example, in a segment display
of length 16, to flash the first 8 characters use a ``flash_mask`` parameter value of ``FFFFFFFF________``.
You can use whatever character you wish for the non-flashing character positions.

flashing:
~~~~~~~~~
Single value, type: one of the following options: off, all, match, mask, not_set. Default: ``not_set``

* ``off`` - Stop flashing this segment display.
* ``all`` - Flash all characters in this segment display.
* ``match`` - Flash the last two characters of the segment display.
* ``mask`` - Use the ``flash_mask`` parameter value to determine which characters of the segment display to flash.

Only used with the ``add`` action.

key:
~~~~
Single value, type: ``string``. Defaults to empty.

Key to use with ``action`` ``add`` and ``remove`` to reference a text on the
segment display.

priority:
~~~~~~~~~
Single value, type: int_or_token. Default: ``0``

Priority of this text. The segment display will maintain a stack and show the text on top (highest
priority).

text:
~~~~~
Single value, type: ``string``. Defaults to empty.

Text to show. You can use :doc:`/config/instructions/text_templates`.

transition:
~~~~~~~~~~~
Unknown type. See description below.

.. note::
   Be sure the ``segment_display`` ``size`` parameter has been properly set for the segment display or the
   transition effects may not be calculated and displayed properly.

transition_out:
~~~~~~~~~~~~~~~
Unknown type. See description below.

.. code-block:: mpf-config

   #! segment_displays:
   #!   display1:
   #!     number: 1
   segment_display_player:
     jackpot_completed:
       display1:
         text: JACKPOT
         priority: 1000
         expire: 2s
         transition:
           type: push
           direction: right
           text: " *** "
         transition_out:
           type: push
           direction: right
           text: " *** "

There can only be one transition between text entries, so if outgoing text has a ``transition_out`` set, and an
incoming text entry has a ``transition`` set, then the incoming transition will take precedence.


Related How To guides
---------------------

* :doc:`/displays/display/alpha_numeric`
* :doc:`/hardware/segment_display_platforms`
