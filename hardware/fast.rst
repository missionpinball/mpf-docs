Fast Pinball
============

The `FAST Pinball <http://fastpinball.com>`_ controllers are created by Aaron Davis and Dave
Beecher from Seattle. FAST has three different controller models: the *FAST WPC Controller*,
the *FAST Core Controller*, and the *FAST Nano Controller*.

Controller boards
-----------------
When you use FAST Pinball hardware, you pick 1 controller which you then connect
to one or more I/O boards. The controller board acts as the interface between
the host computer running MPF and all the I/O boards that interface with your
actual pinball hardware.

FAST has three different models of pinball controllers, so just pick the one
that makes sense for you. All controllers have the following:

* USB port to connect to the computer running MPF
* 4 channels for controlling up to 64 RGB LEDs each (256 total RGB LEDs)
* RJ-45 in/out jacks for connecting the cables that form the ring of I/O boards

FAST Nano controller
~~~~~~~~~~~~~~~~~~~~
The Nano is FAST's lowest-cost controller and is what most people use. It's
small and "bare bones".

FAST Core controller
~~~~~~~~~~~~~~~~~~~~
The Core controller is slightly larger and more expensive than the Nano, but
also adds the following features:

* 14-pin connector to control traditional 16-shade pinball DMDs
* Headers to snap a Beaglebone Black small form factor PC to the board which can
  run Linux and MPF.
* Audio system with audio out, since the Beaglebone Black does not have on-board
  audio.
* Lithium Ion battery to keep the realtime clock set on the Beaglebone.
* Safe shutdown circuitry to properly power down the Beaglebone when power to
  the pinball is cut.

FAST WPC controller
~~~~~~~~~~~~~~~~~~~
The WPC controller is specifically designed to be a drop-in replacement for
Williams WPC, WPC-S, and WPC-95 machines. This board is physically the same size
as the original WPC boards, and it has all the same connectors, so you can drop
the FAST board into your existing machine.

The WPC controller has all the same features as the FAST Core controller, and
also adds:

* 34-pin header to connect to the Williams power driver board
* Switch headers to connect to the WPC switch matrix inputs
* 20pinb header to connect to the Williams Fliptronics boards
* Aux header to connect to Williams Aux bus

..note::
  The FAST WPC controller also contains connections for FAST I/O boards,
  meaning you can add drivers and switches to existing machines for some really
  cool mods! The WPC controller also has the 256 RGB LED connectors to add more
  LEDs to existing WPC machines.

I/O boards
----------

FAST has several different sizes of I/O boards. They all control a certain
number of drivers and switches (which you can decode based on the board model).

Current I/O boards include:

* FAST I/O 3208: 32 switches, 8 drivers
* FAST I/O 1616: 16 switches, 16 drivers
* FAST I/O 0804: 8 switches, 4 drivers

All FAST I/O boards contain extension headers to add daughter boards which can
extend the types of hardware that a particular I/O board can connect to.

Daughter boards
---------------

* Servo daughter board
* Stepper daughter board
* 8x8 switch matrix daughter board
* 8x8 lamp matrix daughter board

Other boards
------------

Finally, FAST has a few other types of boards which are useful when building
your own pinball machine. None of these boards are FAST-specific, meaning you
can use them in your machine even if you're not using FAST for your control
hardware.

Power filter board
~~~~~~~~~~~~~~~~~~
This board has three giant capacitors on it which are used to smooth out the
power that's supplied to your machine's high voltage coils.

It also has fuses all the fuses to protect your high voltage and 12v and 5v
systems.

There's a switch input which you can connect to your coin door switch to cut off
the high power when the coin door is open, and there's a switch output which is
activated when the high power has been cut off. (The idea is you connect this
switch output to one of your regular FAST switch inputs so your MPF code can
show the "High power disabled" message on the display.)

Smart fuse block
~~~~~~~~~~~~~~~~
The FAST smart fuse block is like the power filter board without the capacitors.
It has fuses and LEDs which show you whether the fuses are good or have been
blown, and there's a switch input which you can use to enable or disable the
high power fuses.
