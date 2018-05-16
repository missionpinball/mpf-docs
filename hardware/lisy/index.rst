How to use MPF with Gottlieb System 1 or 80 machines
====================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/lisy`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

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

For Gottlieb System80/80A/80B games, replace the existing Gottlieb CPU with the "LISY80" board.
For System 1 machines, replace the existing Gottlieb CPU board with the "LISY1" board. (Note that
the people who created the LISY boards are also working on a "LIST35" board for old
Bally machines with AS-2518-17 or AS-2518-35 CPU boards).

.. note:: See documentation at `www.lisy80.com <http://www.lisy80.com/>`_ for details.
          Basically you replace the MPU with the LISY board.
          You can still play the original ROM using PinMAME on LISY.


.. image:: /hardware/images/lisy80_board.jpg

2. Configure LISY DIP switches
------------------------------

If you want to run MPF on the LISY controller itself, set DIP 4 (option1) and
DIP 8 (autostart) to 'ON' and all other DIPs on that switch to 'OFF'. This
will configure the LISY board to boot to MPF instead of the default PinMAME.

If you want to use the LISY board in "slave" mode where you run MPF on a
separate computer and remotely control the LISY board, set DIP 6 to 'ON'.
Then to control the mode that the LISY board will communicate with the host
PC running MPF, set DIP 2 to 'ON' for network mode or 'OFF' for serial mode.

.. image:: /hardware/images/LISY_modes.png

As usual, configure your specific Game Hardware via Switch 'S2'.
For instance, for *Devils Dare*, which is internal number '18', set S2 DIP 2 and
DIP 5 to 'ON' and all others to 'OFF' (binary coding of decimal 18).

3a. Add MPF config to SD Card (only needed for MPF Master Mode)
---------------------------------------------------------------

If you're using the "master" mode where MPF runs on the LISY board itself, you need to
get your MPF config installed onto the LISY board. You can do this via the SD card.

Place your MPF config in the folder ``/boot/mpfcfg/xxx/`` on the SD Card (replace "xxx" with
your game number with leading zeros if it's shorter than three digits).
For instance with *Dare Devil*, the game would be at ``/boot/mpfcfg/018/`` on the SD card.

It's easiest to do this with an SD card reader on your computer, though you could also copy
the files using SSH connected to a running LISY controller (see
`www.lisy80.com <http://www.lisy80.com/>`_ for details).

Again, we only recommend this option for your "final" config, as it's much easier to use the
LISY board in slave mode and run MPF off your computer while you're developing your game.

.. warning::

   This mode of operation will not allow you to run the MPF-MC since the LISY's Raspberry Pi Zero
   is not powerful enough. If you want to add an LCD or DMD to your machine, use the slave option
   detailed below.

3b. Connect your PC running MPF to LISY via network or serial (only needed for MPF Slave Mode)
----------------------------------------------------------------------------------------------

If you're using the "slave" mode where you run MPF on a standalone computer and then connect to
the LISY board via the network or serial, once you configure the LISY board's DIP switches from
Step 2 then you need to update your machine config file for MPF running on your computer to
be able to connect to the LISY board.

If you want to use the serial port, add/update the following sections in your machine config:

.. code-block:: mpf-config

  hardware:
    platform: lisy

  lisy:
    connection: serial
    port: com1               # replace this with your com port
    baud: 115200

Alternatively, if you want to connect using WiFi or Ethernet, add/update the following sections
in your machine config:

.. code-block:: mpf-config

  hardware:
    platform: lisy

  lisy:
    connection: network
    network_port: 5963
    network_host: a.b.c.d    # replace this with the IP of LISY

4. Power up LISY
----------------

Power up your system and enjoy.

4a. Start MPF (only needed for MPF Slave Mode)
----------------------------------------------

Start MPF on you PC. Optionally start MPF-MC (if you want to use an additional DMD or LCD).
