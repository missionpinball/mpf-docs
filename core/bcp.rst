BCP
===

MPF's *BCP* module is responsible for interfacing BCP clients to the MPF core engine.

MPF's BCP interface is responsible for connecting the MPF game engine
to other processes via the :doc:`Backbox Display Protocol </bcp/index>` (BCP).
The BCP interface code is in the *mpf/system/bcp.py module*. MPF's BCP
interface can communicate with multiple BCP servers at the same time,
and it's responsible for receiving messages via BCP and translating
them to MPF actions as well as for watching MPF for actions that
should be sent out to BCP servers and building and sending those
messages.
