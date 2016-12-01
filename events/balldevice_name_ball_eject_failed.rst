balldevice_(name)_ball_eject_failed
===================================

*MPF Event*

A ball (or balls) has failed to eject from the device (name).

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``balls``
  The number of balls that failed to eject.

``num_attempts``
  How many attemps have been made to eject this ball (or balls).

``retry``
  Boolean as to whether this eject will be retried.

``target``
  The target device that was supposed to receive the ejected balls.

