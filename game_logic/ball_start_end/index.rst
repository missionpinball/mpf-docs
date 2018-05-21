Ball Start and End Behaviour
============================

There are multiple ways to play show/lights/sounds during ball start or ending.

Triggering simple actions without delay on ball start
-----------------------------------------------------

During game start (see :doc:`/flowcharts/index` for details) you can trigger
shows/lights or any other player on the `ball_started` event (see
:doc:`/flowcharts/ball_start`). This will not delay the ball start and the
ball will eject instantly. This might be useful to start music, flash some
lights or start background shows:

.. code-block:: mpf-config

   ##! mode: my_mode
   # in your mode
   mode:
      start_events: ball_started

   show_player:
      mode_my_mode_started:
        short_start_show:
          loops: 0

   shows:
      short_start_show:
          - duration: .5s
   #!          events: test_start
            # add your show here
   ##! test
   #! mock_event test_start
   #! start_game
   #! advance_time_and_run 1
   #! assert_event_called test_start

This can simply be embedded in any mode (e.g. in your base mode).

Triggering simple actions without delay on ball end
---------------------------------------------------

Similarly, you can trigger events on ball end using the ``ball_ended`` event
(see :doc:`/flowcharts/ball_end` for details).
Unfortunately, normal game modes will stop on ball end and you will never see
the ``ball_ended`` event in a game mode.
This approach will not delay the ball end and the next ball might eject in the
meantime. Use it for very short sounds or light flashes:

.. code-block:: mpf-config

   ##! mode: my_mode
   # in your mode
   mode:
      start_events: ball_ending
      stop_events: end_show_done
      game_mode: False

   show_player:
      mode_my_mode_started:
        short_stop_show:
          loops: 0
          events_when_completed: end_show_done

   shows:
      short_stop_show:
          - duration: 2s
   #!          events: test_stop
            # add your show here
   ##! test
   #! mock_event test_stop
   #! start_game
   #! advance_time_and_run 1
   #! drain_ball
   #! advance_time_and_run .1
   #! assert_event_called test_stop
   #! assert_mode_running my_mode
   #! advance_time_and_run 1
   #! assert_mode_not_running my_mode

Delaying ball start and end
---------------------------

To delay start and end of a ball use the following mode.
It uses a :doc:`/config/queue_relay_player` to delay ``ball_starting`` and
``ball_ending`` for the duration of a show. This can be used to show longer
sequences and delaying the game flow in the meantime:

.. code-block:: mpf-config

   ##! mode: my_mode
   # in your mode
   mode:
       start_events: ball_will_start   # in normal mode use ball_started instead
       priority: 200

   slide_player:
       ball_starting: ball_starting_slide
       ball_ending: ball_ending_slide
       ball_started:
         main_display_slide:
           action: play
         ball_starting_slide:
           action: remove
   queue_relay_player:
      ball_starting:
          post: start_ball_starting_show
          wait_for: mode_ball_starting_show_ended
      ball_ending:
          post: start_ball_ending_show
          wait_for: mode_ball_ending_show_ended

   show_player:
       start_ball_starting_show:
           ball_starting_show:
               loops: 0
               events_when_completed: mode_ball_starting_show_ended
       start_ball_ending_show:
           ball_ending_show:
               loops: 0
               events_when_completed: mode_ball_ending_show_ended
   shows:
      ball_starting_show:
          - duration: 5s
   #!          events: test_start
      ball_ending_show:
          - duration: 5s
   #!          events: test_stop
   ##! test
   #! mock_event test_start
   #! mock_event mode_ball_starting_show_ended
   #! mock_event test_stop
   #! mock_event mode_ball_ending_show_ended
   #! start_game
   #! advance_time_and_run 1
   #! assert_event_called test_start
   #! assert_event_not_called mode_ball_starting_show_ended
   #! advance_time_and_run 5
   #! assert_event_called mode_ball_starting_show_ended
   #! drain_ball
   #! # still on ball 1
   #! advance_time_and_run 1
   #! assert_player_variable 1 ball
   #! assert_event_called test_stop
   #! assert_event_not_called mode_ball_ending_show_ended
   #! advance_time_and_run 5
   #! assert_event_called mode_ball_ending_show_ended
   #! # on ball 2
   #! assert_player_variable 2 ball

You can combine this with conditional variables to only delay the first ball.
E.g. use ``ball_starting{ball==1 and not is_extra_ball}`` to only delay the
first ball (excluding extra balls). Similarly, you can use
``ball_starting{is_extra_ball}`` to delay any extra ball start and show some
animations there.
