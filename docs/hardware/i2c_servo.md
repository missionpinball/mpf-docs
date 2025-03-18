---
title: I2C Servo Controllers
---

# I2C Servo Controllers


Related Config File Sections:

* [hardware:](../config/hardware.md)
* [servo_controllers:](../config/servo_controllers.md)
* [servos:](../config/servos.md)

MPF currently supports PCA9685/PCA9635 based servo controllers via I2C.
One example for such a controller is the [Adafruit 16-Channel 12-bit
PWM/Servo Driver](https://www.adafruit.com/product/815). You can use any
I2C platform supported by MPF (see
[I2C Platforms in MPF](i2c_platforms.md)).

Overview video about [servos](../mechs/servos/index.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wA6KEODwQ5w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wA6KEODwQ5w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 1. Installing I2C Servo Controllers

Connect the controller to the I2C port and add the following config
section:

``` yaml
hardware:
  servo_controllers: i2c_servo_controller
```

0x40 is actually the default I2C address for this chip but it might be
different for some chips.

## 2. Add your servos

Add your servos to config:

``` yaml
servos:
  servo1:
    number: 0  # first servo on controller
```

All these config options are explained in-depth in the
[servos: section](../config/servos.md) of the
config file reference.

You can also provide an I2C address per servo:

``` yaml
servos:
  servo_on_controller_63_0:
    number: 63-0  # first servo on board with ID 0x3F / 63
  servo_on_controller_63_1:
    number: 63-1  # second servo on board with ID 0x3F / 63
```

## What if it did not work?

Have a look at our [hardware troubleshooting guide](troubleshooting_hardware/index.md).
