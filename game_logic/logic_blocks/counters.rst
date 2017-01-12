Counter Logic Blocks
====================

"Counters" are :doc:`logic blocks </game_logic/logic_blocks/index>`
that track the number of times a certain event happens towards the
progress of a completion goal.

Examples include:

* Hit a target (or shot) X number of times to advance.
* Hit pop bumpers 75 times to start a Super Jets mode.
* Counting the number of combos made
* Keeping track of a bonus multiplier (maybe you use the shot group lane
  completion event to count progress towards the bonus multiplier, but you
  configure the max count to be 6, and then if it's hit again, you award
  an extra ball).

You can use optional parameters to specify whether multiple occurrences in
a very short time-frame should be grouped together and counted as one
hit, the counting interval, and whether this counter counts up or
down.

Here's an example of a counter you could use to track progress towards super
jets:

::

    logic_blocks:
        counters:
            super_jets:
                count_events: sw_pop
                events_when_hit: pop_hit
                starting_count: 75
                count_complete_value: 0
                direction: down
                events_when_complete: super_jets_start

count_events:
~~~~~~~~~~~~~

This is an event (or a :doc:`list of events </config/instructions/lists>`) that, when posted, will
increment or decrement the count for this Counter.

Note that if you include multiple events in this list, *any* one of the events being
posted will cause the hit count to increase. If you want to track
different kinds of events separately, use an :doc:`Accrual <accruals>` or
:doc:`Sequence <sequences>` Logic Block instead.

This setting is required.

count_complete_value:
~~~~~~~~~~~~~~~~~~~~~

When the Counter exceeds (or gets below if you're counting down) this
value, it will post its "complete" event and be considered complete.

Default is ``None``.

multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~

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

count_interval:
~~~~~~~~~~~~~~~

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

This is either ``up`` or ``down`` and specifies whether this counter
counts up or counts down.

Default is ``up``.

starting_count:
~~~~~~~~~~~~~~~

This is the starting value of the Counter and the value it goes back
to when it's reset. Default is zero. If you're configuring a counter
with ``direction: down``, you'll want to also set this to something
more than zero.

Default is ``0``.

.. include:: common.rst
