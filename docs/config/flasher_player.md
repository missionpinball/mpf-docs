---
title: "flasher_player: Config Reference"
---

# flasher_player: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `flashers:` section
    of a step.

The `flasher_player:` section of your config is where you can flash
lights. See [Flasher player](../config_players/flasher_player.md) for details.

## Optional settings

The following sections are optional in the `flasher_player:` section of
your config. (If you don't include them, the default will be used).

### color:

Single value, type: `string`. Default: `on`

Set a color for flashing, if the flasher supports RGB coloring.

Color values may be a hex string (e.g. `22FFCC`), a list of RGB values
(e.g. `[50, 128, 206]`), a color name (e.g. `turquoise`), or a
brightness value (i.e. `AA` or `120`). MPF knows 140+ standard web color
names, and you can define your own custom colors in the
[named_colors:](named_colors.md) section of your
config. If you use brightness on an RGB light MPF will use the
brightness for every channel. For instance brigness `AA` will result in
color `AAAAAA`.

### ms:

Single value, type: `ms_or_token`. Default: `100ms`

Configures how long should that flasher be enabled.

## Related How To guides

* [Flashers](../mechs/lights/flashers.md)
