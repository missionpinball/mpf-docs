MPF compatible control systems / hardware
=========================================

MPF controls a pinball machine by interfacing to a modern pinball control system.
(See the :doc:`/start/index` for details.) MPF itself is hardware-independent,
meaning that MPF (and the configs and code you build) runs on a :doc:`normal/embedded PC <computer/index>`
and can work with lots of different kinds of control systems and hardware devices.

Not only does this give you a choice of what type of pinball control hardware
you want to use, it also means that you have the flexibility to change your
hardware at any time without having to change any game code. You could
even release a game code update that works on multiple platforms—all with the
same code!

`Here's a demo video <https://www.youtube.com/watch?v=_Zw_cHw2CXY>`_ of us
switching out a P-ROC controller for a FAST controller in 3 minutes and
running the same game code on both.

It's possible to mix-and-match multiple types of hardware in a single
MPF machine config. For example, you could combine the SmartMatrix RGB DMD with
a FAST Core controller, or a FadeCandy LED controller with a P-ROC, etc. (You
can even mix-and-match platforms within the same type of device, meaning you
could have some LEDs attached to a FAST Pinball controller and others attached
to a FadeCandy. See the :doc:`platform` guide for details.)

MPF currently supports the following hardware control systems. We are always adding
more, so if there's a hardware device that you'd like to use that we don't support,
let us know. (Or better yet, write your own interface to it and submit a pull
request to the MPF codebase!)

Also see our guide on :doc:`voltages found in a pinball machine <voltages_and_power/index>`.

List of supported control systems & hardware
--------------------------------------------

Here's a list of all the different types of control systems and hardware that
MPF currently supports. If there's a type of hardware you'd like us to support
that you don't see on this list, please
`post a message to the MPF Users Google Group
<https://groups.google.com/forum/#!forum/mpf-users>`_ and we'll go from there.

Primary control systems
^^^^^^^^^^^^^^^^^^^^^^^

You'll need to pick one of these three as the main interface between MPF and
your pinball machine.

* :doc:`FAST Pinball <fast/index>`
   * Core Controller, Nano Controller, WPC Controller
   * 0804, 1616, 3208 I/O Boards
   * Servo controller daughter board
   * Power Filter Driver Board coin-door interconnect
   * Plasma & LED mono DMDs (Core & WPC controllers)
   * FAST RGB LED-based DMD

* :doc:`Multimorphic <multimorphic/index>`
   * P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED)
   * P-ROC in all supported existing machines (Williams, Stern, etc.)
   * P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
   * Plasma & LED mono DMDs (P-ROC)
   * Accelerometer-based tilt (P3-ROC)
   * I2C slave boards (see below for which I2C boards are supported) (P3-ROC)
   * Alphanumeric displays via aux port (P-Roc)

* :doc:`Open Pinball Project (OPP) controllers <opp/index>`
   * Gen 2 OPP hardware, with many combinations of wing boards for drivers,
     switches, switch matrix, LEDs & incandescent lights

* :doc:`Stern SPIKE / SPIKE 2 machines <spike/index>`
   * *New in MPF 0.33*
   * A computer running MPF can directly connect to a SPIKE machine with
     a simple "USB to serial" converter which you plug into the SPIKE
     main board.

* :doc:`LISY <lisy/index>`
   * *New in MPF 0.50*
   * Gottlieb System 1 (LISY1)
   * Gottlieb System 80 (LISY80)
   * Bally and Stern Games manufactured from 1977 to 1985 (LISY35) *New in MPF 0.53*
   * Segment displays
   * External sounds
   * Switches, rules and coils
   * Lights and enable triggers

* :doc:`Arduino Pinball Controller (APC) <apc/index>`
   * *New in MPF 0.53*
   * System 3 to System 11c
   * Segment displays
   * External sounds
   * Switches, rules and coils
   * Lights and enable triggers

