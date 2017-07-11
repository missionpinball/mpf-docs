led_player:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``leds:`` section of a step.

.. overview

The ``led_player:`` section of your config is where you...

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``led_player:`` section of your config. (If you don't include them, the default will be used).

color:
~~~~~~
Single value, type: ``string``. Default: ``white``

.. todo::
   Add description.

fade:
~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

.. note:: The ``led_player:`` section of your config may contain additional settings not mentioned here. Read the introductory text for details of what those might be.

