---
title: "sound_player: Config Reference"
---

# sound_player: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `sounds:` section of
    a step.

The `sound_player:` section of your config is where you specify actions
to perform on sounds when MPF events are received.

This is an example:

``` yaml
sound_player:
  mode_attract_started:
    song_01:
      action: play
      loops: -1
  mode_attract_stopped:
    song_01:
      action: stop
  slingshot_hit:
    zap:
      block: true  # "blocks" this event from being passed to sound player sections in lower-priority modes
```

Additional information may be found in the
[sound_player](../config_players/sound_player.md) documentation.

## Express configuration

When referencing sounds in the sound player, there is an alternative
syntax to specify a sound when you don't wish to provide any additional
settings. This shortcut notation is known as the "express
configuration" and for the sound player it is simply the name of the
sound asset. It can be used in both configuration files and show steps.
In the config file example above, `play_sound_slingshot: slingshot_01`
is an example using the express configuration (sound name only).

## Sound behavior upon mode (or show) stop

When the mode or show stops that contains a `sound_player`, all sounds
started in that mode or show will continue to play and stop
automatically when they reach their end. Sounds that are looping will
have their looping stopped so the sound will no longer continue to loop
and will stop when they reach their end. Sounds that are pending
playback and are queued will be canceled (removed from the queue) and
will not be played. If you need a sound to be stopped immediately when a
mode or show ends, you will need to add an entry in the `sound_player`
to trigger a stop action based on the mode or show stop event.

## Optional settings

The following sections are optional in the `sound_player:` section of
your config. (If you don't include them, the default will be used).

### about_to_finish_time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `-1`

--8<-- "todo.md"

### action:

Single value, type: one of the following options: play, stop,
stop_looping, load, unload. Default: `play`

The `action:` setting controls what action will be performed on the
specified sound. Options for `action:` are:

* `play` - The specified sound will be played. Any optional parameter
    values will override the sound's settings.
* `stop` - All currently playing and queued instances of the specified
    sound will stopped/canceled. Any optional parameter values will be
    ignored as the stop action takes no parameters. There is currently
    no way to stop specific instances of a particular sound while
    leaving others playing, but that is on the list to be implemented in
    a future version.
* `stop_looping` - Looping will be canceled for all currently playing
    instances of the specified sound (the sound will continue to play to
    the end of the current loop). In addition, any queued instances of
    the sound awaiting playback will be removed/canceled.
* `load` - Loads the specified sound or sound pool from its source
    file into memory to prepare it to be played. The request is ignored
    if the sound is already loaded.
* `unload` - Unloads the specified sound or sound pool from memory.
    All instances of the sound or sound pool will be immediately
    stopped. The request is ignored if the sound is not currently
    loaded.

### block:

Single value, type: `boolean` (`true`/`false`). Default: `false`

When set to `true`, the triggering event is blocked from being passed to
other sound_player sections in lower priority modes. This is useful if
you have a switch in a base mode that plays a sound (like a jet bumper),
but then in a special mode (like super jets) you want that switch to
play a different sound but you don't also want the base mode to play
the sound configured there (we don't want two simultaneous sounds for
the jet bumper, just one).

``` yaml
##! mode: mode1
sound_player:
  sw_jet_bumper_active:
    super_jet_bumper_sound:
      block: true
```

There is also a shorthand way (express config format):

``` yaml
##! mode: mode1
sound_player:
  sw_jet_bumper_active: super_jet_bumper_sound|block
```

### bus:

!!! info ""

    New in MPF 0.80

Single value, type: `string`. Defaults to empty.

Specifies an audio bus on which this sound should be played. Overrides the sound setting if one exists.

### delay:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

When the triggering event occurs, delay for a certain amount of time
before playing the sound.

### events_when_about_to_finish:

List of one (or more) events. Those will be posted by the device.
Default: `use_sound_setting`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### events_when_looping:

List of one (or more) events. Those will be posted by the device.
Default: `use_sound_setting`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### events_when_played:

List of one (or more) events. Those will be posted by the device.
Default: `use_sound_setting`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### events_when_stopped:

List of one (or more) events. Those will be posted by the device.
Default: `use_sound_setting`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### fade_in:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### fade_out:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### key:

Single value, type: `string`. Default: `use_sound_setting`

Used to reference this sound entry when stopping/pausing/resuming it.

### loops:

Single value, type: `int_or_token`. Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### max_queue_time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `-1`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### mode_end_action:

Single value, type: one of the following options: stop, stop_looping,
use_sound_setting. Default: `use_sound_setting`

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### pan:

Single value, type: `float_or_token`. Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### priority:

Single value, type: `int_or_token`. Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### start_at:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### track:

!!! warning ""

    Deprecated in MPF 0.80. Use `bus` instead.

Single value, type: `string`. Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

### volume:

Single value, type: `gain setting` (-inf, db, or float between 0.0 and
1.0). Defaults to empty.

Please refer to the [sounds:](sounds.md) documentation for details about this setting as it just
overwrites the setting in your sound.

## Related How To guides

* [Sounds, Music & Audio](../mc/sound/index.md)
