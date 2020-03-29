Ball Holds
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_holds`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF's *ball holds* are used to temporarily hold a ball that has entered a
:doc:`/mechs/ball_devices/index` while something else happens.

The most common use cases are to hold a ball while you play a show, or while
a video mode is going on. Ball holds do not affect the balls in play count, and
if all other balls drain while a ball hold is in progress, the players ball does
not end.

Ball holds are *not* used to lock balls for multiball.
(See the :doc:`multiball_locks </game_logic/multiballs/multiball_locks>`
device for that).

You can have lots of different ball holds in your game, typically configured
per mode.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball holds is ``device.ball_holds.<name>``.

*balls_held*
   The number of balls this ball hold is currently holding

*enabled*
   Boolean (true/false) which shows whether this ball hold is enabled.

Related How To guides
---------------------

* :doc:`Using ball_holds for a mystery award </game_design/game_modes/mystery_award>`

Related Events
--------------

.. include:: /events/include_ball_holds.rst
