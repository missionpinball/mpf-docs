p_roc:
======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``p_roc:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``p_roc:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

dmd_timing_cycles:
~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``integer``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

dmd_update_interval:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``33ms``

.. todo::
   :doc:`/about/help_us_to_write_it`

lamp_matrix_strobe_time:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``100ms``

.. todo::
   :doc:`/about/help_us_to_write_it`

use_watchdog:
~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   :doc:`/about/help_us_to_write_it`

watchdog_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1s``

.. todo::
   :doc:`/about/help_us_to_write_it`

