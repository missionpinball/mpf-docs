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
See :doc:`lights_versus_leds` for details.

There are multiple types of lights (read those for specific details):

* :doc:`leds`
* :doc:`gis`
* :doc:`matrix_lights`
* :doc:`flashers`
* :doc:`coils_as_lights`


.. image:: /mechs/images/lights_vs_leds.jpg

This is an example of for a light:

.. code-block:: mpf-config

  lights:
    my_led:
      number: 7

For WS2812 LEDs use ``type: grb`` (WS2811 does not need this):

.. code-block:: mpf-config

  lights:
    my_ws2812_led:
      number: 23
      type: grb

You can also map individual color channels:

.. code-block:: mpf-config

  lights:
    rgb_led:
      type: rgb
      channels:
        red:
          number: 9-29
        green:
          number: 9-30
        blue:
          number: 9-31
        white:
          number: 9-32

If your light is connected to a driver use this example:

.. code-block:: mpf-config

  coils:
    light_connected_to_a_driver:
      number: 42           # number depends on your platform
      allow_enable: True	# this will allow 100% enable without pwm

  lights:     
    light_on_a_driver:
      number: light_connected_to_a_driver	# map this light to a driver
      platform: drivers

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


.. toctree::

   leds
   lights_versus_leds
   gis
   matrix_lights
   flashers
   coils_as_lights
