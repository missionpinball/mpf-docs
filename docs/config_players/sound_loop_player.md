---
title: Sound Loop player
---

# Sound Loop player


The *sound loop player* is a [config player](index.md)
that's used to control sound loop sets (used by sound loop audio
tracks). (This player is part of the MPF media controller and only
available if you're using MPF-MC for your media controller.)

Examples:

``` yaml
sound_loop_player:
  play_basic_beat:
    loops:
      action: play
      sound_loop_set: basic_beat
      timing: loop_end
  add_hi_hats:
    loops:
      action: play_layer
      layer: 1
      timing: loop_end
  stop_hi_hats:
    loops:
      action: stop_looping_layer
      layer: 1
  add_snare:
    loops:
      action: play_layer
      fade_in: 2s
      layer: 2
      timing: now
  add_claps:
    loops:
      action: play_layer
      layer: 3
      timing: loop_end
```

Basic usage:

``` yaml
sound_loop_player:
  <triggering_event_name>:
    <sound_loop track name>:
      action: <action name>
      <optional settings>
  <triggering_event_name>:
    <sound_loop track name>:
      action: <action name>
      <optional settings>
```

## Usage in config files

In config files, the sound player is used via the `sound_loop_player:`
section. Event names that will trigger sound actions are nested
sub-headings and sound_loop_set names are either listed as nested
sub-headings below that.

## Usage in shows

In shows, the sound player is used via the `sounds_loop_sets:` section
of a step.

## Optional settings

Additional information may be found in the
[sound_loop_player](../config/sound_loop_player.md) configuration reference documentation.
