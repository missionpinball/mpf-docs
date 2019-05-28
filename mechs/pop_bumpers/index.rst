Pop Bumpers
===========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/autofire_coils`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

Popbumpers are configured as
:doc:`autofire_coils </mechs/autofire_coils/index>` in MPF.

Hardware
--------

:doc:`TODO: Add a picture of pop bumpers </about/help_us_to_write_it>`

Pop bumpers are made of three elements:

 * A :doc:`blade switch </mechs/switches/mechanical_switches>` to notice balls
 * A #444 or #249 :doc:`bulb </mechs/lights/matrix_lights>` for light shows
 * A :doc:`coil </mechs/coils/index>` to push the ball away.

Config
------

This is an example:

.. code-block:: mpf-config

   switches:
      s_popbumper_left:
         number: 7               # depends on your platform
   coils:
      c_popbumper_left:
         number: 4               # depends on your platform
         default_pulse_ms: 23    # tune this for your machine

   lights:
      l_popbumper_left:
         number: 13              # depends on your platform
         subtype: matrix         # might be differnt

   autofire_coils:
       ac_popbumper_left:
           coil: c_popbumper_left
           switch: s_popbumper_left


Adjust ``default_pulse_ms`` and ``default_pulse_power`` in your coil
to control the strength and sound of your popbumpers.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/mechs/switches/mechanical_switches`                                   |
+------------------------------------------------------------------------------+
| :doc:`/mechs/lights/matrix_lights`                                           |
+------------------------------------------------------------------------------+
| :doc:`/mechs/coils/index`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/mechs/autofire_coils/index`                                           |
+------------------------------------------------------------------------------+
