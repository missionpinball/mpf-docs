---
title: Variable player
---

# Variable player

* [variable_player: Config Reference](../config/variable_player.md)

The `variable_player` is a [config player](index.md) that's used to set
the value of player and machine variables. This is commonly used for
scoring in your machine.

See [variable_player](../config/variable_player.md) for more detailed information.

See our [player variables reference](../player_vars/index.md) and
[machine variables reference](../machine_vars/index.md) to learn about existing variables. You can also create
player variables on the fly if they did not exist. If you want to define
defaults for variables you may define them in the [player_vars:](../config/player_vars.md) or
[machine_vars:](../config/machine_vars.md) sections.

## Usage in config files

In config files, the variable player is used via the `variable_player:` section.

## Usage in shows

In shows, the variable player is used via the `variables:` section of a step.

## Related Pages:

* [variable_player API Reference](../code/api_reference/config_players/variable_player.md)
