How to Drain All Balls on the Playfield and Serve One Back Without Ending the Current Ball
==========================================================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/mode`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/ball_saves`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/autofire_coils`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/event_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/show_player`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/shows`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/queue_event_player`                                            |
+------------------------------------------------------------------------------+
| :doc:`/config/queue_relay_player`                                            |
+------------------------------------------------------------------------------+

You might want to a have a mode that does not end the current ball when a timer expires, a jackpot is collected,
or some other event happens.

When this happens you might want the flippers and possibly other coils to disable (slings, pops, etc) in order to collect the ball/balls.

The first thing you need to do it make sure your flippers, sling, pops, etc have an enable and disable event in their devices config file.

This is an example for left sling:

.. code-block:: mpf-config

    #! switches:
    #!   s_left_slingshot:
    #!     number:
    #! coils:
    #!   c_left_slingshot:
    #!     number:
    autofire_coils:
      left_slingshot:
        switch: s_left_slingshot
        coil: c_left_slingshot
        disable_events: ball_ending, service_mode_entered, disable_sling
        enable_events: ball_started, enable_sling

In the mode that you want to end but not end the ball add a "fake ball save".

In this example this mode had a multiball and the fake ball save is enabled when a multiball ends.
In your mode it can be enabled whenever you want it to, mode start or when a shot is hit, etc.

.. code-block:: mpf-config

    ##! mode: your_mode
    ball_saves:
      fake_<mode_name>_ball_save:
        enable_events:
          - multiball_<multiball_name>_ended
        auto_launch: false
        balls_to_save: 1
        debug: true

When the mode ends either when timer expires or another event happens you should have 2 other modes, another ball save mode
and an end_mode mode.

In the ball save mode you will have another ball_save and maybe a show_player that flashes the shoot again light.

We will call this mode ball_save_end_mode.


.. code-block:: mpf-config

    ##! mode: your_mode
    mode:
      start_events:
        - mode_end_<mode_name>_started
      stop_events:
        - mode_end_<mode_name>_stopped
      priority: 9100

    ball_saves:
      end_mode_ball_save:
        enable_events: mode_ball_save_end_mode_started
        auto_launch: false
        balls_to_save: 1
        debug: true

    show_player:
      ball_save_end_mode_ball_save_enabled:
        fast_flash_show:
          key: end_modes_ball_save_flash
          speed: 3
          show_tokens:
            leds: l_shoot_again
            color: red
          action: play
          priority: 9999
      mode_ball_save_end_mode_stopping:
        end_modes_ball_save_flash:
          action: stop

This ball save mode is started when end_mode is started.  The end_mode is started by whatever you want the mode you don't want
ball to drain end.  For example a timer expired or some other event happened.

This is the end_mode.  It will disable the flippers and drain the balls.
You can display a message on screen or play a video, etc. explaining what just happened.
The queue_relay_player will hold the ball until the show is over.
When this mode is ending you should enable the coils you disabled.


.. code-block:: mpf-mc-config

    ##! mode: your_mode
    mode:
      start_events:
        - start_end_<mode_name>_mode
      stop_events:
        - player_continue_show_ended
      priority: 8150

    event_player:
      mode_end_<mode_name>_started:
        - flipper_off
        - disable_Upper_Left_pop_bumper
        - disable_Upper_Right_pop_bumper
        - disable_Lower_Left_pop_bumper
        - disable_Lower_Right_pop_bumper
        - disable_sling
      player_continue_show_ended:
        - flipper_on
        - enable_Upper_Left_pop_bumper
        - enable_Upper_Right_pop_bumper
        - enable_Lower_Left_pop_bumper
        - enable_Lower_Right_pop_bumper
        - enable_sling
        - start_<another_mode>

    queue_event_player:
      mode_end_<mode_name>_started:
        queue_event: my_queue_end_<mode_name>
        events_when_finished: end_end_<mode_name>

    queue_relay_player:
      my_queue_end_<mode_name>:
        post: start_end_<mode_name>_intro
        wait_for: end_show_ended
      balldevice_bd_trough_ball_eject_attempt:
        post: wait_for_instruction
        wait_for: player_continue_show_ended

    shows:
      end_<mode_name>_ball_over:
        - duration: 11
          slides:
            end_<mode_name>_ball_over_slide:
              widgets:
                - type: text
                  text: "BALL LOST"
                  color: white
                  font_size: 80
                  y: center + 300
                - type: video
                  video: end_mode_video
                - type: text
                  text: "DON'T MOVE"
                  font_size: 80
                  color: red
                  x: center
                  y: center - 300
                  animations:
                    show_slide:
                      - property: opacity
                        value: 1
                        duration: .5s
                      - property: opacity
                        value: 0
                        duration: .5s
                        repeat: true
      player_continue_show:
        - duration: 3
          slides:
            end_mode_player_continue_slide:
              widgets:
                - type: text
                  text: PLAYER (number)
                  color: blue
                  font_size: 120
                  y: center + 90
                - type: text
                  text: Keep Shooting
                  color: red
                  y: center - 10
                  font_size: 90


    show_player:
      start_end_<mode_name>_intro:
        end_<mode_name>_ball_over:
          loops: 0
          events_when_stopped: end_show_ended
      end_show_ended:
        player_continue_show:
          loops: 0
          events_when_stopped: player_continue_show_ended

This is just an example of how I did it in my game.  Every game is different.

If you have any questions about how to do this in your game please post to
`MPF Users Google Group <https://groups.google.com/forum/#!forum/mpf-users>`_.
