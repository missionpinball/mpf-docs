---
title: MPF compatible control systems / hardware
---

# Working with physical hardware

This section will discuss working with Pinball control systems and electronics,
as well as working with physical pinball mechs and devices.

MPF controls a pinball machine by interfacing to a modern pinball
control system. (See the [platform](../start/index.md)
for details.) MPF itself is hardware-independent, meaning that MPF (and
the configs and code you build) runs on a
[normal/embedded PC](computer.md) and
can work with lots of different kinds of control systems and hardware
devices.

Not only does this give you a choice of what type of pinball control
hardware you want to use, it also means that you have the flexibility to
change your hardware at any time without having to change any game code.
You could even release a game code update that works on multiple
platforms---all with the same code!

Here's a demo video of us switching out a P-ROC controller for a FAST
controller in 3 minutes and running the same game code on both:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/_Zw_cHw2CXY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

It's possible to mix-and-match multiple types of hardware in a single
MPF machine config. For example, you could combine the SmartMatrix RGB
DMD with a FAST Core controller, or a FadeCandy LED controller with a
P-ROC, etc. (You can even mix-and-match platforms within the same type
of device, meaning you could have some LEDs attached to a FAST Pinball
controller and others attached to a FadeCandy. See the
[Mixing-and-Matching hardware platforms](platform.md) guide for details.)

MPF currently supports the following hardware control systems. We are
always adding more, so if there's a hardware device that you'd like to
use that we don't support, let us know. (Or better yet, write your own
interface to it and submit a pull request to the MPF codebase!)

Also see our guide on
[voltages found in a pinball machine](voltages_and_power).

## List of supported control systems & hardware

Here's a list of all the different types of control systems and
hardware that MPF currently supports. If there's a type of hardware
you'd like us to support that you don't see on this list, please [post
a message to the MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users) and we'll go
from there.

### Primary control systems

You'll need to pick one of these three as the main interface between
MPF and your pinball machine.

  * [FAST Pinball](fast)
    * Neuron, Nano, and Retro Controllers
    * All I/O Boards (Playfield & Cabinet Controller)
    * Expansion Boards & EXP Bus (LEDs, servos, motors, etc.)
    * Smart Power Filter Board
    * Existing displays & DMDs (Retro platform)
    * FAST LED DMD (All platforms)
    * FAST Audio Interface (Modern & Retro platforms)

  * [Open Pinball Project (OPP) controllers](opp)
    * Gen 2 OPP hardware, with many combinations of wing boards
        for drivers, switches, switch matrix, LEDs & incandescent
        lights
    * [CobraPin Pinball Controller](opp/cobrapin)

  * [Arduino Pinball Controller (APC)](apc)
    * *New in MPF 0.53*
    * System 3 to System 11c
    * Segment displays
    * External sounds
    * Switches, rules and coils
    * Lights and enable triggers

  * [LISY](lisy)
    * *New in MPF 0.50*
    * Gottlieb System 1 (LISY1)
    * Gottlieb System 80 (LISY80)
    * Bally and Stern Games manufactured from 1977 to 1985
      (LISY35) *New in MPF 0.53*
    * Segment displays
    * External sounds
    * Switches, rules and coils
    * Lights and enable triggers

  * [Multimorphic](multimorphic)
    * P-ROC with PDB driver boards (PD-16, PD-8x8, PD-LED)
    * P-ROC in all supported existing machines (Williams, Stern,
      etc.)
    * P3-ROC with PDB driver boards (PD-16, SW-16, PD-LED)
    * Plasma & LED mono DMDs (P-ROC)
    * Accelerometer-based tilt (P3-ROC)
    * I2C slave boards (see below for which I2C boards are
      supported) (P3-ROC)
    * Alphanumeric displays via aux port (P-Roc)

  * [Stern SPIKE / SPIKE 2 machines](spike)
    * *New in MPF 0.33*
    * A computer running MPF can directly connect to a SPIKE
      machine with a simple "USB to serial" converter which you
      plug into the SPIKE main board.

  * [Penny K Pinball PKONE Platform](pkone)
    * Nano Controller
    * PKONE Extension (switches, coils, rules, servos)
    * PKONE Lightshow (simple LEDs, WS281x RGB/RGBW LEDs)

  * [Virtual (software-only) controllers](virtual)
    * MPF includes virtual hardware interfaces you can use to run
      MPF when it's not connected to physical hardware. (This is
      good for working on your game when you're not around your
      machine, or if you don't have real hardware yet.)
    * You can also integrate MPF with a
      [Virtual Pinball (VPX)](virtual/virtual_pinball_vpx.md) table to play your game with simulated hardware.
    * The [MPF Monitor](../tools/monitor/index.md) is a graphical tool you can also use to visually
      interact with MPF which is especially useful if you're not
      using MPF with physical hardware.

