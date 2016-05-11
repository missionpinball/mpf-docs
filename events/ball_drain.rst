ball_drain
==========

*MPF Event*

A ball (or balls) has just drained. (More specifically, ball(s)
have entered a ball device tagged with "drain".)

This is a relay event.


Keyword arguments
-----------------

balls
~~~~~
The number of balls that have just drained. Any balls remaining
after the relay will be processed as newly-drained balls.

device
~~~~~~
The ball device object that received the ball(s)

