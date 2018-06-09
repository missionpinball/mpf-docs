counters:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

+------------------------------------------------------------------------------+
| Related Tutorial                                                             |
+==============================================================================+
| :doc:`/game_logic/logic_blocks/integrating_logic_blocks_and_shows`           |
+------------------------------------------------------------------------------+

The ``counters:`` section of your config is where you configure counter logic blocks.
See also :doc:`counters </game_logic/logic_blocks/counters>`.
The structure of counter logic blocks is like this:

.. code-block:: mpf-config

   ##! config: mode1

  counters:
     the_name_of_this_counter:
        count_events: my_count_event
        count_complete_value: 10
     some_other_counter:
        count_events: s_my_switch_active
        starting_count: 50
        count_interval: 10
        count_complete_value: 100

Note that the actual name of the counter doesn't really matter. Mainly
it's used in the logs and for event names.


Required settings
-----------------

The following sections are required in the ``counters:`` section of your config:

count_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`).

This is an event (or a :doc:`list of events </config/instructions/lists>`) that, when posted, will
increment or decrement the count for this Counter.

Note that if you include multiple events in this list, *any* one of the events being
posted will cause the hit count to increase. If you want to track
different kinds of events separately, use an :doc:`Accrual <accruals>` or
:doc:`Sequence <sequences>` Logic Block instead.

This setting is required.


Optional settings
-----------------

The following sections are optional in the ``counters:`` section of your config. (If you don't include them, the default will be used).

count_complete_value:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: template_int.

When the Counter exceeds (or gets below if you're counting down) this
value, it will post its "complete" event and be considered complete.

Default is ``None``.

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>`
for this setting.

.. include:: template_setting.rst

count_interval:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

Specifies the numeric count change is for each hit. In other
words, this is how much is added or removed from the count with each
hit. Default is 1, but you can make it whatever you want if you want
your count to increase by more or less than one whenever a count event
occurs. You could use this, for example, in a mode to create a counter
that tracks the value of a shot. Maybe it starts at 2,000,000, but
each shot a playfield standup increases the value by 250,000.

Default is ``1``.

direction:
~~~~~~~~~~
Single value, type: ``string``. Default: ``up``

This is either ``up`` or ``down`` and specifies whether this counter
counts up or counts down.

Default is ``up``.

multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`) . Default: ``0``

This is an :doc:`MPF time value string </config/instructions/time_strings>`
that will be used to group
together multiple *count_events* as if they were one single event. So
if you have ``multiple_hit_window: 500ms`` and you get three hit
events 100ms apart, they will all count as one hit.

Note that
subsequent hits that come in during the time window do not extend the
time. So with the 500ms hit_window from above, the first hit counts
and sets the timer, another hit 300ms later won't count, but a third
hit 300ms after the second (and 600ms after the initial hit) will
count (and it will set its own 500ms timer to ignore future hits).

Default is ``0`` (which means all hits are counted).

starting_count:
~~~~~~~~~~~~~~~
Single value, type: template_int. Default: ``0``

This is the starting value of the Counter and the value it goes back
to when it's reset. Default is zero. If you're configuring a counter
with ``direction: down``, you'll want to also set this to something
more than zero.

Default is ``0``.

Note that you can use a :doc:`dynamic value </config/instructions/dynamic_values>`
for this setting.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to true to see additional debug output. This might impact the performance of MPF.

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
List of one (or more) values, each is a type: ``string``.

Currently unused.

.. include:: /game_logic/logic_blocks/common.rst


