---
title: "sound_marker:"
---

# sound_marker:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `markers:` setting in your `sounds:` section of your config is where
you configure markers which trigger events at certain points in
playback.

## Required settings

The following sections are required in the `sound_marker:` section of
your config:

### events:

List of one (or more) events.

A list of one or more names of events that MPF will post when this
marker is reached during sound playback. Enter the list in the MPF
config list format. These events are posted exactly as they're entered.

### time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)).

The marker time (in seconds) relative to the beginning of the sound
file.

## Related How To guides

* [Sounds, Music & Audio](../mc/sound/index.md)
