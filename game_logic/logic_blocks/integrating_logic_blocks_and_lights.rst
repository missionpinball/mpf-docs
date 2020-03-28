Integrating Logic_Blocks and Lights
===================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/counters`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+

You might want to enable lights based on the state of a counter.
This is an example for integrating lights via light_player using subscriptions
on the value of the counter:

.. code-block:: mpf-config

   lights:
     l_chest_matrix_green_2:
       number:
     l_chest_matrix_green_3:
       number:
     l_chest_matrix_green_4:
       number:
     l_chest_matrix_green_5:
       number:

   counters:
     my_counter:
       starting_count: 0
       count_complete_value: 5
       count_events: count_up

   light_player:
     "{device.counters.my_counter.value > 0}":
       l_chest_matrix_green_5: green
     "{device.counters.my_counter.value > 1}":
       l_chest_matrix_green_4: green
     "{device.counters.my_counter.value > 2}":
       l_chest_matrix_green_3: green
     "{device.counters.my_counter.value > 3}":
       l_chest_matrix_green_2: green

   ##! test
   #! start_game
   #! assert_light_color l_chest_matrix_green_2 black
   #! assert_light_color l_chest_matrix_green_3 black
   #! assert_light_color l_chest_matrix_green_4 black
   #! assert_light_color l_chest_matrix_green_5 black
   #! post count_up
   #! advance_time_and_run .1
   #! assert_light_color l_chest_matrix_green_2 black
   #! assert_light_color l_chest_matrix_green_3 black
   #! assert_light_color l_chest_matrix_green_4 black
   #! assert_light_color l_chest_matrix_green_5 green
   #! post count_up
   #! advance_time_and_run .1
   #! assert_light_color l_chest_matrix_green_2 black
   #! assert_light_color l_chest_matrix_green_3 black
   #! assert_light_color l_chest_matrix_green_4 green
   #! assert_light_color l_chest_matrix_green_5 green
   #! post count_up
   #! advance_time_and_run .1
   #! assert_light_color l_chest_matrix_green_2 black
   #! assert_light_color l_chest_matrix_green_3 green
   #! assert_light_color l_chest_matrix_green_4 green
   #! assert_light_color l_chest_matrix_green_5 green
   #! post count_up
   #! advance_time_and_run .1
   #! assert_light_color l_chest_matrix_green_2 green
   #! assert_light_color l_chest_matrix_green_3 green
   #! assert_light_color l_chest_matrix_green_4 green
   #! assert_light_color l_chest_matrix_green_5 green
