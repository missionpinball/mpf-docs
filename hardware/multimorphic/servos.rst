Servos on a PD-LED (P-ROC/P3-ROC)
=================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/servos`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/pd_led_boards`                                                 |
+------------------------------------------------------------------------------+

Starting with PD-LED v3 you can configure up to twelve steppers on a PD-LED.

.. image:: /hardware/images/multimorphic_PD-LED.png

To enable servos you need to configure your PD-LED board in your ``p_roc``
section.
Assuming your PD-LED has the ID 4 you can use the following config to enable
all servos and and define two of them:

.. code-block:: mpf-config

   p_roc:
     pd_led_boards:
       4:
         use_servo_0: True
         use_servo_1: True
         use_servo_2: True
         use_servo_3: True
         use_servo_4: True
         use_servo_5: True
         use_servo_6: True
         use_servo_7: True
         use_servo_8: True
         use_servo_9: True
         use_servo_10: True
         use_servo_11: True

   servos:
      servos_4_0:
         number: 4-0
      servos_4_1:
         number: 4-1

The number of your servos has to be ``id_of_your_ped_led-number``.
In this case ``4-0`` and ``4-1`` for the first and second servo on PD-LED 4.
You will not be able to use LED 72 to LED 83 on the PD-LED when enabling all
servos.

You should hook up your servos to an external power source (usually 5V) and
not draw that power from the PD-LED.
However, make sure to connect the ground of your power supply.
See :doc:`/hardware/voltages_and_power/voltages_and_power` for details.
