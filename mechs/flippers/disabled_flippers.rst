How to temporarily disable flippers
===================================

:doc:`/about/help_us_to_write_it`

.. code-block:: mpf-config

    switches:
        s_left_flipper:
            number: 1
            tags: left_flipper
        s_right_flipper:
            number: 2
            tags: right_flipper

    coils:
        c_flipper_left:
            number: 0
            allow_enable: true
            default_hold_power: 0.125
        c_flipper_right:
            number: 1
            allow_enable: true
            default_hold_power: 0.125

    flippers:
      flipper_left:
        main_coil: c_flipper_left
        activation_switch: s_left_flipper
        hold_coil:
        enable_events: ball_started, flipper_on
        disable_events: ball_will_end, flipper_off
      flipper_right:
        main_coil: c_flipper_right
        activation_switch: s_right_flipper
        hold_coil:
        enable_events: ball_started, flipper_on
        disable_events: ball_will_end, flipper_off

    ##! mode: flipper_mode
    mode:
      priority: 1000

    event_player:
        mode_flipper_mode_started: flippers_on
        timer_flippers_disabled_started: flippers_off
        timer_flippers_disabled_complete: flippers_on

    timers:
        flippers_button_active_left:
            control_events:
                - event: s_flipper_left_active
                  action: restart
                - event: s_flipper_left_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s
        flippers_button_active_right:
            control_events:
                - event: s_flipper_right_active
                  action: restart
                - event: s_flipper_right_inactive
                  action: stop
            start_value: 0
            end_value: 10
            direction: up
            tick_interval: 1s

        flippers_disabled:
            control_events:
                - event: timer_flippers_button_active_left_complete
                  action: start
                - event: timer_flippers_button_active_right_complete
                  action: start
                - event: timer_flippers_disabled_complete
                  action: reset
            start_value: 0
            end_value: 3
            direction: up
            tick_interval: 1s

