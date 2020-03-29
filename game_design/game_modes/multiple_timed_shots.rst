Lighting Multiple Timed Shots at the Same Time
----------------------------------------------

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/timed_switches`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/timers`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/event_player`                                                  |
+------------------------------------------------------------------------------+

In this mode you can active shots for 3s by hitting a target.
We assume that those shots post ``timerx_start``.
The mode succeeds when all three shots are active at the same time.
Every shot starts a timer and checks if the other two are running.

This is a basic example:

.. code-block:: mpf-config

   ##! mode: my_mode
   mode:
     start_events: start_my_mode
     stop_events: my_mode_succeeded
   timers:
     t1:
       start_value: 3
       end_value: 0
       direction: down
       control_events:
         - action: restart
           event: timer1_start
     t2:
       start_value: 3
       end_value: 0
       direction: down
       control_events:
         - action: restart
           event: timer2_start
     t3:
       start_value: 3
       end_value: 0
       direction: down
       control_events:
         - action: restart
           event: timer3_start
   event_player:
     timer_t1_started{device.timers.t2.running and device.timers.t3.running}: my_mode_succeeded
     timer_t2_started{device.timers.t1.running and device.timers.t3.running}: my_mode_succeeded
     timer_t3_started{device.timers.t1.running and device.timers.t2.running}: my_mode_succeeded
   ##! test
   #! start_game
   #! mock_event my_mode_succeeded
   #! post start_my_mode
   #! post timer1_start
   #! assert_mode_running my_mode
   #! assert_bool_condition True device.timers.t1.running
   #! advance_time_and_run 4
   #! assert_bool_condition False device.timers.t1.running
   #! post timer2_start
   #! post timer3_start
   #! advance_time_and_run 1
   #! assert_mode_running my_mode
   #! assert_bool_condition False device.timers.t1.running
   #! assert_bool_condition True device.timers.t2.running
   #! assert_bool_condition True device.timers.t3.running
   #! post timer1_start
   #! assert_mode_not_running my_mode
   #! assert_event_called my_mode_succeeded
