MMA8451-based accelerometers
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/accelerometers`                                                |
+------------------------------------------------------------------------------+

This chips can be connected to I2C and act a tilt and leveler.
Available on `adafruit <https://learn.adafruit.com/adafruit-mma8451-accelerometer-breakout/overview>`_ (and elsewhere).

Configure using:

.. code-block:: mpf-config

   hardware:
     accelerometers: mma8451
   accelerometers:
     my_accelerometer:
       level_x: 0
       level_y: 0
       level_z: 1
       number: 1-29

This will configure an MMA8451 on I2C bus 1 with address 0x1D (29 decimal which
is the default for this device). The exact numbering depends on your i2c platform.

.. image:: /hardware/images/mma8451-i2c-usb-accelerometer.jpg

The device in the picture is using :doc:`smbus on linux </hardware/smbus/index>` as i2c platform with
an Atiny85-based I2C-USB adapter.

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
