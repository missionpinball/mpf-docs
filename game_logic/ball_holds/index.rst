Ball Holds
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_holds`                                                    |
+------------------------------------------------------------------------------+

MPF's *ball holds* are used to temporarily hold a ball that has entered a
:doc:`/mechs/ball_devices/index` while something else happens.

The most common use cases are to hold a ball while you play a show, or while
a video mode is going on. Ball holds do not affect the balls in play count, and
if all other balls drain while a ball hold is in progress, the players ball does
not end.

Ball holds are *not* used to lock balls for multiball. (See the ``ball_locks:``
device for that.

You can have lots of different ball holds in your game, typically configured
per mode.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/ball_hold_name_balls_released`                                 |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_hold_name_full`                                           |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_hold_name_held_ball`                                      |
+------------------------------------------------------------------------------+
