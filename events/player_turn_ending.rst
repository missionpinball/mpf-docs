player_turn_ending
==================

*MPF Event*

The current player's turn is ending. This is a queue event, and
the player's turn won't actually end until the queue is cleared.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``number``
  The player number

``player``
  The player object whose turn is ending.

