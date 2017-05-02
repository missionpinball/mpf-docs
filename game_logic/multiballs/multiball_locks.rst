Multiball Locks
===============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/multiballs`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/multiball_locks`                                               |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Multiball locks work in concert with multiball logic to "lock" balls for multiball.
To use a multiball lock, you configure it for the ball device (or devices) that will
be used to lock balls, and then when a ball enters one of those devices, the lock
count is increased by one.

Ball locks are stored on a per-player basic and are NOT based on the number of balls
that are physically contained in any ball devices.

When a ball is locked, a new ball will be added into play (from whichever ball device
is tagged with the ``ball_add_live`` tag) unless the device that just received the
locked ball is full, in which case the ball will be released from the device that
the ball just entered instead.

Multiball locks can be enabled and disabled with events, so if you want to set up a
scenario where a player must "re-light" the lock after each ball is locked, then you
can use the event which is posted when a ball is locked as a disable event for this
ball lock, and then use the event from some other shot or switch or logic block as
an enable event to re-light the lock.

You can configure multiball locks for the total number of balls they should lock
which will in turn post a "lock full" event which you can use to start a multiball.
That multiball will release all the balls it can from the lock devices this
multiball lock uses, and if it still needs more balls (maybe because you're using
a virtual lock or because a previous player emptied them out), then it will make
up the difference be adding new balls from the ball device tagged with ``ball_add_live``.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for multiballs is ``device.multiballs.<name>``.

*enabled*
   Boolean (true/false) as to whether this multiball lock is enabled.

.. note::

   If you want to track how many balls are locked so far, that's stored in a player
   variable with the name ``<multiball_lock_name>_locked_balls``. So you can monitor
   that or use the player dynamic value if you need to do logic based on it.

Related How To guides
---------------------

* :doc:`multiball_with_traditional_ball_lock`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`add_a_ball_multiball`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`multiball_with_multiple_lock_devices`

Related Events
--------------

* :doc:`/events/multiball_name_ended`
* :doc:`/events/multiball_name_lost_ball`
* :doc:`/events/multiball_name_shoot_again`
* :doc:`/events/multiball_name_shoot_again_ended`
* :doc:`/events/multiball_name_started`
