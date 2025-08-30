---
title: Event player
---

# Event player


The *event player* is a [config player](index.md) that's used to post events.

Video about events in MPF:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/G3UbVP8gFU0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Basic Event Playing

``` yaml
event_player:
  ball_starting:
    - cmd_flippers_enable
    - cmd_autofire_coils_enable
    - cmd_drop_targets_reset
  ball_ending:
    - cmd_flippers_disable
    - cmd_autofire_coils_disable
  tilt:
    - cmd_flippers_disable
    - cmd_autofire_coils_disable
  slam_tilt:
    - cmd_flippers_disable
    - cmd_autofire_coils_disable
```

The event player settings above will post the events
*cmd_flippers_enable*, *cmd_autofire_coils_enable*, and
*cmd_drop_targets_reset* when the *ball_starting* event is posted.
Similarly they will post events to disable the flippers and autofire
coils when ball end and tilt events are posted.

To use this, simply create an `event_player:` entry in your config file.
Then create sub-entries for each event you want to trigger other events,
and add a list of one or more events that should be posted automatically
under each trigger event.

Remember that you can create this event_player: section in either your
machine-wide or in mode-specific config files. For example, if you want
a target called "upper" to reset when a mode called "shoot_here"
starts, you could create an entry like this in the shoot here mode's
shoot_here.yaml mode configuration file:

``` yaml
##! mode: shoot_here
event_player:
  mode_shoot_here_started: cmd_upper_target_reset
```

## Conditional Event Playing

Events in the event player can be conditional, to allow precise control
over when an event is played:

``` yaml
##! mode: base
event_player:
  mode_base_started{current_player.score>10000}:
    - start_mode_superbonusround
    - play_show_richy_rich
  start_mode_battle{device.achievements.ironthrone.state!="completed"}: start_mode_choose_battle
  start_mode_battle{device.achievements.ironthrone.state=="completed"}: start_mode_victory_lap
```

In the above example, both "start_mode_superbonusround" and
"play_show_richy_rich" will only be posted if the player's score is
over 10,000 when base mode starts. And if the battle mode is started,
either "start_mode_choose_battle" or "start_mode_victory_lap" will
be posted depending on whether the *ironthrone* achievement has been
completed.

Conditions can also be applied to events within a list, to allow one
event to trigger a variable number of handlers:

``` yaml
##! mode: base
event_player:
  reenable_nonrecruit_modes:
    - start_mode_shadowbroker_base
    - start_mode_n7_assignments
    - start_mode_overlordlight{device.achievements.collectorship.state!="complete"}
    - start_mode_arrival{device.achievements.collectorship.state=="complete"}
    - start_mode_shopping{current_player.cash>=1000}
```

In the above example, both "start_mode_shadowbroker_base" and
"start_mode_n7_assignments" will be posted every time. One of either
"start_mode_overlord" or "start_mode_arrival" will be posted,
depending on whether the player has completed the collectorship
achievement. And if the player_var "cash" is high enough,
"start_mode_shopping" will also be posted.

In many cases, conditions can be applied to either the triggering event
or the handling event. For more information and examples of conditions,
see
[conditional events](../events/overview/conditional.md).

## Dynamic Values in Events

There are numerous ways to include dynamic values (player variables,
device states, mathematical calculations) in events.

### Dynamic Event Names

An event name can use parenthetical values to dynamically determine the
event.

``` yaml
event_player:
  mode_dynamo_started:
    # Player variables can be dropped into event names
    - play_dynamo_show_phase_(current_player.phase_name)
    # Machine and device states can be used
    - dynamo_started_with_state_(device.achievements.dynamo.state)
    # Dynamic evaluations can be done to calculate values
    - player_score_is_("high" if current_player.score > 10000 else "low")
```

In the above example:

* With the player variable `phase_name` having a value of
    "attackwave", starting the mode would post the event
    *play_dynamo_show_phase_attackwave*
* If the "dynamo" achievement was completed, starting the mode would
    post *dynamo_started_with_state_completed*. If the achievement was
    instead disabled, the event would be
    *dynamo_started_with_state_disabled*
* If the player's score is over 10,000 the event
    *player_score_is_high* will be posted, otherwise the event
    *player_score_is_low* will be posted.

Any
[dynamic values](../config/instructions/dynamic_values.md) can be used. Because event names are always strings, all
dynamic values will be converted to their string equivalent.

### Dynamic Event Arguments

An event post can include arguments to provide event handlers with
additional information about the event. An event configured as an object
will post the object properties as its arguments:

``` yaml
event_player:
  mode_carchase_started:
    # Objects can be expanded for a key/value pair per line
    set_environment_sounds:
      env_name: driving
    # Objects can be inline for brevity
    set_initial_laps_count: {count: 10}
```

You can go a step further and include dynamic values as the values for
event arguments. To indicate that an argument's value is dynamic, use
the `value:` property.

``` yaml
event_player:
  mode_dynamo_started:
    set_dynamo_phase:
      phase_name: {value: current_player.dynamo_phase}
```

In the above example, if the player variable `dynamo_phase` had the
value "attackwave", the event would be posted as such:

``` none
Event: ======'set_dynamo_phase'====== Args={'phase_name': 'attackwave', priority': 0}
```

Because dynamic values can come from a variety of sources, you will need
to explicitly define types for the value's format. Acceptable types are
**int**, **float**, **bool**, and **string**. If no type is configured,
the value will be posted as a string.

``` yaml
event_player:
  mode_dynamo_started:
    # This event arg will be correctly typed
    set_dynamo_round_with_type:
      round_number:
        value: device.counters.dynamo_rounds.value
        type: int
    # This event arg will be converted to a string
    set_dynamo_round_without_type:
      round_number:
        value: device.counters.dynamo_rounds.value
```

### Priority:

Note that as with other config players, event player can accept
priorties for events to be posted. This can be useful in scenarios such
as where a player variable must be updated prior to a conditional check,
so that they happen in the desired order.

``` yaml
event_player:
  mode_dynamo_started:
    reset_pv_tokens_collected_to_0:
      priority: 50
    play_slide{current_player.pv_tokens_collected <= 5}:
      priority: 5
      slide: dynamo_collect_more_tokens_slide
```

## Usage in config files

In config files, the event player is used via the `event_player:` section.

## Usage in shows

In shows, the event player is used via the `events:` section of a step.

## Related Pages:

* [event_player: Config Reference](../config/event_player.md)
* [event_player API Reference](../code/api_reference/config_players/event_player.md)
