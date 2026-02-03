---
title: logicblock_(name)_hit
---

# logicblock_(name)\_hit


--8<-- "event.md"

Event is posted by [counters:](../config/counters.md), [accruals:](../config/accruals.md), and [sequences:](../config/sequences.md)

The logic block (name) was just hit.

Note that this is the default hit event for logic blocks, but
this can be changed in a logic block's `events_when_hit:`
setting, so this might not be the actual event that's posted for all
logic blocks in your machine.

#### Deprecation warning:

In previous versions of MPF, the event `counter_(name)_hit` was used for counters instead of this event, `logicblock_(name)_hit`.
Currently, both events are posted together (if you have not provided a custom [`events_when_hit`](../config/counters.md#events_when_hit) value for the counter),
but `counter_(name)_hit` is considered deprecated and may be removed in future versions of MPF.


## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

Accruals, Counters, and Sequences each have different keyword arguments.

### Accrual Keyword arguments

#### `step`:

The 0-based integer number of the step that was just hit.

### Counter Keyword arguments

If the counter has a config setting for `count_complete_value`,
`count`, `hits` and `remaining` towards that goal will be included as arguments.
If `count_complete_value` is `None`, then only `count` will be included.

#### `count`:

The current value of the counter.

#### `hits`:

The numbers of hits made on this counter.

#### `remaining`:

The numbers of hits remaining before completing this counter.

### Sequence Keyword arguments

#### `step`:

The 0-based integer number of the step that was just hit.
