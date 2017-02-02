How to configure LEDs & GI (Stern SPIKE)
========================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/matrix_lights`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/config/leds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+

Stern SPIKE machines have replaced all incandescent lights with LEDs. Instead of
a lamp matrix, individual LEDs are connected to node boards and can be controlled
with 256 levels of brightness.

GI (general illumination) are regular LEDs, and so are flashers, and so are the
white backlight LEDs in the backbox. So pretty much everything is an LED.

Many LEDs are single element, single color, with colored insers in front of them.
This means that you cannot control the color of the LED, rather, you just control
the brightness and the color is what it is.

Most machines also have RGB LEDs that can be set to any color. In those cases
the individual red, green, and blue channels each have their own addresses, and
then you can group them together into a single, logical RGB LED that you can
set to whatever color you want.

Finally, in SPIKE machines, you'll sometimes see several LEDs connected to a single
output, meaning that when you set the brightness of that output, you're setting the
brightness for all those LEDs.

MPF uses the ``matrix_lights:`` section of the machine config to define LEDs. (This
is somewhat confusing because LEDs in a SPIKE system are certainly *not* matrix lights,
but the LED system in MPF currently assumes that all LEDs are RGB LEDs, and that's not
how Stern SPIKE systems work. So you configure your LEDs as matrix lights. (This will
be fixed in a feature version of MPF.)

Most of the settings in the :doc:`/mechs/lights/index` documentation apply to LEDs
in Stern SPIKE machines, though there are a few SPIKE-specific things to know.

number:
-------

The main thing you need to know about configuring LEDs (besides the fact that you
add them to the ``matrix_lights:`` section of your config) is how the hardware
numbering works.

Pretty much you just look up the number in the manual for your machine and then
enter it without any letters. For example, here is (part of) the lighting chart
from Wrestlemania Pro:

.. image:: /hardware/images/spike_light_table.jpg

Use the address column (highlighted in yellow) to get the numbers for each LED.
Remove the "LP" letters, and also remove any lowercase letters (like the "a") from
the node. What you're left with is the node address and LED number.

For example, the Shoot Again light with the address ``8a-LP-47`` would be entered
as ``number: 8-47``.

.. code-block:: yaml

   matrix_lights:
      backlight:
         number: 0-0  # 0-0 is the special address for the backlight
      start_button:
         number: 1-2
      tourney_start_button:
         number: 1-3
      shoot_again:
         number: 8-47

The backbox backlight
   Stern SPIKE systems have controllable brightness for the white lights in the backbox
   that illuminate the translight. All of those LEDs are tied together and controlled
   as one with the address ``0-0``.

GI (General Illumination)
   GI in Stern SPIKE systems are just regular LEDs. You can tag them with the tag ``gi``
   and then turn them on in the attract mode and/or use them in shows for special effects.
   Really there's nothing special about them. They're just lights. (Just remember they're
   controlled and defined as "lights", not as "GIs".)

Flashers
   Flashers in Stern SPIKE systems are also controlled just like normal lights. They just
   happen to be super bright, but other than that, use them like any other LED. (Just
   remember they're controlled and defined as "lights", not as "flashers".)

RGB LEDs
--------

You'll notice in the operator's manual that RGB LEDs are actually three separate
LEDs with a separate address for the red, green, and blue channel. Since MPF deals
with RGB LEDs as single objects you can set to any color, you need to group the
three individual channels of RGB LEDs into single RGB objects.

Here's an example from the Wrestlemania Pro manual:


.. image:: /hardware/images/spike_rgb_light_table.jpg

You'd enter the three channels as three separate lights in the ``matrix_lights:`` section
of your machine config.

Once you do that, add a ``leds:`` section to your config, and then create an entry for
the RGB LED name you'd like to use to control refer to the RGB LED which you can then
set to any color. Then under there, for the ``number:``, enter the three names from the
``matrix_lights:`` section (in order red, green, blue), and add the entry ``platform: lights``.

What this does is create a new virtual RGB LED which is a grouping of the three LED
channels into the RGB LED. Then you can use it like any LED.

Note that when you do this, you will control the RGB LEDs as "leds" in your configs,
while you'll control the single color LEDs, the GI, and the backbox light as "lights".
Is that weird? Yes. But it works.

.. code-block:: yaml

   matrix_lights:
      left_lane_arrow_red:
         number: 11-3
      left_lane_arrow_green:
         number: 11-4
      left_lane_arrow_blue:
         number: 11-5

   leds:
      left_lane_arrow:
         number: left_lane_arrow_red, left_lane_arrow_green, left_lane_arrow_blue
         platform: lights

