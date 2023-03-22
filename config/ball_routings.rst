ball_routings:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``ball_routings:`` section of your config is where you...

.. todo:: :doc:`/about/help_us_to_write_it`

.. config


Required settings
-----------------

The following sections are required in the ``ball_routings:`` section of your config:

source_devices:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

target_device:
~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`


Optional settings
-----------------

The following sections are optional in the ``ball_routings:`` section of your config. (If you don't include them, the default will be used).

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

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

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
