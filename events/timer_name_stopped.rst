timer_(name)_stopped
====================

*MPF Event*

The timer named (name) has stopped.

This event is posted any time the timer stops, whether it stops because
it ended or because it was stopped early by some other event.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``ticks``
  The current tick number this timer is at.

``ticks_remaining``
  The number of ticks in this timer remaining.

