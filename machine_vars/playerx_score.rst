player(x)_score
===============

*MPF machine variable*

Holds the numeric value of a player's score from the last
game. The "x" is the player number, so this actual machine
variable is ``player1_score`` or ``player2_score``.

Since these are machine variables, they are maintained even after
a game is over. Therefore you can use these machine variables in
your attract mode display show to show the scores of the last game
that was played.

These machine variables are updated at the end of the game,
and they persist on disk so they are restored the next time
MPF starts up.

