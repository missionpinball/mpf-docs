timer_(name)_stopped (MPF event)
================================

The timer named (name) has stopped.

This event is posted any time the timer stops, whether it stops because
it ended or because it was stopped early by some other event.

Keyword arguments:

ticks
~~~~~
The current tick number this timer is at.

ticks_remaining
~~~~~~~~~~~~~~~
The number of ticks in this timer remaining.

