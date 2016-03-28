
MPF's *ball save* abstract device is used to configure ball saves. You
probably know what a ball save is, but if not, it's where the ball
that drains doesn't count and the player gets their ball back.
Typically it's used to give the player their ball back if they drain
right after their ball starts, or it's used to give the player their
ball back if there's a particularly wicked shot that tends to drain
which the game designers feel bad about. (You should avoid the latter
if possible, and instead, as Lyman Sheets would say, "Fix your f-ing
game layout!") You can configure ball saves to have various start and
stop events and timers, and you can configure multiple ones in
different modes that do different things.



Configuring ball saves
----------------------

See the ` `ball_saves:` section`_ of the configuration file reference.



Events posted by ball save devices
----------------------------------

The ball saves in MPF will post the following events. Each ball save
you set up has a name, and that name will be used in the *<name>*
section of the event names below:


+ * ball_save_<name>_enabled * – The ball save has been enabled.
+ * ball_save_<name>_disabled * – The ball save has been disabled.
+ * ball_save_<name>_hurry_up * – The active time remaining has
  decreased into the “hurry up” period.
+ * ball_save_<name>_grace_period * – The active_time remaining is up,
  but the ball save will stay active for the grace_period time.
+ * ball_save_<name>_saving_ball * – The ball save is saving a ball.


.. _ section: https://missionpinball.com/docs/configuration-file-reference/ball_saves/


