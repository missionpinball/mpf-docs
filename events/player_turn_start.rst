player_turn_start
=================

*MPF Event*

A new player's turn is starting. This event is only posted at the
start of a new player's turn. If that player gets an extra ball and
shoots again, this event is not posted a second time.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``number``
  The player number

``player``
  The player object whose turn is starting.

