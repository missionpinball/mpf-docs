---
title: game_start
---

# game_start


--8<-- "event.md"

Starts game while bypassing the many systems which have to "approve"
the start. (Are the balls in the right places, are there enough credits,
etc.) Use of this method is not recommended but may be useful in testing
code. Instead, use the *request_to_start_game* event.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`buttons`

:   A list of switches tagged with *player* that were held in when the
    start button was released. This is used for "alternate" game
    starts (e.g. hold the right flipper and press start for tournament
    mode, etc.)

`hold_time`

:   The time, in seconds, that the start button was held in to start the
    game. This can be used to start alternate games via a "long press"
    of the start button.
