trinamics_steprocker:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``trinamics_steprocker:`` section of your config is where you configure
the :doc:`trinamics steprocker platform </hardware/trinamics/index>`.


Required settings
-----------------

The following sections are required in the ``trinamics_steprocker:`` section of your config:

port:
~~~~~
Single value, type: ``string``.

Serial port to use to connect to the steprocker.


Optional settings
-----------------

The following sections are optional in the ``trinamics_steprocker:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

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
List of one (or more) values, each is a type: ``string``.

.. todo:: :doc:`/about/help_us_to_write_it`


