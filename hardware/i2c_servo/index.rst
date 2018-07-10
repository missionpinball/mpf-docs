I2C Servo Controllers
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/servo_controllers`                                             |
+------------------------------------------------------------------------------+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+

MPF currently supports PCA9685/PCA9635 based servo controllers via I2C.
One example for such a controller is the
`Adafruit 16-Channel 12-bit PWM/Servo Driver <https://www.adafruit.com/product/815>`_.
You can use any I2C platform supported by MPF (see :doc:`/hardware/i2c_platforms`).

1. Installing I2C Servo Controllers
-----------------------------------

Connect the controller to the I2C port and add the following config section:

.. code-block:: mpf-config

   hardware:
     servo_controllers: i2c_servo_controller

   servo_controllers:
     address: 0x40


0x40 is actually the default I2C address for this chip but it might be different
for some chips.

2. Add your servos
------------------
Add your servos to config:

.. code-block:: mpf-config

   servos:
     servo1:
       number: 0

All these config options are explained in-depth in the :doc:`servos: section </config/servos>`
of the config file reference.
