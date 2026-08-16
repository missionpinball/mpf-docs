---
title: score_award_display
---

# score_award_display


--8<-- "event.md"

Event is posted by [high_score](../config/high_score.md) built-in mode
when a player has entered their name for a score award. This is the standard
record type that is included with the mode, and is actually just the "score"
version of the event [(award_name)\_award_display](award_name_award_display.md).

!!! warning "removed in MPF 0.80"

    As of MPF 0.80, this event has been merged into [high_score_award_display](high_score_award_display.md) and is no longer available by default. Use [conditional events](overview/conditional.md) to attach specific behaviors to the various categories or awards if needed.

    The "score" record type is still supported by default, so the event that will
    come built-in would be matched by the conditional event hook: `high_score_award_display{category_name=="score"}`

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `player_name`:

The letters that the player has entered as their name.

#### `award`:

The name of the award the player earned.

#### `value`:

The number value of the record. This may be score or the custom value used to rank the performance.
