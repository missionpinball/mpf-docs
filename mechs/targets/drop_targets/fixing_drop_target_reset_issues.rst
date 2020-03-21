Fixing Drop Target Reset Issues
===============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/drop_targets`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/drop_target_banks`                                             |
+------------------------------------------------------------------------------+
| :doc:`/config/psus`                                                          |
+------------------------------------------------------------------------------+

.. contents::
   :local:


Sometimes your drop targets or drop target banks will not reset reliably.
This often has mechanical reasons but it could be also caused by a stressed
power supply or bad electrical wiring.
Try to rule those out or fix them first.
However, you still might have issues afterwards and we can ease them a bit
in software.

Configuring PSU Magic
---------------------

Behind the scenes MPF performs
:doc:`some magic for you to prevent stress on your power supply unit </hardware/voltages_and_power/power_management>`.
The default should be fine for most machine but if your PSU is very weak try
this config:




Configuring Pulse Times
-----------------------

Increasing the pulse time on your reset coil should help with reliably
resetting your drop target or drop target bank.
However, it will also cause mechanical stress, heats up your reset coil and
might draw a lot of power out of your power supply.

One solution to this is to lower ``default_pulse_power`` to something between
``.5`` and ``.8``.
Your hardware will PWM the pulse and you can use much longer pulse times
without too much stress on your hardware.
Also reduces the sound caused by the reset.

You can try something like this:



Resetting a Drop Target Multiple Times
--------------------------------------

If all the above does not help and you got an old mech which somehow does not
like to snap in place all the time you can also try to trigger the reset
multiple times.
MPF will not reset drop targets or drop target banks if they are already
completely up so this should not cause too much stress.

The following example will try to reset your drop target bank up to three
times on ball start:

.. code-block:: mpf-config

   #! switches:
   #!   s_drop_front:
   #!     number:
   #!   s_drop_middle:
   #!     number:
   #!   s_drop_back:
   #!     number:
   #! coils:
   #!   c_drop_reset:
   #!     number:
   drop_targets:
     front:
       switch: s_drop_front
     middle:
       switch: s_drop_middle
     back:
       switch: s_drop_back
   drop_target_banks:
     vuk_bank:
       drop_targets: front, middle, back
       reset_coils: c_drop_reset
       reset_on_complete: 1s
       reset_events:
         ball_started.1: 0
         ball_started.2: 1s
         ball_started.3: 2s
         machine_reset_phase_3: 0
   ##! test
   #! start_game
   #! advance_time_and_run 1
