---
title: "fast:aud: Config Reference"
---

# fast:aud: Config Reference

--8<-- "deeper_config_section.md"

| Valid in | |
|-----|:----:|
|[machine](../instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](../instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Within the [`fast:`](../fast.md) section of your machine-wide config, you configure the audio board processor in the subsection `aud:`.

### Sample config:

```yaml
fast:
  aud:
    port: auto
    main_amp_enabled: true
    sub_amp_enabled: true
    headphones_amp_enabled: true

    main_steps: 20
    sub_steps: 20
    headphones_steps: 20

    default_main_volume: 32
    default_sub_volume: 32
    default_headphones_volume: 16

    persist_volume_settings: true

    max_hw_volume_main: 63
    max_hw_volume_sub: 63
    max_hw_volume_headphones: 63

    main_levels_list: None
    sub_levels_list: None
    headphones_levels_list: None

    link_sub_to_main: true
    link_headphones_to_main: false

    headphones_level: headphones
    mute_speakers_with_headphones: true
```

### port:

List of one (or more) values, each is a type: `string`. Defaults to `auto`.

A comma-separated list of the serial port names your FAST controller uses.

### baud:

Single value, int, default: `230400`

The connection baud rate.

### FAST Docs:

For the other properties, see the [FAST Audio Interface MPF Config page](https://fastpinball.com/mpf/config/audio/).
