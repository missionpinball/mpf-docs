---
title: "light_player: Config Reference"
---

# light_player: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `lights:` section of
    a step.

The `light_player:` section of your config is where you can control
lights in config or shows. Example in config:

``` yaml
light_player:
  some_event:
    led1:
      color: red
      fade: 200ms
    led2:
      color: ff0000
      fade: 2000ms
```

``` yaml
shows:
  rainbow:
    - lights:
        (leds): red
    - lights:
        (leds): orange
    - lights:
        (leds): yellow
    - lights:
        (leds): green
    - lights:
        (leds): blue
    - lights:
        (leds): purple
```

## Optional settings

The following sections are optional in the `light_player:` section of
your config. (If you don't include them, the default will be used).

### color:

Single value, type: `string`. Default: `white`

Set a color to this light. Color values may be a hex string (e.g.
`22FFCC`), a hex string including a brightness value (e.g. `22FFCC%60`), a color name
(e.g. `turquoise`), or a brightness value (i.e. `AA` or `120`). Note that
a list of RGB values (e.g. `[50, 128, 206]`) cannot be used, these RGB values
are only valid in the [named_colors:](named_colors.md) section of your config file. MPF
knows 140+ standard web color names, and you can define your own custom
colors in the [named_colors:](named_colors.md)
section of your config. The colors MPF knows can be easily checked by reading:
<https://github.com/missionpinball/mpf/blob/dev/mpf/core/rgb_color.py>
If you use brightness on an RGB light MPF will
use the brightness for every channel. For instance brigness `AA` will
result in color `AAAAAA`.

There is a special color `stop` which will remove the current light
entry from the light stack and the current show will become transparent
to underlying shows as if the light has never been used in this show.

### fade:

Single value, type: `ms_or_token`. Defaults to empty.

Time to fade this light in ms. Use this to achieve smooth transitions
between colors.

### priority:

Single value, type: `int_or_token`. Default: `0`

Relative priority of this entry in the light stack.

## Related Pages:

* [Light player Config Player Reference](../config_players/light_player.md)
* [light_player API Reference](../config_players/light_player.md)
