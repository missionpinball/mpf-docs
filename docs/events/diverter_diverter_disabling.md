---
title: diverter_(name)_disabling
---

# diverter_(name)\_disabling


--8<-- "event.md"

Event is posted by [diverters:](../config/diverters.md)

The diverter called (name) is disabling itself. Note that if this
diverter has `activation_switches:` configured, it will not physically
deactivate now, instead deactivating based on switch hits and timing.
Otherwise this diverter will deactivate immediately.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `auto`:

Boolean which indicates whether this diverter disabled itself
automatically for the purpose of routing balls to their proper
location(s).
