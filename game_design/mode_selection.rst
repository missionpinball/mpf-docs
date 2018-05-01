Mode Selection
==============

In most machines there are multiple modes which can start but you need to shoot and/or select them first.
This usually serves multiple purposes:
First, it gives the player options and allows different play styles.
Second, it prevents all modes from starting at once.
We will create a selection/qualification mode which then starts a :doc:`game mode <game_mode>` (or sometimes two).
This selection mode usually runs all the time and provides the following functionality:

* Track whether a mode can be qualified/selected or not.
  Usually you cannot qualify for a mode while a game mode is running.
* When modes can be qualified:
   * Indicate the progress on qualification of modes
   * or: Indicate the current selection which would be started
* Start a mode and wait until it is done (no more selection/qualification possible in the meantime)
* Indicate which modes are already completed (often also active during game modes)

If you got multiple modes which can be selected AND started independently you probably need two selection modes
which run independently.

We assume that you already defined your :doc:`switches </config/switches>` of your shots.
Additionally, we assume that you defined :doc:`sequence_shots </config/sequence_shots>` in case your shots require
multiple shots to be hit in order.
You should be famililar with the events posted by a successful hit of your playfield shots (those do not have to be
defined as ``shots`` in your config).
Usually you will use either ``my_switch_active`` for a single switch called ``my_switch`` (e.g. a standup target) or
``my_sequence_shot_hit`` for a :doc:`sequence_shots </config/sequence_shots>` called ``my_sequence_shot``.


Common types of selection modes:

Select by hitting shot X times
------------------------------

A very common style to qualify and select modes is to light a few shots and once a player has made them a few times
start the mode which belongs to the shot.
This selection style is used in machines such as Stern Batman DK (2008) or Stern Starwars (2017).

This is an example:

.. code-block:: mpf-config

   ##! mode: left_ramp
   # mode: left_ramp
   mode:
     start_events: start_mode_left_ramp
     stop_events: stop_mode_left_ramp

   event_player:
     left_ramp_complete: stop_mode_left_ramp, enable_qualify

   ##! mode: right_ramp
   # mode: right_ramp
   mode:
     start_events: start_mode_right_ramp
     stop_events: stop_mode_right_ramp

   event_player:
     right_ramp_complete: stop_mode_right_ramp, enable_qualify

   ##! mode: qualify
   # mode: qualify
   mode:
     start_events: ball_started

   counters:
     left_ramp_qualify_counter:
       starting_count: 0
       count_complete_value: 3
       events_when_complete: disable_qualify, start_mode_left_ramp
       enable_events: enable_qualify
       disable_events: disable_qualify
       start_enabled: True
       persist_state: True
       reset_on_complete: False
       restart_events: reset_qualify_modes
       count_events: left_ramp_hit
     right_ramp_qualify_counter:
       starting_count: 0
       count_complete_value: 3
       events_when_complete: disable_qualify, start_mode_right_ramp
       enable_events: enable_qualify
       disable_events: disable_qualify
       start_enabled: True
       persist_state: True
       reset_on_complete: False
       restart_events: reset_qualify_modes
       count_events: right_ramp_hit

   ##! test
   # test this (don't copy this to your config)
   # start game hit both shots twice
   start_game
   post left_ramp_hit
   post left_ramp_hit
   post right_ramp_hit
   post right_ramp_hit

   # no game mode running yet
   assert_mode_not_running left_ramp
   assert_mode_not_running right_ramp

   # hit left ramp the third time. left ramp mode should start
   post left_ramp_hit
   assert_mode_running left_ramp
   assert_mode_not_running right_ramp

   # hitting the right ramp should not start the right ramp mode (since left ramp is runnin)
   post right_ramp_hit
   assert_mode_running left_ramp
   assert_mode_not_running right_ramp

   # assume that we completed left ramp mode
   post left_ramp_complete
   assert_mode_not_running left_ramp
   assert_mode_not_running right_ramp

   # hit the right ramp to start right ramp mode
   post right_ramp_hit
   assert_mode_not_running left_ramp
   assert_mode_running right_ramp


Select mode and start by shot
-----------------------------
