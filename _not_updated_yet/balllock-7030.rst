
You can use MPF's *ball lock* device to configure ball locks. Ball
lock devices work with ball devices to lock balls for the player, and
they automatically keep track of how many balls a player has locked
(even if another player causes the ball device to physically release
its balls).



Configuring ball locks
----------------------

See the `ball_locks:` section of the configuration file reference.



Events posted by ball lock devices
----------------------------------

The ball locks in MPF will post the following events. Each ball lock
you set up has a name, and that name will be used in the *<name>*
section of the event names below:


+ * ball_lock_<name>_balls_released * - The ball lock has released one
  or more balls. This event includes a *balls_released* parameter which
  is the number of balls it released.
+ * ball_lock_<name>_locked_ball * - The ball lock has just locked
  another ball (or balls). This event includes a *balls_locked*
  parameter which is the number of balls it just locked, and a
  *total_balls_locked* parameter which is the total number of balls it
  has locked.
+ * ball_lock_<name>_full * - The ball lock is full. A parameter
  *balls* is included which is the number of balls that are locked.




