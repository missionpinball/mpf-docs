segment_displays:
=================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``segment_displays:`` section of your config is where you define your
:doc:`segment displays </displays/display/alpha_numeric>`.
This can be 7-segment or alphanumeric displays which are typically
used in older machines.

.. config


Required settings
-----------------

The following sections are required in the ``segment_displays:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

The number of the display. The meaning depends on the hardware platform.


Optional settings
-----------------

The following sections are optional in the ``segment_displays:`` section of your config. (If you don't include them, the default will be used).

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

This can be used to overwrite the platform which is defined in the *hardware*
section for segment_displays.

