game:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``game:`` section of the machine config holds settings related
to the game play.

.. code-block:: mpf-config

    game:
      balls_per_game: 3
      max_players: 4

.. config


Optional settings
-----------------

The following sections are optional in the ``game:`` section of your config. (If you don't include them, the default will be used).

add_player_event:
~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Defaults to empty.

An event name which will request to add a player.
Same as ``add_player_switch_tag`` but using an event instead oa switch tag
(see below).

add_player_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``start``

The tag of the switch that's used to request to add a player to an existing
game. (We say "request to add a player" instead of "add a player" because
it's possible that adding a player is not allowed. For example, if the
machine is set to require credits and there are not enough credits available,
or the game already has the maximum number of players.)

This is the name of the tag in the ``tags:`` section of one of your switches.

allow_start_with_ball_in_drain:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether it's possible to start a game when a ball is in a ball device
that's tagged with ``drain`` but not ``home`` or ``trough``. (This is needed
in some older machines that have non-standard trough/drain device
configurations.

allow_start_with_loose_balls:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether it's possible to start a game when balls are not all
in ball devices tagged with ``home``.

balls_per_game:
~~~~~~~~~~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``3``

How many balls the game is. Typically it's 3 or 5 but it can be
anything. MPF doesn't care.

.. include:: template_setting.rst

end_ball_event:
~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Default: ``end_ball``

When this event is handled by the game it will end the current ball.
This is similar to the last ball draining.
Use with care if there are still balls in play.

end_game_event:
~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Default: ``end_game``

When this event is handled by the game it will end the game.
This is similar to slam tilt but bonus mode, match mode etc will still run.

max_players:
~~~~~~~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``4``

Controls the maximum number of players that can play a game.

.. include:: template_setting.rst

start_game_event:
~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Defaults to empty.

Event to request to start a game.
Same as ``start_game_switch_tag`` but using an event instead of a switch tag
(see below for details).

start_game_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``start``

The tag of the switch that's used to request to start a game. (We say
"request to start a game" instead of "start a game" because
it's possible that starting a game is not allowed. For example, if the
machine is set to require credits and there are not enough credits available.)

This is the name of the tag in the ``tags:`` section of one of your switches.


Related How To guides
---------------------

* :doc:`/game_logic/index`
