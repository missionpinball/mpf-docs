client_disconnected
===================

*MPF Event*

Posted on the MPF-MC only (e.g. not in MPF) when the BCP
client disconnects. This event is also posted when the MPF-MC
starts before a client is connected.

This is useful for triggering a slide notifying of the
disconnect.

Keyword arguments
-----------------

host
~~~~
The hostname or IP address that the socket is listening
on.

port
~~~~
The port that the socket is listening on.

