# light_player API Reference

`self.machine.light_player`

``` python
class mpf.config_players.light_player.LightPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Sets lights based on config.

## Accessing the light_player in code

The light_player is available via self.machine.light_player.

## Methods & Attributes

The light_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`clear_context(context)`

Remove all colors which were set in context.

`get_express_config(value)`

Parse express config.

`handle_subscription_change(value, settings, priority, context, key)`

Handle subscriptions.

`play(settings, context, calling_context, priority=0, **kwargs)`

Set light color based on config.

## Related Pages:

* [light_player: Config Reference](../../../config/light_player.md)
* [Light player Config Player Reference](../../../config_players/light_player.md)
