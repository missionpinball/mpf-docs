How to create a multiball with a traditional ball lock
======================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/multiballs`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/multiball_locks`                                               |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Most pinball machines use a "virtual" ball lock to track multiball progress and
MPF is designed to handle these by default. Machines that physically lock multiple
balls require a few extra configuration settings to properly count locked balls and
release them for a multiball.

Background: How MPF tracks and replaces balls
---------------------------------------------

When a ball enters a ball device that is not the trough, the ball device checks
for any locks that want to "claim" the ball. If the ball is claimed by anything,
such as an enabled ``multiball_lock``, the ball device will hold the ball and
request a new ball be added from the trough to the playfield. If nothing claims
the ball, the ball device will eject it back onto the playfield.

During this process, the number of "balls in play" never changes. When a ball
is claimed by a lock, MPF simply swaps the location of the inactive ball from the
trough to the ball device. From the game's perspective the playfield always
has one ball in play.

Setting up a simple multiball
-----------------------------

An MPF multiball only has one configuration requirement: the number of balls in
the multiball (by default the total number of balls, but could also be the
number of balls added to those already in play). Consider the following example:

.. code-block:: mpf-config

   ##! mode: multiball_mode
   multiballs:
     my_multiball:
       ball_count: 3
       ball_count_type: total    # Default
       shoot_again: 10s          # Default

With no enable/disable and start/stop events configured, this multiball will
begin as soon as its parent mode starts, and it will increase the number of
balls on the playfield to a total of 3.

Using a multiball_lock to start a multiball
-------------------------------------------

A typical multiball requires the player to "lock" balls up to the total
ball count, which triggers the start of a multiball. You can setup a ``multiball_lock``
to track progress and use its *multiball_lock_(name)_full* event to start a
multiball.

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #!   s_ball2:
   #!     number:
   #! coils:
   #!   c_eject:
   #!     number:
   #! ball_devices:
   #!   lockdevice:
   #!     eject_coil: c_eject
   #!     ball_switches: s_ball1, s_ball2
   ##! mode: multiball_mode
   multiball_locks:
     madnesslock:
       debug: true
       balls_to_lock: 2
       lock_devices: lockdevice
       reset_count_for_current_player_events: multiball_lock_madnesslock_full
   multiballs:
     madnessmball:
       ball_count: 3
       ball_locks: lockdevice
       start_events: multiball_lock_madnesslock_full
   ##! test
   #! start_game
   #! mock_event multiball_lock_madnesslock_full
   #! start_mode multiball_mode
   #! # start mode and lock three balls. mb should start
   #! add_ball_to_device lockdevice
   #! advance_time_and_run 1
   #! assert_int_condition 1 device.multiball_locks.madnesslock.locked_balls
   #! assert_event_not_called multiball_lock_madnesslock_full
   #! assert_balls_in_play 1
   #! add_ball_to_device lockdevice
   #! advance_time_and_run 1
   #! assert_event_called multiball_lock_madnesslock_full
   #! advance_time_and_run 40
   #! assert_balls_in_play 3
   #! drain_one_ball
   #! drain_one_ball
   #! advance_time_and_run 1
   #! assert_balls_in_play 1
   #! assert_int_condition 1 current_player.ball
   #! assert_int_condition 0 device.multiball_locks.madnesslock.locked_balls
   #! # The ball device should be empty now
   #! assert_int_condition 0 device.ball_devices.lockdevice.balls
   #! # second try. mb should start again
   #! mock_event multiball_lock_madnesslock_full
   #! add_ball_to_device lockdevice
   #! advance_time_and_run 1
   #! assert_int_condition 1 device.multiball_locks.madnesslock.locked_balls
   #! assert_event_not_called multiball_lock_madnesslock_full
   #! assert_balls_in_play 1
   #! add_ball_to_device lockdevice
   #! advance_time_and_run 1
   #! assert_event_called multiball_lock_madnesslock_full
   #! advance_time_and_run 40
   #! assert_balls_in_play 3
   #! drain_one_ball
   #! drain_one_ball
   #! advance_time_and_run 1
   #! assert_balls_in_play 1
   #! assert_int_condition 1 current_player.ball
   #! assert_int_condition 0 device.multiball_locks.madnesslock.locked_balls

In the above configuration, the multiball_lock will track the balls entering *lockdevice*
and claim up to three. When the third ball is claimed the lock will post its "full"
event, which will start the multiball.

Ball-in-play count with physically-locked balls
-----------------------------------------------

As noted above, MPF will automatically replace any locked ball with a new ball
from the trough, which is necessary for "virtually" locked balls but causes
undesirable behavior for physically locked balls. In order to maintain the
"balls in play" count, the new ball will be ejected to the playfield immediately—
before the multiball can process the *full* event and start itself.

The multiball therefore assumes (correctly) that the last locked ball has already
been replaced and thus deducts that "in play" ball from its count of balls to add. In the
above example, the multiball would release 2 balls from *lockdevice* which,
in addition to the active ball in play, would result in a 3-ball multiball.

Unfortunately, this also leaves one ball locked in *lockdevice* after the multiball
starts, which is not the desired outcome.

Overwriting ball replacement for physically-locked balls
--------------------------------------------------------

You can overwrite the multiball_lock behavior to prevent the automatic replacement
of a locked ball with the ``balls_to_replace`` setting. The default value of -1
instructs the lock to replace every locked ball, but a value of 2 will replace only
the first two locked balls.

In tandem, you can overwrite the multiball behavior to not assume that the "in play"
ball has been replaced by the lock. The ``replace_balls_in_play`` setting set to
True will instruct the multiball to eject the active ball **and** the additional balls.

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #! coils:
   #!   c_eject:
   #!     number:
   #! ball_devices:
   #!   lockdevice:
   #!     eject_coil: c_eject
   #!     ball_switches: s_ball1
   ##! mode: multiball_mode
   multiball_locks:
     madnesslock:
       balls_to_lock: 3
       balls_to_replace: 2
       lock_devices: lockdevice
   multiballs:
     madnessmball:
       ball_count: 3
       ball_locks: lockdevice
       start_events: multiball_lock_madnesslock_full
       replace_balls_in_play: true

With the above configuration, the final locked ball will start the multiball and the
multiball will eject three balls from *lockdevice*.

.. note::

   Be careful with with *balls_to_replace* and *replace_balls_in_play*.
   They will only work in exactly this combination.
   Used in isolation they will likely lead to incorrect ball counts.

Video about ball locks and multiballs:

.. youtube:: 2mFkgIlksC4
