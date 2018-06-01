Lights
======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_settings`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+

.. contents::
   :local:

In MPF 0.50 all LEDs, matrix lights and GIs are configured as :doc:`/config/lights`.
See :doc:`/mechs/leds/lights_versus_leds` for details.

:doc:`TODO: Add a picture of leds </about/help_us_to_write_it>`
:doc:`TODO: Add a picture of bulbs </about/help_us_to_write_it>`

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for lights is ``device.lights.<name>``.

*brightness*
   The numeric value of the brightness of this light, from 0-255.

*color*
   The current color.


Related How To guides
---------------------

* :doc:`/tutorial/17_add_lights_leds`

Related Events
--------------

None
