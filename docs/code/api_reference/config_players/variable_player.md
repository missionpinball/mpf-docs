---
title: API Reference - variable_player
---

# variable_player API Reference

`self.machine.variable_player`

``` python
class mpf.config_players.variable_player.VariablePlayer(machine: mpf.core.machine.MachineController)
```

Bases: `mpf.core.config_player.ConfigPlayer`

Posts events based on config.

## Accessing the variable_player in code

The variable_player is available via `self.machine.variable_player`.

## Methods & Attributes

The variable_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`clear_context(context: str) → None`

Clear context.

`get_express_config(value: Any) → dict`

Parse express config.

`get_list_config(value: Any)`

Parse list.

`handle_subscription_change(value, settings, priority, context, key)`

Handle subscriptions.

`static is_entry_valid_outside_mode(settings: dict) → bool`

Return true if this entry may run without a game and player.

`play(settings: dict, context: str, calling_context: str, priority: int = 0, **kwargs) → None`

Variable name.

`validate_config_entry(settings: dict, name: str) → dict`

Validate one entry of this player.

## Related Pages:

* [variable_player: Config Reference](../../../config/variable_player.md)
* [Variable player Config Player Reference](../../../config_players/variable_player.md)
