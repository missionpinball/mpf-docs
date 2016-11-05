MPF compatible control systems / hardware
=========================================

MPF controls a pinball machine by interfacing to a modern pinball control system.
(See the :doc:`/start/index` for details.) MPF itself is hardware-independent,
meaning that MPF (and the configs and code you build) can work with lots of
different kinds of control systems and hardware devices.

Not only does this give you a choice of what type of pinball control hardware
you want to use, it also means that you have the flexibility to change your
hardware at any time without having to change any game code. You could
even release a game code update that works on multiple platforms—-all with the
same code!

`Here's a demo video <https://www.youtube.com/watch?v=_Zw_cHw2CXY>`_ of us
switching out a P-ROC controller for a FAST controller in 3 minutes and
running the same game code on both.

It's possible to mix-and-match multiple types of hardware in a single
MPF machine config. For example, you could combine the SmartMatrix RGB DMD with
a FAST Core controller, or a FadeCandy LED controller with a P-ROC, etc.)

MPF currently supports the following hardware control systems. We are always adding
more, so if there's a hardware device that you'd like to use that we don't support,
let us know. (Or better yet, write your own interface to it and submit a pull
request to the MPF codebase!)

List of supported control systems & hardware
--------------------------------------------

Here's a list of all the different types of control systems and hardware that
MPF currently supports. If there's a type of hardware you'd like us to support
that you don't see on this list, please
`post a message to the MPF Users Google Group
<https://groups.google.com/forum/#!forum/mpf-users>`_ and we'll go from there.

Click on the links below for details about how to configure MPF to use each
type of hardware.

* :doc:`FAST Pinball <fast/index>`
   * All FAST controllers, including Core, Nano, and WPC
   * All FAST I/O boards, including 0804, 1616, 3208
   * FAST servo controller daughter board
   * FAST auxiliary boards, including the power filter board and smart fuse block
   * Plasma & LED mono DMDs (Core & WPC controllers)
   * FAST RGB LED-based DMD

* :doc:`Multimorphic <multimorphic/index>`
   * P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED)
   * P-ROC in all supported existing machines (Williams, Stern, etc.)
   * P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
   * Plasma & LED mono DMDs (P-ROC)
   * Accelerometer-based tilt (P3-ROC)

* :doc:`Open Pinball Project (OPP) controllers <opp/index>`
   * Gen 2 OPP hardware, with many combinations of wing boards for drivers, switches, & incandescent
     lights

* :doc:`Snux System 11 driver board <snux/index>`
   * Supported in combination with the P-ROC or FAST WPC controller
   * Supported for System 11, 11A, 11B, 11C
   * Should work in Data East machines too, though it's never been tried

* :doc:`I2C Servo Controllers <i2c_servo/index>`
   * Servos connected to I2C-based servo controllers

* :doc:`Fadecandy RGB LED controllers <fadecandy/index>`
   * 512 RGB LEDs per Fadecandy
   * Can connect multiple Fadecandys to support more LEDs

* :doc:`Pololu Maestro servo controllers <pololu_maestro/index>`
   * Supports up to 24 servos per board

* :doc:`SmartMatrix RGB LED display controller <smartmatrix/index>`
   * Supports a "real" color DMD made up of RGB LED matrix

* :doc:`RGB.DMD RGB LED display controller <eli_dmd/index>`
   * Supports a "real" color DMD made up of RGB LED matrix

Detailed hardware support information
-------------------------------------

Now that we've done a rundown of the various types of hardware that's supported,
here's are details about each platform:

.. toctree::
   :maxdepth: 1
   :hidden:

   FAST Pinball <fast/index>
   multimorphic/index
   opp/index
   snux/index
   fadecandy/index
   i2c_servo/index
   pololu_maestro/index
   smartmatrix/index
   eli_dmd/index
