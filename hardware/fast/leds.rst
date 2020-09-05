How to configure LEDs (FAST Pinball)
====================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/leds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/fast`                                                          |
+------------------------------------------------------------------------------+

Each FAST Pinball Controller has a built-in 4-channel RGB LED
controller which can drive up to 64 RGB LEDs per channel. This
controller uses serially-controlled LEDs (where each LED element has a
little serial protocol decoder chip in it), allowing you to drive
dozens of LEDs from a single data wire. These LEDs are generally known
as "WS2812" (or similar). You can buy them from many different
companies, and they're what's sold as the "NeoPixel" brand of
products from Adafruit. (They have all different shapes and sizes.)

.. image:: /hardware/images/fast-nano.png

Most of the settings in the :doc:`/mechs/lights/index` documentation apply to LEDs
connected to FAST Pinball controllers, however there are a few FAST-specific
things to know.

Channel and Number Syntax
-------------------------

.. include:: /mechs/lights/include_channels_numbers.rst

FAST assumes RGB lights by default.
For everything else (i.e. RGBW) you have to use channels.

The FAST Nano supports 256 LEDs on four chains.
LEDs 0-63 are on chain 0, 64-127 on chain 1, 128-195 on chain 2 and 196-255 on chain 3.

Light Numbers
^^^^^^^^^^^^^

FAST numbers use the format: ``number``

This is as easy as it gets.
Just provide the number of you LED in the chain.
Internally, FAST assumes three channels per LED (RGB/GRB
:doc:`WS2811/WS2812 LEDs </mechs/lights/ws2812>`).

Channels
^^^^^^^^

FAST channels use the format: ``number``-``index``

``number`` is the same as above and ``index`` is a an index from 0 to 2.
This is because serial LEDs are traditionally RGB (or GRB) LEDs with exactly
three channels.
However, this is not true for RGBW or similar LEDs which do not work with this
style of numbering.
Luckily, you can chain them instead and have MPF calculate the internal
channels for you:

.. code-block:: mpf-config

    lights:
      led_0:
        start_channel: 0      # you could also use number: 0
        subtype: led
        type: rgb    # will use red: 0-0, green: 0-1, blue: 0-2
      led_1:
        previous: led_0
        subtype: led
        type: rgbw   # will use red: 1-0, green: 1-2, blue: 1-3, white: 2-0
      led_2:
        previous: led_1
        subtype: led
        type: rgbw   # will use red: 2-1, green: 2-2, blue: 3-0, white: 3-1

See :doc:`/mechs/lights/ws2812` for details.

RGB LED buffering
-----------------

Most computers have the ability to send LED updates to the FAST Pinball
controller faster than the controller can process them. If this happens, then
the LED command messages can get backlogged and it will appear that you have
a "delay" in your LEDs and/or you might get weird colors due to corrupt
messages.

To help combat this, there are two settings you can adjust:

.. code-block:: mpf-config

   mpf:
     default_light_hw_update_hz: 50
   fast:
     rgb_buffer: 3

If you notice that your LEDs seem to be getting behind, you can adjust the
``default_led_hw_update_hz:`` setting to be lower. (Frankly the 50hz by
default is too high and we should lower it to 30.) You can probably drive
128 or so LEDs at 50Hz, but if you have more than that then you might need to
start playing with this number.

Hardware LED fading
-------------------

You can globally set the fade rate for LEDs connected to a FAST Pinball
controller via the ``fast:hardware_led_fade_time:`` setting. (This is ``0ms``
by default, meaning it's disabled.)

See the :doc:`/config/fast` section of the config file reference for details.

Color Correction
----------------

If you are using RGB LEDs, they might not be perfectly white when you turn
them on. They might be pinkish or blueish instead depending on the brand of
the LED. To a certain extend this is normal/expected and you can compensate
for it by configuring
:doc:`color_correction profiles in light_settings </config/light_settings>`.

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
