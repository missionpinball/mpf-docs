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

You can use the following types of placeholders.


Current Player Variables
~~~~~~~~~~~~~~~~~~~~~~~~

You can access a player variable ``X`` of the current player using
``current_player.X``.
For instance, ``current_player.my_player_var`` will access ``my_player_var``
of the current player.
This placeholder is only available when a game is active.

Common player variables are:

* ``current_player.score`` - Score of the current player
* ``current_player.ball`` - Current ball

Player Variables of Specific Player
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access a player variable ``X`` of a specific player ``P`` using
``players[X].P``.
``X`` starts at 0. So player 1 will be ``players[0].P``.
For instance, ``players[1].my_player_var`` will access ``my_player_var``
for player 2. ``players[0].my_player_var`` will access player 1.
This placeholder is only available when a game is active.

Common player variables are:

* ``players[0].score`` - Score of player 1
* ``players[1].score`` - Score of player 2
* ``players[2].score`` - Score of player 3
* ``players[3].score`` - Score of player 4

Game Variables
~~~~~~~~~~~~~~

You can access game variable ``X`` using ``game.X``.
This placeholder is only available when a game is active.

Common game variables are:

* ``game.max_players`` - Maximum players currently allowed
* ``game.num_players`` - Number of players in game
* ``game.balls_per_game`` - Balls per game
* ``game.balls_in_play`` - Balls in play
* ``game.tilted`` - True if the game has been tilted
* ``game.slam_tilted`` - True if the game has been slam tilted

Additionally, a game has all common mode variables (see below).
``game.X`` is just a convenient way to access ``mode.game.X``.

Machine Variables
~~~~~~~~~~~~~~~~~

You can access machine variable ``X`` using ``machine.X``.

Common machine variables are:

* ``machine.player1_score`` - Player 1 score from the last game
* ``machine.player2_score`` - Player 2 score from the last game
* ``machine.player3_score`` - Player 3 score from the last game
* ``machine.player4_score`` - Player 4 score from the last game
* ``machine.credits_string`` - String for credits or freeplay
* ``machine.credits_value`` - Human readable credits string


Settings
~~~~~~~~

You can access setting ``X`` using ``settings.X``.

Devices
~~~~~~~

You can access property ``X`` of device ``D`` of type ``T`` using ``device.T.D.X``.
For instance you can access the value of counter ``my_counter`` using
``device.counters.my_counter.value``.

Common device properties are:

* ``device.counters.my_counter.value``
* ``device.counters.my_counter.enabled``
* ``device.flippers.left_flipper.enabled``
* ``device.playfields.playfield.balls``
* ``device.ball_devices.my_lock.balls``
* ``device.counters.superjets_counter.value``
* ``device.accruals.magic_tokens.enabled``
* ``device.sequences.world_tour.completed``

MPF uses consistent names across devices, so for example any device that tracks a 
number will have a ``value`` property and any device that can be enabled/disabled will
have an ``enabled`` property. The full list of properties available for a specific
device are listed in the "Monitorable Properties" section of that device's
documentation page.

Modes
~~~~~

You can access property ``X`` of mode ``M`` using ``mode.M.X``.

Common mode properties are:

* ``mode.my_mode.active``


Using if/else logic with dynamic values
---------------------------------------

.. code-block:: mpf-config

   ##! mode: mode1
   counters:
      my_counter:
         count_events: count_up
         count_complete_value: 5 if player.wizard_complete else 3
