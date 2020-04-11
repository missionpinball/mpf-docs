pololu_tic:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``pololu_tic:`` section of your config is where you configure your
:doc:`Pololu Tic Stepper Controller </hardware/pololu_tic/index>`.

See :doc:`tic_stepper_settings` for ``platform_settings`` in your steppers.

.. config


Optional settings
-----------------

The following sections are optional in the ``pololu_tic:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.


Related How To guides
---------------------

* :doc:`/hardware/pololu_tic/index`
