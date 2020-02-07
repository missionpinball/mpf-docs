Alpha-Numeric / Segment Displays
================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/segment_displays`                                              |
+------------------------------------------------------------------------------+
| :doc:`/config/segment_display_player`                                        |
+------------------------------------------------------------------------------+

MPF supports segment displays and alpha numeric displays.
There are several hardware options available:
:doc:`/hardware/segment_display_platforms`.

1. Configure your segment displays in MPF config
------------------------------------------------

You can use the following tested config snippet as a starting point to
implement segment displays (make sure to use the correct numbers for your
hardware).

.. literalinclude:: /mpf_examples/segment_display/config/game.yaml
   :caption: your_machine_folder/config/display.yaml
   :language: yaml

2. Implement virtual segment displays
-------------------------------------

If you don't have or want phyiscal segment displays you can also emulate them
using the following slides:

.. code-block:: mpf-mc-config

   slides:
     segment_displays:
       widgets:
         - type: text
           text: (player1|score)
           number_grouping: true
           min_digits: 2
           font_name: ten_segment
           color: blue
           x: 620
           y: 724
           font_size: 240
           anchor_x: right
           anchor_y: bottom
           z: 2
   # show slide on game start
   slide_player:
     game_started: segment_displays
   ##! test
   #! start_game
   #! advance_time_and_run .1
   #! assert_slide_on_top segment_displays
