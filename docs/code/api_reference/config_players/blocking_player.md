
# self.machine.blocking_player

``` python
class mpf.config_players.block_event_player.BlockEventPlayer(machine)
```

Bases: `mpf.core.config_player.ConfigPlayer`

Posts events based on config.

## Accessing the blocking_player in code

The blocking_player is available via `self.machine.blocking_player`.

## Methods & Attributes

The blocking_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

Parse short config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Block event.

`validate_config_entry(settings: dict, name: str) → dict`

Validate one entry of this player.
