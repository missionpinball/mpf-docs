Other Game Modes
================

There are a few very typical modes in almost all machines.
Those either run at start or all the time.

Skill shot mode
---------------

A simple skill shot mode

.. code-block:: mpf-config

   #! switches:
   #!     s_lane_l:
   #!         number:
   #!     s_lane_m:
   #!         number:
   #!     s_lane_r:
   #!         number:
   #! lights:
   #!     l_lane_l:
   #!         number:
   #!     l_lane_m:
   #!         number:
   #!     l_lane_r:
   #!         number:
   ##! mode: skill_shot
   mode:
       start_events: ball_starting
       stop_events:
           - skill_success
           - skill_failed
           - sw_playfield_active
       priority: 500

   shots:
       skill_l:
           switch: s_lane_l
           advance_events: mode_skill_shot_started
           show_tokens:
               light: l_lane_l
       skill_m:
           switch: s_lane_m
           show_tokens:
               light: l_lane_m
       skill_r:
           switch: s_lane_r
           show_tokens:
               light: l_lane_r

   shot_groups:
       skill_shot:
           shots: skill_l, skill_m, skill_r
           rotate_left_events: s_left_flipper_active
           rotate_right_events: s_right_flipper_active

   variable_player:
       skill_success:
           score: 42

   event_player:
      skill_l_lit_hit: skill_success
      skill_m_lit_hit: skill_success
      skill_r_lit_hit: skill_success
      skill_l_unlit_hit: skill_failed
      skill_m_unlit_hit: skill_failed
      skill_r_unlit_hit: skill_failed
   ##! test
   #! # failure
   #! start_game
   #! assert_mode_running skill_shot
   #! hit_and_release_switch s_lane_l
   #! assert_mode_not_running skill_shot
   #! assert_player_variable 42 score
   #! stop_game
   #! # success
   #! start_game
   #! assert_mode_running skill_shot
   #! hit_and_release_switch s_lane_m
   #! assert_mode_not_running skill_shot
   #! assert_player_variable 0 score
   #! stop_game
   #! # move + success
   #! start_game
   #! assert_mode_running skill_shot
   #! post s_right_flipper_active
   #! hit_and_release_switch s_lane_m
   #! assert_mode_not_running skill_shot
   #! assert_player_variable 42 score
   #! stop_game

Lanes Modes
-----------

Most machines award multipliers or small bonuses when completing all lanes during the game.
Those are usually the four to five inlanes and outlane or the three skillshot lanes.

This is an example:

.. code-block:: mpf-config

   #! switches:
   #!     s_lane_l:
   #!         number:
   #!     s_lane_m:
   #!         number:
   #!     s_lane_r:
   #!         number:
   #! lights:
   #!     l_lane_l:
   #!         number:
   #!     l_lane_m:
   #!         number:
   #!     l_lane_r:
   #!         number:
   ##! mode: lanes
   #config_version=5

   mode:
       start_events: ball_starting
       priority: 110

   variable_player:
       lanes_hit:
           score: 50
       lanes_lit_complete:
           score: 300

   shots:
       lane_l:
           switch: s_lane_l
           show_tokens:
               light: l_lane_l
       lane_m:
           switch: s_lane_m
           show_tokens:
               light: l_lane_m
       lane_r:
           switch: s_lane_r
           show_tokens:
               light: l_lane_r

   shot_groups:
       lanes:
           shots: lane_l, lane_m, lane_r
           rotate_left_events: s_left_flipper_active
           rotate_right_events: s_right_flipper_active
           reset_events:
               lanes_lit_complete: 1s

   show_player:
       hot_lanes_lit_complete:
           flash:
               loops: 4
               speed: 4
               show_tokens:
                   lights: lanes

   ##! test
   #! start_game
   #! assert_mode_running lanes
   #! hit_and_release_switch s_lane_l
   #! assert_player_variable 50 score
   #! hit_and_release_switch s_lane_m
   #! assert_player_variable 100 score
   #! post s_left_flipper_active
   #! hit_and_release_switch s_lane_m
   #! assert_player_variable 450 score
   #! advance_time_and_run 2
   #! hit_and_release_switch s_lane_l
   #! hit_and_release_switch s_lane_m
   #! hit_and_release_switch s_lane_r
   #! assert_player_variable 900 score
