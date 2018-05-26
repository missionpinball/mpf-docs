Configuring Drivers in LISY
===========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

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
