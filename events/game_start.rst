game_start
==========

*MPF Event*

A game is starting. (Do not use this event to start a game.
Instead, use the *request_to_start_game* event.


Keyword arguments
-----------------

buttons
~~~~~~~
A list of switches tagged with *player* that were held in
when the start button was released. This is used for "alternate"
game starts (e.g. hold the right flipper and press start for
tournament mode, etc.)

hold_time
~~~~~~~~~
The time, in seconds, that the start button was held in
to start the game. This can be used to start alternate games via a
"long press" of the start button.

