Ball Search
===========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/playfields`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF contains ball search functionality which is used to try to dislodge a stuck
ball if MPF thinks there's a ball loose on the playfield but it hasn't hit any
playfield switches in awhile and the player is not holding the flipper button
in.

Ball searching in MPF has multiple "rounds", with the early rounds doing a
simple search that doesn't screw anything up (like firing pop bumpers and
pulsing eject coils from ball devices that don't contain any balls), but
after a few rounds of that, if it still hasn't found the ball, it can start to
to things like resetting drop targets.

Eventually MPF will give up and mark the ball as lost and kick a new ball
into play.

Everything is fully configurable, including the timeouts, the order devices
are searched, the number of rounds, etc.

Ball search in MPF is fairly automatic. It's enabled when MPF thinks that balls
are on the playfield, and disabled when no balls are free. (This means that
even when a machine tilts, ball search is still active until the balls drain, etc.)

Related How To guides
---------------------
* :doc:`configuring_ball_search`

Related Events
--------------

* :doc:`/events/ball_search_failed`
* :doc:`/events/ball_search_started`
* :doc:`/events/ball_search_stopped`
* :doc:`/events/flipper_cradle`
* :doc:`/events/flipper_cradle_release`


.. toctree::
   :hidden:

   configuring_ball_search
