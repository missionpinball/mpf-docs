playfield_transfers:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``playfield_transfers:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Required settings
-----------------

The following sections are required in the ``playfield_transfers:`` section of your config:

captures_from:
~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device.

.. todo::
   :doc:`/about/help_us_to_write_it`

eject_target:
~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device.

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``playfield_transfers:`` section of your config. (If you don't include them, the default will be used).

ball_switch:
~~~~~~~~~~~~

Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   :doc:`/about/help_us_to_write_it`

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

transfer_events:
~~~~~~~~~~~~~~~~


One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted,