### Additional supported hardware

The following hardware devices can be combined with primary control
systems to provide additional functionality.

* [Snux System 11 driver board](snux.md)
    * Supported in combination with the P-ROC or FAST WPC
      controller
    * Supported for System 11, 11A, 11B, 11C
    * Should work in Data East machines too, though it's never
      been tried

* [I2C Servo Controllers](i2c_servo.md)
    * Servos connected to I2C-based servo controllers

* [Fadecandy RGB LED controllers](fadecandy)
    * 512 RGB LEDs per Fadecandy
    * Can connect multiple Fadecandys to support more LEDs

* [Pololu Maestro servo controllers](pololu_maestro.md)
    * Supports up to 24 servos per board

* [SmartMatrix RGB LED display controller](smartmatrix.md)
    * Supports a "real" color DMD made up of RGB LED matrix

* [RGB.DMD RGB LED display controller](eli_dmd.md)
    * Supports a "real" color DMD made up of RGB LED matrix

* [MyPinballs Segment Display Controller](mypinballs)
    * *New in MPF 0.50*
    * Alphanumeric segment displays
    * Also supports TNA Numeric Score Displays

* [Light Segment Displays](light_segment_displays.md)
    * Control segment displays via light outputs or driver on
      another platform
    * BCD segment displays
    * 7-segment displays
    * Serial driven displays
    * RGB segment displays
    * Other formats and custom built displays

* [Trinamics StepRocker](trinamics.md)
    * *New in MPF 0.50*
    * StepRocker stepper controller

* [Raspberry Pi](rpi.md)
    * *New in MPF 0.50*
    * Local (MPF on the RPi) or remote via ethernet
    * All inputs and outputs
    * I2C and SPI

* [PIN2DMD RGB DMD](pin2dmd)
    * *New in MPF 0.54*
    * 128x32 or 192x64 RGB LED DMD
    * Connected via USB

* [Native I2C on Linux](smbus.md)
    * *New in MPF 0.50*
    * I2C devices on any nativ I2C bus

* [MMA8451-based accelerometers](mma8451.md)
    * *New in MPF 0.50*
    * Connected to I2C

* [Pololu Tic](pololu_tic.md)
    * *New in MPF 0.52*
    * Stepper controller connected to USB

* [Open Sound Control (OSC)](osc.md)
    * Control lights via OSC (i.e. your DMX controller)
    * Receive incoming switch changes (i.e. from your MIDI
      keyboard)
    * Receive incoming events (i.e. from your MIDI keyboard)
    * Send events to OSC (to generate sounds or trigger actions)

Video on how platforms work internally and how to implement them:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PvQVoUzL8Cc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Configuration Guides

We have configuration guides which show you how to setup and use
different types of pinball mechanisms with the various control systems
and hardware that MPF supports:

* [Open Pinball Project (OPP)](opp)
* [LISY platform](lisy)
* [Arduino Pinball Controller](apc)
* [P-ROC/P3-ROC](multimorphic)
* [FAST Pinball](fast)
* [Stern SPIKE / SPIKE 2](spike)
* [Penny K Pinball PKONE Platform](pkone)
* [snux/index FadeCandy RGB LED controllers](fadecandy)
* [i2c_servo/index Pololu Maestro](pololu_maestro.md)
* [Pololu Tic](pololu_tic.md)
* [SmartMatrix RGB DMD](smartmatrix.md)
* [RGB.DMD](eli_dmd.md)
* [PIN2DMD](pin2dmd)
* [Raspberry Pi DMD](rpi_dmd.md)
* [MyPinballs Segment Displays](mypinballs)
* [Light
Segment Displays](light_segment_displays)
* [Trinamics StepRocker](trinamics.md)
* [StepStick Steppers](stepstick.md)
* [Computer
Requirements](computer)
* [Native I2C](smbus.md)
* [Raspberry Pi](rpi.md)
* [MMA8451-based accelerometer](mma8451.md)
* [SPI Big Bang
Switches](spi_bit_bang)
* [Open Sound Control (OSC)](osc.md)
* [Virtual Hardware](virtual)
* [Existing Machines](existing_machines)
* [Voltages and Power](voltages_and_power)

## Browse Platforms by Capabilities

* [i2c_platforms servo_platforms stepper_platforms
segment_display_platforms dmd_platforms](i2c_platforms servo_platforms stepper_platforms
segment_display_platforms dmd_platforms)

* [Segment Display Transitions](segment_display_transitions.md)
