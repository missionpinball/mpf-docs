
# self.machine.queue_relay_player

`class mpf.config_players.queue_relay_player.QueueRelayPlayer(machine)`

Bases: mpf.core.config_player.ConfigPlayer

Blocks queue events and converts them to normal events.

## Accessing the queue_relay_player in code

The queue_relay_player is available via `self.machine.queue_relay_player`.

## Methods & Attributes

The queue_relay_player has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`clear_context(context)`

Clear all queues and remove handlers.

`get_express_config(value)`

No express config.

`play(settings, context, calling_context, priority=0, **kwargs)`

Block queue event.

`validate_config_entry(settings, name)`

Validate one entry of this player.

