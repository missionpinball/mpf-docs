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
   Add description.


Required settings
-----------------

The following sections are required in the ``motors:`` section of your config:

motor_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

.. todo::
   Add description.

position_switches:
~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``machine(switches)``.

.. todo::
   Add description.

reset_position:
~~~~~~~~~~~~~~~
Single value, type: ``string``.

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``motors:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

go_to_position:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3, ball_starting``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


