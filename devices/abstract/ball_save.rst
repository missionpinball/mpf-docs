Ball save
=========

*MPF Device*

MPF's *ball save* abstract device is used to configure ball saves. You
probably know what a ball save is, but if not, it's where the ball
that drains doesn't count and the player gets their ball back.
Typically it's used to give the player their ball back if they drain
right after their ball starts, or it's used to give the player their
ball back if there's a particularly wicked shot that tends to drain
which the game designers feel bad about. (You should avoid the latter
if possible, and instead, as Lyman Sheets would say, "Fix your f-ing
game layout!")

You can configure ball saves to have various start and
stop events and timers, and you can configure multiple ones in
different modes that do different things.


Configuring ball saves
----------------------

See the :doc:`/config/ball_saves` of the config file reference.


Events posted by ball save devices
----------------------------------

The ball saves post several events when they are enabled or disabled, when they
save a ball, and as their timers count down. See the :doc:`/events/index` for details.
(Look for event names that start with "ball_save".)