* :doc:`Virtual (software-only) controllers <virtual/index>`
   * MPF includes virtual hardware interfaces you can use to run MPF when
     it's not connected to physical hardware. (This is good for working on
     your game when you're not around your machine, or if you don't have
     real hardware yet.)
   * You can also integrate MPF with a
     :doc:`Virtual Pinball (VPX) <virtual/virtual_pinball_vpx>` table to play
     your game with simulated hardware.
   * The :doc:`MPF Monitor </tools/monitor/index>` is a graphical tool you can
     also use to visually interact with MPF which is especially useful if
     you're not using MPF with physical hardware.

Additional supported hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following hardware devices can be combined with primary control sytstems
to provide additional functionality.

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

* :doc:`MyPinballs Segment Display Controller <mypinballs/index>`
   * *New in MPF 0.50*
   * Alphanumeric segment displays

* :doc:`Light Segment Displays <light_segment_displays/index>`
   * Control segment displays via light outputs or driver on another platform
   * BCD segment displays
   * 7-segment displays
   * Serial driven displays
   * RGB segment displays
   * Other formats and custom built displays

* :doc:`Trinamics StepRocker <trinamics/index>`
   * *New in MPF 0.50*
   * StepRocker stepper controller

* :doc:`Raspberry Pi <rpi/index>`
   * *New in MPF 0.50*
   * Local (MPF on the RPi) or remote via ethernet
   * All inputs and outputs
   * I2C and SPI

* :doc:`PIN2DMD RGB DMD <pin2dmd/index>`
   * *New in MPF 0.54*
   * 128x32 or 192x64 RGB LED DMD
   * Connected via USB

* :doc:`Native I2C on Linux <smbus/index>`
   * *New in MPF 0.50*
   * I2C devices on any nativ I2C bus

* :doc:`MMA8451-based accelerometers <mma8451/index>`
   * *New in MPF 0.50*
   * Connected to I2C

* :doc:`Pololu Tic <pololu_tic/index>`
   * *New in MPF 0.52*
   * Stepper controller connected to USB

* :doc:`Open Sound Control (OSC> <osc/index>`
   * Control lights via OSC (i.e. your DMX controller)
   * Receive incoming switch changes (i.e. from your MIDI keyboard)
   * Receive incoming events (i.e. from your MIDI keyboard)
   * Send events to OSC (to generate sounds or trigger actions)

There is a :doc:`hardware roadmap <roadmap>` for other hardware which we want
to support in the future.

Configuration Guides
--------------------

We have configuration guides which show you how to setup and use different
types of pinball mechanisms with the various control systems and hardware that
MPF supports:

.. toctree::
   :maxdepth: 2

   FAST Pinball <fast/index>
   P-ROC/P3-ROC <multimorphic/index>
   Open Pinball Project (OPP) <opp/index>
   Stern SPIKE / SPIKE 2 <spike/index>
   LISY platform <lisy/index>
   Arduino Pinball Controller <apc/index>
   snux/index
   FadeCandy RGB LED controllers <fadecandy/index>
   i2c_servo/index
   Pololu Maestro <pololu_maestro/index>
   Pololu Tic <pololu_tic/index>
   SmartMatrix RGB DMD <smartmatrix/index>
   RGB.DMD <eli_dmd/index>
   PIN2DMD <pin2dmd/index>
   Raspberry Pi DMD <rpi_dmd/index>
   MyPinballs Segment Displays <mypinballs/index>
   Light Segment Displays <light_segment_displays/index>
   Trinamics StepRocker <trinamics/index>
   StepStick Steppers <stepstick/index>
   Computer Requirements <computer/index>
   Native I2C <smbus/index>
   Raspberry Pi <rpi/index>
   MMA8451-based accelerometer <mma8451/index>
   SPI Big Bang Switches <spi_bit_bang/index>
   Open Sound Control (OSC) <osc/index>
   Virtual Hardware <virtual/index>
   Existing Machines <existing_machines/index>
   Voltages and Power <voltages_and_power/index>

.. toctree::

   hw_rules
   numbers
   platform
   roadmap
   troubleshooting_hardware

Browse Platforms by Capabilites
-------------------------------

.. toctree::
   :titlesonly:

   i2c_platforms
   servo_platforms
   stepper_platforms
   segment_display_platforms
   dmd_platforms
