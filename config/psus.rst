psus:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``psus:`` section of your config is where you power supply units.
See :doc:`/hardware/voltages_and_power/index` for details about voltages in
pinball machines and some electric details.
Then specify to which PSU your :doc:`coils <coils>` are connected.
This is used for power management. In some cases, MPF ,ay deliberately delay
coil pulses to prevent too many coils from firing and drawing to much current
from your PSU.
:doc:`Ball devices <ball_devices>` and :doc:`drop target <drop_targets>` do
this by default to ensure more consistent pulses.

.. config


Optional settings
-----------------

The following sections are optional in the ``psus:`` section of your config. (If you don't include them, the default will be used).

max_amps:
~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Maximum ampers which can be provided by this PSU. Currently not used.

release_wait_ms:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``10``

Time to wait after a coil pulse.

voltage:
~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Voltage of your PSU. Only informal.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Currently unused.


Related How To guides
---------------------

* :doc:`/hardware/voltages_and_power/power_management`
