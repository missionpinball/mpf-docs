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

Displaying the value of a timer on a slide
------------------------------------------

If you want to use your timer in a slide you have to set the value to a
player variable first:

.. code-block:: mpf-config

   ##! mode: your_mode
   # in your mode
   timers:
       your_timer:
           start_value: 0
           end_value: 20
           control_events:
               - action: start
                 event: mode_your_mode_started

   variable_player:
      timer_your_timer_tick:
         your_timer_variable_times_100:
            int: device.timers.your_timer.ticks * 100
            action: set

   slides:
       show_timer:
           widgets:
           - type: Text
             text: (player|your_timer_variable_times_100)

In this example we update the player variable ``timer_your_timer_tick``
every time the timer changes based on the tick event.
The value is multiplied by 100 (but you can also omit this or do anything
:doc:`/config_players/variable_player` supports).
Afterwards, you can use the variable in your slide.

Related Events
--------------

.. include:: /events/include_timers.rst
