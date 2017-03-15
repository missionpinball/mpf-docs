Timers
======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/timers`                                                        |
+------------------------------------------------------------------------------+

MPF config files include the concept of "timers" which you can use to count
towards a specific event based on time. Timers can be configured to count up
or down, at whatever interval you want, at any speed you want. You can use
events to start, stop, pause, reset, or change their speed.

Timers post events with each "tick" which you can use to update the display,
play sounds, etc. They also post events when they complete which you can use
to stop a mode, play a show, etc.

Example uses of timers might include:

* Hurry up count down to make a shot (with variable score based on how much
  time is left).
* Timer to end a timed mode.
* A timer which ticks periodically to rotate a lit shot left or right.
* Etc.

The example config files section of the documentation contains
:doc:`examples of timers in modes </examples/timer/index>`.

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/timer_name_complete`                                           |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_paused`                                             |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_started`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_stopped`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_tick`                                               |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_time_added`                                         |
+------------------------------------------------------------------------------+
| :doc:`/events/timer_name_time_subtracted`                                    |
+------------------------------------------------------------------------------+
