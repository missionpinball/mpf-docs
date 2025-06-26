# hardware_sound_player API Reference

`self.machine.hardware_sound_player`

``` python
class mpf.config_players.hardware_sound_player.HardwareSoundPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Plays sounds on an external sound card.

## Accessing the hardware_sound_player_player in code

The hardware_sound_player_player is available via `self.machine.hardware_sound_player`.

## Methods & Attributes

The hardware_sound_player_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

Parse express config.

`get_string_config(string)`

Parse string config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Play sound on external card.
