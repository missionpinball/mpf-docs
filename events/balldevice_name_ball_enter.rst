balldevice_(name)_ball_enter
============================

*MPF Event*

A ball (or balls) have just entered the ball device called
"name".

Note that this is a relay event based on the "unclaimed_balls" arg. Any
unclaimed balls in the relay will be processed as new balls entering
this device.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``device``
  A reference to the ball device object that is posting this
event.

``unclaimed_balls``
  The number of balls that have not yet been claimed.

