How to configure WS281XLEDs (Penny K Pinball)
=============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/leds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/pkone`                                                         |
+------------------------------------------------------------------------------+

Each PKONE Lightshow add-on board has a built-in 8-group RGB LED
controller which can drive up to 64 RGB LEDs per group (a total of up to 512 LEDs).
This controller uses serially-controlled LEDs (where each LED element has a
little serial protocol decoder chip in it), allowing you to drive dozens of LEDs
from a single data wire. These LEDs are generally known as "WS2812" (or similar).
You can buy them from many different companies, and they're what's sold as the
"NeoPixel" brand of products from Adafruit. (They have all different shapes and
sizes.)

.. image:: /hardware/images/pkone-lightshow.png

Most of the settings in the :doc:`/mechs/lights/index` documentation apply to LEDs
connected to PKONE Lightshow boards, however there are a few PKONE-specific
things to know.

Channel and Number Syntax
-------------------------

.. include:: /mechs/lights/include_channels_numbers.rst

PKONE assumes RGB lights by default.
For everything else (i.e. RGBW) you have to use channels.

The PKONE Lightshow supports 512 LEDs on eight groups (64 in each group).

Light Numbers
^^^^^^^^^^^^^

The ``number:`` setting for each LED is its board's Address ID number in the
PKONE chain, a dash, the LED output group letter (A-H), another dash, then
finally the LED output number in the group chain (``address id``-``group``-``number``).
Internally, PKONE assumes three channels per LED (RGB/GRB
:doc:`WS2811/WS2812 LEDs </mechs/lights/ws2812>`).

Channels
^^^^^^^^

PKONE channels use the format: ``address id``-``group``-``number``-``index``

``address id``, ``group``, and ``number`` are the same as above and ``index`` is a an index from 0 to 2.
This is because serial LEDs are traditionally RGB (or GRB) LEDs with exactly
three channels. However, this is not true for RGBW or similar LEDs which do not work with this
style of numbering. Luckily, you can chain them instead and have MPF calculate the internal
channels for you:

.. code-block:: mpf-config

    lights:
      led_0:
        start_channel: 0-A-0-0      # you could also use number: 0-A-0
        subtype: led
        type: rgb    # will use red: 0-A-0-0, green: 0-A-0-1, blue: 0-A-0-2
      led_1:
        previous: led_0
        subtype: led
        type: rgbw   # will use red: 0-A-1-0, green: 0-A-1-2, blue: 0-A-1-3, white: 0-A-2-0
      led_2:
        previous: led_1
        subtype: led
        type: rgbw   # will use red: 0-A-2-1, green: 0-A-2-2, blue: 0-A-3-0, white: 0-A-3-1

See :doc:`/mechs/lights/ws2812` for details.

Color Correction
----------------

If you are using RGB LEDs, they might not be perfectly white when you turn
them on. They might be pinkish or blueish instead depending on the brand of
the LED. To a certain extend this is normal/expected and you can compensate
for it by configuring
:doc:`color_correction profiles in light_settings </config/light_settings>`.

What if it did not work?
------------------------

Have a look at our :doc:`PKONE troubleshooting guide <troubleshooting>`.
