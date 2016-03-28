
MPF's BCP interface is responsible for connecting the MPF game engine
to other processes via the `Backbox Display Protocol`_ (BCP). The BCP
interface code is in the *mpf/system/bcp.py module*. MPF's BCP
interface can communicate with multiple BCP servers at the same time,
and it's responsible for receiving messages via BCP and translating
them to MPF actions as well as for watching MPF for actions that
should be sent out to BCP servers and building and sending those
messages. The BCP interface runs as two standalone threads—one for
sending and one for receiving—for each BCP server that MPF is attached
to. (MPF can dynamically connect and disconnect from BCP servers while
its running.)



How MPF's BCP interface works
-----------------------------



BCP 'get' and 'set' commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+ Incoming *get* commands are turned into events in the format
  *bcp_get_<name>*. It's up to an event handler to register for that
  event and to send the response BCP *set* command.
+ Incoming * set * commands are turned into events in the format
  *bcp_set_<name>* with a parameter *value=<value>*. It's up to an event
  handler to register for that event and to do something with it.


Note that BCP *set* commands can contain multiple key/value pairs, and
separate events will be posted for event for each pair

.. _Backbox Display Protocol: https://missionpinball.com/docs/mpf-core-architecture/media-controllers/bcp1-0-spec/


