timer_(name)_complete
=====================

*MPF Event*

The timer named (name) has completed.

Note that this timer may reset and start again after this event is
posted, depending on its settings.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``ticks``
  The current tick number this timer is at.

``ticks_remaining``
  The number of ticks in this timer remaining.

