Game (mode)
===========

MPF includes a built-in mode called *game* which is responsible for actually running a game in
MPF. It starts when a game is started from the attract mode, and it
stays running all the way through the entire game, finally stopping
again when the game ends and the attract mode starts again.

The code and configuration
for the built-in game mode lives in the ``mpf/modes/game`` folder. It's
automatically added to the list of modes in the ``modes:`` section of
your machine-wide config based on settings in the ``mpfconfig.yaml``
baseline configuration file. The game mode runs at priority 20. It
starts when the *game_start* event is posted, and it stops when the
*game_ended* event is posted.

The game mode is responsible for many
things, including:

+ Tracking the number of balls in play. (Remember the number of balls
  in play is not necessarily the same as the number of live balls on the
  playfield that the ball controller tracks.)
+ Watching for start button pushes to add additional players to the
  game.
+ Restarting the game on a "long press" of the start button.
+ Posting the game_started, ball_starting, ball_ending, ball_ended,
  game_ending, and game_ended events.
+ Posting the events relating to multiplayer games.
+ Handling ball drains and ending the current player's turn
+ Rotating the players and starting the next player's turn
+ Processing extra balls and handling shoot again

It's almost never necessary to override or change the behavior of the
game mode. Typically anything you want to do to affect the game is
done in additional modes you create. (And all the configuration for
scoring, game modes, shots, etc. is done in a "base" game mode that
runs per player as their turn starts.) See the tutorial for details.
