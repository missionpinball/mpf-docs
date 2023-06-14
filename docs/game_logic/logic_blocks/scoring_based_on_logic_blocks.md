---
title: Scoring Based on Logic Blocks
---

# Scoring Based on Logic Blocks


Sometimes you want to score points based on the state of a logic block.

## Accruals

This is a simple example with an accrual. Every event can increase the
multiplier exactly once. Multiplier starts at 1 and goes up to 4.

``` mpf-config
##! mode: test
mode:
  start_events: ball_started
accruals:
  my_accrual:
    events:
      - event1_to_increase_multiplier
      - event2_to_increase_multiplier
      - event3_to_increase_multiplier
    events_when_complete: go_bumper
    reset_on_complete: false
variable_player:
  some_score_event:
    score: 10000 * (device.accruals.my_accrual.value[0] + device.accruals.my_accrual.value[1] + device.accruals.my_accrual.value[2] + 1)
##! test
#! # no progress
#! start_game
#! assert_mode_running test
#! post some_score_event
#! assert_player_variable 10000 score
#! stop_game
#! # some progress
#! start_game
#! assert_mode_running test
#! post event1_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 20000 score
#! stop_game
#! # some progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event3_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 20000 score
#! stop_game
#! # more progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 30000 score
#! stop_game
#! # full progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post event1_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 40000 score
#! stop_game
```

## Counters

Similarly, you can use a counter to increase a multiplier. Every event
listed can increase the multiplier multiple times.

``` mpf-config
##! mode: test
mode:
  start_events: ball_started
counters:
  my_counter:
    count_events:
      - event1_to_increase_multiplier
      - event2_to_increase_multiplier
      - event3_to_increase_multiplier
    events_when_complete: go_bumper
    reset_on_complete: false
variable_player:
  some_score_event:
    score: 10000 * (device.counters.my_counter.value + 1)
##! test
#! # no progress
#! start_game
#! assert_mode_running test
#! post some_score_event
#! assert_player_variable 10000 score
#! stop_game
#! # some progress
#! start_game
#! assert_mode_running test
#! post event1_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 20000 score
#! stop_game
#! # some progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event3_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 30000 score
#! stop_game
#! # more progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 30000 score
#! stop_game
#! # full progress
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post event1_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 40000 score
#! stop_game
```

## Sequences

This also works with sequences.

``` mpf-config
##! mode: test
mode:
  start_events: ball_started
sequences:
  my_sequence:
    events:
      - event1_to_increase_multiplier
      - event2_to_increase_multiplier
      - event3_to_increase_multiplier
    events_when_complete: go_bumper
    reset_on_complete: false
variable_player:
  some_score_event:
    score: 10000 * (device.sequences.my_sequence.value + 1)
##! test
#! # no progress
#! start_game
#! assert_mode_running test
#! post some_score_event
#! assert_player_variable 10000 score
#! stop_game
#! # some progress
#! start_game
#! assert_mode_running test
#! post event1_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 20000 score
#! stop_game
#! # wrong shot
#! start_game
#! assert_mode_running test
#! post event3_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 10000 score
#! stop_game
#! # more progress
#! start_game
#! assert_mode_running test
#! post event1_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 30000 score
#! stop_game
#! # full progress
#! start_game
#! assert_mode_running test
#! post event1_to_increase_multiplier
#! post event2_to_increase_multiplier
#! post event3_to_increase_multiplier
#! post some_score_event
#! assert_player_variable 40000 score
#! stop_game
```

Related How To guides:

* [Scoring](../scoring/index.md)
