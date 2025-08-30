---
title: Blinkenlight player
---

# Blinkenlight player

* [blinkenlight_player: Config Reference](../config/blinkenlight_player.md)

The *blinkenlight player* is a [config player](index.md)
that's used add or remove colors from a blinkenlight.

!!! note

    **What is a blinkenlight?**

    A blinkenlight is a flashing light on your pinball machine. But it's
    different than a normal flashing light that you might have in a show,
    because with a blinkenlight, multiple modes (or shows) can add colors to
    the light, and the blinkenlight will flash all the colors in a sequence.

    Blinkenlights are useful if you have a game where multiple modes could
    be running and they all share the same shot(s). Each mode could have a
    different color, and the light for the shot could flash between all the
    colors, to show the player that shooting that shot will score all those
    modes at once.

    For example, this is the kind of thing that happens in Stern's Game of
    Thrones. If you start multiple houses at the same time, and they share
    shot(s) the sigils in front of those shots will flash different colors
    to show you that the same shot will score different modes. The left ramp
    might alternate between white (Stark) and red (Lannister) to show you
    that both modes will score that shot.

This is an example of a blinkenlight player:

``` yaml
blinkenlight_player:
  some_event:
    my_blinkenlight: red
  some_other_event:
    my_blinkenlight:
      action: add
      key: blue_color
      color: blue
```

In the example above, when the event called `some_event` is posted, the
color red will be added to the blinkenlight `my_blinkenlight`. When the
event `some_other_event` is posted, the color blue will be added to the
same blinkenlight. This color has the key `blue_color`, which is useful
if we want to remove the color later.

Note that the `some_event` example has a shortened config than the
`some_other_event` example. This shortened version is called an express
config. The blinkenlight's express config is the same thing as doing an
"add" action with the color you specify. It's just a shorter way to
do the same thing. You can read more about express configs
[here](../config/instructions/express_config.md). Also, see the section below called Express Config for more
information on the express config.

To use a blinkenlight player, you first have to define a blinkenlight
within your machine config (see the blinkenlight page
[here](../config/blinkenlights.md)). The
blinkenlight's config will set which actual light in your pinball
machine is controlled by the blinkenlight. When you add a color to the
blinkenlight from a blinkenlight player, the light will start to flash
that color. As more colors are added, the light will cycle through all
the colors.

!!! note

    It makes the most sense to specify an RGB LED as the underlying light
    for a blinkenlight, since the whole idea is for the light to flash
    different colors. There's nothing that stops you from adding a regular
    light, though. Instead of colors, you could specify different brightness
    levels to flash. Either way, we refer to those as "colors" in this
    documentation.

## A Blinkenlight's cycle

The blinkenlight will cycle through all the colors that have been added
to it. You have control over how this cycle works. All of the options to
control a blinkenlight's cycle are controlled from the `blinkenlights`
section of your config file, and not the `blinkenlight_player` section.

For example, you can specify how long each color is displayed by setting
the `color_duration` property of the blinkenlight. This will cause each
color to be displayed for a specified length of time, and the more
colors you add, the longer the blinkenlight's cycle will take.
Alternatively, if you want the blinkenlight's cycle to last a certain
amount of time regardless of how many colors are added to it, you can
set the `cycle_duration` instead.

When the blinkenlight only has one color, it will flash that single
color in a sequence like this: `on` `off` `on` `off` and so on. When
more than one color is added, however, you might not want the light to
turn off at the end of each cycle. For example, if your blinkenlight has
two colors, red and green, you might want the cycle to be: `red` `green`
`off` `red` `green` `off`, or you might simply want it to be `red`
`green` `red` `green`. You can control this behavior with the
`off_when_multiple` setting of your blinkenlight. Setting this value to
`True` will turn the light off at the end of each cycle. The default
value is `False`, which will not turn the light off when multiple colors
are present.

Blinkenlights will stay in sync with each other automatically, if you
have multiple blinkenlights with the same settings and the same number
of colors. So, for example, if you have two blinkenlights with the same
`cycle_duration`, and each one has 3 colors added to it, then they will
start their cycles at the same time, and end their cycles at the same
time. This way, the blinkenlights will stay in sync with each other.
This is useful if you have a blinkenlight on your left and right ramps,
for example, and you want them both to flash the same colors. You would
want them to show the same colors at the same time.

## A cycle example

Let's say you have a blinkenlight that is set up like this:

``` yaml
#! lights:
#!   l_left_ramp_arrow:
#!     channels:
#!       red:
#!         number: 1
#!       green:
#!         number: 2
#!       blue:
#!         number: 3
#!   l_right_ramp_arrow:
#!     channels:
#!       red:
#!         number: 4
#!       green:
#!         number: 5
#!       blue:
#!         number: 6
blinkenlights:
  blinkenlight_1:
    cycle_duration: 1s
    off_when_multiple: false
    light: l_left_ramp_arrow
```

In this case, `blinkenlight_1` has a `cycle_duration` value of `1s`.
That is, each cycle lasts 1 second, regardless of how many colors the
blinkenlight has. Now, let's say you use a blinkenlight_player to add
the color red to the blinkenlight. Now the blinkenlight's cycle would
look like this:

