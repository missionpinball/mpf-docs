# segment_display_player API Reference

`self.machine.segment_display_player`

``` python
class mpf.config_players.segment_display_player.SegmentDisplayPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Generates texts on segment displays.

## Accessing the segment_display_player in code

The segment_display_player_player is available via `self.machine.segment_display_player`.

## Methods & Attributes

The segment_display_player_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`clear_context(context)`

Remove all texts.

`get_express_config(value)`

Parse express config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Show text on display.
