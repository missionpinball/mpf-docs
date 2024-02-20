---
title: "accruals:"
---

# accruals:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The structure of accrual logic blocks are like this:

``` yaml
accruals:
   the_name_of_this_logic_block:
      <settings>
   some_other_logic_block:
      <settings>
   a_third_logic_block:
      <settings>
```

Note that the actual name of the logic block doesn't really matter.
Mainly they're used in the logs.

## Required settings

The following sections are required in the `accruals:` section of your
config:

### events:

List of one (or more) events. The device will add handlers for those
events. Defaults to empty.

The events section of an accrual logic block is where you define the
events this logic block will watch for in order to make progress towards
completion.

The real power of logic blocks is that you can enter more than one event
for each step, and *only one* of the of the events of that step has to
happen for that step to be complete.

Another way to look at it is that there's an *AND* between all the
steps. For the Accrual to complete, you need Step 1 *AND* Step 2 *AND*
Step 3. But since you can enter more than one event for each step, you
could think of those like *OR*s. So you have Step 1 (event1 *OR* event2)
*AND* Step 2 (event3) *AND* Step 3 (event4 *OR* event5), like this:

``` mpf-config
accruals:
  my_accrual:
    events:
      - event1, event2
      - event3
      - event4, event5
```

It might seem kind of confusing at first, but you can build this up
bit-by-bit and figure them out as you go along.

You can enter anything you want for your events, whether it's one of
MPF's built-in events or a made-up event that another logic block posts
when it completes. (This is how you chain multiple logic blocks together
to form complex logic.)

For example:

``` mpf-config
accruals:
  logic_block_1:
    events:
      - event1
      - event2
      - event3
      - event4
      - event5
    events_when_complete: logic_block_1_done
  logic_block_2:
    events:
      - event1, event2, event3
      - event4
      - event5
    events_when_complete: logic_block_2_done
```

In the example above, there are two logic blocks. The first one just has
five steps that need to complete (in any order since we're dealing with
accrual logic blocks), and each step only has one event that will mark
is as complete. So basically any of those five events 1-5 can be posted
in any order, and then *logic_block_1_done* will be posted.

In the second example, if event 1, 2, or 3 is posted, that will count
for step 1, and then both events 4 and 5 need to be posted for steps 2
and 3. (Again, in any order.)

So in the second one, you could get event4, event2, then event5 posted,
for example, and that will lead to *logic_block_2_done* being posted.

Note that you can have two logic blocks with the same events at the same
time, and MPF will track the state of each logic block separately. So in
the above config with those two logic blocks, if the events were posted
in the order event2, event3, event4, then event5, that would complete
logic block 2. Then later if event1 was posted, that would complete
logic block 1.

## Optional settings

The following sections are optional in the `accruals:` section of your
config. (If you don't include them, the default will be used).

### advance_random_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

The advance_random_events section of an accrual logic block is where you
define the event or events that this logic block will watch for in order
to randomly complete one of the steps in the logic block. As stated
above, while there can be multiple steps that could complete this step
of the logic block, this will act as one of the events as well that will
complete the given step.

This will not update any lights that are associated with the events that
are required to complete this step. For example, if you have a shot that
could complete this step, and the step is completed by this event, the
light will still remain on even though it will not progress this logic
block any further. To update the lights you will want to add a hit_event
to the underlying shot. This should be the event from the log
logicblock_YOUR_ACCRUAL_hit {step == X} where YOUR_ACCRUAL is the name
of your accrual, and X is the value of the step to which this shot is
tied, which begins with 0.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this device in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Currently unused.

## Optional settings

The following sections are optional in the `logic_blocks_common:`
section of your config. (If you don't include them, the default will be
used).

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)).

Event(s) that will disable this logic block.

A logic block must be enabled to track hits, progress, and to post
events.

### disable_on_complete:

Single value, type: `boolean` (`true`/`false`). Default: `true`

True/False (or Yes/No) which controls whether this logic block disables
itself once it completes. This does not reset the current value.

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)).

Event(s) that will enable this logic block.

A logic block must be enabled to track hits, progress, and to post
events.

If you don't have any enable_events listed, then the logic block will
automatically be enabled when the player's ball starts.

### events_when_complete:

List of one (or more) events.

Events that will be posted when this device is completed.

### events_when_hit:

List of one (or more) events.

Events that will be posted when this device is hit or advanced.

### persist_state:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Boolean setting (yes/no or true/false) which controls whether this logic
block remembers where it was from ball-to-ball. If `False`, then this
logic block will reset itself whenever a new ball starts. If `True`,
then this logic block will be saved to the player variable
*\(logic_block_name\)_state*.

Note that logic block state is reset on mode end when this is `False`
and, as normal modes stop at the end of a ball, the state is always
maintained on a per-player basis, regardless of what this setting is
configured for.

### reset_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)).

Event(s) that will reset this logic block back to its original value.
This has no effect on the enabled/disabled state of the block.

Note that there are also `reset_on_complete:` and `persist_state:`
settings which also affect how and when the logic block is reset.

You can reset a logic block regardless of whether it's enabled.

### reset_on_complete:

Single value, type: `boolean` (`true`/`false`). Default: `true`

True/False (or Yes/No) which controls whether this logic block resets
itself once it completes. This just resets the current value or
progress. It does not change the enabled or disabled state.

Note, `disable_on_complete` default is `true`, which may seem like reset
isn't working. For something like a counter that automatically starts
again change `disable_on_complete` to `false`.

### restart_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)).

List of one (or more) events which, when posted, will restart this logic
block. A restart is a reset, then an enable, combined into a single
action.

### start_enabled:

Single value, type: `boolean` (`true`/`false`).

If `true` this device will start enabled. If `false` this device will
start disabled. If you omit this the device will start enabled unless
you specify `enable_events` in which case the device will start
disabled.

## Related How To guides

* [Accrual Logic Blocks](../game_logic/logic_blocks/accruals.md)
* [Integrating Logic_Blocks and Shows](../game_logic/logic_blocks/integrating_logic_blocks_and_shows.md)
