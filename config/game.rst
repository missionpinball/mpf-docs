game: (config setting)
======================

Holds settings related to the game play.

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

Here's a sample ``game:`` section which shows all the settings along with their
default values. Note that you do not need to include a ``game:`` section in your
machine config, as MPF will use these default values unless you specifically
override them.

::

    game:
        balls_per_game: 3
        max_players: 4
        start_game_switch_tag: start
        add_player_switch_tag: start
        allow_start_with_loose_balls: False
        allow_start_with_ball_in_drain: False


Settings & options
------------------

add_player_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string. Default: start

A string name of the tag that's added to the switch that's used to add a player
to a game. Usually this is the same as your start button, so you'd just keep it
at the default value of *start*.


allow_start_with_ball_in_drain:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: boolean (Yes/No or True/False). Default: False

Boolean setting which controls whether MPF can start a game when a ball is
in a device tagged with *drain* that is not also tagged with *trough*.

Older machines (System 11 and prior, Gottlieb, etc.) have separate *drain* and
*trough* devices. Usually when a ball drains, the drain device immediately
ejects the ball into the trough. However many of those older machines have lower
capacity troughs than modern machines (often only 1 or 2 balls), so we can use
this setting to "hack" older machines to tell MPF that it's ok to essentially
use the drain as a ball storage location. This has the effect of letting us add
an additional ball to older machines without having to perform a hardware hack
on the trough to increase its capacity.


allow_start_with_loose_balls:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: boolean (Yes/No or True/False). Default: False

Boolean setting which controls whether MPF is able to start a game when balls
are rolling around loose on the playfield. (This could happen if a player
pushes start after a game has just ended while the machine is in the process of
ejecting balls from playfield devices to move them all to the trough.)

If this setting is *False*, then pushing start won't start a game until all the
balls have been collected.


balls_per_game:
~~~~~~~~~~~~~~~
Single value, type: integer. Default: 3

The number of balls per game. Typically it's 3 or 5 but you can set this value
to whatever you want.


max_players:
~~~~~~~~~~~~
Single value, type: integer. Default: 4

The maximum number of players that can be added to a single game.  Typically
this is 4, but the MPF doesn't really care what this number is.


start_game_switch_tag:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string. Default: start

A string name of the tag that's added to the switch that is used to start a game.
The default is *start* which should be fine for most cases. This is what makes
the switch with the ``tags: start`` setting actually start a game.

