player_adding
=============

*MPF Event*

A new player is in the process of being added to this game. This is a queue
event, and the player won't actually be finished adding until the queue is cleared.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``number``
  The player number

``player``
  The player object for the player being added

