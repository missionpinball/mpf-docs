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
-------------

The following BCP commands have been defined (and implemented) in MPF:

.. toctree::
   :maxdepth: 1

   ball_end <ball_end>
   ball_start <ball_start>
   config <config>
   dmd_frame <dmd_frame>
   error <error>
   external_show_frame <external_show_frame>
   external_show_start <external_show_start>
   external_show_stop <external_show_stop>
   get <get>
   goodbye <goodbye>
   hello <hello>
   mode_start <mode_start>
   mode_stop <mode_stop>
   player_added <player_added>
   player_score
   player_turn_start
   player_variable
   reset
   reset_complete
   set
   shot
   switch
   timer
   trigger


Here are the details for each:



external_show_stop
~~~~~~~~~~~~~~~~~~

Parameters: name Origin: Mediacontroller **Response:** None Stops
anexternally-controlled`hardwareshow`_that is currently running.



**get**
~~~~~~~

**Parameters:** names=variable1,variable2,…,variableN **Origin:** Pin
controller or media controller **Response:** set Asks the other side
to send the value of one or more variables. Variable names are to be
stripped of leading and trailing spaces and lower-cased. The other
side responds with a “set” command. If an unknown variable is
requested, its value is returned as an empty string. For sanity
reasons, all variable are to be lower case, must start with a letter,
and may contain only lowercase letters, numbers, and underscores.
Variable names should be lowercased on arrival. Variable names can be
no more than 32 characters. See “set” for a list of common variables.



**goodbye**
~~~~~~~~~~~

**Parameters:** None **Origin:** Pin controller or media controller
**Response:** None Lets one side tell the other than it’s shutting
down.



**hello**
~~~~~~~~~

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



mode_start
~~~~~~~~~~

Parameters: name, priority Origin: Pin controller **Response:** None A
game mode has just started. The mode is passed via the name parameter,
and the mode's priority is passed as an integer via the priority. For
example: `mode_start?name=base&priority=100`.



mode_stop
~~~~~~~~~

Parameters: name Origin: Pin controller **Response:** None The mode as
stopped.



player_added
~~~~~~~~~~~~

**Parameters:** player_num **Origin:** Pin controller **Response:**
None A player has just been added, with the player number passed via
the *player_num* parameter. Typically these commands only occur during
Ball 1.



player_score
~~~~~~~~~~~~

**Parameters:**value, prev_value, change, player_num **Origin:** Pin
controller **Response:** None Sent to the media controller any time
the player's score changes. It's possible that these events will come
in rapid succession. Also note the parameter *player_num* indicates
which player this score is for (starting with 1 for the first player).
While it's usually the case that the *player_score* command will be
sent for the player whose turn it is, that's not always the case. (For
example, when a second player is added during the first player's ball,
the second player's score will be initialized at 0 and a
*player_score* event for player 2 will be sent even though player 1 is
up.



player_turn_start
~~~~~~~~~~~~~~~~~

