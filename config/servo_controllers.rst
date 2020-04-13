servo_controllers:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``servo_controllers:`` section of your config is where you configure
PCA9685/PCA9635-based I2C servo controllers.
See :doc:`/hardware/i2c_servo/index` for details.


I2C Address
~~~~~~~~~~~
When you configure an I2C servo controller you have to address it on the I2C
bus.
The default of the chip is ``0x40`` which is ``64`` in decimal.
There might be some prefix depending on your I2C interface.

.. config


Optional settings
-----------------

The following sections are optional in the ``servo_controllers:`` section of your config. (If you don't include them, the default will be used).

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``none``

Log level for the console log for this platform.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see more debug output.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this platform.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the platform this servo controller is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

servo_max:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``600``

The controller is driving the servo using PWM. ``servo_max`` defines thes the
upper PWM limit. It will use a duty cycle of ``value/4096`` at 50Hz.

servo_min:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``150``

The controller is driving the servo using PWM. ``servo_min`` defines thes the
lower PWM limit. It will use a duty cycle of ``value/4096`` at 50Hz.


Related How To guides
---------------------

* :doc:`/hardware/i2c_servo/index`
