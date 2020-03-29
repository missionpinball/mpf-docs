Extra Balls
===========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/extra_balls`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/extra_ball_groups`                                             |
+------------------------------------------------------------------------------+

MPF has support for extra balls. Extra balls in MPF are "named", and they're
tracked so that (by default) each extra ball can only be awarded once. You can
configure as many different extra balls as you want, each with different
settings that tie into the events that award them.
Every extra ball device can award up to x extra balls (defaults to 1).
Additionally, you can define extra ball groups which can further limit the
maximum number of extra balls.

Score an Extra Ball Based on Score
----------------------------------

Some games (especially EMs) award extra balls based on the score.
This is an example:

.. code-block:: mpf-config

   ##! mode: base
   # in your base mode
   extra_balls:
     score_one:
       enabled: true
       award_events: player_score{value>=140000}
     score_two:
       enabled: true
       award_events: player_score{value>=210000}
     score_three:
       enabled: true
       award_events: player_score{value>=300000}
   #! variable_player:
   #!   score_100000:
   #!     score: 100000
   ##! test
   #! # start game and score
   #! start_game
   #! start_mode base
   #! post score_100000
   #! assert_player_variable 100000 score
   #! assert_player_variable 0 extra_balls
   #! post score_100000
   #! assert_player_variable 200000 score
   #! assert_player_variable 1 extra_balls
   #! post score_100000
   #! assert_player_variable 300000 score
   #! assert_player_variable 3 extra_balls
   #! post score_100000
   #! assert_player_variable 400000 score
   #! assert_player_variable 3 extra_balls

Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`

Related Events
--------------

.. include:: /events/include_extra_balls.rst
.. include:: /events/include_extra_ball_groups.rst
