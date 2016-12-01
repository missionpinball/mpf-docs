player_add_success
==================

*MPF Event*

A new player was just added to this game

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``num``
  The number of the player that was just added. (e.g. Player 1 will
have *num=1*, Player 4 will have *num=4*, etc.)

``player``
  A reference to the instance of the Player() object.

