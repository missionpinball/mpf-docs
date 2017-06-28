How to use MPF with Gottlieb System 1 or 80 machines
====================================================

.. versionadded:: 0.50

MPF can directly control Gottlieb System 1 or System 80 machines via the
LISY1 or LISY80 controller boards (with firmware 4.02+).

.. note:: For general installation instruction and some background information on
   the LISY hardware platform, visit `www.lisy80.com <http://www.lisy80.com/>`_.

There are two ways this can be done:

a. Run MPF on a standalone PC which connects to the LISY hardware operating in
   "slave" mode via Ethernet, WiFi, or serial. This is generally recommended during
   development since it's easier to work on your MPF config using your own computer.
   You can also use this configuration if you want to add an LCD or DMD to the older
   Gottlieb machine.

b. Run MPF on the LISY hardware directly ("master" mode). (Technically MPF is running
   on the LISY controller's Raspberry Pi Zero.) This option is nice when your game
   is finished and you no longer want to connect a PC. Note that the Raspberry Pi on
   the LISY is not powerful enough to run the MPF media controller, so this option is
   really only valid for simpler, segment display type games. If you want to run a full
   LCD or DMD, then just run MPF on a separate computer (which can still be small and
   inside your machine) and connect to the LISY controller via Option (a) above.


See the following image for an architecture overview:

.. image:: /hardware/images/lisy_mpf_overview.jpg


1. Replace your original MPU with LISY1/80.
-------------------------------------------

For Gottlieb System80/80A/80B games you will have to look for a 'LISY80' board.
In case of an System1 look for 'LISY1' and in case you have an old Bally pinball with
an AS-2518-17 or AS-2518-35 board look for 'LISY35' which will be available in the future.

.. note:: See documentation at `www.lisy80.com <http://www.lisy80.com/>`_ for details.
          Basically you replace the MPU with the LISY board.
          You can still play the original ROM using PinMAME on LISY.

2. Active MPF at startup
------------------------

To activate mpf at startup, instead of default PinMAME, you have to put
DIP 4 (option1) and DIP 8 (autostart) to 'ON' and all other dips on that switch to 'OFF'.
If you want to run MPF on a separate PC set DIP 6 to 'ON' for "MPF Slave Mode".
For "MPF Master Mode" where MPF runs on the Rapsberry Pi of the LISY controller set DIP 6 to 'OFF'.
To enable network mode set DIP 2 to 'ON' or set DIP 2 to 'OFF' for serial mode.

.. image:: /hardware/images/LISY_modes.png

As ususal configure your specific Game Hardware via Switch 'S2'.
For instance, for Devils Dare, which is internal number '18', set S2 DIP 2 and
DIP 5 to 'ON' and all others to 'OFF' (binary coding of decimal 18).

2a. Connect your PC running MPF to LISY via network or serial (only needed for MPF Slave Mode)
----------------------------------------------------------------------------------------------

You can connect the Raspberry Pi via USB to your PC to use the serial port.
In that case add the following config to your machine:

.. code-block:: yaml

  hardware:
    platform: lisy

  lisy:
    connection: serial
    port: com1               # replace this with your com port
    baud: 115200

Alternatively, if you connect LISY via ethernet or WiFi use this config:

.. code-block:: yaml

  hardware:
    platform: lisy

  lisy:
    connection: network
    network_port: 5963
    network_host: a.b.c.d    # replace this with the IP of LISY


2b. Add MPF config to SD Card (only needed for MPF Master Mode)
---------------------------------------------------------------

Place your MPF config in the folder "/boot/mpfcfg/xxx/" on the SD-Card (replace xxx with
your game number with leading zeros if it is shorter than three digits).
For instance with Dare Devil, the game would be at "/boot/mpfcfg/018/" on the SD-Card.
Use an SD-card reader on your PC to add the config.
Alternatively, you could copy the files using SSH onto a running LISY controller (see
`www.lisy80.com <http://www.lisy80.com/>`_ for details).
As noted above, we suggest you to run MPF on your PC first and copy the config over once it it working.
This mode will not allow you to run MPF-MC (which is also not needed for the segment displays):

3. Power up LISY
----------------

Power up your system and enjoy.

3a. Start MPF (only needed for MPF Slave Mode)
----------------------------------------------

Start MPF on you PC. Optionally start MPF-MC (if you want to use an additional DMD or LCD).
