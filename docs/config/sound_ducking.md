---
title: "sound_ducking:"
---

# sound_ducking:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `ducking:` setting in your `sounds:` section of your config is where
you configure ducking settings for a sound.

## Required settings

The following sections are required in the `sound_ducking:` section of
your config:

### target:

List of one (or more) events.

The list of track names to apply the ducking to when the sound is
played. This most commonly contains the name of the track that music is
played on.

## Optional settings

The following sections are optional in the `sound_ducking:` section of
your config. (If you don't include them, the default will be used).

### attack:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `10ms`

The duration of the period over which the ducking starts until it
reaches its maximum attenuation (attack stage). This value is specified
as a [time string](instructions/time_strings.md).

### attenuation:

Single value, type: `gain setting` (-inf, db, or float between 0.0 and
1.0). Default: `1.0`

The attenuation (gain) to apply to the target track while ducking.
`attenuation:` controls how quiet to make the target track while the
sound is playing.

### delay:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The duration to delay after the sound starts playing before ducking
starts. This value is specified as a
[time string](instructions/time_strings.md).

### release:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `10ms`

The duration of the period over which the ducking goes from its maximum
attenuation until the ducking ends (release stage). This value is
specified as a
[time string](instructions/time_strings.md).

### release_point:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `0`

The point relative to the end of the sound at which to start the
returning the attenuation back to normal (release stage). A value of 0.5
seconds means to begin to release the ducking 0.5 seconds prior to the
end of the sound. This value is specified as a
[time string](instructions/time_strings.md).

## Related How To guides

* [Ducking](../mc/sound/ducking.md)
