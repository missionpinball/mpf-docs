How to configure servos (P3-ROC)
================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+

The P3-ROC contains an I2C port (J17) which is accessible to MPF. You can use
this port to control an I2C-based servo. (You can't plug the servo directly
into the P3-ROC, rather, you can buy an I2C-based servo controller and plug it
into the P3-ROC.)

See the :doc:`/hardware/i2c_servo/index` documentation for details on how to
configure this.

If you want to use this with a P3-ROC, you can configure it in your machine
config it similar to this:

::

   hardware:
       driverboards: pdb
       platform: p3_roc
       servo_controllers: i2c_servo_controller

   servo_controller:
       address: 0x40

   servos:
       servo1:
           number: 3

The address and number of your servo and servo controller can be found in the
documentation of your controller.
