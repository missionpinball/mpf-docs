---
title: ball_starting
---

# ball_starting


--8<-- "event.md"

A ball is starting. This is a queue event, so the ball won't actually
start until the queue is cleared.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `ball`:

The ball number

#### `balls_remaining`:

The number of balls left in the game (not including this one)

#### `is_extra_ball`:

True if this ball is an extra ball (default False)

#### `player`:

The player number
