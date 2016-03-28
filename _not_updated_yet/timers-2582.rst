
You can configure timers via the `timers:` section of a mode's config
file. This section *cannot* be used in your machine-wide config files.
This section *can* be used in your mode-specific config files. A timer
is kind of like a logic block and posts events every "tick" and counts
up or down. You can configure how fast the timer ticks and whether it
counts up or down, and you can also stop, start, pause, extend, reset,
or change the speed of the timer. Timers don't really do anything on
their own, rather they just post events (at each tick and on
completion) that you can use for other parts of your game logic, like
starting or stopping modes, hurry up scores, display and sound
updates, etc. Here's an example of a timer that's used to stop a timed
skillshot mode:


::

    
    timers:
        mode_timer:
            start_value: 5
            end_value: 0
            direction: down
            tick_interval: 1.5s
            control_events:
              - event: sw_pop
                action: pause
                value: 2
              - event: balldevice_playfield_ball_enter
                action: start




<name>:
~~~~~~~

Each timer has a sub-entry in the `Timers:` section of the mode config
file. You can name this timer whatever you want (and it's name it
based on whatever the sub-entry is). The name is used to construct the
various MPF events this timer posts. (The timer in the above example's
name is "mode_timer.")



start_value:
~~~~~~~~~~~~

This is the default value the timer starts at (and the value it goes
to when it's reset). The default is 0. If the timer is configured to
count down, then set this start_value to something other than 0.



start_running:
~~~~~~~~~~~~~~

True/False (or yes/no) as to whether this timer should start start
running as soon as the mode starts. If no, then this timer won't start
until one of the control events is posted to start it. Default is
False.



end_value:
~~~~~~~~~~

When the timer hits this value, it will post a `timer_<name>_complete`
event. The default setting for the end_value is 0, so if you have a
count down timer then it will post its complete event when it gets to
0. If you have a count up timer and no end_value specified, it will
count up forever (or until you stop it or the mode ends).



direction:
~~~~~~~~~~

Specifies whether this timer counts up or counts down. The default is
to countup, but you can enter `direction: down` to create a timer that
counts down.



tick_interval:
~~~~~~~~~~~~~~

An `MPF time string`_ which specifies how long each "tick" of the
timer is. The default is 1 second, but you can set this to whatever
you want. This is an easy way to set timers to run in what we call
"pinball time" where a countdown modes count much slower than real-
world time. (For example, you might have a 30-second hurry up mode
that starts a countdown timer on the display from 10 to zero, but
really each "tick" is 3 seconds.)



control_events:
~~~~~~~~~~~~~~~

This is a list of event/action/value pairs that control the behavior
of the timer. Looking atthe example above, when the event
`balldevice_playfield_ball_enter` event is posted, the timer will
start. When the event `sw_pop` is posted, the timer will pause for 2
seconds. Notice that you enter multiple control events in MPF's "list
of lists" format with a minus sign and space denoting each new group
of settings. Settings for control events include:



event:
``````

The name of the event that will cause this control action to take
place.



action:
```````

The name of the action type this event will cause. Valid options
include:


+ `add` - Adds time (specified in the "value" entry below) to the
  timer.
+ `subtract` - Removes time (specified in the "value" entry below) to
  the timer.
+ `jump` - Sets the timer to a specific time(specified in the "value"
  entry below).
+ `start` - Starts the timer. Posts the MPF event
  `timer_<name>_started`. Use this to start a timer that was previously
  stopped or paused.
+ `stop` - Stops the timer.Posts the MPF event `timer_<name>_stopped`.
+ `pause` - Pauses the timer for the amountof timespecified in the
  "value" entry below.Posts the MPF event `timer_<name>_paused`. If you
  don't specify the pause time,it pauses for an indefinite amount of
  time. (This is essentially the same as stopping the timer, with the
  only different being the names of events that get posted.)
+ `set_tick_interval` - Sets a new value for the tick interval.
+ `change_tick_interval` - Adds or subtracts the new time value to the
  current tick interval.




value:
``````

The optional value that goes along with the action above.



restart_on_complete:
~~~~~~~~~~~~~~~~~~~~

If True, automatically restarts this timer when it hits the end.

.. _MPF time string: https://missionpinball.com/docs/configuration-file-reference/entering-time-duration-values/


