Ball Start Sequence
===================

This sequence shows everything that happens when a new ball starts in MPF.
There are actually a few different ways we can end up here: If this the first
ball of the first player in a new game:

#. After the game mode posts the *game_started* event, it will call
   its ``player_turn_start()`` method.
#. The ``player_turn_start()`` method does a few things:

    #. If there's not an active player (because this it the start of a new
       game), it called the game mode's ``player_rotate()`` method which maps
       the game's *player* attribute to the current player.
    #. Posts an event called *player_turn_started*.
    #. The game mode's ``_player_turn_started()`` method is a callback for
       that event, which is called next.

#. The ``_player_turn_started()`` method:

    #. Increments the ball count for the player
    #. Calls the game mode's ``ball_starting()`` method.

#. The ``ball_starting()`` method:

    #. Posts player, ball, and score information to the debug log
    #. Posts the *ball_starting* event. Like the *game_starting* event
       from the last step, this is also a queue event, meaning any component
       can hook in to do whatever it needs to do before releasing control.
       (This could be per-player animations and cut scenes, maybe the tilt
       wants to wait a few seconds for the plumb bob to stop rocking, etc.)

#. The game's ``ball_started()`` method is the callback for the
   ball_starting event.

    #. Event handlers for ball_drain are added.
    #. balls_in_play is set to 1.
    #. The *ball_started* event is posted.

#. Many things are configured to respond to the *ball_started* event,
   including:

    #. Shots are enabled
    #. Autofire devices are enabled
    #. Flippers are enabled
    #. Ball lock devices are enabled
    #. Multiball devices are enabled

#. The playfield's ``add_ball()`` method is called.

    #. The ball controller looks for a ball device tagged with
       ``ball_add_live``, and it changes that device's desired ball count to 1.
       (In this example lets assume that you have a plunger lane and a
       trough.)
    #. The trough sees that one of its eject targets (the plunger lane)
       wants a ball, so it ejects one.
    #. The plunger lane receives and confirms that it now has a ball.
    #. If this machine has a launch button and a coil-fired plunger, the
       player hits a button tagged with ``player_controlled_eject_tag``.
    #. The ball controller receives a request to add a live ball and posts
       the *ball_add_live* event.
    #. The ball device with the ``ball_add_live`` tag responds by
       ejecting its ball.
    #. When that ball eject is confirmed (based on the settings for that
       device), the ball controller posts the *ball_live_added* event.
    #. If the machine is configured with a player_controller_eject_tag,
       that tag is passed as the trigger event that will launch the ball.

The ball is now in play.

