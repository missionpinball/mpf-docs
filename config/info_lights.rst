info_lights:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``info_lights:`` section of a machine config file allows you to
configure the "Info Lights" plugin to automatically set "status"
lights based on different things that are happening in the game. This
is very common in EM and older solid state machines, since they use
lights to tell the player whose turn it is, what ball they're
on, etc.

Here's an example ``info_lights:`` section from a machine configuration file:

.. code-block:: mpf-config

   #! lights:
   #!   match00:
   #!     number:
   #!   match10:
   #!     number:
   #!   match20:
   #!     number:
   #!   match30:
   #!     number:
   #!   match40:
   #!     number:
   #!   match50:
   #!     number:
   #!   match60:
   #!     number:
   #!   match70:
   #!     number:
   #!   match80:
   #!     number:
   #!   match90:
   #!     number:
   #!   bip1:
   #!     number:
   #!   bip2:
   #!     number:
   #!   bip3:
   #!     number:
   #!   bip4:
   #!     number:
   #!   bip5:
   #!     number:
   #!   player1:
   #!     number:
   #!   player2:
   #!     number:
   #!   tilt:
   #!     number:
   #!   gameOver:
   #!     number:
   info_lights:
     match_00:
       light: match00
     match_10:
       light: match10
     match_20:
       light: match20
     match_30:
       light: match30
     match_40:
       light: match40
     match_50:
       light: match50
     match_60:
       light: match60
     match_70:
       light: match70
     match_80:
       light: match80
     match_90:
       light: match90
     ball_1:
       light: bip1
     ball_2:
       light: bip2
     ball_3:
       light: bip3
     ball_4:
       light: bip4
     ball_5:
       light: bip5
     player_1:
       light: player1
     player_2:
       light: player2
     tilt:
       light: tilt
     game_over:
       light: gameOver

The way info lights work is pretty simple. There are sub-sections that
represent different lights that may be in your machine, and then under
each of them you map them to the name of the light.

Then they pretty much just work automatically.

Note that the the ``light:`` entry in each of these refers to a device in the :doc:`/config/lights` section.

match_XX:
---------

This section is for the match lights, with the "XX" replaced with the
number of the match light. In the example configuration above, the
machine has match lights that count up by tens (10, 20, 30...) which
is why the match_xx entries here are ``match_10``, ``match_20``,
``match_30``, etc. If your machine matches by the ones digit, then you'd
enter these items as ``match_1``, ``match_2``, etc.

ball_XX:
--------

This maps the ball-in-play number to the light.

player_XX:
----------

This maps the current player to the number in the light. This plugin
turns on each light when a new player joins a game. So it doesn't show
which player is up, rather, if you have a two-player game then both
the ``player_1`` and ``player_2`` lights are lit. (So how does a player know
that it's his turn? That's handled by the score reel lights.)

tilt:
-----

Turns this light on when the machine tilts.

game_over:
----------

Flashes this light when a game is not in progress at a rate of 1/2 sec
on, 1/2 sec off.
