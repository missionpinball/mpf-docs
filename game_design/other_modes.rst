Other Game Modes
================

There are a few very typical modes in almost all machines.
Those either run at start or all the time.


All the time/Before ball start
------------------------------

Those modes run all the time or before ball start.

Credits Mode
~~~~~~~~~~~~

Count coins and denies game start on insufficient credits.
See :doc:`/game_logic/credits/index` for details.

Attract Mode
~~~~~~~~~~~~

Attract mode stop on game start.
See :doc:`/game_logic/modes/attract`.

Tilt Mode
~~~~~~~~~

Tilt usually run the whole time.
It will end the game on tilt and might remove credits on slam tilt outside
of a game.
See :doc:`/game_logic/tilt/index` for details.

Service Mode
~~~~~~~~~~~~

See :doc:`/game_logic/service_mode/index` for details.

Ball start
----------

Those modes typically run on/after ball start and then stop.

Skill shot mode
---------------

Skill shots typically run on ball start only.
See :doc:`/game_logic/skill_shot/index`.

Mode selection
--------------

Mode selection sometimes delays ball start.
Usually, at least the mode selection mode starts on ball start.
See :doc:`mode_selection`.

During the game
---------------

Those modes typicalls run during the whole game.

Lanes Modes
~~~~~~~~~~~

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
       shot_lanes_lit_complete:
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

Ball End Modes
--------------

See :doc:`ball_end_modes`.


Game End Modes
--------------

See :doc:`game_end_modes`.
