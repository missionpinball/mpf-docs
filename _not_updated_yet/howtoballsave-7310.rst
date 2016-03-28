
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

See the `ball_saves:` section of the configuration file reference. I
added several improvements to the ball save, including:


+ Updated the code so it can be implemented in mode configurations
+ Added settings for hurry_up and grace_period times.
+ Added setting specify whether the save should auto launch a new ball
+ Added setting to specify the number of balls that should be saved
+ Added setting to separate the starting of the count down timer from
  the ball save being enabled. (Since you want it enabled and flashing
  the light while the ball is waiting to be launched, but you don’t want
  to start the timer yet.)


In doing so, the following setting has been REMOVED and is NO LONGER
VALID:


+ `auto_disable_time`


Examples of the new settings (from a mode config for mode “base”):


::

    
    ball_saves:
      default:
        active_time: 10s
        hurry_up_time: 2s
        grace_period: 2s
        enable_events: mode_base_started
        timer_start_events: balldevice_plunger_lane_ball_eject_success
        auto_launch: yes
        balls_to_save: 1
        debug: yes



+ `active_time` – How long the ball save is active for once it starts
  counting down. This includes the *hurry_up_time,* but does not include
  the *grace_period* time. Leave this setting out (or set it to 0) for
  unlimited time.
+ `hurry_up_time` – Causes an event to be posted you can use to change
  the script for the light or trigger other effect.
+ `grace_period` – The “secret” time the ball save is still active.
  This is added onto the *active_time*.
+ `timer_start_events` – optional setting to start the countdown
  timer.
+ `auto_launch` – boolean which controls whether the ball save should
  auto launch the saved ball or wait for the player to launch it.
+ `balls_to_save` – how many balls this ball saver should save before
  disabling itself. Set it to `-1` for unlimited.
+ `enable_events` – enables the ball save. If you do not have a
  *timer_start_events* entry then enabling will also start the timer.
+ `disable_events` – disables the ball save.


Events: The ball save will post several events, each with the “name”
of the ball saver in the event name. (So that’s “default” in the
example above.) This lets you have multiple ball savers. (e.g. some
games have a secret/phantom ball save for a few seconds to prevent
certain ricochet drains.) You can use these events to triggers slides,
lights, etc.


+ * ball_save_<name>_enabled * – The ball save has been enabled.
+ * ball_save_<name>_disabled * – The ball save has been disabled.
+ * ball_save_<name>_hurry_up * – The active time remaining has
  decreased into the “hurry up” period.
+ * ball_save_<name>_grace_period * – The active_time remaining is up,
  but the ball save will stay active for the grace_period time.
+ * ball_save_<name>_saving_ball * – The ball save is saving a ball.


Example flow from the ball save configuration above:


#. The mode called “base” starts.
#. *ball_save_default_enabled* is posted.
#. The player successfully launches the ball and the event
   *balldevice_plunger_lane_ball_eject_success* is posted.
#. After 8 seconds ( *active_time* minus *hurry_up_time*), the event
   *ball_save_default_hurry_up* is posted.
#. After 2 more seconds (10 total), the event
   *ball_save_default_grace_period* is posted.
#. After 2 more seconds (12 total), the event
   *ball_save_default_disabled* is posted, and this ball saver is
   disabled.


Other notes:


+ Ball save only works when balls are in play. (Remember the number of
  balls in play is not necessarily the same as the number of balls on
  the playfield.) So if the player tilts, ball save will automatically
  not work.
+ The *ball_save_<name>_shoot_again* event has been removed. (Replaced
  with *ball_save_<name>_saving_ball*.)




