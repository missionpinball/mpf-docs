# event_player API Reference

Config Reference:

* [event_player:](../../../config/event_player.md)

`self.machine.event_player`

``` python
class mpf.config_players.event_player.EventPlayer(machine)
```

Bases: `mpf.config_players.flat_config_player.FlatConfigPlayer`

Posts events based on config.

## Accessing the event_player in code

The event_player is available via `self.machine.event_player`.

## Methods & Attributes

The event_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

Parse short config.

`get_list_config(value)`

Parse list.

`play(settings, context, calling_context, priority=0, **kwargs)`

Post (delayed) events.
