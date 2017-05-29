I2C Servo Controllers
=====================

MPF currently supports PCA9685/PCA9635 based servo controllers via I2C.
One exemple for such a controller is the
`Adafruit 16-Channel 12-bit PWM/Servo Driver <https://www.adafruit.com/product/815>`_.
We currently only support I2C on the P3-Roc but it would be easy to support
on other devices such as the Raspberry PI. Let us know if you need that.

1. Installing I2C Servo Controllers
-----------------------------------

Connect the controller to the I2C port and add the following config section:

::

   hardware:
     servo_controllers: pololu_maestro
     [...]
     
   servo_controller:
     address: 0x40
     
     
0x40 is actually the default I2C address for this chip but it might be different
for some chips.

2. Add your servos
------------------
Add your servos to config:

::

   servos:
     servo1:
       number: 0

All these config options are explained in-depth in the :doc:`servos: section </config/servos>`
of the config file reference.
