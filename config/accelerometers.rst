accelerometers:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``accelerometers:`` section of your config is where you configure accelerometers, including
how many G forces trigger different events.

Like other hardware devices, you create a sub-entry for each accelerometer, then under there you
configure additional settings. For example:

::

    accelerometers:
       test_accelerometer:
           number: 1
           level_x: 0
           level_y: 0
           level_z: 1
           hit_limits:
               0.5: event_hit1
               1.5: event_hit2
           level_limits:
               2: event_level1
               5: event_level2

Settings:
---------

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Enables additional debug logging for this device.

hit_limits:
~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Friendly name for this device.

level_limits:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``. Default: ``None``

.. todo::
   Add description.

level_x:
~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

level_y:
~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

level_z:
~~~~~~~~
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

number:
~~~~~~~
Single value, type: ``string``.

The platform-specific hardware number of this accelerometer.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this accelerometer is connected to. The default value of ``None`` means the
default hardware platform will be used.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Note there are no "special" tags for accelerometers.
