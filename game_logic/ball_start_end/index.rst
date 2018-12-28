Ball Start and End Behaviour
============================

There are multiple ways to play show/lights/sounds during ball start or ending.

Triggering actions without delay on ball start
----------------------------------------------

During game start (see :doc:`/flowcharts/index` for details) you can trigger
shows/lights or any other player on the `ball_started` event (see
:doc:`/flowcharts/ball_start`). This will not delay the ball start and the
ball will eject instantly.

Shows/Lights
~~~~~~~~~~~~

This might be useful to start music, flash some
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

Ball Save
~~~~~~~~~

It is also very common to start a ball save on eject:

.. code-block:: mpf-config

   playfields:
     playfield:
       default_source_device: bd_plunger
   
   lights:
     l_ball_save:
       number:
   
   switches:
     s_plunger:
       number:
   
   coils:
     c_eject:
       number:
   
   ball_devices:
     bd_plunger:
       eject_coil: c_eject
       ball_switches: s_plunger
       tags: home, trough, drain
       eject_timeouts: 1s
   
   ##! mode: my_mode
   # in your mode
   mode:
      start_events: ball_started
   
   ball_saves:
     ball_save_ball_save:
       active_time: 10s
       hurry_up_time: 3s
       timer_start_events: balldevice_bd_plunger_ejecting_ball
       auto_launch: yes
       balls_to_save: 1
   
   show_player:
      ball_save_ball_save_ball_save_timer_start:
        flash_color:
          key: ball_save
          speed: 2
          show_tokens:
            lights: l_ball_save
            color: orange
      ball_save_ball_save_ball_save_hurry_up:
        flash_color:
          key: ball_save
          speed: 4
          show_tokens:
            lights: l_ball_save
            color: orange
      ball_save_ball_save_ball_save_disabled:
        ball_save: stop
   
   ##! test
   #! hit_switch s_plunger
   #! advance_time_and_run 1
   #! mock_event ball_save_ball_save_ball_save_saving_ball
   #! hit_and_release_switch s_start
   #! advance_time_and_run 2
   #! assert_event_not_called ball_save_ball_save_ball_save_saving_ball
   #! hit_switch s_plunger
   #! advance_time_and_run 1
   #! assert_player_variable 1 ball
   #! assert_event_called ball_save_ball_save_ball_save_saving_ball
   #! advance_time_and_run 5
   #! hit_switch s_plunger
   #! advance_time_and_run 1
   #! assert_player_variable 2 ball
   #! assert_light_flashing l_ball_save orange
   #! advance_time_and_run 7
   #! assert_light_flashing l_ball_save orange .5
   #! advance_time_and_run 5
   #! assert_light_color l_ball_save off
   #! hit_switch s_plunger
   #! advance_time_and_run 1
   #! assert_player_variable 3 ball

The mode will start on ``ball_started``. It will enable a
:doc:`ball save </config/ball_saves>` on mode start and start a timer once the
plunger ejects the ball. This will also work with mechanical eject.
Once the timer is active the shoot again led ``l_ball_save`` will flash.
During the hurry up (last 2s) it will flash faster and turn off afterwards.

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
   #! drain_all_balls
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
       flipper_cancel:
           ball_starting_show: stop
           ball_ending_show: stop
       start_ball_starting_show:
           ball_starting_show:
               loops: 0
               events_when_stopped: mode_ball_starting_show_ended
       start_ball_ending_show:
           ball_ending_show:
               loops: 0
               events_when_stopped: mode_ball_ending_show_ended
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
   #! drain_all_balls
   #! # still on ball 1
   #! mock_event test_start
   #! mock_event mode_ball_starting_show_ended
   #! advance_time_and_run 1
   #! assert_player_variable 1 ball
   #! assert_event_called test_stop
   #! assert_event_not_called mode_ball_ending_show_ended
   #! advance_time_and_run 5
   #! assert_event_called mode_ball_ending_show_ended
   #! # on ball 2
   #! mock_event test_stop
   #! mock_event mode_ball_ending_show_ended
   #! assert_player_variable 2 ball
   #! assert_event_called test_start
   #! assert_event_not_called mode_ball_starting_show_ended
   #! post flipper_cancel
   #! advance_time_and_run 1
   #! assert_event_called mode_ball_starting_show_ended

Both shows can be canceled using both flippers which will post the
``flipper_cancel`` event. Remove that :doc:`show_player </config/show_player>`
entry if you don't want that. See the :doc:`flipper mech </mechs/flippers/index>` documentation for details about the ``flipper_cancel`` event.

You can combine this with conditional variables to only delay the first ball.
E.g. use ``ball_starting{ball==1 and not is_extra_ball}`` to only delay the
first ball (excluding extra balls). Similarly, you can use
``ball_starting{is_extra_ball}`` to delay any extra ball start and show some
animations there.
