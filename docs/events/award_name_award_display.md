---
title: (award_name)\_award_display
---

# (award_name)\_award_display


--8<-- "event.md"

Event is posted by [high_score](../config/high_score.md) built-in mode
when a player has entered their name for an award.

This event will be posted along with [(category_name)\_award_display](category_name_award_display.md)
and [high_score_award_display](high_score_award_display.md),
so you can pick whichever name and level of specificity you prefer to hook
on to, and do not need to check for all three.

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
