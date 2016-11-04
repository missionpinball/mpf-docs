How to temporarily disable flippers
===================================

TODO

::

    #config_version=4

    flippers:
      flipper_left_front:
        main_coil: c_flipper_left_front
        activation_switch: s_flipper_left_front
        hold_coil:
        enable_events: ball_started, flipper_on, flippers_front_on
        disable_events: ball_will_end, flipper_off, flippers_front_off
      flipper_right_front:
        main_coil: c_flipper_right_front
        activation_switch: s_flipper_right_front
        hold_coil:
        enable_events: ball_started, flipper_on, flippers_front_on
        disable_events: ball_will_end, flipper_off, flippers_front_off
      flipper_left_back:
        main_coil: c_flipper_left_back
        activation_switch: s_flipper_left_back
        hold_coil:
        enable_events: ball_started, flipper_on, flippers_back_on
        disable_events: ball_will_end, flipper_off, flippers_back_off
      flipper_right_back:
        main_coil: c_flipper_right_back
        activation_switch: s_flipper_right_back
        hold_coil:
        enable_events: ball_started, flipper_on, flippers_back_on
        disable_events: ball_will_end, flipper_off, flippers_back_off

::

    #config_version=4

    mode:
      start_events: ball_starting, one_on_one_started
      stop_events: ball_ending, one_on_one_start
      priority: 1000

    event_player:
        mode_punishment_started: flippers_on
        timer_flippers_disabled_front_started: flippers_front_off
        timer_flippers_disabled_front_complete: flippers_front_on
        timer_flippers_disabled_back_started: flippers_back_off
        timer_flippers_disabled_back_complete: flippers_back_on

    #show_player:
    #    timer_flippers_button_active_left_front_tick{ticks==5}:
    #        flash_red:
    #            speed: 2
    #            leds: playfield_front
    #            key: front_left
    #    timer_flippers_button_active_left_front_stopped:
    #        front_left: stop

    timers:
        flippers_button_active_left_front:
            control_events:
                - event: s_flipper_left_front_active
                  action: restart
                - event: s_flipper_left_front_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s
        flippers_button_active_right_front:
            control_events:
                - event: s_flipper_right_front_active
                  action: restart
                - event: s_flipper_right_front_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s

        flippers_button_active_left_back:
            control_events:
                - event: s_flipper_left_back_active
                  action: restart
                - event: s_flipper_left_back_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s
        flippers_button_active_right_back:
            control_events:
                - event: s_flipper_right_back_active
                  action: restart
                - event: s_flipper_right_back_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s

        flippers_disabled_front:
            control_events:
                - event: timer_flippers_button_active_left_front_complete
                  action: start
                - event: timer_flippers_button_active_right_front_complete
                  action: start
                - event: timer_flippers_disabled_front_complete
                  action: reset
            start_value: 0
            end_value: 3
            direction: up
            tick_interval: 1s
        flippers_disabled_back:
            control_events:
                - event: timer_flippers_button_active_left_back_complete
                  action: start
                - event: timer_flippers_button_active_right_back_complete
                  action: start
                - event: timer_flippers_disabled_back_complete
                  action: reset
            start_value: 0
            end_value: 3
            direction: up
            tick_interval: 1s
