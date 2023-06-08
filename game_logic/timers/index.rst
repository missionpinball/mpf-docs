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

.. code-block:: mpf-mc-config

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
   slide_player:
     mode_your_mode_started: show_timer
   ##! test
   #! start_game
   #! start_mode your_mode
   #! advance_time_and_run .1
   #! assert_text_on_top_slide 0
   #! advance_time_and_run 1
   #! assert_text_on_top_slide 100

In this example we update the player variable ``timer_your_timer_tick``
every time the timer changes based on the tick event.
The value is multiplied by 100 (but you can also omit this or do anything
:doc:`/config_players/variable_player` supports).
Afterwards, you can use the variable in your slide.

Displaying the value of a timer in minutes and seconds
------------------------------------------------------

If you want to have the value of your timer be displayed as minutes and seconds, you'll need to breakup the display value into two parts: 1 for the value of the minutes and one for the seconds. This means that instead of a single variable, you'll need to define two separate variables. And then, in order to have them display together as one would expect, you'll call them both within the same text widget within your slide_player. Below is an example of how this could be done:

.. code-block:: mpf-mc-config

   ##! mode: your_mode
   # in your mode
   timers:
      song01_intro_timer:
         start_value: 71
         end_value: 0
         direction: down
         tick_interval: 1s
         control_events:
            - action: start
            event: mode_song01_intro_started

   variable_player:
      timer_song01_intro_timer_tick:
         song01_intro_timer_minutes:
            int: device.timers.song01_intro_timer.ticks / 60
            action: set
         song01_intro_timer_seconds:
            int: device.timers.song01_intro_timer.ticks % 60
            action: set

   slide_player:
      mode_song01_intro_started:
         widgets:
         - type: text
           text: 'Time Left: (player|song01_intro_timer_minutes)'
           font_size: 72
           font_name: Teal_DarkBlue_72px_86lh
           bitmap_font: true
           anchor_x: left
           anchor_y: bottom
           x: 100
           y: 906
         - type: text
           text: ':'
           font_size: 72
           font_name: Teal_DarkBlue_72px_86lh
           bitmap_font: true
           anchor_x: left
           anchor_y: bottom
           x: 350
           y: 906
         - type: text
           text: '(player|song01_intro_timer_seconds)'
           min_digits: 2
           font_size: 72
           font_name: Teal_DarkBlue_72px_86lh
           bitmap_font: true
           anchor_x: left
           anchor_y: bottom
           x: 365
           y: 906
   ##! test
   #! start_game
   #! start_mode your_mode
   #! advance_time_and_run .1
   #! assert_text_on_top_slide 0
   #! advance_time_and_run 1
   #! assert_text_on_top_slide 100


In this example we create a variable called ``song01_intro_timer_minutes`` and another variable called ``song01_intro_timer_seconds`` and then have separate definitions for how each is calculated into minutes and seconds via the following lines that begin with ``int:``. We then reference those variables within our text widget on the slide we show during this mode. In order to have the seconds appear with the expected minimum two digits, we need to use the ``min_digits`` setting on our text widget. This setting only works on a text widget that ONLY contains an integer. This means we cannot combine it in the same text widget as our "minutes" variable. And the ":" character also needs to be called within its own text widget. All of these will then need to be aligned manually next to each other within our slide using x and y coordinate values. This will then correctly display our timer value as ``minutes:seconds`` as one would expect (ie ``2:09``)

Related Events
--------------

.. include:: /events/include_timers.rst
