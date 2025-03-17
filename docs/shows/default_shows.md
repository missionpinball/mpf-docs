---
title: MPF's default shows
---

# MPF's default shows

MPF comes out of the box with several default shows included to support common
use cases. These shows use tokens to allow you to control which lights,
and in many of them which colors, are used. Note that the show names are all
written in lowercase when used in code.

The default shows are "[on](#on)", "[off](#off)", "[flash](#flash)", "[led_color](#led_color)", "[bl_color](#bl_color)", and "[flash_color](#flash_color)."


## On

The most basic of shows, "on" just turns a light or lights on to its default color, indefinitely.

### Duration

"On" has a duration of -1, so it will never end until told
(or automatically turned off e.g. by its spawning mode stopping).

### Color

This show does not allow for selection of light color. The default on color
of the light will be used if none has been declared on the device.
See: [lights:default_on_color](../config/lights.md#default_on_color).

### Tokens

#### `light`, `lights`, `led`, `leds`

The "on" show is not picky about how you tell it which lights to turn on.
You can use any token name (or multiple if you really want) of these four to pass
your list of light names.


### Example

To use the "on" show in a show_player, you might write something like:

```yaml
show_player:
  my_triggering_event:
    on:
      show_tokens:
        light: my_light
```


## Off

The next most basic show is "off". This show exists so that you can
explicitly turn a light off. This can be useful when running shows
with different priority values (say, though them inheriting their
mode priorities). With this show you can make sure a light is off
even if a lower priority show wants to have it on for some reason.

### Duration

"Off" has a duration of -1, so it will never end until told
(or automatically turned ended e.g. by its spawning mode stopping).

### Tokens

#### `light`, `lights`, `led`, `leds`

Like "on", the "off" show is not picky about how you tell it which lights to control.
You can use any token name (or multiple if you really want) of these four to pass
your list of light names.


## Flash

Getting a little more complex and interesting, "flash" is a show that
turns lights on and then off with the same duration for both phases.

**Note:** *You can also use the [flasher_player](../config/flasher_player.md) for a more concise way of
configuring flash behaviors*

### Duration

"Flash" has a duration for each step of 1 second. This means that
if you want to go faster or slower, you need to configure a speed in
your show_player. See: [show_player:speed](../config/show_player.md#speed).

### Color

Like "on", this show uses the default_on_color for the given lights.

### Tokens

#### `light`, `lights`, `led`, `leds`

Again, you can use any of these four tokens to tell the show which lights
to control.

### Example

```yaml
show_player:
  my_triggering_event:
    flash:
      speed: 10 # this means it will play 10x faster, so 100ms on, 100ms off
      show_tokens:
        lights: my_flashing_light, my_other_flashing_light
```


## Led_color

The default show "led_color" behaves like "on", but lets you configure the color.

### Duration

Like "on", this show has no duration and will just remain showing the color until stopped.

### Tokens

#### `light`, `lights`, `led`, `leds`

Again, you can use any of these four tokens to tell the show which lights
to control. Even though the show is named "led_color", it works with any light device.

#### `color`

This show is a little more complex than "on" -- you must provide a color for the light
to turn. If the light is configured without a certain light channel, it may instead show
nothing rather than attempting to show an incompatible color.

### Example

```yaml
show_player:
  my_triggering_event:
    led_color:
      show_tokens:
        lights: my_light
        color: blue # or perhaps "0000AA"
```


## BL_color

The default show "bl_color", short for blinkenlights_color, behaves like "on", but lets you configure the color.

### Duration

Like "on", this show has no duration and will just remain showing the color until stopped.

### Tokens

#### `light`, `lights`, `led`, `leds`, `blinkenlight`, `blinkenlights`

This event supports two additional tokens for selecting your lights to control, but any
light may be used in any token name.

#### `color`

This show also wants a "color" token just like "led_color".


## Flash_color

The final default show included with MPF is "flash_color", which
combines the features seen in the other default shows.

### Duration

Like "flash", "flash_color" uses a duration of 1 second for each step.

### Tokens

#### `light`, `lights`, `led`, `leds`

As with the others, any of these tokens will do to identify the relevant lights.

#### `color`

Like "led_color", this show must be configured with a custom color for its lights.

### Example

```yaml
show_player:
  my_triggering_event:
    flash_color:
      speed: 0.5 # so flash for 2 seconds, off for 2 seconds, etc
      show_tokens:
        led: my_flashing_light
        color: 00FF00-f1s #green with a 1s fade
```
