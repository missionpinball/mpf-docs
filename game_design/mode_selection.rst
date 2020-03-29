Mode Selection
==============

In most machines there are multiple modes which can start but you need to shoot and/or select them first.
This usually serves multiple purposes:
First, it gives the player options and allows different play styles.
Second, it prevents all modes from starting at once.
We will create a selection/qualification mode which then starts a :doc:`game mode <game_modes/index>` (or sometimes two).
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

There are generally two types of mode selection:

* Selection by making a shot. This ususally happens during the game.
* Selection using flipper/action/start buttons after hitting a scoop or on ball start.
  In those cases you have to delay the eject of the ball (see below for an example how to do that).

Please let us know if you got a snippet which might be useful for other users and is missing here.
We would be very happy to :doc:`include it </about/help_us_to_write_it>`.

Common types of selection modes:

Skill shot at ball start
------------------------

Skill shots typically run on ball start only.
See :doc:`/game_logic/skill_shot/index`.


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
       start_enabled: true
       persist_state: true
       reset_on_complete: false
       restart_events: reset_qualify_modes
       count_events: left_ramp_hit
     right_ramp_qualify_counter:
       starting_count: 0
       count_complete_value: 3
       events_when_complete: disable_qualify, start_mode_right_ramp
       enable_events: enable_qualify
       disable_events: disable_qualify
       start_enabled: true
       persist_state: true
       reset_on_complete: false
       restart_events: reset_qualify_modes
       count_events: right_ramp_hit
   ##! test
   #! # start game hit both shots twice
   #! start_game
   #! post left_ramp_hit
   #! post left_ramp_hit
   #! post right_ramp_hit
   #! post right_ramp_hit
   #! # no game mode running yet
   #! assert_mode_not_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # hit left ramp the third time. left ramp mode should start
   #! post left_ramp_hit
   #! assert_mode_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # hitting the right ramp should not start the right ramp mode (since left ramp is runnin)
   #! post right_ramp_hit
   #! assert_mode_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # assume that we completed left ramp mode
   #! post left_ramp_complete
   #! assert_mode_not_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # hit the right ramp to start right ramp mode
   #! post right_ramp_hit
   #! assert_mode_not_running left_ramp
   #! assert_mode_running right_ramp

This very basic example should be sufficient for a lot of machines.
Another option here is to add achievments and have those enable/disable the counters.
The advantage of that is that you can use :doc:`/config/achievement_groups` to track
completion of combinations modes (e.g. completions of rows in Stern Starwars).
You can also do that with :doc:`condition events </events/overview/conditional>`
or :doc:`/config/accruals`.

You probably want to :doc:`integrate shows with the logic blocks </game_logic/logic_blocks/integrating_logic_blocks_and_shows>` next.


Select mode and start by shot
-----------------------------

There are multiple options to implement a selection carousel.

Using a carousel
~~~~~~~~~~~~~~~~

One way to achieve mode selection you use a carousel mode which looks like this:

.. code-block:: mpf-config

   ##! mode: carousel
   #config_version=5
   mode:
     start_events: start_selection_mode
     stop_events: carousel_item_selected
     code: mpf.modes.carousel.code.carousel.Carousel
   mode_settings:
     selectable_items: character1, character2, character3
     select_item_events: s_start_active
     next_item_events: s_left_flipper_active
     previous_item_events: s_right_flipper_active
   # TODO: add some slides. If you have a nice example please send it to us (or create a PR).
   variable_player:
     carousel_character1_selected:
       selected_character:
         string: "character1"
     carousel_character2_selected:
       selected_character:
         string: "character2"
     carousel_character3_selected:
       selected_character:
         string: "character3"

A carousel will not currently track which modes are already completed.
Also this in this example the carousel will stop after a selection was made.
Therefore, we advise to create a second mode to track the progress of your modes.

This might be useful for cases where you want to select characters or general awards which
then might influence how fast your modes start.
For instance this might be combined with the example above by influencing the
`starting_count:` or `count_complete_value` using conditional events:

