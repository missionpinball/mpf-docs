---
title: multiball_(name)_restart_grace_period_started
---

# multiball_(name)\_restart_grace_period_started


--8<-- "event.md"

Event is posted by [multiballs:](../config/multiballs.md)

The multiball called (name) is about to end, but has a restart grace period, which it now
is starting. This event is posted when the multiball does not have multiple balls active,
which enables the restart grace period.

If the add a ball is triggered, the multiball will restart instead of ending.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `grace_period`:

The value resolved from the multiball's `restart_grace_period_ms` property.
