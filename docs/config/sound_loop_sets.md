---
title: sound_loop_sets:
---

# sound_loop_sets:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `sound_loop_sets:` section of your config is where you pre-define
"named" sound loop sets for playback in a sound loop audio track using
sound_loop_player section of a config file.

Sound loop sets are special groupings of existing sound assets (See the
[sounds:](sounds.md) reference page for more
details on sound assets.)

**Example 1: Simple Sound Loop Set**

If you want to define a sound loop set that is made up of only a single
sound, you can just add the sound name to the sound loop set. In the
example below, we're defining a sound loop set called *basic_beat* that
references the sound asset named *kick*. This is the simplest sound loop
set definition you can have. The volume of the *kick* sound will be
taken from the sound asset definition.

``` mpf-config
sound_loop_sets:
  basic_beat:
    sound: kick
```

**Option 2: Sound Loop Set With Multiple Layers**

When specifying multiple layers use a dash (and a space) to dictate
where a new layer starts, like this:

``` mpf-config
sound_loop_sets:
  basic_beat:
    sound: kick
    volume: 0.5
    tempo: 130.0
    layers:
      - sound: hihat
        volume: 0.7
        initial_state: stop
      - sound: snare
        volume: 0.6
        initial_state: stop
      - sound: clap
        volume: 0.45
        initial_state: stop
    events_when_played: basic_beat_played
    events_when_stopped: basic_beat_stopped
    events_when_looping: basic_beat_looped
    fade_out: 1s
  basic_beat2:
    sound: kick2
    volume: 0.5
    tempo: 130.0
    layers:
      - sound: hihat
        volume: 0.7
      - sound: snare
        volume: 0.6
      - sound: clap
        volume: 0.4
        initial_state: stop
      - sound: bass_synth
        volume: 0.5
        initial_state: play
    fade_out: 1s
```

## Required settings

The following sections are required for each named sound loop set in
your config:

### sound:

Single value, type: `string`.

The name of the sound asset that will be used as the master sound in the
sound loop set. This must refer to an existing sound asset or an error
will be thrown during initialization. The sound asset also must be
stored in memory (and not streaming). Do not include the sound file
extension here, only the sound asset name.

## Optional settings

The following sections are optional in the `sound_loop_sets:` section of
your config. (If you don't include them, the default will be used).

### volume:

Single value, type: `gain setting`
([Instructions for entering gain values](instructions/gain_values.md)) -inf, db, or float between 0.0 and 1.0. Default: Uses the
volume setting of the sound asset specified in the `sound:` setting.

The volume of the specified sound (overrides the setting in the sound
asset section). This value only controls the master sound and not any
layers defined in the sound loop set. As with all volume parameters in
MPF, this item can be represented as a number between 0.0 and 1.0 (1.0
is max volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented
as a decibel string from -inf to 0.0 db (ex: `-3.0 db`).

### events_when_played:

List of one (or more) values, each is a type: `string`. Default: `None`

A list of one or more names of events that MPF will post when this sound
loop set is played. Enter the list in the MPF config list format. These
events are posted exactly as they're entered.

### events_when_stopped:

List of one (or more) values, each is a type: `string`. Default: `None`

A list of one or more names of events that MPF will post when this sound
loop set stops playing. Enter the list in the MPF config list format.
These events are posted exactly as they're entered.

### events_when_looping:

List of one (or more) values, each is a type: `string`. Default: `None`

A list of one or more names of events that MPF will post when this sound
loop set loops back to the beginning while playing. Enter the list in
the MPF config list format. These events are posted exactly as they're
entered.

### fade_in:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade in the sound loop set when it
is played.

### fade_out:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The number of seconds over which to fade out the sound loop set when it
is stopped. This value is not applied when the sound stops on its own by
reaching the end of the sound. It only comes into play when the sound is
actively stopped by an event. A fade out sounds much more professional
than an abrupt cutoff of a sound.

### tempo:

Single value, type: `float`. Default: `60.0`

The tempo of the sound loop set, expressed in beats per minute. This
setting is used to calculate the timing of beat intervals when switching
between sound loops. This setting only needed when using the
`timing: next_beat_interval` setting in the
([sound_loop_player](sound_loop_player.md)).

## layers:

The `layers:` section controls the additional sound layers for the sound
loop set. It contains the following nested sub-settings:

### Required settings

The following sections are required in the `layers:` section of your
config:

#### sound:

Single value, type: `string`.

The name of the sound asset that will be used in the sound loop set
layer. This must refer to an existing sound asset or an error will be
thrown during initialization. The sound asset also must be stored in
memory (and not streaming). Do not include the sound file extension
here, only the sound asset name.

### Optional settings

The following sections are optional in the `layers:` section of your
config. (If you don't include them, the default will be used).

#### volume:

Single value, type: `gain setting`
([Instructions for entering gain values](instructions/gain_values.md)) -inf, db, or float between 0.0 and 1.0. Default: Uses the
volume setting of the sound asset specified in the layer `sound:`
setting.

The volume of the specified sound in the layer (overrides the setting in
the sound asset section). As with all volume parameters in MPF, this
item can be represented as a number between 0.0 and 1.0 (1.0 is max
volume, 0.0 is off, 0.9 is 90%, etc.) It also can be represented as a
decibel string from -inf to 0.0 db (ex: `-3.0 db`).

### initial_state:

Single value, type: one of the following options: play, stop. Default:
`play`

The `initial_state:` of a sound loop set layer determines the initial
play state for the layer when the sound loop set is played. Options for
`initial_state:` are:

* `play` - The layer will be played whenever the sound loop set begins
    playback.
* `stop` - The layer will be stopped whenever the sound loop set
    begins playback.
