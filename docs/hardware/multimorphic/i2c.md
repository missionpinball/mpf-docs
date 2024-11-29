---
title: How to use I2C on the P3-ROC
---

# How to use I2C on the P3-ROC


Related Config File Sections:

* [hardware:](../../config/hardware.md)

The P3-ROC contains an I2C port (J17) which is accessible to MPF. You
can use this port to control any I2C-based device.

![image](/docs/hardware/images/multimorphic_p3_roc.png)

You need to connect SDA, SCL and ground. You may not need the 3.3V from
the P3-ROC as your controller might be a different voltage (which you
can then get directly from your power supply), but again that depends on
the board.

## I2C Servo Controller

For instance you can connect a
[servo controller via I2c](../i2c_servo.md). You can't plug the servo directly into the P3-ROC, rather,
you can buy an I2C-based servo controller and plug it into the P3-ROC.
However, a better option would be to use a
[servo on a PD-LED](servos.md).

See [I2C Platforms in MPF](../i2c_platforms.md) for other
I2C hardware in MPF.

## What if it did not work?

Have a look at our
[troubleshooting guide for the P/P3-Roc](../../troubleshooting/index.md).
