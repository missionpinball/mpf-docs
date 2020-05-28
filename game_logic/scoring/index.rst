Scoring
=======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/variable_player`                                               |
+------------------------------------------------------------------------------+

The variable_player is commonly used to score points for the current player when a certain event is posted.
This event could be a switch hit (i.e. for `s_your_switch` use the event `s_your_switch_active`).

.. code-block:: mpf-config

  ##! mode: mode1
  variable_player:
    s_your_switch_active:
      score: 100

Furthermore, you can add or set any other player or machine variable.
You can also use :doc:`dynamic values </config/instructions/dynamic_values>` here.

It is very common to use multipliers in your game for scoring.
The simplest way to implement multipliers is to use a
:doc:`player variable </player_vars/index>` to keep the multiplier and
multiply it to your scoring entries in :doc:`variable_player </config/variable_player>`.
This is an example for simple scoring with multiplier:

.. code-block:: mpf-config

   # set initial value for your multiplier player variable (to have it start
   # at 1 instead of 0)
   player_vars:
     multiplier:
       value_type: int
       initial_value: 1
   ##! mode: my_mode
   # in your mode:
   variable_player:
     increment_multiplier:
       multiplier: 1
     score_something:
       score: 100 * current_player.multiplier
   ##! test
   #! start_game
   #! assert_player_variable 1 multiplier
   #! start_mode my_mode
   #! post score_something
   #! assert_player_variable 100 score
   #! post increment_multiplier
   #! assert_player_variable 2 multiplier
   #! post score_something
   #! assert_player_variable 300 score

The multiplier will be tracked per player and carry over to the next ball.
At start we set it to ``1`` using a :doc:``player_vars </config/player_vars>``
entry in config for every player.

You can also reset the multiplier on every ball if you want:

.. code-block:: mpf-config

   ##! mode: my_mode
   # in your mode:
   variable_player:
     # set initial state on mode start of mode "my_mode"
     mode_my_mode_started:
       multiplier:
         int: 1
         action: set
     increment_multiplier:
       multiplier: 1
     score_something:
       score: 100 * current_player.multiplier
   ##! test
   #! start_game
   #! assert_player_variable 0 multiplier
   #! start_mode my_mode
   #! assert_player_variable 1 multiplier
   #! post score_something
   #! assert_player_variable 100 score
   #! post increment_multiplier
   #! assert_player_variable 2 multiplier
   #! post score_something
   #! assert_player_variable 300 score

Sometimes you want to increase your multipliers after multiple events were
posted. For instance, you might want to increase the multiplier after
the player completed two shot_groups:

.. code-block:: mpf-config

   # set initial value for your multiplier player variable (to have it start
   # at 1 instead of 0)
   player_vars:
     multiplier:
       value_type: int
       initial_value: 1
   ##! mode: my_mode
   # in your mode:
   accruals:
     bonus_multiplier:
       events:
         - robo_lanes_shots_lit_complete
         - tech_lanes_shots_lit_complete
       events_when_complete: increment_multiplier, light_bonus_2x_led
       start_enabled: true
   variable_player:
     increment_multiplier:
       multiplier: 1
     score_something:
       score: 100 * current_player.multiplier
   ##! test
   #! start_game
   #! assert_player_variable 1 multiplier
   #! start_mode my_mode
   #! post score_something
   #! assert_player_variable 100 score
   #! post robo_lanes_shots_lit_complete
   #! assert_player_variable 1 multiplier
   #! post tech_lanes_shots_lit_complete
   #! assert_player_variable 2 multiplier
   #! post score_something
   #! assert_player_variable 300 score

You can also combine two (or more) multipliers (see :doc:`dynamic values </config/instructions/dynamic_values>`
for details about other possible placeholders and math operators):

.. code-block:: mpf-config

   # set initial value for your multiplier player variables (to have it start
   # at 1 instead of 0)
   player_vars:
     multiplier:
       value_type: int
       initial_value: 1
     mode_multiplier:
       value_type: int
       initial_value: 1
   ##! mode: my_mode
   # in your mode:
   variable_player:
     increment_multiplier:
       multiplier: 1
     increment_mode_multiplier:
       mode_multiplier: 1
     score_something:
       score: 100 * current_player.multiplier * current_player.mode_multiplier
   ##! test
   #! start_game
   #! assert_player_variable 1 multiplier
   #! start_mode my_mode
   #! post score_something
   #! assert_player_variable 100 score
   #! post increment_multiplier
   #! assert_player_variable 2 multiplier
   #! assert_player_variable 1 mode_multiplier
   #! post score_something
   #! assert_player_variable 300 score
   #! post increment_mode_multiplier
   #! assert_player_variable 2 multiplier
   #! assert_player_variable 2 mode_multiplier
   #! post score_something
   #! assert_player_variable 700 score

You may also just add multipliers instead of multiply them.
For instance you could use: ``score: 100 * (1 + current_player.multiplier + current_player.mode_multiplier)``
and set ``initial_value: 0`` in ``player_vars:`` to have them start at 0.

Another option is to use a counter as multiplier using ``score: 100 * (device.counters.multiplier_counter.value + 1)``.
See :doc:`dynamic values </config/instructions/dynamic_values>` for details about possible placeholder.

Sometimes just using math is getting too complicated.
For instance, you want to have some special scoring under certain *conditions*.
In this case, it is sometimes better to use :doc:`conditional events </events/overview/conditional>`
instead of complicated math formulas in a variable_player.

In this example, we enable special scoring if the ``super_multiball`` mode is active and
the player made more than two loops (just for the sake of the example - you
could also move the scoring into super_multiball and remove the first
condition):

.. code-block:: mpf-config

   # set initial value for your multiplier player variables (to have it start
   # at 1 instead of 0)
   player_vars:
     multiplier:
       value_type: int
       initial_value: 1
     loops_made:
       value_type: int
       initial_value: 0
   ##! mode: super_extraball
   ##! mode: my_mode
   # in your mode:
   variable_player:
     made_loop:
       loops_made: 1
     score_something:
       score: 100 * current_player.multiplier
     score_something{mode.super_extraball.active and current_player.loops_made > 2}:
       score: 1000000
   ##! test
   #! start_game
   #! assert_player_variable 1 multiplier
   #! start_mode my_mode
   #! post score_something
   #! assert_player_variable 100 score
   #! post made_loop
   #! post made_loop
   #! assert_player_variable 2 loops_made
   #! post score_something
   #! assert_player_variable 200 score
   #! post made_loop
   #! assert_player_variable 3 loops_made
   #! post score_something
   #! assert_player_variable 300 score
   #! start_mode super_extraball
   #! post score_something
   #! assert_player_variable 1000400 score

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/game_logic/high_scores/index`                                         |
+------------------------------------------------------------------------------+
| :doc:`/game_logic/logic_blocks/scoring_based_on_logic_blocks`                |
+------------------------------------------------------------------------------+
| :doc:`/game_design/game_modes/top_lanes_with_multiplier`                     |
+------------------------------------------------------------------------------+
| :doc:`ss_style_score_queues`                                                 |
+------------------------------------------------------------------------------+

.. toctree::

   ss_style_score_queues
