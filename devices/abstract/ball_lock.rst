Ball lock
=========

*MPF Device*

You can use MPF's *ball lock* devices to configure logic ball locks that hold
balls which will eventually be released for multiball.

Ball lock devices are "abstract" devices. They work in tandem with the physical
*ball devices* that actually maintain balls.

Ball lock devices track the number of balls "locked" on a per-player basis, so
even if one player empties out a physical ball device, the ball lock for another
player will know how many balls that player had locked, even if the number of
balls in the physical ball device doesn't match.

You can have lots of different ball locks in your game, typically configured
per mode.

Configuring ball locks
----------------------

See the `ball_locks: </config/ball_locks>`_ section of the config file reference.


Events posted by ball lock devices
----------------------------------

The ball locks post several events when they lock or release balls and when they're
full. See the `:doc:</events`>_ for details. (Look for event names that start with
"ball_lock".)
