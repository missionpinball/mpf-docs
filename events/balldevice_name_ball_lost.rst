balldevice_(name)_ball_lost
===========================

*MPF Event*

A ball has been lost from the device (name), meaning the ball
never made it to the target when this device attempted to eject
it.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``target``
  The target device which was expecting to receive a ball from this device.

