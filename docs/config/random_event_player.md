---
title: "random_event_player:"
---

# random_event_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `random_events:`
    section of a step.

The `random_event_player:` section of your config is where you can play
a random event out of a list based on an event.

``` yaml
# in your global config:
random_event_player:
  play_random_event_global:
    scope: machine
    events:
      - event1
      - event2
      - event3
##! mode: base
# in your mode:
random_event_player:
  play_random_event:
    events:
      - event1
      - event2
      - event3
  play_random_event_with_weight:
    events:
      unlikely_event1: 2
      unlikely_event2: 3
      likely_event1: 45
      likely_event2: 50
  play_random_event_with_weight_and_conditional:
    events:
      event1{mode.field.active}: 25
      event2{device.ball_devices.bd_ramp_lock.balls==2}: 25
      event3{device.accruals.base_locking_engaged.completed}: 10
      event4{device.counters.health.value>9}: 30
      event5{current_player.hearts < current_player.hearts_max}: 10
    fallback_event: event_posts_if_everything_above_false
```

## Optional settings

The following sections are optional in the `random_event_player:`
section of your config. (If you don't include them, the default will be
used).

### disable_random:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Disable random.

### events:

Unknown type. See description below.

List the events to choose from. If you use a list all events will be
equiprobable. You can also use a dict with `eventname: probablity`. See
the example above.

You can also use
[conditional events](../events/overview/conditional.md) here.

### fallback_event:

Single value, type: `string`. Defaults to empty.

If all of the events in the random_event_player are conditional and none
of them are true, this event name will be posted instead. If not
defined, no event will be posted.

### force_all:

Single value, type: `boolean` (`true`/`false`). Default: `true`

Enforce that all events are posted once before a event is posted a
second time.

### force_different:

Single value, type: `boolean` (`true`/`false`). Default: `true`

If set to true it will enforce that the same entry will never appear
twice in a row. When setting `force_all` to true this will prevent that
the last event is the same as the first of the next iteration.

### scope:

Single value, type: one of the following options: player, machine.
Default: `player`

The scope of the random selection for `force_different` and `force_all`.
When setting to `player` this is enforced per player and persisted
between balls.

## Related How To guides

* [Random event player](../config_players/random_event_player.md)
* [Mystery Awards](../cookbook/mystery_award.md)
