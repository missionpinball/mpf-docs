timer_control_events:
=====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``timer_control_events:`` section of your config is where you configure control events for your :doc:`timer <timers>`.

They're entered as a list (with dashes) under the ``control_events:`` section. All control events have an
``event:`` and ``action:`` setting. (When the "event" is posted, the "action" is taken. Some actions require
an additional ``value:`` setting. For example, for the "add" action which adds time, you need to to specify
how much time you want to add. But other actions, like "start" or "stop" don't need values.

Here's an example of control events in action:

.. code-block:: mpf-config

   ##! mode: mode1
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

.. config


Required settings
-----------------

The following sections are required in the ``timer_control_events:`` section of your config:

action:
~~~~~~~
Single value, type: one of the following options: add, subtract, jump, start, stop, reset, restart, pause, set_tick_interval, change_tick_interval, reset_tick_interval.

Take a look at the various types of actions you can perform on timers with control events:

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

event:
~~~~~~
Single value, type: ``string``.

The event which will trigger this value.


Optional settings
-----------------

The following sections are optional in the ``timer_control_events:`` section of your config. (If you don't include them, the default will be used).

value:
~~~~~~
Single value, type: ``number`` or ``template`` (will be converted to floating point; :doc:`Instructions for entering templates </config/instructions/dynamic_values>`).

The value for this ``action``.
Not all actions require a value (i.e. ``start`` and ``stop`` do not).
You can use placeholders here to calculate it during runtime.


Related How To guides
---------------------

* :doc:`/game_logic/timers/index`
