How to use I2C on the P3-ROC
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+

The P3-ROC contains an I2C port (J17) which is accessible to MPF. You can use
this port to control any I2C-based device.

.. image:: /hardware/images/multimorphic_p3_roc.png

You need to connect SDA, SCL and ground. You may not need the 3.3V from the
P3-ROC as your controller might be a different voltage (which you can then
get directly from your power supply), but again that depends on the board.


I2C Servo Controller
--------------------

For instance you can connect a :doc:`servo controller via I2c </hardware/i2c_servo/index>`.
You can't plug the servo directly into the P3-ROC, rather, you can buy an
I2C-based servo controller and plug it into the P3-ROC.
However, a better option would be to use a :doc:`servo on a PD-LED <servos>`.

See :doc:`/hardware/i2c_platforms` for other I2C hardware in MPF.

What if it did not work?
------------------------

Have a look at our
:doc:`troubleshooting guide for the P/P3-Roc <troubleshooting>`.
