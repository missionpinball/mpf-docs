---
title: Skill Shot
---

# Skill Shot


Related Config File Sections:

* [mode:](../config/mode.md)
* [shots:](../config/shots.md)
* [shot_groups:](../config/shot_groups.md)
* [timers:](../config/timers.md)
* [state_machines:](../config/state_machines.md)

Types of skill shots:

* Time based
* Hit some target before another target
* Super skill shot
* How to create a lane-change skill shot

A simple skill shot mode:

``` mpf-config
#! switches:
#!   s_lane_l:
#!     number:
#!   s_lane_m:
#!     number:
#!   s_lane_r:
#!     number:
#! lights:
#!   l_lane_l:
#!     number:
#!   l_lane_m:
#!     number:
#!   l_lane_r:
#!     number:
##! mode: skill_shot
mode:
  start_events: ball_started
  stop_events:
    - skill_success
    - skill_failed
  priority: 500
shots:
  skill_l:
    switch: s_lane_l
    profile: skill_shot_profile
    advance_events: mode_skill_shot_started        # replace "skill_shot" with your mode name
    show_tokens:
      light: l_lane_l
  skill_m:
    switch: s_lane_m
    profile: skill_shot_profile
    show_tokens:
      light: l_lane_m
  skill_r:
    switch: s_lane_r
    profile: skill_shot_profile
    show_tokens:
      light: l_lane_r
shot_groups:
  skill_shot:
    shots: skill_l, skill_m, skill_r
    rotate_left_events: s_left_flipper_active
    rotate_right_events: s_right_flipper_active
shot_profiles:
  skill_shot_profile:
    states:
      - name: unlit
        show: off
      - name: flashing
        show: flash_color
        show_tokens:
          color: red
        speed: 4
      - name: lit
        show: on
    loop: true
variable_player:
  skill_success:
    score: 42
timers:
  skill_shot_timeout:
    start_value: 0
    end_value: 5     # set the timeout of your skill shot here
    direction: up
    tick_interval: 1s
    start_running: false
    control_events:
      - action: start
        event: balldevice_plunger_lane_ball_eject_success  # replace "plunger_lane" with the name of your plunger device
state_machines:
  skill_shot_success:
    debug: true
    states:
      start:
        label: Skill shot ready
      success:
        label: Skill successful
        events_when_started: skill_success
      failed:
        label: Skill failed
        events_when_started: skill_failed
    transitions:
      - source: start
        target: success
        events: skill_shot_flashing_hit
      - source: start
        target: failed
        events: skill_shot_unlit_hit, timer_skill_shot_timeout_complete
##! test
#! # failure
#! start_game
#! assert_mode_running skill_shot
#! hit_and_release_switch s_lane_l
#! assert_mode_not_running skill_shot
#! assert_player_variable 42 score
#! stop_game
#! # success
#! start_game
#! assert_mode_running skill_shot
#! hit_and_release_switch s_lane_m
#! assert_mode_not_running skill_shot
#! assert_player_variable 0 score
#! stop_game
#! # move + success
#! start_game
#! assert_mode_running skill_shot
#! post s_right_flipper_active
#! hit_and_release_switch s_lane_m
#! assert_mode_not_running skill_shot
#! assert_player_variable 42 score
#! stop_game
#! # test race between success and failed -> success first
#! start_game
#! mock_event skill_success
#! mock_event skill_failed
#! assert_mode_running skill_shot
#! hit_and_release_switches_simultaneously s_lane_l s_lane_m
#! assert_mode_not_running skill_shot
#! assert_event_called skill_success
#! assert_event_not_called skill_failed
#! stop_game
#! # test race between success and failed -> failed first
#! start_game
#! mock_event skill_success
#! mock_event skill_failed
#! assert_mode_running skill_shot
#! hit_and_release_switches_simultaneously s_lane_m s_lane_l
#! assert_mode_not_running skill_shot
#! assert_event_called skill_failed
#! assert_event_not_called skill_success
#! stop_game
#! # test timeout
#! start_game
#! mock_event skill_success
#! mock_event skill_failed
#! assert_mode_running skill_shot
#! advance_time_and_run 10
#! assert_mode_running skill_shot
#! post balldevice_plunger_lane_ball_eject_success
#! advance_time_and_run 10
#! assert_mode_not_running skill_shot
#! assert_event_called skill_failed
#! assert_event_not_called skill_success
#! stop_game
```

This works the following way: The three shots `skill_l`, `skill_m` and
`skill_r` represent the three lanes. `skill_l` starts lit. The group
`skill_shot` can be rotated using the flippers. When a lit shot it hit
the group posts `skill_shot_lit_hit` and `skill_shot_unlit_hit` when a
unlit shot is hit. To prevent races between the two events we use a
state_machine called `skill_shot_success` which has three states:

![image](/docs/game_logic/images/skill_shot_state_machine.png)

When the mode started it starts at `start`. Then when either
`skill_shot_lit_hit` or `skill_shot_unlit_hit` are posted in transitions
to `success` or `failed`. Those states will post either `skill_success`
or `skill_failed`. Additionally, there is a timer `skill_shot_timeout`
which will fail the skill shot 5s after the ball left the plunger.

Usually, you want to create a modes which starts on `skill_success` and
another mode which starts on `skill_failed` to play some shows.

Related How To guides:

* [How to design a game in MPF using Modes](../game_design/index.md)
