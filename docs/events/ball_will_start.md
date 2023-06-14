---
title: ball_will_start
---

# ball_will_start


--8<-- "event.md"

The ball is about to start. This event is posted just before
[/events/overview/conditional](ball_starting.md).

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`ball`

:   The ball number

`balls_remaining`

:   The number of balls left in the game (not including this one)

`is_extra_ball`

:   True if this ball is an extra ball (default False)

`player`

:   The player number
