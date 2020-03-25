fast_firmware_update:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``firmware_updates:`` section of your ``fast:`` config is where you list
all your firmware images.
Those can then be installed using :doc:`mpf hardware firmware_update </running/commands/hardware>`.

.. config


Required settings
-----------------

The following sections are required in the ``fast_firmware_update:`` section of your config:

file:
~~~~~
Single value, type: ``string``.

The path of your firmware file.

type:
~~~~~
Single value, type: one of the following options: net, rgb.

For which CPU is this firmware file?

version:
~~~~~~~~
Single value, type: ``string``.

The exact version of the firmware.
MPF will check that if this is higher than the installed version reported by
the FAST CPU.


Related How To guides
---------------------

* :doc:`/hardware/fast/index`
