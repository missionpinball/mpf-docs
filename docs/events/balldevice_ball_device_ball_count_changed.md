---
title: balldevice_(name)_ball_count_changed
---

# balldevice_(name)\_ball_count_changed


--8<-- "event.md"

The ball count for device (name) just changed.

This event may also be called without a change in some circumstances.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `balls`:

The number of new balls in this device.

Event is posted by [ball_devices:](../config/ball_devices.md)
