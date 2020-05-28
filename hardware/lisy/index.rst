How to use MPF with the LISY platform
=====================================

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
Additionally, `LISY35 <https://lisy.dev/lisy35.html>`_ can control Bally and
Stern Games manufactured from 1977 to 1985 with MPU AS-2518-17 or AS-2518-35.

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

LISY can controll all features of your Gottlieb System1/80 machine.
This includes:

* Switches (:doc:`LISY1 <switches_lisy1>` and :doc:`LISY80 <switches_lisy80>`)
* :doc:`Coils <drivers>`
* :doc:`Lights <lights>`
* :doc:`Enabling/disabling flipper, slings and popbumpers <flippers_slings_popbumpers>`
* :doc:`Segment displays <segment_displays>`
* :doc:`Original sounds of your game <sound>`
* :doc:`Text to speech and additional sounds <sound>`

.. toctree::
   :titlesonly:

   connection
   switches_lisy1
   switches_lisy80
   drivers
   flippers_slings_popbumpers
   lights
   segment_displays
   sound
   protocol
   troubleshooting
