timers:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``timers:`` section of your config is where configure
:doc:`timers </game_logic/timers/index>` that can "tick" up or down.
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

.. code-block:: mpf-config

   ##! mode: mode1
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

.. code-block:: mpf-config

   ##! mode: mode1
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

See :doc:`timer_control_events` for more details about all the actions available in a timer.

.. config


Optional settings
-----------------

The following sections are optional in the ``timers:`` section of your config. (If you don't include them, the default will be used).

bcp:
~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether the various timer events (count, start, stop, complete, etc.) are sent to the MPF-MC via BCP.

control_events:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: :doc:`timer_control_events <timer_control_events>`. Defaults to empty.

Timer control events is where you specify what happens to this timer when other events are posted.
See :doc:`timer_control_events` for more details.

direction:
~~~~~~~~~~
Single value, type: one of the following options: up, down. Default: ``up``

Controls which direction this timer runs in. Options are ``up`` or ``down``.

end_value:
~~~~~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Defaults to empty.

Specifies what the final value for this timer will be. When the timer value equals or exceeds this (for timers counting
up), or when it equals or is lower than this (for timers counting down), the *timer_<name>_complete* event is
posted and the timer is stopped. (If the ``restart_on_complete:`` setting is true, then the timer is also reset
back to its ``start_value:`` and started again.)

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>`
for this setting.

max_value:
~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

The maximum value this timer can be. If you try to add value above this, the timer's value will be reset
to this value.

restart_on_complete:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls what should happen when this timer completes. If you have ``restart_on_complete: true``, then
this timer will reset back to the start_value and start again after it completes.

start_running:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether this timer starts running ("started"), or whether it needs to be started with one of the
start control events.

start_value:
~~~~~~~~~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``0``

The initial value of the timer.

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>`
for this setting.

tick_interval:
~~~~~~~~~~~~~~
Single value, type: ``time string (secs) or template`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>` and :doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``1s``

A time value for how fast each tick is. The default is 1 second, but quite often "pinball time" is slower
than real world time, and a countdown timer will actually tick a speed that's slower than 1 second per
tick. (So in that case, you might set ``tick_interval: 1.25s`` or something like that. You can also set this
really short if you want a hurry up, maybe every 100ms removed 77,000 worth of points or something.

.. include:: template_setting.rst

.. toctree::
   :maxdepth: 1
   :hidden:

   timer_control_events: <timer_control_events>

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If true/yes, adds additional logging information to the verbose log for this timer.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/timers/index`
