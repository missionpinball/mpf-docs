---
title: timer_(name)_tick
---

# timer_(name)\_tick


--8<-- "event.md"

The timer named (name) has just counted down (or up, depending on its
settings).

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `ticks`:

The new tick number this timer is at.

#### `ticks_remaining`:

The new number of ticks in this timer remaining.

Event is posted by [timers:](../config/timers.md)
