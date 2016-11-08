snux:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``snux:`` section of your config is where you...

.. todo::
   Add description.

Required settings
-----------------

The following sections are required in the ``snux:`` section of your config:

diag_led_driver:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

.. todo::
   Add description.

flipper_enable_driver:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

.. todo::
   Add description.

Optional settings
-----------------

The following sections are optional in the ``snux:`` section of your config. (If you don't include them, the default will be used).

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

