Coils as Lights
===============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coil_player`                                                   |
+------------------------------------------------------------------------------+

Sometimes you will find lights on a (coil) driver.
There are various reasons for this and MPF supports it.
You can either use :doc:`/config/coil_player` to control those lights but it
will be different from normal lights (and light shows).
Alternatively, you can map the coils to a light (recommended).
To map a coil as light you can use the following config:

.. code-block:: mpf-config

  coils:
    your_light_coil:
      number: 42                 # number depends on your platform
      allow_enable: true        # this will allow 100% enable without pwm
  lights:
    your_light_on_a_coil:
      number: your_light_coil     # map this light to a driver
      platform: drivers

This is sometimes done for :doc:`gis` and :doc:`flashers`.
