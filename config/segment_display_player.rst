segment_display_player:
=======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``segments:`` section of a step.

.. overview

The ``segment_display_player:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`


Optional settings
-----------------

The following sections are optional in the ``segment_display_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: add, remove, flash, no_flash. Default: ``add``

.. todo:: :doc:`/about/help_us_to_write_it`

expire:
~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`

key:
~~~~
Single value, type: ``string``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo:: :doc:`/about/help_us_to_write_it`

text:
~~~~~
Single value, type: ``string``. Default: ``None``

.. todo:: :doc:`/about/help_us_to_write_it`


