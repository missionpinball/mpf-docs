---
title: counters:
---

# counters:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `counters:` section of your config is where you configure counter
logic blocks. See also
[counters](../game_logic/logic_blocks/counters.md). The structure of counter logic blocks is like this:

``` mpf-config
##! mode: mode1
counters:
  the_name_of_this_counter:
    count_events: my_count_event
    count_complete_value: 10
  some_other_counter:
    count_events: s_my_switch_active
    starting_count: 50
    count_interval: 10
    count_complete_value: 100
```

Note that the actual name of the counter doesn't really matter. Mainly
it's used in the logs and for event names.

Counters no longer save their state in player variables. If you are
using something like `(YOUR_COUNTER_count)` in a slide or widget you can
use a
[variable_player](../config_players/variable_player.md) to restore the old behavior:

``` mpf-config
##! mode: my_mode
variable_player:
  logicblock_YOUR_COUNTER_updated:
    YOUR_COUNTER_count:
      int: value
      action: set
```

## Required settings

The following sections are required in the `counters:` section of your
config:

### count_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

This is an event (or a
[list of events](instructions/lists.md)) that, when posted, will increment or decrement the count
for this Counter.

Note that if you include multiple events in this list, *any* one of the
events being posted will cause the hit count to increase. If you want to
track different kinds of events separately, use an
[Accrual](accruals.md) or
[Sequence](sequences.md) Logic Block
instead.

This setting is required.

## Optional settings

The following sections are optional in the `counters:` section of your
config. (If you don't include them, the default will be used).

### control_events:

List of one (or more) values, each is a type:
[counter_control_events:](counter_control_events.md). Defaults to empty.

Control events to change the value of this counter. MPF currently
supports adding/substracting from the count or jumping to a certain
value.

For instance in the following example `add_five_event` will add `5` to
the counter:

``` mpf-config
counters:
  counter_with_control_events:
    count_events: count_up
    control_events:
      - event: add_five_event
        action: add
        value: 5
```

### count_complete_value:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)). Defaults to empty.

When the Counter exceeds (or gets below if you're counting down) this
value, it will post its "complete" event and be considered complete.

### count_interval:

Single value, type: `integer`. Default: `1`

Specifies the numeric count change is for each hit. In other words, this
is how much is added or removed from the count with each hit. Default is
1, but you can make it whatever you want if you want your count to
increase by more or less than one whenever a count event occurs. You
could use this, for example, in a mode to create a counter that tracks
the value of a shot. Maybe it starts at 2,000,000, but each shot a
playfield standup increases the value by 250,000.

Default is `1`.

### direction:

Single value, type: one of the following options: up, down. Default:
`up`

This is either `up` or `down` and specifies whether this counter counts
up or counts down.

Default is `up`.

### multiple_hit_window:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

This is an
[MPF time value string](instructions/time_strings.md) that will be used to group together multiple *count_events*
as if they were one single event. So if you have
`multiple_hit_window: 500ms` and you get three hit events 100ms apart,
they will all count as one hit.

Note that subsequent hits that come in during the time window do not
extend the time. So with the 500ms hit_window from above, the first hit
counts and sets the timer, another hit 300ms later won't count, but a
third hit 300ms after the second (and 600ms after the initial hit) will
count (and it will set its own 500ms timer to ignore future hits).

Default is `0` (which means all hits are counted).

### starting_count:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)). Default: `0`

This is the starting value of the Counter and the value it goes back to
when it's reset. Default is zero. If you're configuring a counter with
`direction: down`, you'll want to also set this to something more than
zero.

Default is `0`.

Note that you can use a
[dynamic value](instructions/dynamic_values.md) for this setting.

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
*<logic_block_name>_state*.

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

* [Counter Logic Blocks](../game_logic/logic_blocks/counters.md)
* [Integrating Logic_Blocks and Shows](../game_logic/logic_blocks/integrating_logic_blocks_and_shows.md)
