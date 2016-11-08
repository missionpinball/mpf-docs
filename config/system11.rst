system11:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``system11:`` section of your config is where you...

.. todo::
   Add description.

Required settings
-----------------

The following sections are required in the ``system11:`` section of your config:

ac_relay_driver:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``system11:`` section of your config. (If you don't include them, the default will be used).

ac_relay_delay_ms:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``75ms``

.. todo::
   Add description.

