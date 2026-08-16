---
title: API Reference - queue_event_player
---

# queue_event_player API Reference

`self.machine.queue_event_player`

``` python
class mpf.config_players.queue_event_player.QueueEventPlayer(machine)
```

Bases: `mpf.core.config_player.ConfigPlayer`

Posts queue events based on config.

## Accessing the queue_event_player in code

The queue_event_player is available via `self.machine.queue_event_player`.

## Methods & Attributes

The queue_event_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_express_config(value)`

No express config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Post queue events.

`validate_config_entry(settings, name)`

Validate one entry of this player.

## Related Pages:

* [Queue Events](../../../events/overview/event_types.md#queue-events)
* [queue_event_player: Config Reference](../../../config/queue_event_player.md)
* [Queue Event player Config Player Reference](../../../config/queue_event_player.md)
