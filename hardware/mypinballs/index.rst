MyPinballs Segment Display Controller
=====================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/mypinballs`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/segment_displays`                                              |
+------------------------------------------------------------------------------+
| :doc:`/config/segment_display_player`                                        |
+------------------------------------------------------------------------------+


Connect it to your PC using USB and control up to six segment displays.

Config looks like this:

.. code-block:: mpf-config

   hardware:
     segment_displays: mypinballs
   mypinballs:
     port: /dev/ttyUSB0
   segment_displays:
     display1:
       number: 1
     display2:
       number: 2
     display3:
       number: 3
     display4:
       number: 4
     display5:
       number: 5
     display6:
       number: 6

You can configure your serial port in `port`.
See :doc:`segment_display </displays/display/alpha_numeric>` for more informations about how to drive segment display in your
game.

.. toctree::
   :titlesonly:
   :hidden:

   Wiring 3rd-Party Segment Displays <wiring>

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
