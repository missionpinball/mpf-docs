How to use MPF with Gottlieb System 1 or 80 machines
====================================================

Starting with MPF 0.50 and LISY firmware version 4.02, Gottlieb System 1 and 80 machines
can be interfaced from MPF using the LISY1 or LISY80 controller boards.
You can run MPF on the LISY controller or on an external PC (via ethernet/wifi or serial).
The image of LISY Version 4.x and above includes the MPF game engine.

.. note:: For general installation instruction and some background information visit www.lisy80.com.
          More documentation is available there.


Two ways exist to use MPF with LISY:

a. Running MPF on a separate PC and connecting to LISY via network or serial (slave mode)
   This is generally recommended during development because it is easier to work on your MPF config using this setup.
   You may use a LCD/DMD and the MPF media controller as well.

b. Running MPF on LISY directly (master mode).
   This is useful when your game is finished and you no longer want to connect a PC.
   Please note that the Raspberry Pi on LISY is not powerful enough to run the MPF media controller.


See the following image for an architecture overview:

.. image:: /hardware/images/lisy_mpf_overview.jpg


1. Replace your original MPU with LISY1/80.
-------------------------------------------

For Gottlieb System80/80A/80B games you will have to look for a 'LISY80' board.
In case of an System1 look for 'LISY1' and in case you have an old Bally pinball with
an AS-2518-17 or AS-2518-35 board look for 'LISY35' which will be available in the future.

.. note:: See documentation at www.lisy80.com for details. Basically you replace
          the MPU with the LISY board. You can still play the original ROM using
          PinMAME on LISY.

2. Active MPF at startup
------------------------

To activate mpf at startup, instead of default PinMAME, you have to put
DIP 4 (option1) and DIP 8 (autostart) to 'ON' and all other dips on that switch to 'OFF'.
If you want to run MPF on a separate PC set DIP 6 to 'ON' for "MPF Slave Mode".
For "MPF Master Mode" where MPF runs on the Rapsberry Pi of the LISY controller set DIP 6 to 'OFF'.

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
Alternatively, you could copy the files using SSH onto a running LISY controller (see www.lisy.com for details).
As noted above, we suggest you to run MPF on your PC first and copy the config over once it it working.

3. Power up LISY
----------------

Power up your system and enjoy.

3a. Start MPF (only needed for MPF Slave Mode)
----------------------------------------------

Start MPF on you PC. Optionally
