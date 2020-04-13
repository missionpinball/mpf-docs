accelerometers:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

+--------------------------------------------------------------------------------------+
| Hardware platforms which support accelerometers                                      |
+--------------------------------------------------------------------------------------+
| :doc:`P3-Roc </hardware/multimorphic/accelerometer>`                                 |
+--------------------------------------------------------------------------------------+
| :doc:`MMA8451-based I2C accelerometers </hardware/mma8451/index>`                    |
+--------------------------------------------------------------------------------------+


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

.. config


Required settings
-----------------

The following sections are required in the ``accelerometers:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``. Defaults to empty.

Number of this device in your hardware platform. The actual meaning of this number depends on your hardware platform.


Optional settings
-----------------

The following sections are optional in the ``accelerometers:`` section of your config. (If you don't include them, the default will be used).

alpha:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.8``

The smoothing factor for single exponential smoothing (aka sliding window).

hit_limits:
~~~~~~~~~~~
One or more sub-entries. Each in the format of ``number`` (will be converted to floating point) : ``string``

Events which are posted at a certain G-force/acceleration. You can specify
multiple limits. You might use those to trigger :doc:`tilt </config/tilt>`
warnings.

level_limits:
~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``number`` (will be converted to floating point) : ``string``

How much degree may the level be off? You can define multiple limits and which
event should be posted when it exceeded.

level_x:
~~~~~~~~
Single value, type: ``integer``. Default: ``0``

``level_x``, ``level_y`` and``level_z`` define the default axis which is
considered as levelled. Defaults to ``(0, 0, 1)`` which means that the board
is laying straight on the ground. If you mount it in the cab you want about
3 degree. Under the playfield you want 6-7 degree.

level_y:
~~~~~~~~
Single value, type: ``integer``. Default: ``0``

``level_x``, ``level_y`` and``level_z`` define the default axis which is
considered as levelled. Defaults to ``(0, 0, 1)`` which means that the board
is laying straight on the ground. If you mount it in the cab you want about
3 degree. Under the playfield you want 6-7 degree.

level_z:
~~~~~~~~
Single value, type: ``integer``. Default: ``1``

``level_x``, ``level_y`` and``level_z`` define the default axis which is
considered as levelled. Defaults to ``(0, 0, 1)`` which means that the board
is laying straight on the ground. If you mount it in the cab you want about
3 degree. Under the playfield you want 6-7 degree.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the platform this accelerometer is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

platform_settings:
~~~~~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

The platform-specific hardware settings of this accelerometer.

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

* :doc:`/mechs/accelerometers/index`
