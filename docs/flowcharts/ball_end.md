---
title: Ball End Sequence
---

# Ball End Sequence


This sequence starts with a ball live and in play and ends when the ball
drains and the ball is over.

1.  The ball enters a ball device device tagged with drain.

2.  The ball controller's `_ball_drained_handler()` method responds to
    the ball having entered a device tagged with `drain`.

3.  It posts a relay event called *ball_drain*, along with the number of
    balls that just drained.

    1.  Various modules can hook event this to "remove" a ball from
        the *ball_drain* event so it doesn't count as a drain. (For
        example, ball save.)

4.  The game mode's `ball_drained()` method is registered as a handler
    for the *ball_drain* event.

5.  It subtracts the number of balls that just drained from its
    *balls_in_play* count.

6.  If the balls_in_play count was a positive number and goes to zero,
    the game mode's ball_ending() method is called.

7.  The game mode posts the queue event *ball_ending*.

8.  Once that event is done, the game mode's `_ball_ending_done()`
    method is called.

9.  The event *ball_ended* is posted.

10. The game mode's `ball_ended()` method is called.

    1.  If the player has any extra balls, the game mode's
        `shoot_again()` method is called.
    2.  If the player is the last player, and the ball is the last
        ball, the game mode's `game_ending()` method is called.

11. Otherwise the game mode's `player_rotate()` method is called.

12. The game mode's `player_turn_start()` method is called.
