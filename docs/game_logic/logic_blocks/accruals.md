---
title: Accrual Logic Blocks
---

# Accrual Logic Blocks


Related Config File Sections:

* [accruals:](../../config/accruals.md)

Related How To Guides

* [Integrating Logic Blocks and Shows](integrating_logic_blocks_and_shows.md)
* [Scoring Based on Logic Blocks](scoring_based_on_logic_blocks.md)
* [Integrating Logic_Blocks and Lights](integrating_logic_blocks_and_lights.md)
* [Integrating Logic_Blocks and Slides](integrating_logic_block_and_slides.md)
* [Persisting the State of a Logic Block in a Player Variable](persisting_state_in_a_player_variable.md)

-------------

"Accruals" are a type of
[Logic Block](index.md) where you can trigger a new event based on a series of one
or more other events.

Accruals are almost identical to
[Sequence Logic Blocks](sequences.md), the
only difference being that the steps in an Accrual Logic Block can be
completed in any order, and the steps in a Sequence Logic Block must be
completed in the specific order they're listed.

An example might be if you have 3 different things which need to happen
in your machine, and when they're all complete, some other event is
posted which kicks off some kind of award mode.

You would use an accrual if these 3 events can happen in any order. If
they need to happen in a specific 1-2-3 sequence, then you would use a
*sequence* logic block instead. (And if you just need the same event to
happen three times, then you would use a *counter* logic block instead.

For example, let's say you had a mode where you wanted three shots to
be hit, in any order, and when they were all hit, you lit another shot.
You'd use an accrual logic block like this:

``` mpf-config
##! mode: my_mode
accruals:
  name_of_my_logic_block:
    events:
      - shot1_hit
      - shot2_hit
      - shot3_hit
    events_when_complete: enable_winning_shot
```

There are much more settings (as you'll see below), but the basic logic
block above (which is called "name_of_my_logic_block") will watch for
the events *shot1_hit*, *shot2_hit*, and *shot3_hit* to be posted. Once
all three of them have been posted once, this logic block will post an
event called *enable_winning_shot* which you can use to play a show,
light some other shot, play a sound, award points, etc.

Again, since this is an accrual logic block, those three events can be
happen in any order. If one of them is posted twice, that's fine. It
doesn't count as one of the other events nor does it "undo" the fact
that it was hit.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for accruals is `device.accruals.(name)`.

*value*

:   The state of this accrual as list. There will be one entry for every
    element in the accrual. For instance, if your accrual has three
    elements if will be a list of len three with index 0 for the status
    of your first element, 1 for the seconds and 2 for the third
    element. Elements will be 0 at the beginning and turn to 1 when
    completed.

*enabled*

:   Boolean (true/false) which shows whether this accrual is enabled.

*completed*

:   True if the block is completed. Otherwise False.

This is an example:

``` mpf-config
##! mode: my_mode
accruals:
  test_accrual:
    events:
      - shot1_hit
      - shot2_hit
      - shot3_hit
    reset_on_complete: false     # this is needed for the last event player
event_player:
  test_event{device.accruals.test_accrual.value[0]}: shot1_was_hit
  test_event{device.accruals.test_accrual.value[1]}: shot2_was_hit
  test_event{device.accruals.test_accrual.value[2]}: shot3_was_hit
  test_event{device.accruals.test_accrual.completed}: accrual_completed
# Note: For this last conditional logic to be able to evaluate as true, the accrual setting
# reset_on_complete must be set to No/False. Otherwise the accrual will reset instantly and this will never be true.
##! test
#! start_game
#! start_mode my_mode
#! mock_event shot1_was_hit
#! mock_event shot2_was_hit
#! mock_event shot3_was_hit
#! mock_event accrual_completed
#! assert_bool_condition False device.accruals.test_accrual.value[0]
#! assert_bool_condition False device.accruals.test_accrual.value[1]
#! assert_bool_condition False device.accruals.test_accrual.value[2]
#! post test_event
#! assert_event_not_called shot1_was_hit
#! assert_event_not_called shot2_was_hit
#! assert_event_not_called shot3_was_hit
#! post shot1_hit
#! assert_bool_condition True device.accruals.test_accrual.value[0]
#! assert_bool_condition False device.accruals.test_accrual.value[1]
#! assert_bool_condition False device.accruals.test_accrual.value[2]
#! assert_bool_condition False device.accruals.test_accrual.completed
#! post test_event
#! assert_event_called shot1_was_hit
#! assert_event_not_called shot2_was_hit
#! assert_event_not_called shot3_was_hit
#! assert_event_not_called accrual_completed
#! post shot3_hit
#! post shot2_hit
#! post test_event
#! assert_event_called shot1_was_hit 2
#! assert_event_called shot2_was_hit
#! assert_event_called shot3_was_hit
#! assert_event_called accrual_completed
#! assert_bool_condition True device.accruals.test_accrual.value[0]
#! assert_bool_condition True device.accruals.test_accrual.value[1]
#! assert_bool_condition True device.accruals.test_accrual.value[2]
#! assert_bool_condition True device.accruals.test_accrual.completed
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