.. code-block:: mpf-config

   ##! mode: qualify
   counters:
     left_ramp_qualify_counter:
       starting_count: 2 if current_player.selected_character == "character1" else 0
       count_complete_value: 3
       count_events: left_ramp_hit

Using Achivement Groups
~~~~~~~~~~~~~~~~~~~~~~~

You can define multiple :doc:`groups </config/achievement_groups>` of
:doc:`achievements </config/achievements>` and rotate them:

.. code-block:: mpf-config

   #! lights:
   #!   l_left_ramp:
   #!     number:
   #!   l_right_ramp:
   #!     number:
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
   achievements:
     left_ramp:
   #!     select_events: select_first
       show_tokens:
         leds: l_left_ramp
       show_when_enabled: off
       show_when_selected: flash
       show_when_completed: on
       complete_events: stop_mode_left_ramp
       events_when_started: start_mode_left_ramp
     right_ramp:
       show_tokens:
         leds: l_right_ramp
       show_when_enabled: off
       show_when_selected: flash
       show_when_completed: off
       complete_events: stop_mode_right_ramp
       events_when_started: start_mode_right_ramp
   achievement_groups:
     all_achievements:
       achievements: left_ramp, right_ramp
       auto_select: true
       start_selected_events: hit_scoop
       rotate_right_events: s_action_button_active
       enable_events: enable_qualify, ball_started
       debug: true
   #! ##! test
   #! start_game
   #! post select_first
   #! assert_mode_running qualify
   #! assert_mode_not_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # select first mode
   #! post hit_scoop
   #! assert_mode_running qualify
   #! assert_mode_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # end mode
   #! post left_ramp_complete
   #! assert_mode_running qualify
   #! assert_mode_not_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # start the remaining one
   #! post hit_scoop
   #! assert_mode_running qualify
   #! assert_mode_running right_ramp
   #! assert_mode_not_running left_ramp
   #! stop_game
   #! # another try
   #! start_game
   #! post select_first
   #! assert_mode_running qualify
   #! assert_mode_not_running left_ramp
   #! assert_mode_not_running right_ramp
   #! # rotate
   #! post s_action_button_active
   #! advance_time_and_run 1
   #! # and start
   #! post hit_scoop
   #! assert_mode_running qualify
   #! assert_mode_not_running left_ramp
   #! assert_mode_running right_ramp

This is a very flexible way to achieve this.


Select a mode at the start of ball 1
------------------------------------

Use this to delay the start of a player's first ball until they select a mode:

.. code-block:: mpf-config

   ##! mode: start_selecton_on_ball_one
   #config_version=5
   mode:
     start_events: ball_ended
     stop_events: ball_started
     priority: 100
     game_mode: false   # this is needed to interfere with game start
   queue_relay_player:
     player_turn_starting{player.ball==0}:
       post: show_mode_selection       # use this event to enable selection
       wait_for: selection_mode_ended  # make sure you post this event is posted when a selection was made

You can replace ``player_turn_starting{player.ball==0}`` with just ``player_turn_starting`` to have the selection
on every ball (but not on extra balls). If you also want to trigger it on extra balls use
``ball_starting``.

Using the start button to select modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normally, pressing the start button will cause MPF to add another player.
To suppress this during mode selection you can do the following:

.. code-block:: mpf-config

   # Add the following to the game section of your machine's config.yaml
   # This will disable the start button for adding players
   game:
     add_player_switch_tag: add_player
   ##! mode: attract
   # Add this to your attract.yaml
   event_player:
     s_start_active: sw_add_player
   ##! mode: game_running
   # Have something in your base mode to trigger another mode (e.g. the carousel above)
   # and in that mode have the following (to reenable the start button):
   event_player:
     s_start_active: sw_add_player
   #! ##! test
   #! start_game
   #! assert_player_count 1
   #! hit_and_release_switch s_start
   #! assert_player_count 1
   #! start_mode game_running
   #! hit_and_release_switch s_start
   #! assert_player_count 2

