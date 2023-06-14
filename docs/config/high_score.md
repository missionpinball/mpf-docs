---
title: high_score:
---

# high_score:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `high_score:` section of your config is where you configure the
built-in high score mode. See
[High Scores](../game_logic/high_scores/index.md) for
details.

## Required settings

The following sections are required in the `high_score:` section of your
config:

### categories:

Ordered list for one (or more) sub-settings. Each in the format of
`string` : `list`
([Instructions](instructions/lists.md) for entering lists)

An ordered map of categories which contain a list of awards. See
[High Scores](../game_logic/high_scores/index.md) for an
example.

## Optional settings

The following sections are optional in the `high_score:` section of your
config. (If you don't include them, the default will be used).

### award_slide_display_time:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `4s`

How long should the award slide be displayed?

### defaults:

One or more sub-entries. Each in the format of `string` : `list`
([Instructions](instructions/lists.md) for entering lists)

A map of categories with a list of player/score tuples. See
[High Scores](../game_logic/high_scores/index.md) for an
example.

### enter_initials_timeout:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `20s`

Timeout for the player to enter his/her initials.

### reset_high_scores_events:

List of one (or more) events. The device will add handlers for those
events. Default: `high_scores_reset,factory_reset`

Event to reset high scores. The default is used by the service mode.

### reverse_sort:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

A list of categories where the sort should be inverted. Usually the
highest score is the best but sometimes you want the shortest time or
least amount of shots to be the best score.

## Related How To guides

* [High Scores](../game_logic/high_scores/index.md)
