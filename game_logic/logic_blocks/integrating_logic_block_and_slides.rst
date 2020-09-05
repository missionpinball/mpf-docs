Integrating Logic_Blocks and Slides
===================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/counters`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/slide_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/variable_player`                                               |
+------------------------------------------------------------------------------+

You might want to show the count of your counter on a slide.
Unfortunately, MC currently cannot subscribe on the value of your counter.
However, you can use variable_player to set the value of your counter to a
player variable and then use that variable in your slide.

This is an example:

.. code-block:: mpf-mc-config

   #config_version=5

   ##! mode: my_mode
   counters:
     my_counter:
       starting_count: 0
       count_complete_value: 5
       count_events: count_up

   variable_player:
     counter_my_counter_hit:
       my_counter:
         action: set
         int: (count)

   slide_player:
     show_slide:
       widgets:
         - type: text
           text: "Count (player|my_counter)"

   ##! test
   #! start_game
   #! start_mode my_mode
   #! post show_slide
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Count 0"
   #! post count_up
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Count 1"
   #! post count_up
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Count 2"
   #! post count_up
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Count 3"
   #! post count_up
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "Count 4"
