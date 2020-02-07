Servos
======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+

.. image:: /mechs/images/servos.jpg

A servo is device which can move to a certain position based on internal
feedback.
There is no need to add position switches and the servo will hold its position
even if something pushes it aside.
On the downside, there is no way to tell when the servo reached its position
since it will not provide any position feedback to the software side.

This is an example:

.. code-block:: mpf-config

   servos:
     servo1:
       servo_min: 0.1
       servo_max: 0.9
       positions:
         0.0: servo1_down
         0.8: servo1_up
       reset_position: 0.5
       reset_events: reset_servo1
       number: 1
     servo2:
       positions:
         0.2: servo2_left
         1.0: servo2_home
       reset_position: 1.0
       reset_events: reset_servo2
       number: 2

.. contents::
   :local:

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for servos is ``device.servos.<name>``.

*position*
   Value, stored in memory of what servo position should be, on a scale from 0.0 to 1.0.

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`servo_sequence`                                                        |
+------------------------------------------------------------------------------+


Related Events
--------------

None

.. toctree::
   :titlesonly:

   servo_sequence
