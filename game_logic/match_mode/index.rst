Match Mode
==========

To use the built-in MPF match mode add this config:

.. code-block:: mpf-config

   ##! mode: match
   # in modes/match/config/match.yaml
   queue_relay_player:
     match_no_match:
       post: no_match
       wait_for: slide_no_match_slide_removed
       pass_args: true
     match_has_match:
       post: has_match
       wait_for: slide_match_slide_removed
       pass_args: true
   mode_settings:
     non_match_number_step: 10
   slide_player:
     no_match:
       no_match_slide:
         expire: 3s
     has_match:
       match_slide:
         expire: 3s
   sound_player:
     match_no_match:
       no_match_sound:
         action: play
     match_has_match:
       match_sound:
         action: play
   slides:
     match_slide:
       - type: text
         text: MATCH
       - type: text
         text: "Player 1: (match_number0)"
       - type: text
         text: "Player 2: (match_number1)"
       - type: text
         text: "Player 3: (match_number2)"
       - type: text
         text: "Player 4: (match_number3)"
       - type: text
         text: "Match number: (winner_number)"
     no_match_slide:
       - type: text
         text: NO MATCH
         font_size: 12
         anchor_y: bottom
       - type: text
         text: "Player 1: (match_number0)"
       - type: text
         text: "Player 2: (match_number1)"
       - type: text
         text: "Player 3: (match_number2)"
       - type: text
         text: "Player 4: (match_number3)"
       - type: text
         text: "Match number: (winner_number)"

You can extend the slides. See the two events below for available paramters.

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/match_has_match`                                               |
+------------------------------------------------------------------------------+
| :doc:`/events/match_no_match`                                                |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+
