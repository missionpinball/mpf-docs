Slingshots
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/drop_target_banks`                                             |
+------------------------------------------------------------------------------+

Slingshots are configured as :doc:`autofire_coils </config/autofire_coils>` in MPF.

This is an example:

.. code-block:: mpf-config

   switches:
       s_sling_left:
           number: 5
   coils:
       c_sling_left:
           number: 7
           default_pulse_ms: 15

   autofire_coils:
       ac_slingshot_left:
           coil: c_sling_left
           switch: s_sling_left

Adjust ``default_pulse_ms`` and ``default_pulse_power`` in your coil
to control the strength and sound of your slingshots.
