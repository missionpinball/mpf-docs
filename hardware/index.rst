MPF compatible hardware
=======================

One of the primary goals of MPF is to be hardware-independent. In other words, we
want MPF to work with any hardware pinball controller out there. We achieve
hardware independence by abstracting all the hardware calls to MPF's platform
interface modules, and then the platform modules talk to the actual hardware
platform you're using.

This also means that a game programmer, you have the flexibility to change your
hardware platform at any time without having to change any game code. You could
even release a game code update that works on multiple platforms—-all with the
same code!

If you're using your custom code in an existing Williams WPC game, you can
literally switch platforms by changing a single line in a config file. `Here's a demo video`_
of us switching out a P-ROC controller for a FAST controller in 3 minutes and
running the same game code on both.

Note that it's possible to mix-and-match multiple hardware platforms in a single
MPF machine config. (For example, you can combine the SmartMatrix RGB DMD with
a FAST Core controller, or a FadeCandy LED controller with a P-ROC, etc.)

MPF currently supports the following hardware devices. We are always adding
more, so if there's some device that you'd like to use that we don't support,
let us know. (Or better yet, write your own interface to it and submit a pull
request to the MPF codebase!)

FAST Pinball
------------
* All FAST controllers, including Core, Nano, and WPC
* All FAST I/O boards, including 0804, 1616, 3208
* FAST servo controller daughter board
* FAST auxiliary boards, including the power filter board and smart fuse block
* Plasma & LED mono DMDs (Core & WPC controllers)

Multimorphic (P-ROC / P3-ROC)
-----------------------------
* P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED)
* P-ROC in all supported existing machines (Williams, Stern, etc.)
* P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
* Plasma & LED mono DMDs (P-ROC)
* Accelerometer-based tilt (P3-ROC)

Snux System 11 driver board
---------------------------
* Supported in combination with the P-ROC or FAST WPC controller
* Supported for System 11, 11A, 11B, 11C
* Should work in Data East machines too, though it's never been tried

Open Pinball Project Gen2 controllers
-------------------------------------
* Supports many combinations of wing boards for drivers, switches, & incandescent lights (:doc:`How To </howto/controller_hardware/opp>`)

Pololu Maestro servo controllers
--------------------------------
* Support up to 24 servos per board (:doc:`How To </howto/controller_hardware/pololu_maestro>`)

Fadecandy RGB LEDs
------------------
* 512 RGB LEDs per Fadecandy
* Can connect multiple Fadecandys to support more LEDs

SmartMatrix RGB LED display controller
--------------------------------------

RGB.DMD RGB LED display controller
----------------------------------

Existing versus new ("home brew") machines
------------------------------------------
You can use MPF to rewrite the rules for existing commercial machines, or to
power a branch new "home brew" machine you build yourself:

.. toctree::

   existing_machines
   homebrew_machines

Detailed hardware support information
-------------------------------------

Now that we've done a rundown of the various types of hardware that's supported,
here's are details about each platform:

.. toctree::
   :maxdepth: 1

   fast
   multimorphic

.. toctree::
   :hidden:

   host_computer
