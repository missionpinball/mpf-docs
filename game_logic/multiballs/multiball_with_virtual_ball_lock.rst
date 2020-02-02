How to create a multiball with a virtual ball lock
==================================================

If your machine does not have a physical ball lock you can use a counter to
count how many times a ball has been "locked".
This could be a ball device (as in the example) or any normal shot.

This is an example:

.. code-block:: mpf-config

   switches:
       s_middle_ramp:
           number:

   coils:
       c_plunger:
           number:

   ball_devices:
       bd_middle_ramp_ball_lock:
           eject_coil: c_plunger
           ball_switches: s_middle_ramp

   ##! mode: mb_mode
   multiballs:
       3balls_multiball:
           ball_count: 3
           ball_count_type: total
           shoot_again: 30s
           start_events: logicblock_mb_counter_complete

   counters:
      mb_counter:
         count_events: balldevice_bd_middle_ramp_ball_lock_ball_entered
         count_complete_value: 3

   ##! test
   #! start_game
   #! start_mode mb_mode
   #! hit_switch s_middle_ramp
   #! advance_time_and_run 15
   #! hit_switch s_middle_ramp
   #! advance_time_and_run 15
   #! hit_switch s_middle_ramp
   #! advance_time_and_run 15
   #! assert_balls_in_play 3
