---
title: Sequence Logic Blocks
---

# Sequence Logic Blocks


Related Config File Sections:

* [sequences:](../../config/sequences.md)

Related How To Guides

* [/events/logicblock_name_updated](integrating_logic_blocks_and_shows.md)
* [Scoring Based on Logic Blocks](scoring_based_on_logic_blocks.md)
* [Integrating Logic_Blocks and Lights](integrating_logic_blocks_and_lights.md)
* [Integrating Logic_Blocks and Slides](integrating_logic_block_and_slides.md)
* [Persisting the State of a Logic Block in a Player Variable](persisting_state_in_a_player_variable.md)-------------

"Sequences" are a type of
[Logic Block](index.md) where you can trigger a new event based on a series of one
or more other events that are first posted in a specific order.

Sequences are almost identical to
[Accrual Logic Blocks](accruals.md), the
only difference being that the steps in an Accrual Logic Block can be
completed in any order, and the steps in a Sequence Logic Block must be
completed in the specific order they're listed.

An example might be if you have to hit four shots in a specific order to
complete a mode, like this example from the World Tour mode of *Brooks
'n Dunn*:

``` mpf-config
##! mode: my_mode
sequences:
  finish_world_tour:
    events:
      - shot_north_america_hit
      - shot_south_america_hit
      - shot_europe_hit
      - shot_australia_hit
    events_when_complete: wt_done
```

The example above has a single sequence logic block called
"finish_world_tour". When it's enabled, it starts watching for the
event *shot_north_america_hit* to be posted. Once it's posted, then it
starts watching for the event *shot_south_america_hit* to be posted. At
this point, if the europe or australia event is posted, it doesn't
matter because this is a "sequence" logic block and the events have to
happen in order. So this logic block will just sit there waiting for the
current event only to be posted, and then once it is, it moves on, and
any posted before or after are just ignored.

Once all four events have been posted in order, the event *wt_done* is
posted which you can use to stop the mode or add a score or play a show
or whatever you want.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for sequences is `device.sequences.<name>`.

*value*

:   The state of this sequence as list. There will be one entry for
    every element in the sequence. For instance, if your sequence has
    three elements if will be a list of len three with index 0 for the
    status of your first element, 1 for the seconds and 2 for the third
    element. Elements will be 0 at the beginning and turn to 1 when
    completed.

*enabled*

:   Boolean (true/false) which shows whether this sequence is enabled.

*completed*

:   True if the block is completed. Otherwise False.

This is an example:

``` mpf-config
##! mode: my_mode
sequences:
  test_sequence:
    events:
      - shot1_hit
      - shot2_hit
      - shot3_hit
    reset_on_complete: false
event_player:
  test_event{device.sequences.test_sequence.value == 1}: shot1_was_hit
  test_event{device.sequences.test_sequence.value == 2}: shot2_was_hit
  test_event{device.sequences.test_sequence.value == 3}: shot3_was_hit
  test_event{device.sequences.test_sequence.completed}: sequence_completed
##! test
#! start_game
#! start_mode my_mode
#! mock_event shot1_was_hit
#! mock_event shot2_was_hit
#! mock_event shot3_was_hit
#! mock_event sequence_completed
#! assert_int_condition 0 device.sequences.test_sequence.value
#! post test_event
#! assert_event_not_called shot1_was_hit
#! assert_event_not_called shot2_was_hit
#! assert_event_not_called shot3_was_hit
#! post shot1_hit
#! assert_int_condition 1 device.sequences.test_sequence.value
#! assert_bool_condition False device.sequences.test_sequence.completed
#! post test_event
#! assert_event_called shot1_was_hit
#! assert_event_not_called shot2_was_hit
#! assert_event_not_called shot3_was_hit
#! assert_event_not_called sequence_completed
#! post shot3_hit
#! post shot2_hit
#! post test_event
#! assert_event_called shot1_was_hit
#! assert_event_called shot2_was_hit
#! assert_event_not_called shot3_was_hit
#! assert_event_not_called sequence_completed
#! assert_int_condition 2 device.sequences.test_sequence.value
#! assert_bool_condition False device.sequences.test_sequence.completed
#! post shot3_hit
#! post test_event
#! assert_event_called shot1_was_hit
#! assert_event_called shot2_was_hit
#! assert_event_called shot3_was_hit
#! assert_event_called sequence_completed
#! assert_int_condition 3 device.sequences.test_sequence.value
#! assert_bool_condition True device.sequences.test_sequence.completed
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

### When should I used logic blocks and when should I use shots/show_groups?

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
