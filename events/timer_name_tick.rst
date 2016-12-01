timer_(name)_tick
=================

*MPF Event*

The timer named (name) has just counted down (or up,
depending on its settings).

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``ticks``
  The new tick number this timer is at.

``ticks_remaining``
  The new number of ticks in this timer remaining.

