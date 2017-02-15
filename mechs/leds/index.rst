LEDs
====

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/leds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/led_settings`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/led_stripes`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/led_rings`                                                     |
+------------------------------------------------------------------------------+
| :doc:`/config/led_player`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF can control LEDs, including single-channel (single color) and full RGB
LEDs. (You can control the order too, so you can control RGB, BRG, etc.)
You can set default fade rates and control strips and rings of LEDs.

Monitorable Properties
----------------------

For :doc:`config placeholders </config/instructions/placeholders>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for LEDs is ``device.leds.<name>``.

*color*

*corrected_color*


Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/tutorial/17_add_lights_leds`                                          |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+

.. toctree::

   lights_versus_leds


