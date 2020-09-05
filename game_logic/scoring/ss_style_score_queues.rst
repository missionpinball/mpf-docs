How to implement solid state game style score queues in MPF
===========================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/score_queues`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/score_queue_player`                                            |
+------------------------------------------------------------------------------+


When scoring in solid state games the game will typically play chimes
while adding the player score and wait after each digit.
You can use :doc:`/config/score_queues` and :doc:`/config/score_queue_player`
to implement this in MPF.

.. code-block:: mpf-config

   coils:
     c_chime_1000:
       number:
     c_chime_100:
       number:
     c_chime_10:
       number:
   score_queues:
     score:
       chimes: c_chime_1000, c_chime_100, c_chime_10,  None
   ##! mode: my_mode
   # in your mode
   score_queue_player:
     score_2k:
       score: 2000
     score_200:
       score: 200
   ##! test
   #! start_game
   #! assert_player_variable 0 score
   #! start_mode my_mode
   #! post score_2k
   #! post score_200
   #! advance_time_and_run .1
   #! assert_player_variable 1000 score
   #! advance_time_and_run .2
   #! assert_player_variable 2000 score
   #! advance_time_and_run .2
   #! assert_player_variable 2100 score
   #! advance_time_and_run .2
   #! assert_player_variable 2200 score

