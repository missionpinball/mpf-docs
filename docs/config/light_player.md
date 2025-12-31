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

The `light_player:` section of your config is where you can control lights in standalone config files or in show steps.


## Structure

The most common place you will put light players is in your shows, where it uses the config name `lights`.

``` yaml
shows:
  stoplight:
    - duration: 1s
      lights:
        (leds): green
    - duration: 1s
      lights:
        (leds): yellow
    - duration: 1s
      lights:
        (leds): red
    - duration: 300ms
      lights:
        (leds): off

```

The example above shows a four-step show that cycles through green, yellow, red, and off states for lights passed to the show via the [show_token](show_player.md#show_tokens) "leds".

Less commonly you might also define standalone `light_player` entries consists of an event trigger and one or more lights that will have their colors set.

``` yaml
light_player:
  some_event:
    led1:
      color: red
      fade: 200ms
    led2: off
    my_light_tag: 0000ff
```

In the above example, `some_event` is a trigger event which sets the light `led1` to red (via named color, with expanded options including fade), turns `led2` off, and lights tagged with "my_light_tag" will be set to blue (via the hex color code for blue in the shorthand format).
You can mix and match tags and light device names, but if a light is both listed by name and also matches one or more tags within the same triggering event handler, whichever value is set to the named light _last_ will win.

#### Wildcard light tag

There is also a special wildcard / catch-all that can be used to address ALL lights in the machine configuration at once.
Using the asterisk (or star) instead of a tag name will make the setting apply to every light.
This is **not** a true wildcard matcher like you can use with filesystem searches (e.g. where "file_12*.txt" might match "file_123.txt" and also "file_12345.txt").

```yaml
light_player:
  turn_everything_on_event:
    "*": on
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

#### Special color directives: `on`, `off`, and `stop`

MPF supports a few special terms that may be used instead of a color value.

##### `on`

If your light has a [default_on_color](lights.md#default_on_color) set, then instead of having
to name that color in particular, you can just use `on`. If you do not have one set, the light will
instead turn white (or its native color if single-channel.)

##### `off`

When you turn a light on to a certain color in a show, it will remain on throughout the show unless
directed otherwise. If you want your light to turn on for only a specific time, you will need to
explicitly set it to `off`. Another use case for `off` is when a lower-priority show has a light turned on,
but another show at a higher prority wants to override this -- you can set a light to `off` in a show without
having turned it on in that show first, just to ensure it is truly off.

##### `stop`

The `off`directive tells the light controller to specifically hold a light to no power, but does *not*
release the light from control. If you instead have a show that *no longer needs control* over a light
that it has already set at least once, you can use `stop` to remove the show's priority level hold on
the light's color. Imagine having something like a lightning strike show, where lights from all over
your machine flash yellow, but then immediately return to their previous color setting -- you would use
`stop` the step after each light flash to allow the previously-set color to show through again.


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
