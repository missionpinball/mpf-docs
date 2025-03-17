---
title: "blinkenlight_player:"
---

# blinkenlight_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `blinkenlights:`
    section of a step.

The `blinkenlight_player:` section of your config is where you add or
remove colors to or from a blinkenlight based on events. It's also used
in shows (via the `blinkenlights:` section) to add or remove colors in
that show step.

Example from a config file:

``` yaml
blinkenlight_player:
  some_event:
    my_blinkenlight1:
      action: add
      color: red
      key: mykey1
  some_other_event:
    my_blinkenlight1:
      action: remove
      key: mykey1
```

In the example above, when the event called `some_event` is posted, the
color red will be added to my_blinkenlight1's list of colors (this will
cause the light to immediately start flashing if it wasn't already).
The new color will have the key `mykey1`. The key is used like a name of
the color, so that it can be removed later using that key. When the
event `some_other_event` is posted, the red color (key `mykey1`) will be
removed from the blinkenlight.

Example blinkenlight player from a show:

``` yaml
##! show: test
- time: 0
  blinkenlights:
    my_blinkenlight1:
      action: add
      color: blue
      key: blue_color
    my_blinkenlight2: purple
```

The first example shows the full config, while the second shows the
"express" config. (What's an "express config?" Details
[here](instructions/express_config.md).

The blinkenlight player's express config is the "add" action.

See [Blinkenlight player](../config_players/blinkenlight_player.md)
for details.

## Optional settings

The following sections are optional in the `blinkenlight_player:`
section of your config. (If you don't include them, the default will be
used).

### action:

Single value, type: one of the following options: add, remove,
remove_mode, remove_all. Default: `add`

What action the blinkenlight should perform. The `remove_all` action
will remove all the colors from the blinkenlight, effectively turning it
off. The `remove_mode` action will remove all the colors that were added
by the mode that the `remove_mode` action is coming from (remember that
a blinkenlight can have colors added from lots of different modes --
that's its whole purpose!).

### color:

Single value, type: color_or_token. Default: `white`

The only action that requires a color setting is the `add` action. It
sets the color to add to this blinkenlight. Color values may be a hex
string (e.g. `22FFCC`), a list of RGB values (e.g. `[50, 128, 206]`), a
color name (e.g. `turquoise`), or a brightness value (i.e. `AA` or
`120`). MPF knows 140+ standard web color names, and you can define your
own custom colors in the [named_colors:](named_colors.md) section of your config. If you use brightness on an RGB
light MPF will use the brightness for every channel. For instance
brigness `AA` will result in color `AAAAAA`.

### key:

Single value, type: `string`. Defaults to empty.

You can think of this value as a name for the color you're adding or
removing from the blinkenlight. If you add a color, then the key allows
you to remove the color later using the key to specify which color to
remove. If you don't specify a key, then the color is considered
"keyless" (see [Blinkenlight player](../config_players/blinkenlight_player.md) for more information about keyless colors).

## Related How To guides

* [Blinkenlight player](../config_players/blinkenlight_player.md)
