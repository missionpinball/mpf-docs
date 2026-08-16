---
title: player_turn_started
---

# player_turn_started


--8<-- "event.md"

A new player's turn started. This event is only posted after the start
of a new player's turn. If that player gets an extra ball and shoots
again, this event is not posted a second time.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `number`:

The player number

#### `player`:

The player object whose turn is starting.
