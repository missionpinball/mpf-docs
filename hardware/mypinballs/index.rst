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

Those segment displays are controlled by a very simple serial protocol.
Two variants exist:
The original MyPinball controller which can controll existing segments
and the TNA segment displays sold by PBL which includes four segments.
Both can be controlled using this platform.

Video about segment displays:

.. youtube:: Jyf3jxGXnTw

Mypinballs Segment Displays Controller
--------------------------------------

MyPinballs sells segment display controller which can be used with MPF to
control existing Bally/Stern segment displays (or replacement displays).
See the :doc:`wiring` section for details about how to wire those.
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

Total Nuclear Annihilation Remake Serial Score Display Assembly
---------------------------------------------------------------

Alternative, PBL sells TNA segment displays which use the same serial protocol.
The board is ready-made with four segment displays and a controller which can
be controlled by MPF via USB.

Part number:

 * PBL-600-0473-00

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

You can configure your serial port in `port`.
See :doc:`segment_display </displays/display/alpha_numeric>` for more informations about how to drive segment display in your
game.

See `Scotts description of the display for details <https://www.scottdanesi.com/?p=4220>`_.

.. toctree::
   :titlesonly:
   :hidden:

   Wiring 3rd-Party Segment Displays <wiring>

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
