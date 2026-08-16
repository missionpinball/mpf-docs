---
title: player_turn_starting
---

# player_turn_starting


--8<-- "event.md"

The player's turn is in the process of starting. This is a queue event,
and the player's turn won't actually start until the queue is cleared.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `number`:

The player number

#### `player`:

The player object whose turn is starting.
