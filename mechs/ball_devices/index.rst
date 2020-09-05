Ball Devices
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+

.. contents::
   :local:

A *ball device* is any physical thing in a pinball machine which is able to
hold (i.e. "capture") a ball and then release it. (Either
automatically or based on some action by the player.) Examples of ball
devices include the trough, the plunger lane, VUKs, poppers, playfield
locks, etc.—basically anything that can hold a ball. (Even the
playfield is technically a ball device since balls rolling around are "in" the
playfield device.)

Ball devices are usually made up of switches (which
are typically used to count how many balls the ball device has) and
coils (which are typically used to eject a ball from a device.) Most
games have several ball devices. At a minimum they'll have the device
that holds the ball when it drains and the playfield.

Ball devices are probably the most important element of MPF (because no one
likes it when a machine gets confused about where the balls are) and
something we've spent a lot of time on. They work hand-in-hand with MPF's
Ball Controller to keep track of where all the balls are at any given time.

In MPF, ball devices are implemented as
`finite state machines <https://en.wikipedia.org/wiki/Finite-state_machine>`_.

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

.. image:: /mechs/images/ball_device_fsm_diagram.png

When you configure ball devices in MPF, you configure the list of other
devices that a ball device can eject to. This allows MPF to have an understanding
of the "chain" of devices and enables it to route balls to where they need to
go. (:doc:`/mechs/diverters/index` also figure into this chain, meaning MPF
can ensure that diverters are set properly as it's routing balls around.)

Here's a simplified example of how the "chain" of ball devices works:

A simple modern machine would have a minimum of three ball devices:

* The trough
* The plunger lane
* The playfield (remember in MPF, the playfield is technically a ball device)

When you configure your ball devices, the trough is configured so that the
plunger lane is its eject target, the plunger lane is configured with the
playfield as its eject target, and the playfield is configured to know that it
drains into the trough. So you have a complete loop of devices.

This means that, for example, if the playfield wants another ball (like for
a multiball), MPF knows that the playfield gets balls from the plunger lane, and
if the plunger lane doesn't have a ball, MPF knows that the plunger lane can get
a ball from the trough.

Pretty cool!

Of course in a real machine, you'll have a lot more than the three ball devices
listed above.

Picking a random machine as an example, *Judge Dredd* has eight(!) ball devices:

1. :doc:`The trough </mechs/troughs/index>`
2. The right :doc:`plunger lane </mechs/plungers/index>`
3. The left plunger lane
4. The Sniper VUK
5. The Hall of Justice VUK
6. The Deadworld orbit thingy
7. The crane
8. :doc:`The playfield </mechs/playfields/index>`

MPF keeps track of how many balls are in each ball device at all
times, and it knows which devices are in the process of ejecting (and which
target devices they're ejecting to), so it also knows if balls get stuck along
the way.

Ball devices support all sorts of settings and events. You can also configure counting
delays to account for balls bouncing around before they settle, you
can specify how devices confirm that balls have successfully ejected,
as well as dozens of other options that allow MPF to support every
known type of device in every pinball machine ever created.
(Seriously.)

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball devices is ``device.ball_devices.<name>``.

*available_balls*
   Number of balls that are available to be ejected. This differs from
   *balls* since it's possible that this device could have balls that are
   being used for some other eject, and thus not available.

*state*
   What state this device is in.

*balls*
   How many balls this device is currently holding.

Related How To guides
---------------------

* :doc:`/mechs/troughs/modern_opto`
* :doc:`/mechs/troughs/modern_mechanical`
* :doc:`/mechs/troughs/two_coil_multiple_switches`
* :doc:`/mechs/troughs/two_coil_one_switch`
* :doc:`/mechs/troughs/classic_single_ball`

Related Events
--------------

.. include:: /events/include_ball_devices.rst
