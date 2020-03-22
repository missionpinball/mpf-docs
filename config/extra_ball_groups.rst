extra_ball_groups:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``extra_ball_groups:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`

.. config


Optional settings
-----------------

The following sections are optional in the ``extra_ball_groups:`` section of your config. (If you don't include them, the default will be used).

award_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

.. todo:: :doc:`/about/help_us_to_write_it`

enabled:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo:: :doc:`/about/help_us_to_write_it`

lit_memory:
~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo:: :doc:`/about/help_us_to_write_it`

max_lit:
~~~~~~~~
Single value, type: ``integer``.

.. todo:: :doc:`/about/help_us_to_write_it`

max_per_ball:
~~~~~~~~~~~~~
Single value, type: ``integer``.

.. todo:: :doc:`/about/help_us_to_write_it`

max_per_game:
~~~~~~~~~~~~~
Single value, type: ``integer``.

.. todo:: :doc:`/about/help_us_to_write_it`

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


