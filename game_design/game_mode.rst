Game Modes
==========

Make to Top Lanes Lit to Increase a Multiplier
----------------------------------------------

This example shows how to make a classic rule used in many games.  By making the three top lanes light (J, A, and M), the playfield multiplier is increased from 1X to 2X, 3X, 4X, 5X, and then to 10X.  The Right and Left Flipper buttons are used to control a lane change, and ending the ball resets the mode.

This example is based on Bally's Heavy Metal Meltdown.

Example:

.. code-block:: yaml

  mode:
    start_events: ball_starting
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

    JAM_lanes_comple:
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
