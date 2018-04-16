Pop Bumpers
===========

Popbumpers are configured as :doc:`autofire_coils </config/autofire_coils>` in MPF.

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

:doc:`/about/help_us_to_write_it`
