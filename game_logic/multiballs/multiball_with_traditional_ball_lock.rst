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

::

    multiballs:
      ball_count: 3
      ball_count_type: total  # Default
      shoot_again: 10s        # Default

With no enable/disable and start/stop events configured, this multiball will
begin as soon as its parent mode starts, and it will increase the number of
balls on the playfield to a total of 3.

Using a multiball_lock to start a multiball
-------------------------------------------

A typical multiball requires the player to "lock" balls up to the total
ball count, which triggers the start of a multiball. You can setup a ``multiball_lock``
to track progress and use its *multiball_lock_(name)_full* event to start a
multiball.

::

    multiball_locks:
      madnesslock:
        balls_to_lock: 3
        lock_devices: lockdevice

    multiballs:
      madnessmball:
        ball_count: 3
        ball_locks: lockdevice
        start_events: multiball_lock_madnesslock_full

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

::

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
