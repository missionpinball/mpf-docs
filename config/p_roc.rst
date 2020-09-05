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

.. config


Optional settings
-----------------

The following sections are optional in the ``p_roc:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to ``True`` if you want to know what is going on under the hood.
We will usually ask you to set this if you experience any hardware related problems
and send us your log.

dmd_timing_cycles:
~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``integer``. Defaults to empty.

Only P-Roc (not P3-Roc).

Those values determine the timing to drive the different shades of your DMD.
See :doc:`/hardware/multimorphic/dmd` for details.

dmd_update_interval:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``33ms``

Only P-Roc (not P3-Roc).

The update interval of your DMD. Usually you do not have to change this.

driverboards:
~~~~~~~~~~~~~
Single value, type: one of the following options: wpc, wpcAlphanumeric, wpc95, sternSAM, sternWhitestar, pdb, custom, None. Defaults to empty.

Similar to ``driverboards`` in the :doc:`/config/hardware` section.
Use this setting if you use multiple playforms (i.e. FAST and P3-Roc) in one
machine.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

lamp_matrix_strobe_time:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100ms``

Default: ``100ms``

The column strobe time for your lamp matrix. See :doc:`/hardware/multimorphic/lights` for details.

pd_led_boards:
~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``integer`` : :doc:`pd_led_boards <pd_led_boards>`

A map of PD-LED boards with their ID as key and a :doc:`configuration map <pd_led_boards>` as value.
This can be used to configure indivdual features per board.

See :doc:`/hardware/multimorphic/servos`, :doc:`/hardware/multimorphic/steppers` or
:doc:`/hardware/multimorphic/leds` for details.

trace_bus:
~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Log all calls to libpinproc.
This will cause a lot of additional log lines and might considerably slow down
MPF.
Use only during debugging.

use_separate_thread:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Whether MPF should spawn a separate thread to talk to the P/P3-Roc or not.
If you set this to ``False`` any IO to the P/P3-Roc will block the game loop
which might cause lags unrelated to the hardware.
This has a small overhead but should be enabled in most cases.

use_watchdog:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Enable or disable the watchdog. Usually you want to keep this enabled.

watchdog_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``1s``

Watchdog timeout. The P/P3-Roc will disable all coils when the watchdog expires.


Related How To guides
---------------------

* :doc:`/hardware/multimorphic/index`
