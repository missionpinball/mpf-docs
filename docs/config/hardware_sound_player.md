---
title: "hardware_sound_player: Config Reference"
---

# hardware_sound_player: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `hardware_sounds:`
    section of a step.

The `hardware_sound_player:` section of your config is where you can
control external sound modules (e.g. in LISY).

This is an example:

``` yaml
hardware_sound_systems:
  default:
    label: Default external sound system
hardware_sound_player:
  event_posted_elsewhere1:
    2:
      action: play
  ball_started:
    3: play
  test_stop: stop
```

## Optional settings

The following sections are optional in the `hardware_sound_player:`
section of your config. (If you don't include them, the default will be
used).

### action:

Single value, type: one of the following options: play, play_file,
text_to_speech, set_volume, increase_volume, decrease_volume, stop.
Default: `play`

`play` will play a sound. Depending on the hardware this might stop
previous sounds. Also loop behavior depends on the hardware and might
be different per sound.

`stop` will stop all sounds.

### platform_options:

Single value, type: `dict`. Defaults to empty.

--8<-- "todo.md"

### sound_system:

Single value, type: `string` name of a
[hardware_sound_systems:](hardware_sound_systems.md) device. Default: `default`

In case you got multiple hardware_sound platforms you can expliticly
select one here.

### track:

Single value, type: `integer`. Default: `1`

The track number to play this sound on. What this means depends on your
hardware. Usually, there are one or two tracks.

### value:

Single value, type: `string`. Defaults to empty.

The number of your sound.

## Related How To guides

* [Arduino Pinball Controller](../hardware/apc/index.md)
* [How to use MPF with the LISY platform](../hardware/lisy/index.md)
