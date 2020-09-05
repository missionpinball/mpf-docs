Configuring Drivers in LISY
===========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

Configure drivers according to the manual of your machine.
LISY does not support any ``hold_power`` or ``pulse_power`` other than 1.0.
So the coil will always enable with full power (which is fine in older
machines and should not break things).
However, you can still choose the pulse length using ``pulse_ms``.

.. code-block:: mpf-config

   coils:
     c_some_coil:
       number: 04
       default_pulse_ms: 10
       allow_enable: true

In some Gottlieb machines coils were connected to the lights bank.
To address those you have to add 100 to their number from the manual.
For instance, to address a coil which is connected to the light output ``05``
use coil ``105``:

.. code-block:: mpf-config

   coils:
     c_coil_on_light_bank:
       number: 107
       default_pulse_ms: 10

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.

.. include:: ../driver_related_howto_guides.rst
