Ball Saves
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_saves`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

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

This is an example:

.. code-block:: mpf-config

    ball_saves:
      random_ball_save:
        active_time: 5s
        hurry_up_time: 2s
        grace_period: 2s
        enable_events: event_on_dangerous_action
        auto_launch: yes
        balls_to_save: 1

When ``event_on_dangerous_action`` is posted the ball save will be active for
5s ``active_time`` + 2s ``grace_period`` = 7s.
Hurry up will start after 5s ``active_time`` - 2s ``hurry_up_time`` = 3s.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for ball saves is ``device.ball_saves.<name>``.

*enabled*
   Boolean (true/false) which shows whether this ball hold is enabled.

*saves_remaining*
   How many balls saves are remaining.

*state*
   String value of the state of this ball save. Values will be one of
   the following: *enabled*, *disabled*, *hurry_up*, or *grace_period*.

*timer_started*
   Boolean (true/false) which shows whether the timer is started.

Related How To guides
---------------------

* :doc:`Ball save at ball start </game_logic/ball_start_end/index>`

Related Events
--------------

.. include:: /events/include_ball_saves.rst
