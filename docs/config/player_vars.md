---
title: player_vars:
---

# player_vars:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `player_vars:` section of your machine-wide config file lets you
specify the initial state of player variables that are set for a player
when the game starts.

## Required settings

The following sections are required in the `player_vars:` section of
your config:

### initial_value:

Single value, type: `string`. Defaults to empty.

The initial value of this player variable that you're setting. This is
set when the player is created.

## Optional settings

The following sections are optional in the `player_vars:` section of
your config. (If you don't include them, the default will be used).

### value_type:

Single value, type: one of the following options: str, float, int.
Default: `int`

Select one of the options from this list: `int` (integer), `float`, or
`str` (string). The default is "int", and there is no intelligence to
try to detect which type of value you have, so if you have a floating
point number or a string, you also need to set the value_type.

## Related How To guides

* [Tutorial step 15: Add scoring](../tutorial/15_scoring.md)
* [Player Variables Reference](../player_vars/index.md)
* [Scoring](../game_logic/scoring/index.md)
* [Player Variables](../game_logic/players.md)
