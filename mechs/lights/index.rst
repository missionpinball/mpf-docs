Lights
======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/matrix_lights`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/config/matrix_light_settings`                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+

.. contents::
   :local:

.. todo::
   TODO

Note that LEDs plugged into lamp matrices are configured here as lights, not
in the ``leds:`` section. See :doc:`/mechs/leds/lights_versus_leds` for details.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for lights is ``device.lights.<name>``.

*brightness*
   The numeric value of the brightness of this light, from 0-255.

Related How To guides
---------------------

* :doc:`/tutorial/17_add_lights_leds`

Related Events
--------------

None
