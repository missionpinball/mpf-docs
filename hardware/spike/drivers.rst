How to configure coils & drivers (Stern SPIKE)
==============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

To configure coils, drivers, motors, and/or magnets (basically anything connected to an
node's driver outputs) for Stern SPIKE machines, you can follow the guides
and instructions in the :doc:`/mechs/coils/index` docs.

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

However there are a few things to know and some additional options you get
with SPIKE hardware that are discussed here.

number:
-------

The ``number:`` setting for each driver is a combination of the node it's connected to
and its address from the manual. For example, here's the driver reference table from
Page 11 of the Wrestlemania Pro manual:

.. image:: /hardware/images/spike_driver_table.jpg

The address for each driver is in the highlighted column. To enter the
number for the driver into MPF, remove the middle "DR" letters so you just have
the node number and address number (with a dash between them). For example,
the driver for the left flipper coil with the address ``8-DR-0``
would be entered into the MPF config as ``8-0``, etc.

.. code-block:: mpf-config

   coils:
      c_shaker:
         number: 1-10  # Node 1, coil 10
         default_pulse_ms: 100
         allow_enable: true
      c_flipper:
         number: 8-1  # Node 8, coil 1
