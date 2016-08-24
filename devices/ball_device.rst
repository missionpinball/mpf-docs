Ball device
===========

*MPF device*

A *ball device* is any device in a pinball machine which is able to
hold (i.e. "capture") a ball and then release it. (Either
automatically or based on some action by the player.) Examples of ball
devices include the trough, the plunger lane, VUKs, poppers, playfield
locks, etc.—basically anything that can hold a ball. (Even the
playfield is a ball device since balls rolling around are "in" the
playfield device.)

Ball devices are usually made up of switches (which
are typically used to count how many balls the ball device has) and
coils (which are typically used to eject a ball from a device.) Most
games have several ball devices. At a minimum they'll have the device
that holds the ball when it drains and the playfield. (In MPF, the
playfield is a type of ball device.) Ball devices are very
intelligent in MPF and are implemented as `finite state machines <https://en.wikipedia.org/wiki/Finite-state_machine>`_.

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
the states an arrow is connected to.

.. todo:: Add the image

Ball devices know where they
fit in the "chain" (so they know which devices feed them and which
devices they feed), and they work with the ball controller to help MPF
know where all the balls are at any given time.











1. Understand what a "ball device" is
-------------------------------------

The first step to setting up your ball devices is that you have to
understand what a ball device is. :) Back in Step 3 we showed you how to add
your flipper *devices* and we briefly
outlined what devices are. We also said there are low level,
*physical* devices (switches, coils, lights, LEDs, etc.) and
higher-level *logical* devices that intelligently group together the
lower-level physical devices.

A *ball device* quite literally anything in a pinball machine that
holds a pinball (even for a moment), including your trough, the
plunger lane, playfield locks, VUKs, the gumball machines in *Twilight
Zone*, a kickout hole, etc. (Actually behind the scenes the playfield
is a ball device too, because when a ball is rolling around on it,
it's "in" the playfield device.)

Your machine will most likely have
lots of ball devices. Turning around and looking at the *Judge Dredd*
machine behind me, I count eight(!) ball devices: the trough, the
right plunger lane, the left plunger lane, the Sniper VUK, the Hall of
Justice VUK, the Deadworld orbit thingy, the crane, and the playfield.

MPF keeps track of how many balls are in each ball device at all
times, and it assumes that any balls *not* in ball devices are either
in transit from one device to another, or they're stuck somewhere.
Most ball devices have a one-to-one ratio of ball switches to ball
capacity, so MPF can simply count how many switches are active to see
how many balls each device has at any given time. (Not all ball
devices have ball switches for every ball—-the gumball machine in
*Twilight Zone* is a good example of this—-but we'll get to that
later.)

Ball devices support all sorts of settings and commands. They
can create events when balls enter or exit, (which you can use to do things in
your config files,
like how we set up the ``slide_player:`` to show certain slides when
certain events happened).  You can also configure counting
delays to account for balls bouncing around before they settle, you
can specify how devices confirm that balls have successfully ejected,
as well as dozens of other options that allow MPF to support every
known type of device in every pinball machine ever created.
(Seriously.)