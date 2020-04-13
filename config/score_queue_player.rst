score_queue_player:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``score_queue_player:`` section of your config is where you configure your
SS style scoring.
This is an example:

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
       debug: true
   ##! mode: my_mode
   # in your mode
   score_queue_player:
     score_2k:
       score: 2000
     score_200:
       score: 200

.. config


Optional settings
-----------------

The following sections are optional in the ``score_queue_player:`` section of your config. (If you don't include them, the default will be used).

int:
~~~~
Single value, type: ``integer`` or ``template`` (:doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Defaults to empty.

Score value to add to the queue.


Related How To guides
---------------------

* :doc:`/game_logic/scoring/ss_style_score_queues`
