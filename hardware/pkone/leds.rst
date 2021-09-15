How to configure WS281XLEDs (Penny K Pinball)
=============================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/leds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/pkone`                                                         |
+------------------------------------------------------------------------------+

Each PKONE Lightshow add-on board has a built-in 8-group RGB or RGBW LED
controller (depending upon which firmware is loaded on the Lightshow) which can
drive up to 64 RGB or RGBW LEDs per group (a total of up to 512 LEDs).
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

Overview video about serial LEDs:

.. youtube:: Q9BG9T7Kj4A

Channel and Number Syntax
-------------------------

.. include:: /mechs/lights/include_channels_numbers.rst

PKONE assumes RGB or RGBW lights by default (depending upon which firmware your
Lightshow board is running). For everything else (i.e. RGBW) you have to use channels.

The PKONE Lightshow supports 512 LEDs on eight groups (64 in each group).

Light Numbers
^^^^^^^^^^^^^

The ``number:`` setting for each LED is its board's Address ID number in the
PKONE chain, a dash, the LED output group number (1-8), another dash, then
finally the LED output number in the group chain (1-64) (``address id``-``group``-``number``).
Internally, PKONE assumes three channels per LED (RGB/GRB) when running RGB firmware and four
channels per LED (RGBW) when running RGBW firmware. While assigning numbers manually will
work, it is recommended you use the newer chaining syntax referenced below in the Channels
section.

Channels
^^^^^^^^

PKONE channels use the format: ``address id``-``group``-``index``

``address id`` and ``group`` are the same as above and ``index`` is a an index from 0 to 191
for RGB firmware and 0 to 255 for RGBW firmware. The channel syntax makes it easy to mix LEDs
of various types in the same group chain (as long as they are WS281X compatible). The easiest,
and recommended, method of numbering is to chain the LEDs in your configuration file and have
MPF calculate the internal channel numbers for you (please note the ``type`` setting is
required when using ``start_channel``/``previous`` settings):

.. code-block:: mpf-config

    lights:
      led_0:
        start_channel: 0-1-0
        subtype: led
        type: rgb    # will use red: 0-1-0, green: 0-1-1, blue: 0-1-2
      led_1:
        previous: led_0
        subtype: led
        type: rgbw   # will use red: 0-1-3, green: 0-1-4, blue: 0-1-5, white: 0-1-6
      led_2:
        previous: led_1
        subtype: led
        type: rgbw   # will use red: 0-1-7, green: 0-1-8, blue: 0-1-9, white: 0-1-10

This method of chaining your LEDs works exactly the same way whether your Lightshow board is
running RGB or RGBW firmware.

See :doc:`/mechs/lights/ws2812` for additional details.

Color Correction
----------------

If you are using RGB LEDs, they might not be perfectly white when you turn
them on. They might be pinkish or blueish instead depending on the brand of
the LED. To a certain extend this is normal/expected and you can compensate
for it by configuring
:doc:`color_correction profiles in light_settings </config/light_settings>`.

subtype:
--------
Single value, type: ``string``. Defaults to empty.

This value is used to distinguish between simple LEDs and WS281X RGB LEDs in the
PKONE hardware system. This value must be set to ``led`` or left empty when setting
up WS281X RGB/RGBW LEDs.

What if it did not work?
------------------------

Have a look at our :doc:`PKONE troubleshooting guide <troubleshooting>`.
