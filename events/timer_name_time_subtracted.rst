timer_(name)_time_subtracted
============================

*MPF Event*

The timer named (name) just had some ticks removed.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``ticks``
  The new current tick number this timer is at.

``ticks_remaining``
  The new number of ticks in this timer remaining.

``time_subtracted``
  How many ticks were just subtracted from this timer. (This number will be positive, indicating the ticks subtracted.)

