MMA8451-based accelerometers
============================

This chips can be connected to I2C and act a tilt and leveler.
Available on adafruit (and others): https://learn.adafruit.com/adafruit-mma8451-accelerometer-breakout/overview

Configure using:

::

   hardware:
     accelerometers: mma8451

   accelerometers:
     my_accelerometer:
       level_x: 0
       level_y: 0
       level_z: 1
       number: 1-29


This will configure an MMA8451 on I2C bus 1 with address 0x1D (29 decimal which
is the default for this device).

:doc:`/about/help_us_to_write_it`
