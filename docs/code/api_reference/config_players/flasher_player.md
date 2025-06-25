
# self.machine.flasher_player

``` python
class mpf.config_players.flasher_player.FlasherPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Triggers flashers based on config.

## Accessing the flasher_player in code

The flasher_player is available via `self.machine.flasher_player`.

## Methods & Attributes

The flasher_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

Parse express config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Flash flashers.
