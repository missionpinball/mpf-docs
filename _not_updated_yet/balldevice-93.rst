
A *ball device* is any device in a pinball machine which is able to
hold (i.e. "capture") a ball and then release it. (Either
automatically or based on some action by the player.) Examples of ball
devices include the trough, the plunger lane, VUKs, poppers, playfield
locks, etc.—basically anything that can hold a ball. (Even the
playfield is a ball device since balls rolling around are "in" the
playfield device.) Ball devices are usually made up of switches (which
are typically used to count how many balls the ball device has) and
coils (which are typically used to eject a ball from a device.) Most
games have several ball devices. At a minimum they'll have the device
that holds the ball when it drains and the playfield. (In MPF, the
`playfield`_ is a type of ball device.) Ball devices are very
intelligent in MPF and are implemented as `finite state machines`_.
Each ball device is responsible for managing its own state, which can
be:


+ idle
+ missing_balls
+ waiting_for_ball
+ waiting_for_ball_mechanical
+ ball_left
+ wait_for_eject
+ ejecting
+ failed_eject
+ eject_confirmed


Here's a diagram which shows the relationships between the various
states. A device can only transition from its current state to one of
the states an arrow is connected to. ` `_ Ball devices know where they
fit in the "chain" (so they know which devices feed them and which
devices they feed), and they work with the ball controller to help MPF
know where all the balls are at any given time.

.. _playfield: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/playfield/
.. _finite state machines: https://en.wikipedia.org/wiki/Finite-state_machine


