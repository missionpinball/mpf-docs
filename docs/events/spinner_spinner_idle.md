---
title: [spinner](../index.md)(name)_idle
---

# [spinner](../index.md)(name)_idle


--8<-- "event.md"

The spinner (name) is now idle

This event will post whenever a spinner has not received hits and its
idle_ms has timed out. If no idle_ms is defined, this event will not
post.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`hits`

:   The number of switch hits the spinner had while it was active

Event is posted by [spinners:](../config/spinners.md)
