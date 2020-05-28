smart_virtual:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``smart_virtual:`` section of your config is where you configure the
:doc:`smart virtual platform </hardware/virtual/smart_virtual>`.

.. config


Optional settings
-----------------

The following sections are optional in the ``smart_virtual:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

File level for the console log for this platform.

simulate_manual_plunger:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

When ``simulate_manual_plunger`` is set to ``True`` the smart_virtual platform
will automatically plunge balls in devices with mechanical
eject after ``simulate_manual_plunger_timeout`` ms.

simulate_manual_plunger_timeout:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``10s``

When ``simulate_manual_plunger`` is set to ``True`` the smart_virtual platform
will automatically plunge balls in devices with mechanical
eject after ``simulate_manual_plunger_timeout`` ms.


Related How To guides
---------------------

* :doc:`/hardware/virtual/smart_virtual`
