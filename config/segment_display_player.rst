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
Single value, type: one of the following options: add, remove, flash, no_flash. Default: ``add``

* ``add`` - Add a text to the segment_display.
* ``remove`` - Add a text to the segment_display by key.
* ``flash`` - Flash this segment display.
* ``no_flash`` - Stop flashing this segment display.

expire:
~~~~~~~
Single value, type: ms_or_token. Defaults to empty.

Only used with ``action`` ``add``. Text will be removed after ``exire`` ms.

key:
~~~~
Single value, type: ``string``. Defaults to empty.

Key to use with ``action`` ``add`` and ``remove`` to reference a text on the
segment display.

priority:
~~~~~~~~~
Single value, type: int_or_token. Default: ``0``

Priority of this text.
The segment display will maintain a stack and show the text on top.

text:
~~~~~
Single value, type: ``string``. Defaults to empty.

Text to show. You can use :doc:`/config/instructions/text_templates`.


Related How To guides
---------------------

* :doc:`/displays/display/alpha_numeric`
* :doc:`/hardware/segment_display_platforms`
