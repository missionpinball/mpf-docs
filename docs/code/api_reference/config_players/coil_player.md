
# self.machine.coil_player

``` python
class mpf.config_players.coil_player.CoilPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Triggers coils based on config.

### Accessing the coil_player in code

The coil_player is available via `self.machine.coil_player`.

## Methods & Attributes

The coil_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

` clear_context(context)`

Disable enabled coils.

` get_express_config(value: str)`

Parse short config version.

` play(settings, context: str, calling_context: str, priority: int = 0, **kwargs)`

Enable, Pulse or disable coils.
