---
title: Ball Start Sequence
---

# Ball Start Sequence


This sequence shows everything that happens when a new ball starts in
MPF. There are actually a few different ways we can end up here: If this
the first ball of the first player in a new game:

1.  After the game mode posts the *game_started* event, it will call its
    `player_turn_start()` method.

2.  The `player_turn_start()` method does a few things:

    1.  If there's not an active player (because this it the start of
        a new game), it called the game mode's `player_rotate()`
        method which maps the game's *player* attribute to the
        current player.
    2.  Posts an event called *player_turn_started*.
    3.  The game mode's `_player_turn_started()` method is a callback
        for that event, which is called next.

3.  The `_player_turn_started()` method:

    1.  Increments the ball count for the player
    2.  Calls the game mode's `ball_starting()` method.

4.  The `ball_starting()` method:

    1.  Posts player, ball, and score information to the debug log
    2.  Posts the *ball_starting* event. Like the *game_starting*
        event from the last step, this is also a queue event, meaning
        any component can hook in to do whatever it needs to do before
        releasing control. (This could be per-player animations and
        cut scenes, maybe the tilt wants to wait a few seconds for the
        plumb bob to stop rocking, etc.)

5.  The game's `ball_started()` method is the callback for the
    ball_starting event.

    1.  Event handlers for ball_drain are added.
    2.  balls_in_play is set to 1.
    3.  The *ball_started* event is posted.

6.  Many things are configured to respond to the *ball_started* event,
    including:

    1.  Shots are enabled
    2.  Autofire devices are enabled
    3.  Flippers are enabled
    4.  Ball lock devices are enabled
    5.  Multiball devices are enabled

7.  The playfield's `add_ball()` method is called.

    1.  The ball controller looks for a ball device in the
        `default_source_device` setting of your playfield, and it
        changes that device's desired ball count to 1. (In this
        example lets assume that you have a plunger lane and a
        trough.)
    2.  The trough sees that one of its eject targets (the plunger
        lane) wants a ball, so it ejects one.
    3.  The plunger lane receives and confirms that it now has a ball.
    4.  If this machine has a launch button and a coil-fired plunger,
        the player hits a button tagged with
        `player_controlled_eject_tag`.
    5.  The ball controller receives a request to add a live ball.
    6.  The ball device in the `default_source_device` of your
        playfield ejects its ball.
    7.  If the machine is configured with a
        player_controller_eject_tag, that tag is passed as the trigger
        event that will launch the ball.

The ball is now in play.

## Related Guides:

Flowchart: [Ball End Sequence](ball_end.md)

## Related Events:

* [Ball Lifecycle Events](../events/ball_lifecycle/index.md)
    * [ball_will_start](../events/ball_will_start.md)
    * [ball_starting](../events/ball_starting.md) *Queue Event*
    * [ball_started](../events/ball_started.md)

    * [ball_start_target](../events/ball_start_target.md)
    * [balls_in_play](../events/balls_in_play.md)
    * [multi_player_ball_started](../events/multi_player_ball_started.md)
    * [single_player_ball_started](../events/single_player_ball_started.md)
