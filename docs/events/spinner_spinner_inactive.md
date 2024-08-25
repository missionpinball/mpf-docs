---
title: spinner_(name)_inactive
---

# spinner_(name)_inactive


--8<-- "event.md"

The spinner (name) is no longer receiving hits

This event will post whenever a spinner has not received hits and its
active_ms has timed out.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`hits`

:   The number of switch hits the spinner had while it was active

Event is posted by [spinners:](../config/spinners.md)
