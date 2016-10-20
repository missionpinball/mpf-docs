MPF compatible control systems / electronic boards
==================================================

MPF controls a pinball machine by interfacing to a modern pinball control system.
(See :doc:`/start/hardware_interface` for details.) MPF itself is hardware-independent,
meaning that MPF (and the configs and code you build) can work with lots of
different kinds of control systems.

Not only does this give you a choice of what type of pinball control hardware
you want to use, it also means that you have the flexibility to change your
hardware at any time without having to change any game code. You could
even release a game code update that works on multiple platforms—-all with the
same code!

`Here's a demo video <https://www.youtube.com/watch?v=_Zw_cHw2CXY>`_ of us
switching out a P-ROC controller for a FAST controller in 3 minutes and
running the same game code on both.

Note that it's possible to mix-and-match multiple hardware platforms in a single
MPF machine config. (For example, you can combine the SmartMatrix RGB DMD with
a FAST Core controller, or a FadeCandy LED controller with a P-ROC, etc.)

MPF currently supports the following hardware control systems. We are always adding
more, so if there's a hardware device that you'd like to use that we don't support,
let us know. (Or better yet, write your own interface to it and submit a pull
request to the MPF codebase!)

FAST Pinball
------------
* All FAST controllers, including Core, Nano, and WPC (:doc:`More Info <fast>` | :doc:`How To <configuring_fast_hardware>`)
* All FAST I/O boards, including 0804, 1616, 3208
* FAST servo controller daughter board
* FAST auxiliary boards, including the power filter board and smart fuse block
* Plasma & LED mono DMDs (Core & WPC controllers)
* FAST RGB LED-based DMD

Multimorphic (P-ROC / P3-ROC)
-----------------------------
* P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED) (:doc:`More Info <multimorphic>`)
* P-ROC in all supported existing machines (Williams, Stern, etc.)
* P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
* Plasma & LED mono DMDs (P-ROC)
* Accelerometer-based tilt (P3-ROC)


Open Pinball Project (OPP) controllers
--------------------------------------
* Gen 2 OPP hardware, with many combinations of wing boards for drivers, switches, & incandescent
  lights (:doc:`How To <configuring_opp_hardware>`)

Snux System 11 driver board
---------------------------
* Supported in combination with the P-ROC or FAST WPC controller
* Supported for System 11, 11A, 11B, 11C
* Should work in Data East machines too, though it's never been tried

Pololu Maestro servo controllers
--------------------------------
* Support up to 24 servos per board (:doc:`How To <pololu_maestro>`)

Fadecandy RGB LEDs
------------------
* 512 RGB LEDs per Fadecandy
* Can connect multiple Fadecandys to support more LEDs

SmartMatrix RGB LED display controller
--------------------------------------
* Supports a "real" color DMD made up of RGB LED matrix

RGB.DMD RGB LED display controller
----------------------------------
* Supports a "real" color DMD made up of RGB LED matrix

Detailed hardware support information
-------------------------------------

Now that we've done a rundown of the various types of hardware that's supported,
here's are details about each platform:

.. toctree::
   :maxdepth: 1

   FAST Pinball (overview) <fast>
   FAST Pinball (configuration) <configuring_fast_hardware>
   Multimorphic P-ROC/P3-ROC <multimorphic>
   Open Pinball Project (OPP) <configuring_opp_hardware>
   Pololu Maestro Servo Controllers <pololu_maestro>