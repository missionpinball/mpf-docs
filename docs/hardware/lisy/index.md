---
title: How to use MPF with the LISY platform
---

# How to use MPF with the LISY platform

--8<-- "hardware_platform.md"

Related Config File Sections:

* [hardware:](../../config/hardware.md)
* [lisy:](../../config/lisy.md)
* [switches:](../../config/switches.md)
* [coils:](../../config/coils.md)

MPF can directly control Gottlieb System 1 or System 80 machines via the
LISY1 or LISY80 controller boards (with firmware 4.02+). Additionally,
[LISY35](https://lisy.dev/lisy35.html) can control Bally and Stern Games
manufactured from 1977 to 1985 with MPU AS-2518-17 or AS-2518-35.

!!! note

    For general installation instruction and some background information on
    the LISY hardware platform, visit
    [www.lisy80.com](http://www.lisy80.com/).

There are two ways this can be done:

a.  Run MPF on a standalone PC which connects to the LISY hardware
    operating in "slave" mode via Ethernet, WiFi, or serial. This is
    generally recommended during development since it's easier to work
    on your MPF config using your own computer. You can also use this
    configuration if you want to add an LCD or DMD to the older Gottlieb
    machine.
b.  Run MPF on the LISY hardware directly ("master" mode).
    (Technically MPF is running on the LISY controller's Raspberry Pi
    Zero.) This option is nice when your game is finished and you no
    longer want to connect a PC. Note that the Raspberry Pi on the LISY
    is not powerful enough to run the MPF media controller, so this
    option is really only valid for simpler, segment display type games.
    If you want to run a full LCD or DMD, then just run MPF on a
    separate computer (which can still be small and inside your machine)
    and connect to the LISY controller via Option (a) above.

See the following image for an architecture overview:

![image](../images/lisy_mpf_overview.jpg)

LISY can controll all features of your Gottlieb System1/80 machine. This
includes:

* Switches ([LISY1](switches_lisy1.md) and [LISY80](switches_lisy80.md))
* [Coils](drivers.md)
* [Lights](lights.md)
* [Enabling/disabling flipper, slings and popbumpers](flippers_slings_popbumpers.md)
* [Segment displays](segment_displays.md)
* [Original sounds of your game](../../mc/sound/index.md)
* [Text to speech and additional sounds](../../mc/sound/index.md)
