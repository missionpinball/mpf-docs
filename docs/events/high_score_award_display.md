---
title: high_score_award_display
---

# high_score_award_display


--8<-- "event.md"

Event is posted by [high_score](../config/high_score.md) built-in mode
when a player has entered their name for an award.

This event will be posted for every award earned in every category of the game that was just completed.
Prior to MPF 0.80, the category and award information was included in the name of this event and its variants, but with MPF 0.80+ only `high_score_award_display` is used.

If you want to make behaviors unique to the different categories or awards, you can use [conditional events](overview/conditional.md). For example, the default high score configuration includes a "score" category. To write a conditional event binding for only award display events in this category, you would write:

``` yaml
event_player:
  high_score_award_display{category_name=="score"}:
    - my_score_award_granted_behavior
```


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

#### `player_num`:

!!! note "`player_num` added in MPF 0.80"

The number (1-4) of the player.

#### `category_name`:

!!! note "`category_name` added in MPF 0.80"

The name of the overall category of the award.
