---
title: balldevice_(name)_ejecting_ball
---

# balldevice_(name)\_ejecting_ball


--8<-- "event.md"

The ball device called (name) is ejecting a ball right now.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `balls`:

The number of balls that are to be ejected.

#### `mechanical_eject`:

Boolean as to whether this is a mechanical eject.

#### `num_attempts`:

How many eject attempts have been tried so far.

#### `source`:

The source device that will be ejecting the balls.

#### `target`:

The target ball device that will receive these balls.

Event is posted by [ball_devices:](../config/ball_devices.md)
