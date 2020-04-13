playfield_transfers:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``playfield_transfers:`` section of your config is where you configure
devices which transfer balls between :doc:`playfields </mechs/playfields/index>`.

This is an example:

.. code-block:: mpf-config

   switches:
     s_transfer:
       number:
   playfield_transfers:
     transfer1:
       ball_switch: s_transfer
       captures_from: playfield1
       eject_target: playfield2
     transfer2:
       transfer_events: transfer_ball
       captures_from: playfield1
       eject_target: playfield2
   playfields:
     playfield1:
       label: Playfield 1
       default_source_device: None
     playfield2:
       label: Playfield 2
       default_source_device: None

.. config


Required settings
-----------------

The following sections are required in the ``playfield_transfers:`` section of your config:

captures_from:
~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

Source playfield for the transfer.

eject_target:
~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

Target playfield for the transfer.


Optional settings
-----------------

The following sections are optional in the ``playfield_transfers:`` section of your config. (If you don't include them, the default will be used).

ball_switch:
~~~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Ball switch which triggers the transfer.

transfer_events:
~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, will trigger a ball transfer.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see more debug output.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Tags of the device. Not used currently.


Related How To guides
---------------------

* :doc:`/mechs/playfields/index`
