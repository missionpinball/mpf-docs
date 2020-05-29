Downloading & Installing MPF
============================

Installing MPF is fairly straightforward. It can be used on Windows, Mac, or Linux, on both Intel x86 and ARM
processors, and in 64-bit and 32-bit systems (see :doc:`/hardware/computer/index` for details).

Installing MPF for the first time
---------------------------------

We've created step-by-step installation guides which walk you through the
entire process. Select the OS you're using from the list below:

.. toctree::
   :maxdepth: 1

   Windows <windows>
   Mac <mac>
   Linux <linux/index>
   Virtual Machine (Debian) <virtual-machine/index>

.. note::
   These guides just show you how to get MPF up and running. If you're using
   MPF with a physical machine, check out the :doc:`/hardware/index` guide for
   details about how to get the drivers and configuration set for the
   specific hardware controller platform you've chosen.

Installing the MPF Monitor
--------------------------

We have a rough prototype of a graphical tool called the "MPF Monitor" which
you can use to connect to a running instance of MPF to graphically interact
with switches, lights, and LEDs, and to see the status of various devices. You
can even add a picture of your playfield and drag-and-drop the MPF mechanisms
onto it which makes it possible to "play" your machine via a simulation.

Details in the MPF Monitor are :doc:`here </tools/monitor/index>`.

Migrating from previous versions of MPF
---------------------------------------

.. toctree::
   :maxdepth: 1

   migrating
   migrate4to5

