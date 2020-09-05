system11:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``system11:`` section of your config is where your system11 machine.
This is usually used together with the :doc:`snux platform </hardware/snux/index>`
or :doc:`apc platform </hardware/apc/index>`.

.. config


Required settings
-----------------

The following sections are required in the ``system11:`` section of your config:

ac_relay_driver:
~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The driver to use to drive the AC relay which switches between A and C side drivers.


Optional settings
-----------------

The following sections are optional in the ``system11:`` section of your config. (If you don't include them, the default will be used).

ac_relay_delay_ms:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``75ms``

Delay when switching between A and C side.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Upstream platform for hardware.
System 11 is a virtual platform which drives coils on another underlying
platform which can be configured here.

prefer_a_side_event:
~~~~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Default: ``game_ended``

Event to trigger A-side preference.
This is triggered at game end by default to reduce stress on the AC-relay
during attract.

prefer_c_side_event:
~~~~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Default: ``game_will_start``

Event to trigger C-side preference.
This is triggered at game start by default to increase response times.


Related How To guides
---------------------

* :doc:`/hardware/snux/index`
* :doc:`/hardware/apc/index`
