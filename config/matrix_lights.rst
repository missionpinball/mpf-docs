matrix_lights:
==============

.. include:: /not_updated_yet.rst

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``matrix_lights:`` section of your config is where you...

.. todo::
   Add description.

Required settings
-----------------

The following sections are required in the ``matrix_lights:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the light which specifies which output the
light is physically connected to. The exact format used here will
depend on which control system you're using and how the light is connected.

See the :doc:`/hardware/numbers` guide for details.

Optional settings
-----------------

The following sections are optional in the ``matrix_lights:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

fade_ms:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

off_events:
~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, turn this light off.

on_events:
~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, turn this light on.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this light is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

x:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

y:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

z:
~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

