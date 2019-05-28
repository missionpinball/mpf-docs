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

.. code-block:: mpf-config

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

Events which are posted at a certain G-force/acceleration. You can specify
multiple limits. You might use those to trigger :doc:`tilt </config/tilt>`
warnings.


number:
~~~~~~~
Single value, type: ``string``.

Number of this device in your hardware platform. The actual meaning of this number depends on your hardware platform.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Friendly name for this device.

level_limits:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``float``:``str``. Default: ``None``

How much degree may the level be off? You can define multiple limits and which
event should be posted when it exceeded.


level_x,y,z:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

``level_x``, ``level_y`` and``level_z`` define the default axis which is
considered as levelled. Defaults to ``(0, 0, 1)`` which means that the board
is laying straight on the ground. If you mount it in the cab you want about
3 degree. Under the playfield you want 6-7 degree.

For instance ``(0, sin(3), 1 - sin(3))`` might be a vector to use for an
accelerometer in your cab.


platform_settings:
~~~~~~~~~~~~~~~~~~
One or more sub-entries.

The platform-specific hardware settings of this accelerometer.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this accelerometer is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Note there are no "special" tags for accelerometers.


Hardware platforms which support accelerometers:
------------------------------------------------

+--------------------------------------------------------------------------------------+
| :doc:`P3-Roc </hardware/multimorphic/accelerometer>`                                 |
+--------------------------------------------------------------------------------------+
| :doc:`MMA8451-based I2C accelerometers </hardware/mma8451/index>`                    |
+--------------------------------------------------------------------------------------+
