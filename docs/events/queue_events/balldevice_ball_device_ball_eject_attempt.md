---
title: balldevice_(name)_ball_eject_attempt
---

# balldevice_(name)\_ball_eject_attempt


!!! note "This is an MPF Event"

    The content on this page is technical documentation for an [MPF Event](../overview/index.md).

Event is posted by [ball_devices:](../../config/ball_devices.md)

The ball device called (name) is attempting to eject a ball (or
balls). This is a queue event. The eject will not actually be attempted
until the queue is cleared.

## Keyword arguments

(See the [Conditional Events](../overview/conditional.md)
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
