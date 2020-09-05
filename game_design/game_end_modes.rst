Game End Modes
==============

After the last ball of the last player ended (and all modes which blocked ball
ending ended) the game ending sequence will run.
A few modes typically exist which delay game ending and are built-in to MPF.

If you want to implement your own game end mode use this template:

.. code-block:: mpf-config

    ##! mode: custom_high_score
    #config_version=5
    mode:
      start_events: game_ending     # start on game ending process
      use_wait_queue: true          # delay ball ending
      game_mode: false              # the game is no longer running at this point
      priority: 500                 # determines the order of game end modes
      stop_events: stop_my_mode     # post this event to stop the mode and continue the game ending process

This example will block the game ending process until you post ``stop_my_mode``
in your config or stop the mode from code.

Start Mode After Last Ball of Every Player
------------------------------------------

Alternatively, you can use :doc:`/config_players/queue_relay_player` to achieve
the same as above.
In this example we start a mode after the last ball of every player (but you can
also use ``game_ending`` as above).
Put this into your base mode to start your custom mode on the end of ball three
(or remove the condition to start if after every ball):

.. code-block:: mpf-config

    ##! mode: base
    queue_relay_player:
      ball_ending{current_player.ball==3}:
        post: start_your_mode
        wait_for: mode_your_mode_stopped

Ending the Game by Long-Pressing Start
--------------------------------------

See :doc:`game_modes/long_presssing_start_to_end_game`.

Highscore Mode
--------------

Allow players to enter their initials on high score.
See :doc:`/game_logic/high_scores/index` for details.

Match Mode
----------

Evaluates a match with the end of the player score.
Typically awards a credit on match,
See :doc:`/game_logic/match_mode/index` for details.
