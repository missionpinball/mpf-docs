---
title: balldevice_(name)_ball_enter
---

# balldevice_(name)_ball_enter


--8<-- "event.md"

A ball (or balls) have just entered the ball device called (name).

Note that this is a relay event based on the "unclaimed_balls" arg.
Any unclaimed balls in the relay will be processed as new balls entering
this device.

Please be aware that we did not add those balls to balls or
available_balls of the device during this event.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`device`

:   A reference to the ball device object that is posting this event.

`unclaimed_balls`

:   The number of balls that have not yet been claimed.

Event is posted by [ball_devices:](../config/ball_devices.md)
