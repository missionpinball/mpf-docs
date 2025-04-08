---
title: "sound_loop_player:"
---

# sound_loop_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|
|[shows](../shows/index.md) & show files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `sound_loops:`
    section of a step.

The `sound_loop_player:` section of your config is where you specify
actions to perform on
[sound loop sets](sound_loop_sets.md) when
MPF events are received.

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

Additional information may be found in the
[sound_player](../config_players/sound_loop_player.md) documentation.

## Express configuration

The `sound_loop_player` does not support an express configuration.

## Required settings

The following sections are required in the `sound_loop_player:` section
of your config:

### track:

Single value, type: `string`.

This is the name of the track on which to perform the specified action.
This must be an existing sound loop track. (You configure tracks and
track names in the
[sound_system:](sound_system.md)
section of your machine config files.)

## Optional settings

The following sections are optional in the `sound_loop_player:` section
of your config. (If you don't include them, the default will be used).

### action:

Single value, type: one of the following options: play, stop.

The `action:` setting controls what action will be performed on the
specified sound loop set. The other settings for each action vary
(additional details may be found below). Options for `action:` are:

* `play` - The specified sound loop set will be played. Additional
    settings control whether the playback will begin immediately or
    after the currently playing loop set reaches the end of the master
    sound. Will cross-fade with the currently playing sound loop set if
    a `fade_in` setting is used.
* `stop` - The currently playing sound loop set will be stopped. Will
    fade out before stopping if a `fade_out` setting is used.
* `stop_looping` - Looping will be cancelled for the currently playing
    sound loop set (the sound loop set will continue to play to the end
    of the current loop).
* `play_layer` - Plays the sound on the specified layer in the
    currently playing loop set. Additional settings control whether the
    layer will begin immediately or will wait until after the currently
    playing loop set reaches the end of the sound. Will fade in if a
    `fade_in` setting is used.
* `stop_layer` - Stops the sound on the specified layer in the
    currently playing loop set. Will fade out before stopping if a
    `fade_out` setting is used.
* `stop_looping` - Looping will be cancelled for the sound on the
    specified layer in the currently playing sound loop set (the sound
    on the layer will continue to play to the end of the current loop).

## Settings for *play* action:

Only the `sound_loop_set:` setting is required for the *play* action.

### sound_loop_set:

Single value, type: `string`.

This is the name of the `sound_loop_set` asset used to perform the
specified action. This must be the name an existing `sound_loop_set`
specified in the `sound_loop_sets:` section of your machine config
files. This setting is required for the *play* action.

### timing:

Single value, type: one of the following options: `now`, `loop_end`,
`next_beat_interval`, `next_time_interval`. Default: `loop_end`

The `timing:` setting determines when the specified sound loop set
should be played. If the sound loop track is not currently playing any
sound, this value is ignored and the sound loop is played immediately.
Options for `timing:` are:

* `now` - Play the specified sound loop set immediately, even if
    another sound loop is currently playing. If the `fade_in:` parameter
    has a non-zero value, the sound loops will be cross-faded over the
    `fade_in:` time interval.
* `loop_end` - Play the specified sound loop set as soon as the
    currently playing sound loop reaches the end of the loop. This will
    be a gapless switch. The `fade_in:` setting is ignored when
    `loop_end` is used.
* `next_beat_interval` - Switch to the specified sound loop set on a
    beat interval of the currently playing sound loop. In order for this
    to work well the `tempo:` setting must be accurately set in all
    sound_loop_set assets. This setting works in conjunction with the
    `interval:` setting to determine the next beat interval to use when
    switching sound loops. For example, a setting of `1` indicates the
    switch can occur on any beat while a setting of `4` indicates the
    sound loops may only be switched every 4 beats (counted from the
    beginning of the currently playing sound loop set). This is useful
    to ensure sound loop sets are switched only at musically useful
    times.
* `next_time_interval` - Switch to the specified sound loop set on a
    time interval of the currently playing sound loop. This setting
    works in conjunction with the `interval:` setting to determine the
    next time interval to use when switching sound loops. For example, a
    setting of `1` indicates the switch can occur on any second boundary
    while a setting of `2.5` indicates the sound loops may only be
    switched every 2.5 seconds (counted from the beginning of the
    currently playing sound loop set).

### interval:

Single value, type: `float`. Default: `1`

Used in conjunction with the `timing: next_beat_interval` and
`timing: next_time_interval` setting values, this setting determines the
next beat or time interval to use when switching sound loop sets.

### synchronize:

Single value, type: `boolean` (Yes/No or True/False). Default: `False`

Indicates whether or not the sound loop will be synchronized in time
with the currently playing sound loop. This setting only applies when
using the `timing: now` setting value. It most useful to smoothly
cross-fade between different variations of the same sound loop.

### volume:

Single value, type: `gain setting`
([Instructions for entering gain values](instructions/gain_values.md)) -inf, db, or float between 0.0 and 1.0. Default: None (Uses
the volume setting of the sound_loop_set asset specified in the
`sound_loop_set:` setting.

The volume of the specified sound loop master sound (overrides the
setting in the sound asset section). This value only controls the master
sound and not any layers defined in the sound loop set. As with all
volume parameters in MPF, this item can be represented as a number
between 0.0 and 1.0 (1.0 is max volume, 0.0 is off, 0.9 is 90%, etc.) It
also can be represented as a decibel string from -inf to 0.0 db (ex:
`-3.0 db`).

### fade_in:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade in the sound loop set when it
is played (when cross-fading between sound loops).

### fade_out:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade out the sound loop set when it
is stopped. This value is not applied when the sound stops on its own by
reaching the end of the sound. It only comes into play when the sound is
actively stopped by an event. A fade out sounds much more professional
than an abrupt cutoff of a sound.

### start_at:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The position in the sound loop file (in seconds) to start playback of
the sound loop when it is played. When the sound loop is looped it will
loop back to the beginning of the sound file.

### events_when_played:

List of one (or more) values, each is a type: `string`. Default:
`use_sound_loop_setting`

A list of one or more names of events that MPF will post when this sound
loop set is played. Enter the list in the MPF config list format. These
events are posted exactly as they're entered. When set to
`use_sound_loop_setting`, the `events_when_played:` setting value
specified in the sound loop set will be used.

### events_when_stopped:

List of one (or more) values, each is a type: `string`. Default:
`use_sound_loop_setting`

A list of one or more names of events that MPF will post when this sound
loop set stops playing. Enter the list in the MPF config list format.
These events are posted exactly as they're entered. When set to
`use_sound_loop_setting`, the `events_when_stopped:` setting value
specified in the sound loop set will be used.

### events_when_looping:

List of one (or more) values, each is a type: `string`. Default:
`use_sound_loop_setting`

A list of one or more names of events that MPF will post when this sound
loop set loops back to the beginning while playing. Enter the list in
the MPF config list format. These events are posted exactly as they're
entered. When set to `use_sound_loop_setting`, the `looping:` setting
value specified in the sound loop set will be used.

## Settings for *stop* action:

No settings are required for the *stop* action.

### fade_out:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade out the sound loop set when it
is stopped. This value is not applied when the sound stops on its own by
reaching the end of the sound. It only comes into play when the sound is
actively stopped by an event. A fade out sounds much more professional
than an abrupt cutoff of a sound.

## Settings for *stop_looping* action:

There are no settings available for the *stop_looping* action.

## Settings for *jump_to* action:

The `time:` setting is required for the *jump_to* action.

### time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The position in the sound loop file (in seconds) to immediately jump to
during playback of the current sound loop. When the sound loop reaches
the end of the sound, it will loop back to the beginning of the sound
file.

## Settings for *play_layer* action:

The `layer:` setting is required for the *play_layer* action. This
action has no effect if there is no sound loop set currently playing on
the specified track.

### layer:

Single value, type: `integer`.

An integer value that specifies which layer number of the currently
playing sound loop set should be played. Layers are numbered beginning
with 1.

### timing:

Single value, type: one of the following options: `now`, `loop_end`.
Default: `loop_end`

The `timing:` setting determines when the specified layer should be
played. Layers are always played in synchronized time with the master
sound in the currently playing sound loop set. Options for `timing:`
are:

* `now` - Play the specified layer immediately. If the `fade_in:`
    parameter has a non-zero value, the layer will faded in over the
    `fade_in:` time interval.
* `loop_end` - Play the specified layer as soon as the currently
    playing sound loop reaches the end of the loop. If the `fade_in:`
    parameter has a non-zero value, the layer will faded in over the
    `fade_in:` time interval.

### volume:

Single value, type: `gain setting`
([Instructions for entering gain values](instructions/gain_values.md)) -inf, db, or float between 0.0 and 1.0. Default: None (uses
the volume setting of the sound asset specified in the layer `sound:`
setting.

The volume of the specified layer sound (overrides the setting in the
sound asset section). As with all volume parameters in MPF, this item
can be represented as a number between 0.0 and 1.0 (1.0 is max volume,
0.0 is off, 0.9 is 90%, etc.) It also can be represented as a decibel
string from -inf to 0.0 db (ex: `-3.0 db`).

### fade_in:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade in the sound loop set layer
when it is played.

## Settings for *stop_layer* action:

The `layer:` setting is required for the *stop_layer* action. This
action has no effect if there is no sound loop set currently playing on
the specified track or if the specified layer is not currently playing.

### layer:

Single value, type: `integer`.

An integer value that specifies which layer number of the currently
playing sound loop set should be stopped. Layers are numbered beginning
with 1.

### fade_out:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade out the sound loop set layer
when it is stopped.

## Settings for *stop_looping_layer* action:

The `layer:` setting is required for the *stop_looping_layer* action.
This action has no effect if there is no sound loop set currently
playing on the specified track or if the specified layer is not
currently playing.

### layer:

Single value, type: `integer`.

An integer value that specifies which layer number of the currently
playing sound loop set should be stopped when the sound loop set master
sound reaches the end. Layers are numbered beginning with 1.

## Related How To guides

* [Sound Loop player](../config_players/sound_loop_player.md)