+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     |       | 1     |       | 1     |       | 1     |       |
| s     |       | s     |       | s     |       | s     |       |
| econd |       | econd |       | econd |       | econd |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| > red | > off | > red | > off | > red | > off | > red | > off |
+-------+-------+-------+-------+-------+-------+-------+-------+

If green color is added to the blinkenlight, the cycle would change to
this:

+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     |       | 1     |       | 1     |       | 1     |       |
| s     |       | s     |       | s     |       | s     |       |
| econd |       | econd |       | econd |       | econd |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| > red | green | > red | green | > red | green | > red | green |
+-------+-------+-------+-------+-------+-------+-------+-------+

Now let's say a third color (blue) is added:

<table style="width:86%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3">1 second</td>
<td colspan="3">1 second</td>
<td colspan="3">1 second</td>
<td colspan="3">1 second</td>
</tr>
<tr class="even">
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td><blockquote>
<p>b</p>
</blockquote></td>
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td><blockquote>
<p>b</p>
</blockquote></td>
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td><blockquote>
<p>b</p>
</blockquote></td>
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td><blockquote>
<p>b</p>
</blockquote></td>
</tr>
</tbody>
</table>

Note that each color now is only 1/3 of a second long, since there are
three of them per cycle now.

Now, blue is removed from the blinkenlight, while the blinkenlight is
currently showing a blue color during the second cycle:

<table style="width:88%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3">1 second</td>
<td colspan="4">1 second</td>
<td colspan="2">1 second</td>
<td colspan="2">1 second</td>
</tr>
<tr class="even">
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td><blockquote>
<p>b</p>
</blockquote></td>
<td><blockquote>
<p>r</p>
</blockquote></td>
<td><blockquote>
<p>g</p>
</blockquote></td>
<td>b</td>
<td>g</td>
<td><blockquote>
<p>red</p>
</blockquote></td>
<td>green</td>
<td><blockquote>
<p>red</p>
</blockquote></td>
<td>green</td>
</tr>
</tbody>
</table>

Notice how blue is displayed when the color is removed, and the light
immediately switches to green, since green should be displayed at that
point in time now that the blinkenlight only has 2 colors. So the end
result is green "flashes" very briefly before red is displayed again
and the red/green cycle starts.

## Using Blinkenlights in shows

You can also use blinkenlight_player from within a show. This lets you
add colors to a blinkenlight during a show. It probably doesn't make
sense most of the time to do this, because colors you add to a
blinkenlight will only stick around while the show is active. Once the
show ends, the colors you added during that show will automatically be
removed from the blinkenlight.

!!! note

    This is true of colors added during modes as well. If a mode in your
    game adds colors to a blinkenlight, those colors will be automatically
    removed from the blinkenlight when the mode ends. If you restart the
    mode, those colors won't come back automatically, however, so keep that
    in mind. You might need to add the colors again when the mode restarts,
    depending on how your game works.

Example blinkenlight player from a show:

``` yaml
##! show: test
- time: 0
  blinkenlights:
    my_blinkenlight: red
```

## Usage in config files

In config files, the blinkenlight player is used via the
`blinkenlight_player:` section.

## Usage in shows

In shows, the blinkenlight player is used via the `blinkenlights:`
section of a step.

## Express Config and Keyless Colors

As mentioned above, the express config for `blinkenlight_player`
performs the `add` action. So, the color you specify as the express
config value will be the color to add to the blinkenlight. However, if
you add a color this way, there is no `key` value for the color. Or,
more specifically, the `key` value will be empty. We could refer to
colors without a `key` value as a keyless color. If you later use the
`remove` action and don't specify a `key` to remove, then the keyless
color will be removed.

This is better explained with an example. Consider this
`blinkenlight_player`:

``` yaml
blinkenlight_player:
  some_event:
    my_blinkenlight: red
  some_other_event:
    my_blinkenlight:
      action: remove
```

In this case, the color `red` will be added to `my_blinkenlight` when
the `some_event` event is posted. This color doesn't have a `key`
value, so this color is keyless. When the `some_other_event` event is
posted, the `remove` action is performed. Since this `remove` action
also didn't specify a `key` value, then MPF will look for a keyless
color and remove that color from the blinkenlight. In this case, the
color red will be removed.

Note that keyless colors are only valid within the context of the mode
or show that is performing the keyless action. So, a `remove` action
from `mode1` will not remove the keyless color that was added by
`mode2`. It will only remove the keyless color added by `mode1`.

There's a special value you can use in the express config to remove a
keyless color. Instead of using the full config and specifying an
`action: remove` as we did above, you can use the special color `stop`
or `remove` in the express config to do the same thing. The following is
equivalent to the example above:

``` yaml
blinkenlight_player:
  some_event:
    my_blinkenlight: red
  some_other_event:
    my_blinkenlight: remove
```

In this case, the red color is added to the blinkenlight when
`some_event` is posted, and then removed when `some_other_event` is
posted.