**Parameters:**player_num **Origin:** Pin controller **Response:**
None A new player's turn has begun. If a player has an extra ball,
this commandwill *not* be sent between balls. (However a new
*ball_start* command will be sent when the same player's additional
balls start.



player_variable
~~~~~~~~~~~~~~~

**Parameters:**name, value, prev_value, change, player_num **Origin:**
Pin controller **Response:** None This is a generic "catch all" which
sends player-specific variables to the media controller any time they
change. Since the pin controller will most likely track hundreds of
variables per player (with many being internal things that the media
controller doesn't care about), it's recommended that the
pincontroller has a way to filter which player variables are sent to
the media controller. Also note the parameter *player_num* indicates
which player this variable is for (starting with 1 for the first
player). While it's usually the case that the *player_variable*
command will be sent for the player whose turn it is, that's not
always the case. (For example, when a second player is added during
the first player's ball, the second player's default variables will be
initialized at 0 and a *player_variable* event for player 2 will be
sent even though player 1 is up.



**set**
~~~~~~~

**Parameters:** variable1=value1&variable2=value2&etc=etc **Origin:**
Pin controller or media controller **Response:** None Tells the other
side to set the value of one or more variables. For sanity reasons,
all variable are to be lower case, must start with a letter, and may
contain only lower case letters, numbers, and underscores. Variable
names should be lowercased on arrival. Variable names can be no more
than 32 characters. Variable values are of unbounded length. A value
can be blank. Setting a variable should have an immediate effect. For
example if the system audio volume is set, it is expected that audio
will immediate take on that volume value. Or if the high score is
currently being displayed and its variable it set, it should
immediately update the display.



shot
~~~~

Parameters: name, profile, state Origin: Pin controller **Response:**
None Indicates that a shot was just hit. Parameter *name* is the name
of the shot, *profile* is the name of the shot profile that was active
when it was hit, and *state* is the name of the state that the profile
was at when it was hit.



switch
~~~~~~

Parameters: name, state Origin: Pin controller or media controller
**Response:** None Indicates that the other side should process the
changed state of a switch.Two parameters are required, name which is
the name of the switch, and state which is "1" for active and "0" for
inactive. When sent from the media controller to the pin controller,
this is typically used to implement a virtual keyboard interface via
the media controller (where the player can activate pinball machine
switches via keyboard keys for testing).For example, for the media
controller to tell the pin controller that the player just pushed the
start button, the command would be:
`switch?name=start&state=1`followed very quickly by
`switch?name=start&state=0`. When sent from the pin controller to the
media controller, this is used to send switch inputs to things like
video modes, high score name entry, and service menu navigation. Note
that the pin controller should not send the state of every switch
change at all times, as the media controller doesn't need it and that
would add lots of unnecessary commands. Instead the pin controller
should only send switches based on some mode of operation that needs
them. (For example, when the video mode starts, the pin controller
would start sending the switch states of the flipper buttons, and when
the video mode ends, it would stop.)



timer
~~~~~

Parameters: name, action, ticks Origin: Pin controller **Response:**
Varies This command allows the pin controller to notify the media
controller about timer action that needs to be communicated to the
player. There are many timers in MPF (configured via the ` `Timers:`
section`_ of a config file). You can enable a timer to send its
details to the media controller by adding a `bcp: yes` setting to a
timer's settings.



trigger
~~~~~~~

Parameters: name Origin: Pin controller or media controller
**Response:** Varies This command allows the one side to trigger the
other side to do something. For example, the pin controller might send
trigger commands to tell the media controller to start shows, play
sound effects, or update the display. The media controller might send
a trigger to the pin controller to flash the strobes at the down beat
of a music track or to pulse the knocker in concert with a replay
show.



BCP Command Flow (Reference Order)
----------------------------------

If you want to get an idea of the order events are sent in (and the
exact types of events), the easiest way to do that is to run MPF's
sample game Demo Man with verbose logging enabled. Then open the MPF
log file (not the MC one) and filter it based on "bcpclient" and
you'll see all the BCP commands that are sent from MPF's BCP client.
Demo Man includes a config file called "autorun" which uses the switch
player plugin to automatically play through a game, so you can run
that to generate a full log file that includes lots of different thing
happening, like this:


::


    mpf demo_man -v -c autorun


Here's the high-level order the BCP commands will be sent from MPF.
This process starts with MPF boot and then follows through a game
starting. The `...` sections are where stuff has been left out, but
you get the idea. Note that in many cases (such as this one), the game
mode actually begins before the attract mode ends. These two events
were sent 7ms apart, so it's quick, but just FYI to be ready for the
game to start whenever the attract mode is running.


::


    hello?version=1.0
    reset
    mode_start?priority=10&name=attract
    ...
    mode_start?priority=20&name=game
    mode_stop?name=attract
    player_added?number=1
    player_turn_start?player=1
    ball_start?player=1&ball=1
    ...
    ball_end






Credits
-------

The Backbox Control Protocol is being developed by:


+ Quinn Capen
+ Kevin Kelm (responsible for the initial concept and first draft of
  the specification)
+ Gabe Knuth
+ Brian Madden
+ Mike ORourke

