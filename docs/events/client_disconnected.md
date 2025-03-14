---
title: client_disconnected
---

# client_disconnected


*MPF-MC Event*

Posted on the MPF-MC only (e.g. not in MPF) when the BCP client
disconnects. This event is also posted when the MPF-MC starts before a
client is connected.

This is useful for triggering a slide notifying of the disconnect.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `host`:

The hostname or IP address that the socket is listening on.

#### `port`:

The port that the socket is listening on.
