
A *counter* is a type of `logic block`_ that tracks the number of
times an event is postedtowards the progress of a completion goal. You
can use optional parameters to specify whether multiple occurrencesin
a very short time-frame should be grouped together and counted as one
hit, the counting interval, and whether this counter counts up or
down. This sectioncan be used in your machine-wide config files. This
sectioncan be used in your mode-specific config files. Counter logic
blocks can be used for things like counting total combos made,
counting down progression towards super jets, etc. Here's an example
of a counter you could use to track progress towards super jets:


::

    
    logic_blocks:
        counters:
            super_jets:
                count_events: sw_pop
                event_when_hit: pop_hit
                starting_count: 75
                count_complete_value: 0
                direction: down
                events_when_complete: super_jets_start


Some settings for Logic Blocks apply to all logic blocks, so you can
`read about them there`_, including:


+ The "name" of the counter (e.g. "tilt" or "super_jets" in the
  examples above)
+ enable_events
+ disable_events
+ reset_events
+ events_when_complete
+ restart_on_complete
+ disable_on_complete
+ reset_each_ball




"Counter"-specific settings
---------------------------

In addition to the general Logic Block settings, the Counter type of
logic block has the following specific settings:



count_events:
~~~~~~~~~~~~~

This is an event (or a list of events) that, when posted, will
increment or decrement the count for this Counter. Note that if you
include multiple events in this list, *any* one of the events being
posted will cause the hit count to increase. (If you want to track
different kinds of events separately, use an Accrual or Sequence Logic
Block instead.)



event_when_hit:
~~~~~~~~~~~~~~~

This is the name of the event that will be automatically posted when
when this Counter tracks a hit. The name of this event can be whatever
you want (since this Counter is the one that's posting it). Note this
event will be posted with aparameter "count" which will be set to the
integer value of counter, so make sure that any handlers that have
registered for this event are expecting that parameter.



count_complete_value:
~~~~~~~~~~~~~~~~~~~~~

When the Counter exceeds (or gets below if you're counting down) this
value, it will post its "complete" event and be considered complete.



multiple_hit_window:
~~~~~~~~~~~~~~~~~~~~

This is an `MPF time value string`_ that will be used to group
together multiple *count_events*as if they were one single event. So
if the *multiple_hit_window* isset to *500ms* and you get three hit
events 100ms apart, they will all count as one hit. Note that
subsequent hits that come in during the time window do not extend the
time. So with the 500ms hit_window from above, the first hit counts
and sets the timer, another hit 300ms later won't count, but a third
hit 300ms after the second (and 600ms after the initial hit) will
count (and it will set its own 500ms timer to ignore future hits).



player_variable:
~~~~~~~~~~~~~~~~

This lets you specify the name of the player variable that will hold
the count progress for this counter. If you don't specify a name, the
player variable used will be called *<counter_name>_count*.



count_interval:
~~~~~~~~~~~~~~~

Let's you specify what the count change is for each hit. (In other
words, this is how much is added or removed from the count with each
hit). Default is 1, but you can make it whatever you want if you want
your count to increase by more or less than one whenever a count event
occurs. You could use this, for example, in a mode to create a counter
that tracks the value of a shot. Maybe it starts at 2,000,000, but
each shot a playfield standup increases the value by 250,000.



direction:
~~~~~~~~~~

This is either `up` or `down` and specifies whether this counter
counts up or counts down.



starting_count:
~~~~~~~~~~~~~~~

This is the starting value of the Counter and the value it goes back
to when it's reset. Default is zero. If you're configuring a counter
with a direction of *down*, you'll want to also set this to something
more than zero.

.. _logic block: https://missionpinball.com/docs/mpf-core-architecture/system-modules/logic-blocks-manager/
.. _MPF time value string: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/
.. _read about them there: https://missionpinball.com/docs/configuration-file-reference/logicblocks/%20


