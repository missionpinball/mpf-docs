Switch/Opto Breakout Boards
===========================

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

Stern occasionally also uses breakouts for optos (usually for two optos).
In Stern Spike they added a few "breakout" connectors to some of their node
boards to add optos and above playfield features without additional breakouts.

Common parts:

* PBL-600-0385-00 - Optos Breakout Board for 8 optos (emitter + receiver)
  intended to be used with Multimorphic SW-16.
  (Should also work with FAST hardware)
* FAST - FAST 4-Channel 12v Constant Current Opto Emitter (4 emitter)
* Stern Spike Opto Amplifier - 520-5239-01 (2 emitter + receiver)
* Multimorphic PCBA-0018-0002 - One JST connector per switch and also
  distributes power to optos.

Have a look at the
`PCB section of hardware.missionpinball.org <https://hardware.missionpinball.org/pcbs.html>`_
for DIY designs.

See also :doc:`optos` for how this works technically.
