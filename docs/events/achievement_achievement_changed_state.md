---
title: achievement_(name)_changed_state
---

# achievement_(name)\_changed_state


--8<-- "event.md"

The achievement called (name) changed state.

Valid states are: disabled, enabled, started, completed, stopped

This is only posted once per state. Its also posted on restart on the
next ball to restore state.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `restore`:

true if this is reposted to restore state

#### `selected`:

Whatever this achievement is selected currently

#### `state`:

Current state

Event is posted by [achievements:](../config/achievements.md)
