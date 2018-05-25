Other Game Modes
================

There are a few very typical modes in almost all machines.
Those either run at start or all the time.

Skill shot mode
---------------

See :doc:`/game_logic/skill_shot/index`.

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
       start_events: ball_started
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
