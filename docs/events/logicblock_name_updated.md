---
title: logicblock_(name)_updated
---

# logicblock_(name)\_updated


--8<-- "event.md"

Event is posted by [counters:](../config/counters.md), [accruals:](../config/accruals.md), and [sequences:](../config/sequences.md)

The logic block called (name) has changed.

This might happen when the block advanced, was reset, or was restored.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `enabled`:

Whatever this block is enabled or not.

#### `value`:

The current value of this block.
