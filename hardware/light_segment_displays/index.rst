How to Connect Segment Displays as Lights to MPF
================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/segment_displays`                                              |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_segment_displays`                                        |
+------------------------------------------------------------------------------+

MPF can map segment displays to arbitrary lights which can be controlled via
any hardware platform.
You can select from multiple mappings (see
:doc:`platform_settings </config/light_segment_displays>` for details).
Let us know if you need another mapping.

Hardware
--------

BCD Seven Segment
^^^^^^^^^^^^^^^^^

Segment displays are readily available at most electronics suppliers.
Most of them use some BCD encoder to save connectors.
Those are easily recognizable because they got less than 8 connectors.
You can use any driver or digital outputs on those.
Be a bit careful with current driven light controllers (i.e. the PD-LED) here.
Those cannot be dimmed currently (let us know if you need that).

Parallel Seven Segment
^^^^^^^^^^^^^^^^^^^^^^

Those are not as common as BCD segment displays but still available.
You can recognize them by more than 8 connectors.
Make sure that your display is not multiplexed or it will not work without
an additional controller chip.
Those can be driven by any parallel LED controller
(see :doc:`/mechs/lights/leds` for details).
If you use drivers you will probably need current limiting resistors.
In most cases BCD is simpler to use and will save you some outputs.

Those are also available as RGB.
However, they often are multiplexed and will not work without an additional
chip.

Serial Segment Displays
^^^^^^^^^^^^^^^^^^^^^^^

Additionally, there are serial segment displays which use chips such as WS2811
internally.
Those can also be used here using a serial LED controller
(see :doc:`/mechs/lights/leds` for details).

There is a `hackaday project for monochrome serial segment displays <https://hackaday.com/2019/01/12/addressable-7-segment-displays-may-make-multiplexing-a-thing-of-the-past/>`_.
Furthermore, there are also `full RGB serial segment displays <https://www.rgbdigit.com/rgbdigit/>`_.
Both are controlled using WS2811 controllers.

You can also buy WS2811 controller with PCB in China (bulk 100 pcs) for about
ten bucks solder your own display.

Color and Brightness
^^^^^^^^^^^^^^^^^^^^

There is no color or brightness support for segment displays in MPF yet.
Let us know if you need that.
However, you can control both using normal light shows.

Config
------

This is an example:

.. code-block:: mpf-config

   hardware:
     segment_displays: light_segment_displays

   lights:
     segment1_a:
       number: 1
     segment1_b:
       number: 2
     segment1_c:
       number: 3
     segment1_d:
       number: 4
     segment1_e:
       number: 5
     segment1_f:
       number: 6
     segment1_g:
       number: 7
     segment2_a:
       number: 8
     segment2_b:
       number: 9
     segment2_c:
       number: 10
     segment2_d:
       number: 11
     segment2_e:
       number: 12
     segment2_f:
       number: 13
     segment2_g:
       number: 14

   segment_displays:
     display1:
       number: 1
       platform_settings:
         lights:
           - a: segment1_a
             b: segment1_b
             c: segment1_c
             d: segment1_d
             e: segment1_e
             f: segment1_f
             g: segment1_g
           - a: segment2_a
             b: segment2_b
             c: segment2_c
             d: segment2_d
             e: segment2_e
             f: segment2_f
             g: segment2_g
         type: 7segment

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
