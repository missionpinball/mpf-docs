p_roc:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``p_roc:`` section of your config is where you configure hardware specific bits about the P-Roc.
In most cases you can omit this config and stick with the defaults.


Optional settings
-----------------

The following sections are optional in the ``p_roc:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to ``True`` if you want to know what is going on under the hood.
We will usually ask you to set this if you experience any hardware related problems
and send us your log.

dmd_timing_cycles:
~~~~~~~~~~~~~~~~~~
List of four values, each is a type: ``integer``. Default: ``None``

Those values determine the timing to drive the different shades of your DMD.
See :doc:`/hardware/multimorphic/dmd` for details.

dmd_update_interval:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``33ms``

The update interval of your DMD. Usually you do not have to change this.

lamp_matrix_strobe_time:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``100ms``

The column strobe time for your lamp matrix. See :doc:`/hardware/multimorphic/lights` for details.

use_watchdog:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Enable or disable the watchdog. Usually you want to keep this enabled.

watchdog_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1s``

Watchdog timeout. The P/P3-Roc will disable all coils when the watchdog expires.
