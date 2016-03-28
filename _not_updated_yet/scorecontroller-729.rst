
The *Score Controller* in the Mission Pinball Framework is responsible
for adding (or subtracting) points from a player's score based on
what's happening in the game. (Actually, the score controller can
add/subtract any values from any player variable, so you can use it to
automatically track a player's points, the number of modes completed,
extra balls, aliens vaporized, etc.) The score controller lives in the
*mpf/system/scoring.py* module. The score controller performs its
actions based on events, and you can set any player variable to change
value based on any event that's posted. See the ` *scoring:* section
of the configuration file reference`_ for details on how to set this
up.



Scoring-related events that are posted
--------------------------------------

Events from scores are automatically created via the `player variable
events functionality`_ which you can use to update your slides. If you
just want to update the value of the score on the display, you don’t
have to do anything special since the player variable change will
update on the display automatically. But if you want to do a little
+5000 animation or something, you can hook the player variable change
event which is posted like this: *player_<variable>* with parameters
*value*, *prev_value*, and *change*. For example, if the player’s
current score was 1,250,000 and then you have a scoring event with
score: 5000, then an event called *player_score* will be posted with
parameters *value:125500*, *prev_value: 1250000*, *change: 5000*.



Mode-based scoring
~~~~~~~~~~~~~~~~~~

The score controller is tightly integrated with MPF’s modes. It
automatically tracks the changes from each mode of any player variable
from your scoring section and posts events for them. For example, if
you have this section in a mode called frenzy:


::

    
    scoring:
      any_target_hit:
        score: 5000
        targets: 1


Then whenever the *any_target_hit* is posted, in addition to the
regular *player_score* and *player_target* events you would expect,
you’ll also get *mode_frenzy_score_score* and
*mode_frenzy_targets_score* events, each with *value*, *prev_value*,
and *change* parameters that have the values from that mode only. (The
formula for the event names for mode scoring is
*mode_<mode_name>_<player_var_name>_score*.) A few other notes on
scoring:


+ Scoring now MUST be done in a mode config. It is not valid to have
  scoring entries in your machine-wide config.
+ Scoring can be used for much more than just scores. Since bonus,
  high score, and scoring is all tied to player variables, you can get
  creative. Use it to track progress, jets, ramps, aliens zapped, modes
  complete, etc.
+ You can enter negative values to subtract scores or to “count down”
  scores.
+ In the future, we’ll add the ability to specify scoring multiplier
  events.
+ Scoring entries only work when a ball is in play.


.. _ section of the configuration file reference: https://missionpinball.com/docs/configuration-file-reference/scoring/
.. _player variable events functionality: https://missionpinball.com/docs/mpf-core-architecture/player-management/


