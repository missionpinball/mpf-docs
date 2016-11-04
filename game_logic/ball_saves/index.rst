Ball Saves
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_saves`                                                    |
+------------------------------------------------------------------------------+

MPF uses *ball saves* to automatically re-serve a ball that has drained. (Essentially
this means the ball drain doesn't count.)

Ball saves are typically used in several scenarios:

* Give the player their ball back if they drain right after their ball starts.
* Give the player their ball back if there's a particularly wicked shot that
  tends to drain which the game designers feel bad about. (You should avoid
  this if possible, and instead, as Lyman Sheets would say, "Fix your f-ing
  game layout!")
* Use to make a timed mode where the player has unlimited drains.
* Etc.

You can configure ball saves to have various start and
stop events and timers, and you can configure multiple ones in
different modes that do different things.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/ball_save_name_disabled`                                       |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_enabled`                                        |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_grace_period`                                   |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_hurry_up`                                       |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_saving_ball`                                    |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_timer_start`                                    |
+------------------------------------------------------------------------------+
