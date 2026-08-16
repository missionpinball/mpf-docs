---
title: balldevice_(name)_ball_entered
---

# balldevice_(name)\_ball_entered


--8<-- "event.md"

Event is posted by [ball_devices:](../config/ball_devices.md)

A ball (or balls) have just entered the ball device called (name).

The ball was also added to `balls` and `available_balls` of the device.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `device`:

A reference to the ball device object that is posting this event.

#### `new_balls`:

The number of new balls that have not been claimed (by locks or
similar).
