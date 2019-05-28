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

Multiball locks can be configured in one of four modes of operation:

``virtual_only``
   When a new ball is locked, the lock count is increased. Period. It does not matter
   how many physical balls are locked. Separate counts are maintained per player.
   This is usually the best option for locks in modern machines.

``physical_only``
   As the name implies, the number of balls locked is always the same as the physical
   number of balls in the lock. A new ball locked will increase the lock count for that
   player and lock the ball.
   However if another player "steals" one of the locked balls, then when the previous
   player starts their turn, the lock count is updated based on the physical balls
   locked. This is mostly for EM and early solid state machines where balls would be
   locked in different places on the playfield but the next player could steal them if
   the player who locked them didn't get multiball started.

``min_virtual_physical``
   Similar to physical only except a player locking a ball will always increase the
   lock count even if that same ball is ejected again.

``no_virtual``
   MPF forgets everything when the player changes.


Ball locks are stored on a per-player basic and are NOT based on the number of balls
that are physically contained in any ball devices.

When a ball is locked, a new ball will be added into play (from whichever ball device
set in ``default_source_device`` of the playfield) unless the device that just received the
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
up the difference be adding new balls from the ball device set in
``default_source_device`` of your :doc:`playfield </config/playfields>`.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for multiball locks is ``device.multiball_locks.<name>``.

*enabled*
   Boolean (true/false) as to whether this multiball lock is enabled.

*locked_balls*
   The number of balls that are locked. Note that how this number is calculated
   varies depending on how the ball counting strategy is configured for this
   multiball lock.

Related How To guides
---------------------

* :doc:`multiball_with_traditional_ball_lock`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`add_a_ball_multiball`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`multiball_with_multiple_lock_devices`

Related Events
--------------

.. include:: /events/include_multiball_locks.rst
