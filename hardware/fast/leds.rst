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

number:
-------

There are two ways you can configure RGB LEDs for your FAST
controller: by channel & output number, or directly with the FAST
hardware number. It's more straightforward to configure them by
channel and output, like this:

.. code-block:: mpf-config

   lights:
       l_led0:
           number: 0-0
           type: grb
       l_right_ramp:
           number: 2-28
           type: grb

In the example above, RGB LED *l_led0* is LED #0 on channel 0, and
*l_right_ramp* is LED #28 on channel 2. Note both the channel and LED
numbers start with 0, so your channel options for a FAST controller
are 0-3, and your LED number options are 0-63. Also note that when you
enter your FAST LED numbers with a dash like this, the values are
integers, even if the rest of your FAST settings are in hex.
Type `grb` configures the LED as WS2812 (such as the FAST LEDs) but it
might be different for other types of LEDs. See :doc:`/config/lights`
for details.

If you know the actual hex numbers of your LEDs, you can enter the numbers like
that, ranging from 00 to FF. If you don't know what this means, then just
ignore it and use the channel and LED number format with the dash. :)

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
