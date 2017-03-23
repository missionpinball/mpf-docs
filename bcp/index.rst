BCP protocol & specification
============================

This document describes the Backbox Control Protocol, (or "BCP"), a
simple, fast protocol for communications between an implementation of
a pinball game controller and a multimedia controller.

BCP transmits semantically relevant information and attempts to isolate
specific behaviors and identifiers on both sides. i.e., the pin controller is
responsible for telling the media controller “start multiball mode”. The pin
controller doesn't care what the media controller does with that information,
and the media controller doesn't care what happened on the pin controller
that caused the multiball mode to start.

BCP is versioned to prevent conflicts. Future versions of the BCP will be
designed to be backward compatible to every degree possible. The reference
implementation uses a raw TCP socket for communication. On localhost the
latency is usually sub-millisecond and on LANs it is under 10 milliseconds.
That means that the effect of messages is generally under 1/100th of a
second, which should be considered instantaneous from the perspective of
human perception.

It is important to note that this document specifies the details of the
protocol itself, not necessarily the behaviors of any specific
implementations it connects. Thus, there won’t be details about fonts or
sounds or images or videos or shaders here; those are up to specific
implementation being driven.

.. warning::
   Since the pin controller and media controller are both state
   machines synchronized through the use of commands, it is possible for
   the programmer to inadvertently set up infinite loops. These can be
   halted with the “reset” command or “hello” described below.

Background
----------

The BCP protocol was created as part of the Mission Pinball Framework (MPF)
project. MPF uses BCP to communicate between the MPF pinball controller and
the MPF media controller, though BCP is intended to be an open protocol that
could connect *any* pinball controller to *any* media controller.

We'd like to give a shout-out to Kevin Kelm who was responsible for the initial
concept of BCP and first draft of the specification. As such, he's the guy who
picked the ports (5050 and 5051).

Protocol Format
---------------

+ Commands are human-readable text in a format similar to URLs, e.g.
  `command?parameter1=value&parameter2=value`
+ Commands characters are encoded with the utf-8 character encoding.
  This allows ad-hoc text for languages that use characters past ASCII-7
  bit, such as Japanese Kanji.
+ Commands and parameter names are whitespace-trimmed on both ends by
  the recipient
+ Commands are case-insensitive
+ Parameters are optional. If present, a question mark separates the
  command from its parameters
+ Parameters are in the format name=value
+ Parameter names are case-insensitive
+ Parameter values are case-sensitive
+ Simple parameter values are prefixed with a string that indicates
  their data type: (int:, float:, bool:).  For example, the integer
  5 would appear in the command string as `int:5`.
+ When a command includes one or more complex value types (list or dict)
  all parameters are encoded using JSON and the resulting encoded value
  is assigned to the ``json`` parameter.
+ Parameters are separated by an ampersand
+ Parameter names and their values are escaped using percent encoding
  as necessary; see ``https://en.wikipedia.org/wiki/Percent-encoding``
+ Commands are terminated by a line feed character (`\n`). Carriage
  return characters (`\r`) should be tolerated but are not significant.
+ A blank line (no command) is ignored
+ Commands beginning with a hash character (`#`) are ignored
+ If a command passes unknown parameters, the recipient should ignore
  them.
+ To accommodate Backbox's asynchronous nature, commands may include
  an optional 'id' parameter. This allows subsequent responses to be
  tied back to a specific command. Most situations do not warrant this
  level of tracking, but it may be important in some scenarios, e.g. the
  pinball controller requesting a ‘wave_your_hands_in_the_air’ show, but
  no such show exists. The value of an id may be any string up to 32
  characters. When the id parameter is not present in a command, that
  command’s value is used for any response id (just the command itself,
  not the parameters). Any subsequent response from commands such as a
  show ending or triggers should send the corresponding id back that the
  show was started with.
+ The pinball controller and the media controller must be resilient to
  network problems; if a connection is lost, it can simply re-open it to
  resume operation. There is no requirement to buffer unsendable
  commands to transmit on reconnection.
+ The pinball controller is responsible for initiating the connection
  to the media controller, never the other way around.
+ Once initial handshaking has completed on the first connection,
  subsequent re-connects do not have to handshake again.
+ An unrecognized command results in an error response with the
  message “unknown command”

In all commands referenced below, the `\n` terminator is implicit. Some
characters in parameters such as spaces would really be encoded as %20
in operation, but are left unencoded here for clarity.

Initial Handshake
-----------------

When a connection is initially established, the pinball controller
transmits the following command:

::

    hello?version=1.0

...where *1.0* is the version of the Backbox protocol it wants to
speak. The media controller may reply with one of two responses:

::

    hello?version=1.0

...indicating that it can speak the protocol version named, and
reporting the version it speaks, or

::

    error?message=unknown protocol version

...indicating that it cannot. How the pin controller handles this
situation is implementation-dependent.

BCP commands
------------

The following BCP commands have been defined (and implemented) in MPF:

.. toctree::
   :maxdepth: 1

   ball_end
   ball_start
   device
   error
   goodbye
   hello
   machine_variable
   mode_start
   mode_stop
   monitor_start
   monitor_stop
   player_added
   player_turn_start
   player_variable
   register_trigger
   remove_trigger
   reset
   switch
   trigger
