MPF supported hardware
======================
Note that it's possible to mix-and-match multiple hardware platforms in a single
MPF machine config. (For example, you can combine the SmartMatrix RGB DMD with
a FAST Core controller, or a FadeCandy LED controller with a P-ROC, etc.)

FAST Pinball Core, Nano, & WPC controllers
------------------------------------------
* Support all I/O boards, including 0804, 1616, 3208
* FAST servo controller daughter board
* Gas & LED mono DMDs (Core & WPC controllers)

Multimorphic P-ROC & P3-ROC
---------------------------
* P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED)
* P-ROC in all supported existing machines
* P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
* Gas & LED mono DMDs (P-ROC)
* Accelerometer-based tilt (P3-ROC)

Snux System 11 driver board
---------------------------
* Support with P-ROC and FAST WPC controller
* Support in System 11, 11A, 11B, 11C
* Should work in Data East machines too, though it's never been tried

Open Pinball Project Gen2 controllers
-------------------------------------

Fadecandy RGB LEDs
------------------
* 512 RGB LEDs per Fadecandy
* Can connect multiple Fadecandys to support more LEDs

SmartMatrix RGB LED display controller
--------------------------------------

RGB.DMD RGB LED display controller
----------------------------------

One of the primary goals of MPFis to behardware-independent. In other
words we want MPF to work with any hardware pinball controller out
there. We achieve hardware independence by abstracting all the
hardware calls to our `platform interface module`_, and then our
platformmodule talks to a hardware-specific module which is specific
to the actual hardware platform you're using. (So in our
`/platforms`folder we have a Python module called `p_roc.py`which is
used to talk to a P-ROC, `p3_roc.py` talks to a P3-ROC, `fast.py`
talks to FAST controllers, etc.) It's sort of a *"we know the low-
level details of the different hardware controllers so you don't have
to"* kind of thing. :) This also means that a game programmer, you
have the flexibility to change your hardware platform at any time
without having to change any game code. You could even release a game
code update that works on multiple platforms—all with the same code!
If you're using your custom code in an existing Williams WPC game, you
can literally switch platforms by changing a single line in a config
file. `Here's a demo video`_ of us switching out a P-ROC controller
for a FAST controller in 3 minutes and running the same game code on
both.
