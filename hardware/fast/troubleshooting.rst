Troubleshooting FAST
====================

If you got problems with your hardware platform we first recommend to read our
:doc:`troubleshooting guide </troubleshooting/index>`.
Here are some hardware platform specific steps:

Run Hardware Scan
-----------------

Using ``mpf hardware scan`` you can find out if your Nano is talking
properly to MPF using USB.
Additionally, it will show you which node boards are connected:

.. code-block:: console

   $ mpf hardware scan

   NET CPU: NET FP-CPU-002-1 01.03
   RGB CPU: RGB FP-CPU-002-1 00.89
   DMD CPU: DMD FP-CPU-002-1 00.88

   Boards:
   Board 0 - Model: FP-I/O-3208-2    Firmware: 01.00 Switches: 32 Drivers: 8
   Board 1 - Model: FP-I/O-0804-1    Firmware: 01.00 Switches: 8 Drivers: 4
   Board 2 - Model: FP-I/O-1616-2    Firmware: 01.00 Switches: 16 Drivers: 16
   Board 3 - Model: FP-I/O-1616-2    Firmware: 01.00 Switches: 16 Drivers: 16

If you are missing boards here check your wiring.
Also verify that firmware versions match.
In the example above the NET CPU has firmware 1.03 but the nodes still run on
1.00 which indicates an issue.
See :doc:`/running/commands/hardware` for details about the command.

Enable Debugging
----------------

If you got problems with your platform try to enable ``debug`` first.
As described in the
:doc:`general debugging section </troubleshooting/general_debugging>`
of our :doc:`troubleshooting guide </troubleshooting/index>`
this is done by
adding ``debug: true`` to your ``fast`` config section:

.. code-block:: mpf-config

   fast:
     debug: true

This will add a lot more debugging and might slow down MPF a bit.
We recommend to disable/remove it after finishing debugging.

.. include:: ../include_troubleshooting.rst
