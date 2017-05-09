Multiballs
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/multiballs`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/multiball_locks`                                               |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF includes a *multiball* feature which can be used to automatically start and
stop multiballs.

Each multiball in MPF has a separate name. There are several different types of
multiballs (run until a single ball is left, timed multiballs, etc.) Multiballs
can also be configured with multiball saves so that (for example) any balls
lost in the first 15 seconds of a multiball are automatically re-launched back
into play.

MPF also supports stacking of multiple multiballs at the same time.

Balls can be locked for multiball with the related :doc:`multiball_locks` config
section.

Common Issues
-------------

Why does MPF wait about 10s when adding balls to the playfield from the trough
during a multiball?
   When MPF adds a ball to the playfield the launcher waits until the ball is
   confirmed to be on the playfield. For the first ball this happens when a
   playfield switch is hit after the eject. However, this will not work with
   more than one ball on the playfield (e.g. during a multiball). In this case,
   the launcher will wait until its eject timeout passed (
   :doc:`eject timeouts in ball_devices </config/ball_devices>`) which defaults
   to 10s. Therefore, you need to tune ``eject_timeouts`` of your launcher to
   fix this issue.


Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for multiballs is ``device.multiballs.<name>``.

*balls_added_live*
   Numeric value of how many balls this multiball added into play.

*balls_live_target*
   Numeric value of how many balls this multiball is attempting to keep in play.

*enabled*
   Boolean (true/false) as to whether this multiball is enabled.

*shoot_again*
   Boolean (true/false) as to whether this multiball is in "shoot again" mode which
   means it's attempting to keep live.

Related How To guides
---------------------

* :doc:`multiball_with_traditional_ball_lock`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`add_a_ball_multiball`
* :doc:`multiball_with_virtual_ball_lock`
* :doc:`multiball_with_multiple_lock_devices`

Related Events
--------------

* :doc:`/events/multiball_name_ended`
* :doc:`/events/multiball_name_lost_ball`
* :doc:`/events/multiball_name_shoot_again`
* :doc:`/events/multiball_name_shoot_again_ended`
* :doc:`/events/multiball_name_started`

.. toctree::
   :hidden:

   multiball_locks
   multiball_with_traditional_ball_lock
   multiball_with_virtual_ball_lock
   add_a_ball_multiball
   multiball_with_virtual_ball_lock
   multiball_with_multiple_lock_devices
