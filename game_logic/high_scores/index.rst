High Scores
===========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/high_score`                                                    |
+------------------------------------------------------------------------------+

MPF includes support for high scores which is where players can enter their
names (or initials) when they've achieved a high score. Features include:

+ Set any player variable as a high score option. So in addition to
  score you could set high score entries for loops, ramps, aliens
  destroyed, etc.
+ Set how many of each high score type are tracked (Top 5 for high
  scores, Top 3 for loops, Top 1 for aliens, etc.)
+ Set what each “award name” is called. (The highest score is “GRAND
  CHAMPION,” the second highest score is “HIGH SCORE 1”, the highest
  loop score is “MAJOR LOOPER”, etc.)
+ How many characters a player can enter for their name.
+ A list of valid characters the player can choose from
+ The layout of the display for entering their names and show their
  rewards.
+ Events for high score awards and entry, so you can configure
  high score entry screens.

Don't have a display to enter initials? See :doc:`high_scores_in_ems` for how
to use the high score mode without entering initials.

This is an example (for machines with display):

.. code-block:: mpf-config

   ##! mode: my_mode
   #! variable_player:
   #!   score_100:
   #!     score: 2000000
   ##! mode: high_score
   # modes/high_score/config/high_score.yaml
   mode:
     priority: 500
     start_events: game_ending, start_high_score
     use_wait_queue: true

   high_score:
     _overwrite: True
     enter_initials_timeout: 60
     award_slide_display_time: 4s

     # define your high score categories and the awards
     categories: !!omap
     - score:
         - GRAND CHAMPION
         - HIGH SCORE 1
         - HIGH SCORE 2
         - HIGH SCORE 3
         - HIGH SCORE 4
         - HIGH SCORE 5
         - HIGH SCORE 6
         - HIGH SCORE 7
         - HIGH SCORE 8
     - loops:
         - LOOP CHAMP

     # set the defaults
     defaults:
       score:
         - MPF: 1000000
         - BRI: 900000
         - JAN: 800000
         - QUI: 700000
         - MAR: 600000
         - JOH: 500000
         - ELI: 400000
         - MIK: 300000
         - ANT: 200000
       loops:
         - JAN: 42

   # optional: change the slides (you can omit all the following)
   slide_player:
     _overwrite: True
     high_score_enter_initials: high_score_enter_initials
     high_score_award_display: high_score_award_display

   slides:
     _overwrite: True
     high_score_enter_initials:
     - type: text
       style: tall_title
       font_size: 18
       text: PLAYER (player_num)
       color: ffff00
       x: 105
       y: 90

     - type: text
       style: tall_title
       font_size: 18
       text: (award)
       color: f0f0f0
       x: 105
       y: 70

     - type: text_input
       initial_char: A
       dynamic_x: false
       key: high_score
       style: tall_title
       font_size: 18
       max_chars: 3
       x: 105
       y: 20
       shift_left_event: sw_lower_left_flipper
       shift_right_event: sw_lower_right_flipper
       select_event: sw_start
       color: ff0000

     - type: text
       style: tall_title
       text: '<       >'
       font_size: 18
       x: 105
       y: 20
       color: ff0000


     - type: text
       text: ''
       key: high_score
       font_size: 18
       style: tall_title
       x: 105
       y: 50
       color: ff00ff
       animations:
         show_slide:
         - property: opacity
           value: 1
           duration: 0.3s
           easing: in_out_quint
         - property: opacity
           value: 0
           duration: 0.3s
           repeat: true
           easing: in_out_quint

     high_score_award_display:
     - type: text
       text: (player_name)
       font_size: 18
       style: tall_title
       anchor_y: middle
       anchor_x: middle
       x: middle
       y: middle
       color: 00ff00
       animations:
         show_slide:
         - property: opacity
           value: 1
           duration: 0.05s
         - property: opacity
           value: 0
           duration: 0.05s
           repeat: true
     - type: text
       text: (award)
       font_size: 18
       style: tall_title
       x: 105
       y: 110
       color: 0000ff
     - type: text
       text: (value)
       style: tall_title
       x: 105
       y: 30
       color: 4040FF
       font_size: 20
       number_grouping: true
       min_digits: 2

   ##! test
   #! assert_machine_variable 1000000 score1_value
   #! assert_machine_variable MPF score1_name
   #! assert_machine_variable "GRAND CHAMPION" score1_label
   #! assert_machine_variable 200000 score9_value
   #! assert_machine_variable ANT score9_name
   #! assert_machine_variable "HIGH SCORE 8" score9_label
   #! start_game
   #! start_mode my_mode
   #! post score_100
   #! assert_player_variable 2000000 score
   #! drain_all_balls
   #! advance_time_and_run 1
   #! assert_player_variable 2 ball
   #! drain_all_balls
   #! advance_time_and_run 1
   #! assert_player_variable 3 ball
   #! mock_event high_score_enter_initials
   #! drain_all_balls
   #! advance_time_and_run 1
   #! assert_player_variable 3 ball
   #! assert_event_called high_score_enter_initials
   #! post text_input_high_score_complete text=JAB
   #! advance_time_and_run 10
   #! assert_mode_not_running game
   #! assert_machine_variable 2000000 score1_value
   #! assert_machine_variable JAB score1_name
   #! assert_machine_variable "GRAND CHAMPION" score1_label
   #! assert_machine_variable 1000000 score2_value
   #! assert_machine_variable MPF score2_name
   #! assert_machine_variable "HIGH SCORE 1" score2_label
   #! assert_machine_variable 300000 score9_value
   #! assert_machine_variable MIK score9_name
   #! assert_machine_variable "HIGH SCORE 8" score9_label

High score mode will also create a few machine variables for you:

* :doc:`/machine_vars/high_score_categoryposition_label` - ``score1_label`` = GRAND CHAMPION
* :doc:`/machine_vars/high_score_categoryposition_name` - ``score1_name`` = MPF
* :doc:`/machine_vars/high_score_categoryposition_value` - ``score1_value`` = 1000000

In this case this will be ``score1_value``, ``score1_name`` and
``score1_label`` (till ``score9_value``, ``score9_name`` and ``score9_label``).
Additionally, there will be ``loop1_label``, ``loop1_value`` and
``loop1_name``. You can use those in your attract slides to show previous high
scores.
This is an example of an attract mode which shows high scores:

.. code-block:: mpf-config

   # in your machine wide config file
   widget_styles:
       attract_mode_high_score_display_label:
           font_size: 30
           anchor_x: right
           anchor_y: top
           x: center-10
           bold: true
       attract_mode_high_score_display_name:
           font_size: 30
           anchor_x: right
           anchor_y: top
           x: center+70
       attract_mode_high_score_display_score:
           font_size: 30
           anchor_x: left
           anchor_y: top
           x: center+90
           number_grouping: true
           min_digits: 1

   ##! show: attract
   # in your attract mode show file
   - duration: 20s
     slides:
       show_high_scores:
           widgets:
           - type: Text
             text: HIGH SCORES
             font_size: 60
             bold: true
             anchor_x: center
             anchor_y: center
             x: center
             y: top-100
           - type: Text
             text: (machine|score1_label)
             style: attract_mode_high_score_display_label
             y: top-200
           - type: Text
             text: (machine|score1_name)
             style: attract_mode_high_score_display_name
             y: top-200
           - type: Text
             text: (machine|score1_value)
             style: attract_mode_high_score_display_score
             y: top-200
           - type: Text
             text: (machine|score2_label)
             style: attract_mode_high_score_display_label
             y: top-240
           - type: Text
             text: (machine|score2_name)
             style: attract_mode_high_score_display_name
             y: top-240
           - type: Text
             text: (machine|score2_value)
             style: attract_mode_high_score_display_score
             y: top-240
           - type: Text
             text: (machine|score3_label)
             style: attract_mode_high_score_display_label
             y: top-280
           - type: Text
             text: (machine|score3_name)
             style: attract_mode_high_score_display_name
             y: top-280
           - type: Text
             text: (machine|score3_value)
             style: attract_mode_high_score_display_score
             y: top-280
           - type: Text
             text: LOOP CHAMPION
             font_size: 60
             bold: true
             anchor_x: center
             anchor_y: center
             x: center
             y: top-500
           - type: Text
             text: (machine|loops1_label)
             style: attract_mode_high_score_display_label
             y: top-600
           - type: Text
             text: (machine|loops1_name)
             style: attract_mode_high_score_display_name
             y: top-600
           - type: Text
             text: (machine|loops1_value)
             style: attract_mode_high_score_display_score
             y: top-600

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/game_logic/scoring/index`                                             |
+------------------------------------------------------------------------------+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+
| :doc:`high_scores_in_ems`                                                    |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`mode_high_score_started </events/mode_name_started>`                   |
+------------------------------------------------------------------------------+
| :doc:`mode_high_score_stopped </events/mode_name_stopped>`                   |
+------------------------------------------------------------------------------+

.. toctree::
   :hidden:

   high_scores_in_ems
