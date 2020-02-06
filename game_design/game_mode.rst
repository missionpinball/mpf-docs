Game Modes
==========

Weak Flipper Modes
------------------

See: :doc:`/mechs/flippers/weak_flippers`.

Lighting Multiple Timed Shots at the Same Time
----------------------------------------------

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

Light All Top Lanes to Increase Multiplier
------------------------------------------

This example shows how to make a classic rule used in many games.
By making the three top lanes light (J, A, and M), the playfield multiplier
is increased from 1X to 2X, 3X, 4X, 5X, and then to 10X.
The Right and Left Flipper buttons are used to control a lane change,
and ending the ball resets the mode.
This example is based on Bally's Heavy Metal Meltdown.  The example below creates a new mode called JAM_rollover, and uses a machine-wide player variable named pf_multiplier.  This variable is what can be used in other parts of the game logic to multiply values based on the current multiplier value, for example, when calculating end of ball bonuses.  The counter value lb_JAM_complete_count is used as the count value in the JAM_lanes_done{count==2} within the variable_player conditional event statements.

.. code-block:: mpf-config

  # in your machine config
  #! switches:
  #!   s_top_lane_J:
  #!     number:
  #!   s_top_lane_A:
  #!     number:
  #!   s_top_lane_M:
  #!     number:
  #! lights:
  #!   l_jam_J:
  #!     number:
  #!   l_jam_A:
  #!     number:
  #!   l_jam_M:
  #!     number:
  #!   JAM_lanes:
  #!     number:
  #!   Playfield_2X:
  #!     number:
  #!   Playfield_3X:
  #!     number:
  #!   Playfield_4X:
  #!     number:
  #!   Playfield_5X:
  #!     number:
  #!   Playfield_10X:
  #!     number:
  #! shows:
  #!   Playfield_2x_on:
  #!     - duration: 1
  #!   Playfield_3x_on:
  #!     - duration: 1
  #!   Playfield_4x_on:
  #!     - duration: 1
  #!   Playfield_5x_on:
  #!     - duration: 1
  #!   Playfield_10x_on:
  #!     - duration: 1
  ##! mode: JAM_rollover
  # in modes/JAM_rollover
  mode:
    start_events: ball_started
    priority: 110
  counters:
    lb_JAM_complete_count:
      count_events: JAM_lanes_complete
      events_when_hit: JAM_lanes_done
      starting_count: 1
      direction: up
      persist_state: false
  shots:
    top_lane_J:
      switch: s_top_lane_J
      show_tokens:
        light: l_jam_J
    top_lane_A:
      switch: s_top_lane_A
      show_tokens:
        light: l_jam_A
    top_lane_M:
      switch: s_top_lane_M
      show_tokens:
        light: l_jam_M
  shot_groups:
    JAM_lanes:
      shots: top_lane_J, top_lane_A, top_lane_M
      rotate_left_events: s_left_flipper_active
      rotate_right_events: s_right_flipper_active
      reset_events:
        JAM_lanes_lit_complete: 1s
  variable_player:
    mode_JAM_rollover_started:
      pf_multiplier:
        int: 1
        action: set
    JAM_lanes_done{count==2}:
      pf_multiplier:
        int: 2
        action: set
    JAM_lanes_done{count==3}:
      pf_multiplier:
        int: 3
        action: set
    JAM_lanes_done{count==4}:
      pf_multiplier:
        int: 4
        action: set
    JAM_lanes_done{count==5}:
      pf_multiplier:
        int: 5
        action: set
    JAM_lanes_done{count==6}:
      pf_multiplier:
        int: 10
        action: set
    JAM_lanes_complete:
      score: 1000 * current_player.pf_multiplier
  show_player:
    JAM_lanes_lit_complete:
      flash:
        loops: 4
        speed: 4
        show_tokens:
          lights: JAM_lanes
    JAM_lanes_done{count==2}:
      Playfield_2x_on:
        show_tokens:
          lights: Playfield_2X
    JAM_lanes_done{count==3}:
      Playfield_3x_on:
        show_tokens:
          lights: Playfield_2X, Playfield_3X
    JAM_lanes_done{count==4}:
      Playfield_4x_on:
        show_tokens:
          lights: Playfield_2X, Playfield_3X, Playfield_4X
    JAM_lanes_done{count==5}:
      Playfield_5x_on:
        show_tokens:
          lights: Playfield_2X, Playfield_3X, Playfield_4X, Playfield_5X
    JAM_lanes_done{count>=6}:
      Playfield_10x_on:
        show_tokens:
          lights: Playfield_2X, Playfield_3X, Playfield_4X, Playfield_5X, Playfield_10X
  ##! test
  #! start_game
  #! assert_player_variable 1 pf_multiplier
  #! hit_and_release_switch s_top_lane_J
  #! hit_and_release_switch s_top_lane_A
  #! hit_and_release_switch s_top_lane_M
  #! assert_player_variable 2 pf_multiplier
  #! advance_time_and_run 2
  #! hit_and_release_switch s_top_lane_J
  #! hit_and_release_switch s_top_lane_A
  #! hit_and_release_switch s_top_lane_M
  #! assert_player_variable 3 pf_multiplier
  #! advance_time_and_run 2
  #! drain_all_balls
  #! advance_time_and_run 2
  #! assert_player_variable 1 pf_multiplier
  #! hit_and_release_switch s_top_lane_J
  #! hit_and_release_switch s_top_lane_A
  #! hit_and_release_switch s_top_lane_M
  #! assert_player_variable 2 pf_multiplier

Delay Ball Start/Stop to Show Slides/Sounds
-------------------------------------------

See :doc:`/game_logic/ball_start_end/index`.
