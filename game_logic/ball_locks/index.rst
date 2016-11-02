Ball Locks
==========

MPF's *ball locks* are used to hold a ball that has entered a
:doc:`/mechs/ball_devices/index while something else happens.

Example use cases include:

* Lock a ball for multiball (and then launch a new ball from the trough)
* Temporarily hold (lock) a ball while you play some kind of award show, then
  release (unlock) the ball back into play when that show is over.

Ball locks are "logical" (not physical), so different ball locks can exist in
different modes that hold balls in the same device (depending on what mode is
running).

Ball lock devices track the number of balls "locked" on a per-player basis, so
even if one player empties out a physical ball device, the ball lock for another
player will know how many balls that player had locked, even if the number of
balls in a contained physical ball device doesn't match.

You can have lots of different ball locks in your game, typically configured
per mode.

Configuring ball locks
----------------------

See the :doc:`/config/ball_locks` section of the config file reference.

Events posted by ball locks
---------------------------

There are several events posted by ball locks: (click each for details from the
event reference guide)

* :doc:`/events/ball_lock_name_balls_released`
* :doc:`/events/ball_lock_name_full`
* :doc:`/events/ball_lock_name_locked_ball`
