---
title: player_turn_will_end
---

# player_turn_will_end


--8<-- "event.md"

The player's turn is about to end. This event is only posted when this
player's turn is totally over. If the player gets an extra ball and
shoots again, this event is not posted until after all their extra balls
and it's no longer their turn.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `number`:

The player number

#### `player`:

The player object whose turn is over.
