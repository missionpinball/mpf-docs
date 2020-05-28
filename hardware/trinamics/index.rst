Trinamic's StepRocker
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/trinamics_steprocker`                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/steppers`                                                      |
+------------------------------------------------------------------------------+

Connect the StepRocker to USB and MPF can control any steppers connected to it.

:doc:`TODO: Add a picture of a StepRocker </about/help_us_to_write_it>`

This is an example:

.. code-block:: mpf-config

   hardware:
     platform: virtual
     stepper_controllers: trinamics_steprocker

   trinamics_steprocker:
     port: /dev/ttyACM0

   steppers:
       # Scenario: 1.8 degree stepper attached to a 7:1 gear ratio with homing flag that you want to control in units of revolutions
     positionStepper:
       number: 0
       homing_direction: clockwise        # when facing the shaft
       homing_mode: hardware
       reset_position: 0
       reset_events: test_reset
       named_positions:
         0.0: test_00
         0.6: test_01
         1.0: test_10
       platform_settings:
         move_current: 25                      # percent
         hold_current: 5                       # percent
         homing_speed: 0.1                     # user units/sec
         microstep_per_fullstep: 16            # 1/16 mode (1 step = 1/16 of a full step)
         fullstep_per_userunit: 1400           # UU=1 Revolution = 200 full steps per rev (1.8 deg stepper) * 7 gear ratio
         velocity_limit: 0.5                   # user units/sec   (so, 0.8 RPS of output gear )
         acceleration_limit: 2.0               # user units/sec^2  (so, 2 RPS^S of output gear)

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
