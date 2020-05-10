How to configure DMDs (Stern SPIKE)
===================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/spike`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/dmds`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/displays`                                                      |
+------------------------------------------------------------------------------+

Stern Spike 1 machines support a monochrome DMD.
MPF can drive the DMD over serial but you have to make sure that your serial
is fast enough to provide sufficient throughput (at least 1.5Mbaud).
This can be configured using ``runtime_baud`` (as described in :doc:`config`):

.. code-block:: mpf-config

   hardware:
     platform: spike
   spike:
     port: /dev/ttyUSB0
     baud: 115200
     runtime_baud: 2000000       # play with this setting
     nodes: 0, 1, 8, 9, 10, 11

Then configure your dmd like in this example:

.. code-block:: mpf-mc-config

   displays:
     window:  # on screen window
       width: 600
       height: 200
     dmd:  # source display for the DMD
       width: 128
       height: 32
       default: true
   dmds:
     my_dmd:
       platform: spike
       fps: 30
   # some default slides (you don't need those but they are a nice start)
   slides:
     window_slide_1:  # slide we'll show in the on-screen window
       - type: display
         width: 512
         height: 128
         effects:
           - type: dmd
     dmd_slide_1:  # slide we'll show on the physical DMD
       - type: text
         text: MPF
         font_size: 30
         color: red
         x: 0
         animations:
           add_to_slide:
             - property: x
               value: 250
               duration: 30
               relative: true
   slide_player:
     init_done:
       window_slide_1:
         target: window
       dmd_slide_1:
         target: dmd
   ##! test
   #! assert_text_on_top_slide MPF dmd
   #! assert_text_on_top_slide MPF window

Note that the :doc:`/displays/display/dmd` guide has more details
on the window and slide settings used in this machine config.

What if it did not work?
------------------------

Have a look at our :doc:`SPIKE troubleshooting guide <troubleshooting>`.
