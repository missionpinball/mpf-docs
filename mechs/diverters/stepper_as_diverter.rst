Using a Stepper as Diverter
===========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/diverters`                                                     |
+------------------------------------------------------------------------------+
| :doc:`/config/steppers`                                                      |
+------------------------------------------------------------------------------+


You can use a stepper as a diverter by tying it into a diverter using events.
Specifically, we are using :doc:`/events/diverter_diverter_deactivating` and
:doc:`/events/diverter_diverter_activating`.
This is an example:

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #!   s_ball2:
   #!     number:
   #! coils:
   #!   c_eject1:
   #!     number:
   #!   c_eject2:
   #!     number:
   #! ball_devices:
   #!   bd_trough:
   #!     eject_coil: c_eject1
   #!     ball_switches: s_ball1
   #!   bd_target:
   #!     eject_coil: c_eject2
   #!     ball_switches: s_ball2
   diverters:
     d_diverter:
       debug: true
       feeder_devices: bd_trough
       targets_when_active: playfield
       targets_when_inactive: bd_target
   steppers:
     s_diverter:
       number:
       named_positions:
         20: diverter_d_diverter_activating
         400: diverter_d_diverter_deactivating

This diverter will not wait for the stepper to reach the position.
If you need that let us know in the forum.
