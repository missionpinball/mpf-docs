---
title: Match Mode
---

# Match Mode


To use the built-in MPF match mode add this config:

``` yaml
##! mode: match
# in modes/match/config/match.yaml
queue_relay_player:
  match_no_match:
    post: no_match
    wait_for: slide_no_match_slide_removed
    pass_args: true
  match_has_match:
    post: has_match
    wait_for: slide_match_slide_removed
    pass_args: true
mode_settings:
  non_match_number_step: 10
slide_player:
  no_match:
    no_match_slide:
      expire: 3s
  has_match:
    match_slide:
      expire: 3s
sound_player:
  match_no_match:
    no_match_sound:
      action: play
  match_has_match:
    match_sound:
      action: play
slides:
  match_slide:
    - type: text
      text: MATCH
    - type: text
      text: "Player 1: (match_number0)"
    - type: text
      text: "Player 2: (match_number1)"
    - type: text
      text: "Player 3: (match_number2)"
    - type: text
      text: "Player 4: (match_number3)"
    - type: text
      text: "Match number: (winner_number)"
  no_match_slide:
    - type: text
      text: NO MATCH
      font_size: 12
      anchor_y: bottom
    - type: text
      text: "Player 1: (match_number0)"
    - type: text
      text: "Player 2: (match_number1)"
    - type: text
      text: "Player 3: (match_number2)"
    - type: text
      text: "Player 4: (match_number3)"
    - type: text
      text: "Match number: (winner_number)"

##! test
#! start_game
#! advance_time_and_run 5
#! assert_mode_not_running match
#! drain_all_balls
#! advance_time_and_run 5
#! drain_all_balls
#! advance_time_and_run 5
#! drain_all_balls
#! advance_time_and_run .1
#! assert_mode_running match
#! advance_time_and_run 5
#! assert_mode_not_running match
```

You can extend the slides. See the two events below for available
parameters.

Related Events

* [match_has_match](../events/match_has_match.md)
* [match_no_match](../events/match_no_match.md)

## Related How To guides

* [How to design a game in MPF using Modes](../game_design/index.md)
