Pop Bumpers
===========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/autofire_coils`                                                |
+------------------------------------------------------------------------------+

Popbumpers are configured as :doc:`autofire_coils </config/autofire_coils>` in MPF.

:doc:`TODO: Add a picture of pop bumpers </about/help_us_to_write_it>`

This is an example:

.. code-block:: mpf-config

   switches:
       s_popbumper_left:
           number: 7
   coils:
       c_popbumper_left:
           number: 4
           default_pulse_ms: 23

   autofire_coils:
       ac_popbumper_left:
           coil: c_popbumper_left
           switch: s_popbumper_left


Adjust ``default_pulse_ms`` and ``default_pulse_power`` in your coil
to control the strength and sound of your popbumpers.
