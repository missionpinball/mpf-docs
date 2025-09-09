---
title: queue_event_complete
---

# queue_event_complete


--8<-- "event.md"

A queue event has completed and normal behavior will resume. This is posted
by the `queue_event_player` when no [`events_when_finished`](../config/queue_event_player.md#events_when_finished) is provided.
If you have defined custom `events_when_finished`, this event name will not be posted,
but the custom names you have picked will have the following keyword arguments included.

This is *NOT* itself a queue event.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `queue_event`:

The name of the queue event that 

#### `**args`:

Additional args may be provided if you have configured them
via [`args`](../config/queue_event_player.md#args)
