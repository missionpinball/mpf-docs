Steppers on a PD-LED (P-ROC/P3-ROC)
===================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/steppers`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/pd_led_boards`                                                 |
+------------------------------------------------------------------------------+

Starting with PD-LED v3 you can configure up to two steppers on a PD-LED.
You need an additional cheap external stepper driver to drive the load of the
stepper.
Those are sold for a few bucks as StepStick or DRV8825 on amazon, ebay,
aliexpress or similar platforms.

.. image:: /hardware/images/multimorphic_PD-LED.png

To enable steppers you need to configure your PD-LED board in your ``p_roc``
section.
Assuming your PD-LED has the ID 4 you can use the following config to enable
and define two steppers:

.. code-block:: mpf-config

   p_roc:
     pd_led_boards:
       4:
         use_stepper_0: true
         use_stepper_1: true
         # stepper_speed: 13524    # uncomment to tune the speed
   switches:
     s_stepper_4_0_home:
       number: A4-B0-0
     s_stepper_4_1_home:
       number: A4-B0-1
   steppers:
     stepper_4_0:
       number: 4-0
       homing_mode: switch
       homing_switch: s_stepper_4_0_home
     stepper_4_1:
       number: 4-1
       homing_mode: switch
       homing_switch: s_stepper_4_1_home

The number of your stepper has to be ``id_of_your_ped_led-number``.
In this case ``4-0`` and ``4-1`` for the first and second stepper on PD-LED 4.
Every stepper needs a homing switch so MPF can home it at startup.
You will not be able to use LED 75 to LED 80 on the PD-LED when enabling both
steppers.

You might have to fine-tune the ``stepper_speed`` setting to your steppers.
Increasing the value will reduce the speed of your steppers.

You should hook up your steppers to an external power source and
not draw that power from the PD-LED.
However, make sure to connect the ground of your power supply.
See :doc:`/hardware/voltages_and_power/voltages_and_power` for details.
Connect those stepper drivers as described in
:doc:`/hardware/stepstick/index` (but use the PD-LED outputs).

What if it did not work?
------------------------

Have a look at our
:doc:`troubleshooting guide for the P/P3-Roc <troubleshooting>`.
