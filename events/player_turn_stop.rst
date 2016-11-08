player_turn_stop
================

*MPF Event*

The player's turn is ending. This event is only posted when this
player's turn is totally over. If the player gets an extra ball and
shoots again, this event is not posted until after all their extra
balls and it's no longer their turn.

Keyword arguments
-----------------

number
~~~~~~
The player number

player
~~~~~~
The player object whose turn is over.

