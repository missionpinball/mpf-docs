
Keeping track of where all the balls are at any given time is a big
part of a pinball. There are fourcomponents that make up MPF's ball
tracking and management system:


+ The Ball Controller (located in the
  `/mpf/system/ball_controller.py`module) whichmanages everything.
+ Individual ` *Ball Devices*`_ (troughs, locks, etc.) which track how
  many balls they're currently holding, request new balls, eject balls,
  etc.
+ The *playfield* device which is a special type of ball device that
  represents how many balls are loose on the playfield at any given
  time.
+ Individual ` *diverters*`_ which are integral in routing balls to
  devices that request them.


These four components are active at all times—regardless of whether or
not a game is in progress. In other words, if MPF is running, it's
tracking balls.



'Playfield' balls versus 'balls in play'
----------------------------------------

One important concept for ball tracking to understand is that there's
a difference between "playfield" balls and "balls in play."
*Playfieldballs* are any balls that are loose on the playfield, while
*balls in play*is an in-game concept which representshow many balls a
player has in play at any moment. In most cases, the number of
playfieldballs and balls in playwill be the same, but not always. For
example, when the machine tilts, the player's ball is "dead" and the
number of balls in play is set to zero. But of course when that
happens, there are still balls loose on the playfield, sothe ball
controller still has to track them and wait for them all to drain.
(Why?Well, the machine has to wait for all the balls on the tilted
playfield to drain before it moves on to the next ball, and ball
search has to keep running in case a ball gets stuck on its way to
drain.) Actually there are many scenarios where you have more
playfieldballs than live balls. If the player shoots the ball into a
lock, at that moment you won't actually have any playfield balls but
that player still has a ball in play. By the way, the ball controller
has nothing to do with the number of balls in play. It literally
doesn't know what that concept is. All the ball controller cares about
is tracking where all the balls are at all times. Whether a live ball
is actually in play or not is the responsibility of the game logic—not
the ball controller.

.. _Ball Devices: https://missionpinball.com/docs/devices/ball-device/
.. _diverters: https://missionpinball.com/docs/devices/diverter/


