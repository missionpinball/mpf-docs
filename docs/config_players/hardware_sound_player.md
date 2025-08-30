---
title: Hardware Sound player
---

# Hardware Sound player

The *hardware sound player* is a [config player](index.md)
that's used to control sounds. (This player is part of the MPF media
controller and only available if you're using MPF-MC for your media
controller.)

## Usage in config files

In config files, the sound player is used via the
`hardware_sound_player:` section. Event names that will trigger sound
actions are nested sub-headings and sound names are either listed as
nested sub-headings below that.

## Usage in shows

In shows, the sound player is used via the `hardware_sounds:` section of
a step.

## Optional settings

Additional information may be found in the
[hardware_sound_player](../config/hardware_sound_player.md) configuration reference documentation.

## Related Pages:

* [hardware_sound_player: Config Reference](../config/hardware_sound_player.md)
* [hardware_sound_player API Reference](../code/api_reference/config_players/hardware_sound_player.md)
