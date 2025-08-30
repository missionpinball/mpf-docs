---
title: Random event player
---

# Random event player


The *random event player* is a [config player](index.md)
that's used to post random events from a list of events.

This is an example:

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
```

When `play_random_event` is posted a random event is posted
out of the list `event1`, `event2` or
`event3`.

## Usage in config files

In config files, the random event player is used via the
`random_event_player:` section.

## Usage in shows

In shows, the random event player is used via the `random_events:`
section of a step.

## Related Pages:

* [random_event_player: Config Reference](../config/random_event_player.md)
* [random_event_player API Reference](../code/api_reference/config_players/random_event_player.md)
