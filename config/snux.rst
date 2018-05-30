snux:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``snux:`` section of your config is where you configure the
:doc:`snux platform </hardware/snux/index>`.

This is an example:

.. code-block:: mpf-config

   hardware:
       platform: virtual	# use your platform here
       driverboards: wpc
       coils: snux
   
   system11:
       ac_relay_delay_ms: 75
       ac_relay_driver: c_ac_relay
   
   snux:
       flipper_enable_driver: c_flipper_enable_driver
       diag_led_driver: c_diag_led_driver
       platform: virtual	# use your platform here
   
   coils:
       c_diag_led_driver:
           number: c24
           default_hold_power: 1.0
       c_flipper_enable_driver:
           number: c23
           default_hold_power: 1.0
       c_ac_relay:
           number: c25
           default_hold_power: 1.0
       c_side_a1:
           number: c11a
       c_side_a2:
           number: c12a
           default_hold_power: 0.5
       c_side_c1:
           number: c11c
       c_side_c2:
           number: c12c
           default_hold_power: 0.5


Required settings
-----------------

The following sections are required in the ``snux:`` section of your config:

diag_led_driver:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

The coil to use to drive the diag LED on the snux board.

flipper_enable_driver:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

System 11 does not support any rules in software since the CPUs were too slow
at that time. Instead, they use a relay to enable flippers, pop bumpers and
slingshots.
Configure the driver to use to enable the flipper enable relay.

Optional settings
-----------------

The following sections are optional in the ``snux:`` section of your config. (If you don't include them, the default will be used).

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

:doc:`WPC Platform </hardware/existing_machines/wpc>` to connect to the
:doc:`SNUX board </hardware/snux/index>`.
