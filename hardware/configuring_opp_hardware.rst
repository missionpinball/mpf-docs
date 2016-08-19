How to configure Open Pinball Project (OPP) hardware for MPF
============================================================

This how to guide explains how to set up your MPF configuration files
to interface with an Open Pinball Project (OPP) pinball controller.


1. Configure the Hardware platform for OPP
------------------------------------------

To use MPF with OPP, you need to configure your platform as *opp*,
like this:

::

    hardware:
        platform: opp
        driverboards: gen2


You also need to configure the ``driverboards:`` entry for what kind of
driver boards you’re controlling: right now, only *gen2* is supported.


2. Configure the OPP-specific hardware settings
-----------------------------------------------

When you use OPP hardware with MPF, you also need to add an ``opp:``
section to your machine-wide config which contains some OPP-
specific hardware settings. MPF's default config file
(*mpfconfig.yaml*) contains enough default settings to get you up and
running. The only thing you absolutely have to configure is your
ports.


Understanding OPP hardware ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though OPP controllers are USB devices, they use "virtual"
COM ports to communicate with the host computer running MPF. On your
computer, if you look at your list of ports and then plug-in your
OPP controller, you will see a new port appear. The exact
names and numbers of these ports will vary depending on your computer
and what else you've plugged in in the past.

Note: USB to serial converters add latency when communicating between
the host computer, and the target device.  It probably will not matter,
but if given the choice between a "real" serial port, and a USB-serial
port converter, the "real" serial port will have less latency.  The
real serial port must use 5V signal levels when talking to OPP hardware.

Adding the port to your config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using an OPP controller, you need to add the serial port to
your MPF config. So if you plug in the OPP controller and see a port
such as *COM7* appear, you'd set your config like this:

::

    opp:
        ports: COM7

Full details of the port options as well as the other options
available here are in the ``opp:`` section of the configuration
file reference. Note that if you're using Windows and you have COM
port numbers greater than 9, you may have to enter the port names like
this: ``\\.\COM10`` ``\\.\COM11`` ``\\.\COM12``, etc. (It's a Windows
thing. Google it for details.) That said, it seems that Windows 10 can
just use the port names like normal: ``com10, com11, com12``, so try
that first and then try the alternate format if it doesn't work.


3. Configuring Switches
-----------------------

For switches, you can use most of the settings as outlined in the
``switches:`` section of the config file reference. There are only a
few things that are OPP-specific:

Number:
~~~~~~~

OPP switches are numbered sequentially depending on which wing board
is the switch input.  Wing position 0 contains switch numbers 0 to 7.
Wing position 1 contains switch numbers 8 to 15.  Wing position 2
contains switch numbers 16 to 23.  Wing position 3 contains switch
numbers 24 to 31. The switch is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the switch number
on the card.

Enter them as a combination of board-switch, like ``0-12``.

::

    switches:
      some_switch:
        number: 0-15

The above example configures a switch input as the first OPP card, and
the second wing board, last input.  On the microprocessor card, the
input is marked as 1.7 (wing port 1, position 7).

Switch inputs for solenoids follow the same number convention.  Since
only four inputs are available for each wing card, it uses the first
four switch numbers.  Solenoid wing 0 uses switch numbers 0 to 3.
Solenoid wing 1 uses switch numbers 8 to 11.  Solenoid wing 2 uses
switch numbers 16 to 19.  Solenoid wing 3 uses switch numbers 24 to 27.

4. Configuring coils
--------------------

There are a few things to know about controlling drivers and coils
with OPP hardware.

Number
~~~~~~

OPP coils are numbered sequentially depending on which wing board
is the coil output.  Wing position 0 contains coil numbers 0 to 3.
Wing position 1 contains coil numbers 4 to 7.  Wing position 2
contains coil numbers 8 to 11.  Wing position 3 contains coil
numbers 12 to 15. The coil is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the coil number
on the card.


::

    coils:
      some_coil:
        number: 0-12

The above example configures a coil output as the first OPP card, and
the third wing board, first output.  On the microprocessor card, the
output is marked as 3.4 (wing port 3, position 4).



Pulse time
~~~~~~~~~~

The OPP hardware also has the ability to specify the "pulse time".
Pulse time is the coil's initial kick time. For
example, consider the following configuration:


::

    coils:
        some_coil:
            number: 0-12
            pulse_ms: 30

When MPF sends this coil a pulse command, the coil will be fired for
30ms.


Hold Power
~~~~~~~~~~
If you want to hold a driver on at less than full power, MPF does this by using
"hold_power" parameter which works for all platforms. It can range from 0 to 8
and hold_power/8 = time share the coil is on.

The period is fixed at 16ms for OPP. To set the hold power to 25%, set
hold_power to 2 and OPP will use 4ms/16ms = 25%.

Because of firmware limitations in OPP hold_power 8 will translate to 15ms/16ms
= 93.75% on. Same happens when allow_enable is set to true and no hold_power is
provided. There is currently no way to permanently enable a hold coil in OPP. 

By using the MPF hold_power parameter you can only use 8 out of 16 possible
steps. Therefore, you can also use the OPP specific parameter hold_power16
which can range from 0 to 15.

::


    coils:
      some_coil:
        number: 0-3
        pulse_ms: 32
        hold_power: 4

This will configure OPP card 0, solenoid wing 0, last solenoid to
have an initial pulse of 32 ms, and then be held on at 50% power.



5. Configuring lights with an incandescent board
------------------------------------------------

If you're using an OPP incandescent wing card, the lights are
numbered the same as the input switches.  OPP bulbs are numbered
sequentially depending on which wing board controls the output.
Wing position 0 contains bulbs 0 to 7.  Wing position 1 contains
bulbs 8 to 15.  Wing position 2 contains bulbs 16 to 23.  Wing
position 3 contains bulbs 24 to 31. The bulb is numbered using
the position of the OPP card (starting at 0), then a '-', and
finally the bulb number on the card.


::

    matrix_lights:
      some_light:
        number: 1-16

The above example configures a bulb on the second OPP card, and
the third wing board, first bulb  On the microprocessor card, the
input is marked as 2.0 (wing port 2, position 0).



6. Configuring individually addressable LED strips
--------------------------------------------------

OPP hardware can directly drive LED strips.  This features is
currently being developed.  Documentation will be added as the
feature becomes more mature.
