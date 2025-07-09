# show_player API Reference

Config Reference:

* [show_player:](../../../config/show_player.md)

`self.machine.show_player`

``` python
class mpf.config_players.show_player.ShowPlayer(machine)
```

Bases: `mpf.config_players.device_config_player.DeviceConfigPlayer`

Plays, starts, stops, pauses, resumes or advances shows based on config.

## Accessing the show_player in code

The show_player is available via `self.machine.show_player`.

## Methods & Attributes

The show_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`clear_context(context)`

Stop running shows from context.

`get_express_config(value)`

Parse express config.

`handle_subscription_change(value, settings, priority, context, key)`

Handle subscriptions.

`play(settings, context, calling_context, priority=0, **kwargs)`

Play, start, stop, pause, resume or advance show based on config.
