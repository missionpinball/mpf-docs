How to configure MPF for Stern SPIKE hardware
=============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+

This guide explains how to configure MPF to work with Stern SPIKE pinball
machines. It applies to SPIKE and SPIKE 2 systems.

1. Install the drivers for your USB-to-serial adapter
-----------------------------------------------------

Before you proceed, make sure that you have the drivers
properly installed for your USB-to-serial adapter and that
when you plug it in, you see the serial port.

2. Configure your hardware platform for SPIKE
---------------------------------------------

To use MPF with a SPIKE hardware, you need to configure your platform as ``spike`` in your
machine-wide config file. You'll also need to add a "spike:" section with some additional
settings:

.. code-block:: yaml

   hardware:
      platform: spike

   spike:
      port: /dev/ttyUSB0
      baud: 115200
      debug: False
      nodes: 0, 1, 8, 9, 10, 11

Some notes on the settings:

port:


   Use the port of your USB-serial adapter or of the internal serial
   on the RPi. On Windows, this will have a name like "COM5".

baud:
   This needs to match the value from Step 3 in the
   :doc:`MPF SPIKE bridge instructions <mpf-spike-bridge>`. Note that since
   only control and switch information is sent across this bus, 115k baud is
   plenty fast enough, though it can technically support more.

debug:
   Set this to true for print more details in the log.

nodes:
   This is a list of the node board addresses that your system has. You can
   get this from the manual. Here's an example from Wrestlemania Pro:

   .. image:: /hardware/images/spike_node_table.png

   Only map the node boards and ignore the extension boards because those
   are transparent to MPF. Just consider 8 and 8a/8b to be the same node.
