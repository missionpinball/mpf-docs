timers:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

The ``timers:`` section of your config is where configure timers that can "tick" up or down.
Timers post events with each tick which you can use to update slides, etc. You can set the
start and stop values of the timers, as well as how fast they tick, how much they change per
tick, and other settings.

The settings structure of timers is like this:

.. code-block:: yaml

   timers:
      timer_name:
         <settings>
      some_other_timer_with_a_different_name:
         <settings>
      a_third_timer:
         <settings>

Here's an example timers: section from the "Money Bags" mode in *Brooks 'n Dunn* which
contains two timers:

.. code-block:: yaml

   timers:
       mb_intro_timer:
           start_value: 3
           end_value: 0
           direction: down
           control_events:
               - action: start
                 event: mode_money_bags_started
       money_bags_timer:
           start_value: 15
           end_value: 0
           direction: down
           tick_interval: 1.25s
           control_events:
               - action: start
                 event: timer_mb_intro_timer_complete
               - action: add
                 event: money_bags_advertise_flashing_hit
                 value: 5
               - action: stop
                 event: logicblock_money_bags_counter_complete

In the example above, an intro timer which runs for 3 seconds is started by the event
*mode_money_bags_started* (which means this timer starts when the mode starts).
A second timer (the "money_bags_timer") starts when the intro timer is complete. It starts
with a value of 15 and counts down to 0 (but at a count interval of 1.25 seconds so it's
a bit slower than real time. It will also get reset back to 15 each time a flashing shot
is hit.

Here's another example of timers from *Demo Man's* skillshot mode:

.. code-block:: yaml

   timers:
     mode_timer:
       start_value: 3
       end_value: 0
       direction: down
       tick_interval: 1s
       control_events:
       - event: balldevice_playfield_ball_enter
         action: start
       start_running: false
     target_rotator:
       start_running: true
       tick_interval: 1s

The skillshot mode starts when the ball is waiting to be plunged. The timer called
"mode_timer" in the example above starts when the ball enters the playfield and runs
for 3 seconds. If it runs all the way down, the skill shot mode will stop (meaning
the player missed the skillshot).

A second timer doesn't have any count values associated with it, rather it just "ticks"
once a second. That tick event is used to rotate the lit skillshot.

Settings
--------

Individual timers can use the following options:

bcp:
~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether the various timer events (count, start, stop, complete, etc.) are sent to the MPF-MC via BCP.

TODO Is this needed? If a slide_player, etc. uses one of these events, then they'll automatically be sent to the MC?

control_events:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: sub-configuration containing control_events settings. Default: ``None``

Timer control events is where you specify what happens to this timer when other events are posted.

They're entered as a list (with dashes) under the ``control_events:`` section. All control events have an
``event:`` and ``action:`` setting. (When the "event" is posted, the "action" is taken. Some actions require
an additional ``value:`` setting. For example, for the "add" action which adds time, you need to to specify
how much time you want to add. But other actions, like "start" or "stop" don't need values.

Take a look at the various types of actions you can perform on timers with control events:

Options:

``add``
   Adds the time (specified in the ``value:`` setting) to the timer. If the value would be higher than the timer's ``max_value:`` setting, then the
   value is set to the max value. Posts the *timer_<name>_time_added* event.

   This action does not change the timer's running state.

   The timer is checked for done after the value has been added. (So, for example, if you have a timer
   that's set to count up, and the timer finishes at 10, and the timer is currently at 6, and you add value
   of 5, then the timer will be complete.

``subtract``
   Subtracts time (specified in the ``value:`` setting) from the timer. Posts the *timer_<name>_time_subtracted* event and checks to see if the
   timer is complete.

``jump``
   "Jumps" the timer to a specific new value (specified in the ``value:`` setting) and checks to see if the timer is complete.

``start``
   Starts the timer if it's not running. Does nothing if the timer is already running.
   Posts the *timer_<name>_started* event.

``stop``
   Stops the timer and posts the *timer_<name>_stopped* event. Removes any outstanding "pause" delays.

``reset``
   Changes the timers current value back to the ``start_value:``. Nothing else is touched, so if the
   timer is running, it stays running, etc.

``restart``
   Acts as a combination of reset, then start.

``pause``
   Pauses the timer for a given ``value:`` time (in seconds). Note that the timer pause value is
   real world seconds and does not take the timers tick interval into consideration. If the pause
   value is 0, the timer is paused indefinitely. Posts the *timer_<name>_paused* event.

``set_tick_interval``
   Sets the tick interval to a new value (specified in the ``value:`` setting).

``change_tick_interval``
   Changes the tick interval by multiplying the current tick interval by the new one specified in the ``value:`` setting.
   In other words, if you want to make the tick interval 10% faster, than set this to ``value: 1.1``. If you want to make it
   50% slower, set this to ``value: 0.5``, etc.

``reset_tick_interval``
   (added in MPF 0.33)

   Resets the timer's tick interval back to the original from the ``tick_interval:`` setting.

Here's an example of control events in action:

.. code-block:: yaml

   timers:
      my_timer:
         direction: down
         start_value: 10
         tick_interval: 125s
         control_events:
            - event: start_my_timer
              action: start
            - event: reset_my_timer
              action: reset
            - event: add_5_secs
              action: add
              value: 5

In the example above, when the event *start_my_timer* is posted, the timer called "my_timer" will start
running. When the event *add_5_secs* is posted, 5 seconds will be added to whatever the current value of "my_timer"
is, etc.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

If true/yes, adds additional logging information to the verbose log for this timer.

direction:
~~~~~~~~~~
Single value, type: ``string``. Default: ``up``

Controls which direction this timer runs in. Options are ``up`` or ``down``.

end_value:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

Specifies what the final value for this timer will be. When the timer value equals or exceeds this (for timers counting
up), or when it equals or is lower than this (for timers counting down), the *timer_<name>_complete* event is
posted and the timer is stopped. (If the ``restart_on_complete:`` setting is true, then the timer is also reset
back to its ``start_value:`` and started again.)

Note that you can use a :doc:`placeholder value </config/instructions/placeholders>`
for this setting.

max_value:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

The maximum value this timer can be. If you try to add value above this, the timer's value will be reset
to this value.

restart_on_complete:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls what should happen when this timer completes. If you have ``restart_on_complete: true``, then
this timer will reset back to the start_value and start again after it completes.

start_running:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether this timer starts running ("started"), or whether it needs to be started with one of the
start control events.

start_value:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The initial value of the timer.

Note that you can use a :doc:`placeholder value </config/instructions/placeholders>`
for this setting.

tick_interval:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1s``

A time value for how fast each tick is. The default is 1 second, but quite often "pinball time" is slower
than real world time, and a countdown timer will actually tick a speed that's slower than 1 second per
tick. (So in that case, you might set ``tick_interval: 1.25s`` or something like that. You can also set this
really short if you want a hurry up, maybe every 100ms removed 77,000 worth of points or something.

