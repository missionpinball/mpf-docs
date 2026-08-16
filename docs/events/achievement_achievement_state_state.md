---
title: achievement_(name)_state_(state)
---

# achievement_(name)\_state_(state)


--8<-- "event.md"

Event is posted by [achievements:](../config/achievements.md)

The achievement called (name) changed to state (state).

Valid states are: `disabled`, `enabled`, `started`, `completed`, `stopped`

This is only posted once per state. Its also posted on restart on the
next ball to restore state and when selection changes.

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
