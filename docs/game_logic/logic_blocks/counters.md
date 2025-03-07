---
title: Counter Logic Blocks
---

# Counter Logic Blocks


Related Config File Sections:

* [counters:](../../config/counters.md)

Related How To Guides

* [Integrating Logic Blocks and Shows](integrating_logic_blocks_and_shows.md)
* [Scoring Based on Logic Blocks](scoring_based_on_logic_blocks.md)
* [Integrating Logic_Blocks and Lights](integrating_logic_blocks_and_lights.md)
* [Integrating Logic_Blocks and Slides](integrating_logic_block_and_slides.md)
* [Persisting the State of a Logic Block in a Player Variable](persisting_state_in_a_player_variable.md)

-------------

"Counters" are
[logic blocks](index.md) that track the number of times a certain event happens
towards the progress of a completion goal.

Examples include:

* Hit a target (or shot) X number of times to advance.
* Hit pop bumpers 75 times to start a Super Jets mode.
* Counting the number of combos made
* Keeping track of a bonus multiplier (maybe you use the shot group
    lane completion event to count progress towards the bonus
    multiplier, but you configure the max count to be 6, and then if
    it's hit again, you award an extra ball).

You can use optional parameters to specify whether multiple occurrences
in a very short time window should be grouped together and counted as
one hit, the counting interval, and whether this counter counts up or
down.

Here's an example of a counter you could use to track progress towards
super jets:

``` mpf-config
##! mode: my_mode
counters:
  super_jets:
    count_events: sw_pop
    events_when_hit: pop_hit
    starting_count: 75
    count_complete_value: 0
    direction: down
    events_when_complete: super_jets_start
```

And here's the logic block we use for the
[Addams Family mansion awards](../../cookbook/TAF_mansion_awards.md) to make sure the mansions is initialized only once per game:

``` mpf-config
##! mode: my_mode
counters:
  initialize_mansion:
    count_events: mode_chair_lit_started
    events_when_complete: initialize_mansion
    count_complete_value: 1
    persist_state: true
```

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for counters is `device.counters.(name)`.

*value*

:   The count of this counter.

*enabled*

:   Boolean (true/false) which shows whether this counter is enabled.

*completed*

:   True if the block is completed. Otherwise False.

This is an example:

``` mpf-config
##! mode: my_mode
counters:
  test_counter:
    count_events: count_up
    reset_on_complete: false
    count_complete_value: 3
event_player:
  test_event{device.counters.test_counter.value > 1}: count_above_one
  test_event{device.counters.test_counter.completed}: count_completed
##! test
#! start_game
#! start_mode my_mode
#! mock_event count_above_one
#! mock_event count_completed
#! post test_event
#! assert_event_not_called count_above_one
#! post count_up
#! assert_int_condition 1 device.counters.test_counter.value
#! post test_event
#! assert_event_not_called count_above_one
#! post count_up
#! assert_int_condition 2 device.counters.test_counter.value
#! assert_bool_condition False device.counters.test_counter.completed
#! post test_event
#! assert_event_called count_above_one
#! assert_event_not_called count_completed
#! post count_up
#! assert_int_condition 3 device.counters.test_counter.value
#! assert_bool_condition True device.counters.test_counter.completed
#! post test_event
#! assert_event_called count_completed
```

## Related Events

* [logicblock_(name)_complete](../../events/logicblock_name_complete.md)
* [logicblock_(name)_hit](../../events/logicblock_name_hit.md)
* [logicblock_(name)_updated](../../events/logicblock_name_updated.md)

## Common Issues

We try to answer some common questions regarding logic blocks here. If
you question is not answered please ask in the forum.

### My block only works once. Why?

This is the default configuration of all logic blocks. To change it you
first need to set `reset_on_complete` to `True`. As a result you blocks
will reset when they reach the final step. However, that will not be
enough in most cases because `disable_on_complete` is `True` by default.
Unless you have some enable logic to re-enable the block later, you
probably want to set `disable_on_complete` to `False`.

### When should I used logic blocks and when should I use shots/shot_groups?

There is no definitive answer to this question. Generally, it depends on
your usecase. Shots and shot_groups serve a very specific usecase.
Basically, they implement a sequences of switch hits which trigger
lights along the way. If you want to stay within that specific usecase
then go with shots because it will be more convenient. If you plan to
extend your mode to use more advanced features then go with logic
blocks. For instance if you got conditions in your logic (i.e. on how
many balls are locked). Another clear indicator for logic blocks would
be if your logic is triggered by other elements such as locks (and not
just switches).
