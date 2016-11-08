Ball End Sequence
=================

This sequence starts with a ball live and in play and ends when the
ball drains and the ball is over.

#. The ball enters a ball device device tagged with drain.
#. The ball controller's ``_ball_drained_handler()`` method responds to
   the ball having entered a device tagged with ``drain``.
#. It posts a relay event called *ball_drain*, along with the number
   of balls that just drained.

    #. Various modules can hook event this to "remove" a ball from the
       *ball_drain* event so it doesn't count as a drain. (For example, ball
       save.)

#. The game mode's ``ball_drained()`` method is registered as a handler
   for the *ball_drain* event.
#. It subtracts the number of balls that just drained from its
   *balls_in_play* count.
#. If the balls_in_play count was a positive number and goes to zero,
   the game mode's ball_ending() method is called.
#. The game mode posts the queue event *ball_ending*.
#. Once that event is done, the game mode's ``_ball_ending_done()``
   method is called.
#. The event *ball_ended* is posted.
#. The game mode's ``ball_ended()`` method is called.

    #. If the player has any extra balls, the game mode's ``shoot_again()``
       method is called.
    #. If the player is the last player, and the ball is the last ball,
       the game mode's ``game_ending()`` method is called.

#. Otherwise the game mode's ``player_rotate()`` method is called.
#. The game mode's ``player_turn_start()`` method is called.

