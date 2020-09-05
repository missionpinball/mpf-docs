How to create a multiball which uses multiple lock devices
==========================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/multiballs`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/multiball_locks`                                               |
+------------------------------------------------------------------------------+

Some machines have multiple locks and a multiball may use multiple source
devices to eject balls.
However, you have to unterstand that :doc:`/config/multiball_locks` and
:doc:`/config/multiballs` are independent.
A multiball can use one or multiple :doc:`ball device </config/ball_devices>`
as source devices to eject balls.
Locks will keep balls inside ball devices and request new balls to the
playfield.
To use multiple locks in one multiball you need to combine those:
Define locks to lock balls in your lock ball devices.
Additionally, define a multiball device with your lock ball devices as source.
Then, use the :doc:`/events/multiball_lock_multiball_lock_full` events to enable/start
your multiball mode.
When the multiball starts reset counters of your locks.

In the following example, you have to lock balls sequentially in your three
locks.
Every lock will enable the next lock using the
:doc:`/events/multiball_lock_multiball_lock_full` event.
The last lock will start the `multiball` mode.
If you hit `s_target1` the multiball will start which will reset and disable
all locks using the :doc:`/events/multiball_multiball_started` event.
After all the balls from the multiball drained all lock modes and the
multiball mode will stop using the :doc:`/events/multiball_multiball_ended` event.

.. code-block:: mpf-config

   coils:
     eject_coil1:
       number:
     eject_coil2:
       number:
     eject_coil3:
       number:
   switches:
     s_lock1:
       number:
     s_lock2:
       number:
     s_lock3:
       number:
     s_target1:
       number:
   ball_devices:
     bd_lock1:
       eject_coil: eject_coil1
       ball_switches: s_lock1
       eject_timeouts: 2s
     bd_lock2:
       eject_coil: eject_coil2
       ball_switches: s_lock2
       eject_timeouts: 2s
     bd_lock3:
       eject_coil: eject_coil3
       ball_switches: s_lock3
       eject_timeouts: 2s
   # mode lock1
   ##! mode: lock1
   mode:
     restart_on_next_ball: true
     stop_events: multiball_my_multiball_started
   multiball_locks:
     lock1:
       lock_devices: bd_lock1
       balls_to_lock: 1
       disable_events: mode_multiball_started
       reset_count_for_current_player_events: multiball_my_multiball_started
   # mode lock2
   ##! mode: lock2
   mode:
     restart_on_next_ball: true
     start_events: multiball_lock_lock1_full
     stop_events: multiball_my_multiball_started
   multiball_locks:
     lock2:
       lock_devices: bd_lock2
       balls_to_lock: 1
       disable_events: mode_multiball_started
       reset_count_for_current_player_events: multiball_my_multiball_started
   # mode lock3
   ##! mode: lock3
   mode:
     restart_on_next_ball: true
     start_events: multiball_lock_lock2_full
     stop_events: multiball_my_multiball_started
   multiball_locks:
     lock3:
       lock_devices: bd_lock3
       balls_to_lock: 1
       disable_events: mode_multiball_started
       reset_count_for_current_player_events: multiball_my_multiball_started
   # mode multiball
   ##! mode: multiball
   mode:
     start_events: multiball_lock_lock3_full
     stop_events: multiball_my_multiball_ended
   multiballs:
     my_multiball:
       ball_count: 4
       ball_count_type: total
       shoot_again: 2s
       start_events: s_target1_active
       ball_locks: bd_lock1, bd_lock2, bd_lock3
   ##! test
   #! start_game 5
   #! # there is one ball on playfield by default
   #! assert_balls_on_playfield 1
   #! assert_balls_in_play 1
   #! assert_int_condition 0 device.multiball_locks.lock1.locked_balls
   #! hit_switch s_lock1
   #! advance_time_and_run 3
   #! # it should not be locked
   #! assert_balls_on_playfield 1
   #! assert_balls_in_play 1
   #! assert_int_condition 0 device.multiball_locks.lock1.locked_balls
   #! start_mode lock1
   #! hit_switch s_lock1
   #! advance_time_and_run 3
   #! # it should not be locked
   #! assert_balls_on_playfield 1
   #! assert_balls_in_play 1
   #! assert_int_condition 1 device.multiball_locks.lock1.locked_balls
   #! hit_switch s_lock2
   #! advance_time_and_run 2
   #! hit_switch s_lock3
   #! advance_time_and_run 3
   #! assert_balls_on_playfield 1
   #! assert_balls_in_play 1
   #! assert_int_condition 1 device.multiball_locks.lock1.locked_balls
   #! assert_int_condition 1 device.multiball_locks.lock2.locked_balls
   #! assert_int_condition 1 device.multiball_locks.lock3.locked_balls
   #! hit_switch s_target1
   #! advance_time_and_run 3
   #! assert_balls_on_playfield 4
   #! assert_balls_in_play 4
   #! assert_int_condition 0 device.multiball_locks.lock1.locked_balls
   #! assert_int_condition 0 device.multiball_locks.lock2.locked_balls
   #! assert_int_condition 0 device.multiball_locks.lock3.locked_balls
   #! advance_time_and_run 3
   #! drain_one_ball
   #! drain_one_ball
   #! drain_one_ball
   #! assert_balls_on_playfield 1
   #! assert_balls_in_play 1
   #! assert_mode_not_running lock1
   #! assert_mode_not_running lock2
   #! assert_mode_not_running lock3
   #! assert_mode_not_running multiball

