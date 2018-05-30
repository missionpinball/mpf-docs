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
devices which transfer balls between playfields.

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


Required settings
-----------------

The following sections are required in the ``playfield_transfers:`` section of your config:

captures_from:
~~~~~~~~~~~~~~
Single value, type: string name of a ``playfields:`` device.

Source playfield for the transfer.

eject_target:
~~~~~~~~~~~~~
Single value, type: string name of a ``playfields:`` device.

Target playfield for the transfer.

Optional settings
-----------------

The following sections are optional in the ``playfield_transfers:`` section of your config. (If you don't include them, the default will be used).

ball_switch:
~~~~~~~~~~~~

Single value, type: string name of a ``switches:`` device. Default: ``None``

Ball switch which triggers the transfer.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to true to see more debug output.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Tags of the device. Not used currently.

transfer_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, will trigger a ball transfer.
