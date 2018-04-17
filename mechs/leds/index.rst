LEDs
====
+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_settings`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/light_stripes`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/config/light_rings`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF can control LEDs, including single-channel (single color) and full RGB
LEDs. (You can control the order too, so you can control RGB, BRG, etc.)
You can set default fade rates and control strips and rings of LEDs.

In general there are two ways to wire LEDs in a pinball machine.
Either parallel or serial.
With serial LEDs you got a chain of LEDs which are connected to a controller
board on one side.
In contrast, with parallel LEDs every LED has its own wire(s) to the controller.
While parallel LEDs are more robust in general they also require much more wiring.
Which kind of LEDs your using usually depends on what is supported in your
platform (some support both).

Serial LEDs
-----------

With serial LEDs the order of colors is usually fixed. For instance, in WS2811
LEDs (a common serial LED controller embedded inside the LED), the first
channel is red, the second green and third is blue (RGB order).
Newer WS2812 LEDs have GRB order (green, red and blue).
Some LEDs also contain an additional white channel and thereby have four
channels (either RGBW or GRBW order).
Other serial LEDs contain three white LEDs (WWW order).
If nothing is specified MPF assumes RGB order so you need to specify it for any
LED with a different channel order.


.. code-block:: mpf-config

  lights:
      my_ws2811:
            number: 0   # first LED in chain (with three channels)
            type: rgb   # redundant
      my_ws2812:
            number: 1   # second LED in chain (with three channels)
            type: grb
      my_serial_white_leds:
            number: 2   # third LED in chain (with three channels)
            type: www


The numbering depends on your platform. Internally the first LED will
map to the first three LEDs in the chain (because one LED contains three
interal LEDs). The second will map to LED four to six and so on.

The config above is equivalent to the following (again numbers may be different per platform):

.. code-block:: mpf-config

  lights:
     my_ws2811:
       channels:
           red:
              - number: 0-0
           green:
              - number: 0-1
           blue:
              - number: 0-2
     my_ws2812:
        channels:
           red:
              - number: 1-1
           green:
              - number: 1-0
           blue:
              - number: 1-2

RGBW LEDs are special in most serial LED controllers since the controller
assumes that every LED has exactly three channels. Therefore, you have to
assign the channels directly:

.. code-block:: mpf-config

  lights:
     my_rgbw_serial_led:
        channels:
           red:
              - number: 3-0
           green:
              - number: 3-1
           blue:
              - number: 3-2
           white:
              - number: 4-0
     my_ws2812_after_rgbw: 
        channels:
           red:
              - number: 4-1
           green:
              - number: 4-2
           blue:
              - number: 5-0

The RGBW shifts all the channels by one internally. As you can see this can
quickly become confusing so it might be wise to run RGBW LEDs (or any 
non-three-channel LEDs) as a separate chain.

Parallel LEDs
-------------

With parallel LEDs you usually got a bit more flexibility with your channel
assignments. You can dedice to make an LED with only a red channel for example.
MPF cannot guess your hardware layout in most platforms.
Therefore your have to explicitly tell MPF your channel layout:

.. code-block:: mpf-config

  lights:
      my_red_only_insert:
        channels:
           red:
              - number: 0
      my_rgb_insert:
        channels:
           red:
              - number: 1
           green:
              - number: 3
           blue:
              - number: 2
      my_white_light:
        channels:
           white:
              - number: 4

You can also have multiple channels per color (if you do not want to make them different lights):

.. code-block:: mpf-config

  lights:
      multi_white_channels:
        channels:
           white:
              - number: 5
              - number: 6
              - number: 7


Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for LEDs is ``device.lights.<name>``.

*color*

*corrected_color*


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


