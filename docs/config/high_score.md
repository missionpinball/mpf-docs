---
title: "high_score: Config Reference"
---

# high_score: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `high_score:` section of your config is where you configure the
built-in high score mode. See
[High Scores](../game_logic/high_scores/index.md) for
details.

Example section:

``` yaml
#config_version=5
high_score:
  _overwrite: True
  categories: !!omap
  - score:
      - GRAND CHAMPION
      - HIGH SCORE 1
      - HIGH SCORE 2
      - HIGH SCORE 3
      - HIGH SCORE 4
  - loops:
      - LOOP CHAMP
  - hits:
      - MOST HITS
  defaults:
    score:
      - BRI: 4242
      - GHK: 2323
      - JK: 1337
      - QC: 42
      - MPF: 23
    loops:
      - JK: 42
    hits:
      - A: 1
  vars:
    loops:
      - player: number
    hits:
      - player: number
      - machine: credits_string
```

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

How long should the award slide be displayed? If you are not using an award slide,
you should set this to 0.

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

### vars:

(Added in MPF 0.56.1)

One or more sub-entries. Each in the format of `string` : `list`
([Instructions](instructions/lists.md) for entering lists) Defaults
to empty.

By default player name/initials and value of high score entry are 
saved for later use in slides, such as in your attract mode. Adding
additional values here allows for unique variables to be saved.
These can include both player and machine variables.

Entered in the form of variable type: variable name (e.g., player: number)

--8<-- "todo.md"


## Related How To guides

* [High Scores](../game_logic/high_scores/index.md)
