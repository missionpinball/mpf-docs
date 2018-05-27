Skill Shot
==========

Types of skill shots:

   * Time based
   * Hit some target before another target
   * Super skill shot
   * How to create a lane-change skill shot

A simple skill shot mode:

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
       start_events: ball_started
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


+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+
