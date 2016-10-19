hello (BCP command)
===================

**Parameters:** version=xxx **Origin:** Pin controller or media
controller **Response:** See below This is the initial handshake
command upon first connection as described above. It sends the
protocol version that the origin controller speaks. When received by
the media controller, this command automatically triggers a hard
“reset”, described below. If the pin controller is sending this
command, the media controller will respond with either its own “hello”
command, or the error “unknown protocol version.” The pin controller
should never respond to this command when it receives it from the
media controller; that would trigger an infinite loop.