Switch Breakout Boards
======================

Normally, eight switches are connected to one bank of a pinball controller
(in almost all platforms).
Ground is then chained from one switch to the next to simplify wiring (as only
one connector with one ground pin is required on the board).
This works well for all sub-playfield switches.
However, it would be tricky for optos or switches in ramps above the playfield.

To solve this breakout boards are used which connect to the bank and provide a
separate connector per switch.
If you are building a homebrew game there are a few designs around which can be
build in China for a few bucks (just ask in our forum).
Some of those boards also provide power for :doc:`optos <optos>`.
There is one commercial board from Multimorphic (part number: unknown) which
provides one JST connector per switch and also distributes power to optos (see
:doc:`optos` for details).

Stern occasionally also uses breakouts for optos (usually for two optos).
In Stern Spike they added a few "breakout" connectors to some of their node
boards to add optos and above playfield features without additional breakouts.
