End of Ball Bonus
=================

MPF contains a built-in end of ball bonus mode which you can use
to calculate and display a player's bonus score when they drain a ball.

The built-in bonus mode can manage bonus scoring, multipliers, awarding points
based on any player variables, and other "standard" things. You can also
extend and enhance it if you have specific requirements that aren't covered by
the built-in mode.

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`configuring_bonus`                                                     |
+------------------------------------------------------------------------------+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+

Overview of Bonus Mode
----------------------

The built-in bonus mode will automatically handle the following steps when it is
enabled:

* Pause the game when the ball ends in order to show the bonus awards
* Calculate the score for each bonus entry in the ``bonus_entries:`` list
* Post an event for each bonus entry with a delay between each event
* Skip events for bonus entries with a zero score (by default, can be overridden)
* Post an event for the subtotal of all bonuses awarded
* Post an event for a total bonus multiplier (if present)
* Post an event for the total of all bonuses awarded
* Add the total bonus award to the player's score
* Start the next ball after all bonuses have been awarded

See the :doc:`How to Configure End of Ball Bonus <configuring_bonus>` guide
for instructions on enabling bonus mode.

Calculating Points for Bonus Awards
-----------------------------------

Each award entry will calculate a bonus score based on the *score* value of the
entry. If provided, the *player_score_entry* value will be multiplied by the *score*.
This makes it very easy to award, for example, 200 points for every time the player
captured a castle (tracked by the player variable "castles_captured").

..  code-block:: mpf-config

  ##! mode: bonus
  #config_version=5
  mode_settings:
    bonus_entries:
      - event: bonus_castles
        score: 200
        player_score_entry: castles_captured

For advanced score calculation, the *score* value can utilize all of MPF's
:doc:`dynamic and placeholder variables </config/instructions/dynamic_values>`.

.. code-block:: mpf-config

  ##! mode: bonus
  #config_version=5
  mode_settings:
    bonus_entries:
      - event: bonus_minerals
        score: (current_player.platinum + current_player.iridium) / 100
      - event: bonus_dropbanks
        score: device.counters.dropbank_completions.value * 20

The calculated score is included in the posted event for displaying on a slide,
and the score is automatically added to the current player's ``score`` value.

Showing Slides for Bonus Awards
-------------------------------

Each award in the ``bonus_entries:`` setting requires an *event* value, which is
the name of the event that MPF will post when that award is calculated. You can
use these events to show slides, play sounds, and anything else. The events will
post sequentially at the interval specified by the ``display_delay_ms`` setting.

After all awards in the entries list have been posted, a final *bonus_total* event
will post with the total amount awarded as bonus. This event can be used to show
a final slide.

.. code-block:: mpf-mc-config

   #config_version=5
   #! slides:
   #!   bonus_start_slide: []
   #!   bonus_minerals_slide: []
   #!   bonus_dropbanks_slide: []
   #!   bonus_total_slide: []
   slide_player:
     mode_bonus_started: bonus_start_slide
     bonus_minerals: bonus_minerals_slide
     bonus_dropbanks: bonus_dropbanks_slide
     bonus_total: bonus_total_slide

Bonus Multipliers
-----------------

If the player has a variable called *bonus_multiplier* with a value other than 1,
MPF will add two more events between the entries and the total. First it will
post *bonus_subtotal* with an argument *score*, which is the sum of all entry
awards. Then it will post *bonus_multiplier* with an argument *multiplier*, which
is the value of the player's bonus multiplier. The resulting *bonus_total* event
value (and the amount added to the player's score) is the bonus subtotal
multiplied by the bonus multiplier.

If the player does not have a *bonus_multiplier* value or if this value is 1,
these events will not post and the bonus total will be the subtotal.

Additional Configuration
------------------------

The bonus mode can be configured with more options, including:

* Reset player variables and/or multipliers after bonuses are awarded
* Show bonus scores for entries that awarded zero points
* "Hurry up" the bonus mode based on a triggering event (e.g. *flipper_cancel*)
* After awarding all bonuses, wait for an event before ending the mode

All these options are detailed in the :doc:`/config/bonus` documentation.

Related Events
--------------

* :doc:`/events/bonus_multiplier`
* :doc:`/events/bonus_start`
* :doc:`/events/bonus_subtotal`
* Plus other events defined in your bonus mode's ``bonus_entries`` settings

.. toctree::
   :hidden:

   configuring_bonus
