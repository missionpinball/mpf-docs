Attract (mode)
==============

MPF includes a built-in attract mode which is what runs the machine
when a game is not in progress. It starts when either the *game_ended*
or *reset_complete* event is posted, and it stops when the
*game_start* mode is posted. The attract mode runs at priority 10.

The
code and configuration for the built-in attract mode is in the
*mpf/modes/attract* folder. It's automatically added to the list of
modes in the ``modes:`` section of your machine-wide config based on
settings in the ``mpfconfig.yaml`` baseline configuration file.

The attract mode is responsible for many things, including:

+ Watching for the start button to be pressed & released to kick off
  the request_to_start_game event
+ Recording how long the start button was held in for in order to take
  different actions based on different times. (For example, maybe
  pressing the start button normally starts a regular game, and doing a
  long-press lets the player login with a custom player profile.)
+ Recording what other buttons were active when the start button is
  pressed. (Maybe holding the right flipper button and pushing start
  enables tournament mode.)

You can completely customize and extend the attract mode. In most
cases that's as simple as adding a config file for the attract mode
to your game folder and then configuring light and display shows to
play. See the tutorial for details on how to do this.
