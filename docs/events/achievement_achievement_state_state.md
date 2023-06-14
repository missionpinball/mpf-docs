---
title: [achievement](../index.md)(name)_[state](../index.md)(state)
---

# [achievement](../index.md)(name)_[state](../index.md)(state)


--8<-- "event.md"

Achievement (name) changed to state (state).

Valid states are: disabled, enabled, started, completed, stopped

This is only posted once per state. Its also posted on restart on the
next ball to restore state and when selection changes.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`restore`

:   true if this is reposted to restore state

`selected`

:   Whatever this achievement is selected currently

`state`

:   Current state

Event is posted by [achievements:](../config/achievements.md)
