How to use MPF with Gottlieb System 1 or 80 machines
====================================================

Starting with MPF 0.50, Gottlieb System 1 and 80 can be interfaced using the LISY1 or LISY80 platform.
You can run MPF on the LISY controller or on an external PC (via ethernet/wifi or serial).
The image of LISY Version 4.x and above includes the MPF game engine.

.. note:: For general installation instruction and some background information FIRST
          visit www.lisy80.com, lot of documentation is available there.


Two ways exist to use MPF with LISY.

a. Running MPF on a separate PC and connecting to LISY via network or serial (slave mode)
   This is generally recommended during development because it is easier to work on your MPF config using this setup.
   You may use a LCD/DMD and the MPF media controller as well.

b. Running MPF on LISY directly (master mode).
   This is useful when your game is finished and you no longer want to connect a PC.
   Please note that the Raspberry Pi on LISY is not powerful enough to run the MPF media controller.


See the following image for an architecture overview:

.. image:: /hardware/images/lisy_mpf_overview.jpg


In this example we will assume you have a System80 pinball 'Devils Dare', where
the image includes a small example of configuration mpf yaml configuration files.

1. Replace your original MPU with LISY80.
-----------------------------------------

As Devils Dare is a Gottlieb System80A Game you will have to look for a 'LISY80' board.
LISY80 supports all System80, System80A and SyStem80B games.
In case of an System1 look for 'LISY1' and in case you have an old Bally pinball with
an AS-2518-17 or AS-2518-35 board look for 'LISY35' which will be available in the future.

.. note:: See documentation at www.lisy80.com for details. Basically you replace
          the MPU with the LISY board. You can still play the original ROM using
          PinMAME on LISY.

2. Active MPF at startup
------------------------

To activate mpf at startup, instead of default pinmame, you have to put
dip4 (Option1) and dip8 (Autostart) to 'ON' and all other dips on that switch to 'OFF'.
As ususal configure your specific Game Hardware via Switch 'S2'.
In our example, for Devils Dare which is internal number'18', this means you have to
configure S2 dip2 & dip5 to 'ON' and all others to 'OFF' (binary coding of decimal 18)

3. Add MPF config to SD Card
----------------------------

As with internal number '18', the mpf configuration has to be placed in the folder
"/boot/mpfcfg/018/" on the SD-Card. For this example you can run with the exisitng
example yaml files or edit them within Windows (mount SD card) or within Linux.
For Linux the systen can be accessed via network or via the serial console, again please have
a look at the existing documentation at www.lisy80.com.

4. Power up
-----------

Power up your system and enjoy.

