Using dynamic runtime values in config files
============================================

MPF config files can contain values in the form of links to dynamic
placeholders which are evaluated live when MPF is running
rather than being hard-coded into a config file.

Dynamic values can come from several sources, including player variables,
machine variables, operator settings, properties of devices, etc. (Read
on for a full list.)

For example, you might want to have a shot called "jackpot" that scores
a multiplier which is the number of shots made times 100k points.

Without dynamic values, your variable_player (scoring) section would be static, like this:

.. code-block:: mpf-config

   ##! config: mode1
   variable_player:
      shot_jackpot_hit:
         score: 100000

But let's say you have a player variable called "troll_hits" which
holds the number of trolls hit that you want to multiply by 100,000
when the shot is made. You can use the "current_player" dynamic value
in your variable_player config like this:

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
      shot_jackpot_hit:
         score: current_player.troll_hits * 100000

You can access other values dynamically as well, such as a timer ticking away
a hurry-up or a counter to track how many times a multiplier switch has been hit

.. code-block:: mpf-config

   ##! mode: mode1
   variable_player:
      collect_hurryup:
         score: 1000 * device.timers.hurryup_clock.ticks_remaining * device.counters.hurryup_multiplier.value


Another example might be operator settings. Rather than hard coding
tilt warnings to 3, you might want to like the operator choose the
tilt warnings.

So instead of this:

.. code-block:: mpf-config

   tilt:
      warnings_to_tilt: 3

You would have this instead:

.. code-block:: mpf-config

   tilt:
      warnings_to_tilt: settings.tilt_warnings

(Note the example above requires that you have a ``settings:`` section
in your machine config and that you've defined a setting called
"tilt_warnings").

You can also use dynamic values in :doc:`conditional events </events/overview/conditional>`.

Types of dynamic values
-----------------------

current_player
   Used to get a player variable from the current player. The format is
   ``current_player.variable_name``, for example ``current_player.ball``.
   A list of player variables is here.

players
   Used to access player variables from specific players (by number), regardless
   of who the current player is.
   ``players[0].variable_name``

game
   game.tilted
   game.slam_tilted
   game.num_players
   game.balls_in_play


machine

   machine.game

settings

   todo

device

   Devices that have been registered with the machine can be found here, like logic blocks.
   ``device.counters.superjets_counter.value``
   ``device.accruals.magic_tokens.enabled``
   ``device.sequences.world_tour.completed``

Using if/else logic with dynamic values
---------------------------------------

.. code-block:: mpf-config

   ##! mode: mode1
   counters:
      my_counter:
         count_events: count_up
         count_complete_value: 5 if player.wizard_complete else 3
