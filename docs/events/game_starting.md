---
title: game_starting
---

# game_starting


--8<-- "event.md"

A game is in the process of starting. This is a queue event, and the
game won't actually start until the queue is cleared.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`game`

:   A reference to the game mode object.
