balldevice_(name)_ball_eject_attempt
====================================

*MPF Event*

The ball device called "name" is attempting to eject a ball (or
balls). This is a queue event. The eject will not actually be attempted
until the queue is cleared.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``balls``
  The number of balls that are to be ejected.

``mechanical_eject``
  Boolean as to whether this is a mechanical eject.

``num_attempts``
  How many eject attempts have been tried so far.

``source``
  The source device that will be ejecting the balls.

``taget``
  The target ball device that will receive these balls.

