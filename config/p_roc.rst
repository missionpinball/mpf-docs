p_roc:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``p_roc:`` section of your config is where you configure hardware specific bits about the P-Roc or P3-Roc.
In most cases you can omit this config and stick with the defaults.


Optional settings
-----------------

The following sections are optional in the ``p_roc:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to ``True`` if you want to know what is going on under the hood.
We will usually ask you to set this if you experience any hardware related problems
and send us your log.

dmd_timing_cycles:
~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``integer``.

Only P-Roc (not P3-Roc).

Those values determine the timing to drive the different shades of your DMD.
See :doc:`/hardware/multimorphic/dmd` for details.

dmd_update_interval:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``33ms``

Only P-Roc (not P3-Roc).

The update interval of your DMD. Usually you do not have to change this.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

lamp_matrix_strobe_time:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``100ms``

Default: ``100ms``

The column strobe time for your lamp matrix. See :doc:`/hardware/multimorphic/lights` for details.

pd_led_boards:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``int``:``subconfig(pd_led_boards)``. Default: ``none``

A map of PD-LED boards with their ID as key and a :doc:`configuration map <pd_led_boards>` as value.
This can be used to configure indivdual features per board.

See :doc:`/hardware/multimorphic/servos`, :doc:`/hardware/multimorphic/steppers` or
:doc:`/hardware/multimorphic/leds` for details.

use_watchdog:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Enable or disable the watchdog. Usually you want to keep this enabled.

watchdog_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``1s``

Watchdog timeout. The P/P3-Roc will disable all coils when the watchdog expires.
