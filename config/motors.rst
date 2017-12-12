motors:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``motors:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Required settings
-----------------

The following sections are required in the ``motors:`` section of your config:

motor_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

.. todo::
   :doc:`/about/help_us_to_write_it`

position_switches:
~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``machine(switches)``.

.. todo::
   :doc:`/about/help_us_to_write_it`

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``string``.

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``motors:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

go_to_position:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   :doc:`/about/help_us_to_write_it`

reset_events:
~~~~~~~~~~~~~

One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``machine_reset_phase_3, ball_starting``

.. todo::
   :doc:`/about/help_us_to_write_it`

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   :doc:`/about/help_us_to_write_it`

