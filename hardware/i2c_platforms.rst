I2C Platforms in MPF
====================

The following platforms allow controlling I2C devices in MPF:

* :doc:`Linux Nativ I2C <smbus/index>` - If your linux PC has a driver for the I2C interface it will work in MPF
* :doc:`P3-Roc <multimorphic/index>` (but not the P-Roc)
* :doc:`Raspberry Pi <rpi/index>` - Remote via network or locally using pigpio

The following platforms need to be interfaced by one of the above platforms:
* :doc:`PCA9685/PCA9635 I2C Servo Controllers </hardware/i2c_servo/index>`
* :doc:`MMA8451 Accelerometers </hardware/mma8451/index>`
