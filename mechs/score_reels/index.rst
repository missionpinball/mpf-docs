How to Configure Score Reels
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/score_reels`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/score_reel_groups`                                             |
+------------------------------------------------------------------------------+

Multiple score reels are grouped to show the player score.
Score reels detect certain position using switches (usually 0)

:doc:`TODO: Add a picture of score reels </about/help_us_to_write_it>`


This is an example:

.. code-block:: mpf-config

   lights:
       light_p1:
           number:
           tags: player1
       light_p2:
           number:
           tags: player2
   switches:
       score_1p_10k_0:
           number:
       score_1p_1k_0:
           number:
       score_1p_100_0:
           number:
       score_1p_10_0:
           number:
       score_2p_10k_0:
           number:
       score_2p_1k_0:
           number:
       score_2p_100_0:
           number:
       score_2p_10_0:
           number:

   coils:
       player1_10k:
           number:
       player1_1k:
           number:
       player1_100:
           number:
       player1_10:
           number:
       player2_10k:
           number:
       player2_1k:
           number:
       player2_100:
           number:
       player2_10:
           number:
       chime1:
           number:
       chime2:
           number:
       chime3:
           number:

   score_reels:
       score_1p_10k:
           coil_inc: player1_10k
           switch_0: score_1p_10k_0
           limit_hi: 9
           limit_lo: 0
       score_1p_1k:
           coil_inc: player1_1k
           switch_0: score_1p_1k_0
           limit_hi: 9
           limit_lo: 0
       score_1p_100:
           coil_inc: player1_100
           switch_0: score_1p_100_0
           limit_hi: 9
           limit_lo: 0
       score_1p_10:
           coil_inc: player1_10
           switch_0: score_1p_10_0
           limit_hi: 9
           limit_lo: 0
       score_2p_10k:
           coil_inc: player2_10k
           switch_0: score_2p_10k_0
           limit_hi: 9
           limit_lo: 0
       score_2p_1k:
           coil_inc: player2_1k
           switch_0: score_2p_1k_0
           limit_hi: 9
           limit_lo: 0
       score_2p_100:
           coil_inc: player2_100
           switch_0: score_2p_100_0
           limit_hi: 9
           limit_lo: 0
       score_2p_10:
           coil_inc: player2_10
           switch_0: score_2p_10_0
           limit_hi: 9
           limit_lo: 0

   score_reel_groups:
       player1:
           reels: score_1p_10k, score_1p_1k, score_1p_100, score_1p_10, None
           tags: player1
           chimes: None, chime1, chime2, chime3, None
           lights_tag: player1
       player2:
           reels: score_2p_10k, score_2p_1k, score_2p_100, score_2p_10, None
           tags: player2
           chimes: None, chime1, chime2, chime3, None
           lights_tag: player2

Related Events
--------------

.. include:: /events/include_score_reels.rst
