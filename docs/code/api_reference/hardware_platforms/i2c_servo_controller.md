
# self.machine.hardware_platforms[‘i2c_servo_controller’]

`class mpf.platforms.i2c_servo_controller.I2CServoControllerHardwarePlatform(machine)`

Bases: mpf.core.platform.ServoPlatform

Supports the PCA9685/PCA9635 chip via I2C.

## Accessing the i2c_servo_controller platform via code

Hardware platforms are stored in the self.machine.hardware_platforms dictionary, so the i2c_servo_controller platform is available via `self.machine.hardware_platforms['i2c_servo_controller']`.

## Methods & Attributes

The i2c_servo_controller platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_servo(number: str)`

Configure servo.

`initialize()`

Initialise platform.

`stop()`

Stop platform.

