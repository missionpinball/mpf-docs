# random_event_player API Reference

`self.machine.random_event_player`

``` python
class mpf.config_players.random_event_player.RandomEventPlayer(machine)
```

Bases: `mpf.core.config_player.ConfigPlayer`

Plays a random event based on config.

## Accessing the random_event_player in code

The random_event_player is available via `self.machine.random_event_player`.

## Methods & Attributes

The random_event_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

Parse express config.

`get_list_config(value)`

Parse list.

`static is_entry_valid_outside_mode(settings) → bool`

Return true if scope is not player.

`play(settings, context, calling_context, priority=0, **kwargs)`

Play a random event from list based on config.

`validate_config_entry(settings, name)`

Validate one entry of this player.
