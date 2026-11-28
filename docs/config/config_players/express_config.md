---
title: Config Player - Express Configs
---

# Config player - Express Configs

Config_players support two general formats for specifying their behavior, full and express.
The express format is used for common or simple cases, to reduce how much structure you need in your yaml files.

What each config player type supports is up to it. For these examples we will consider the light player.

Express configs entries for light player look like:

``` yaml
light_player:
  event1:
    light_1: off
    light_2: red
  event2:
    light_1: blue-f100ms
    light_2: white-f100 # defaults to ms
```

Full configs look like this:

``` yaml
light_player:
  event1:
    light_1:
      color: off
    light_2:
      color: red
  event2:
    light_1:
      color: blue
      fade: 100ms
    light_2:
      color: white
      fade: 100 # defaults to ms
```

In both cases, these configurations are saying,
"When *event1* is posted, *light_1* turns off and light_2 goes red.
"When *event2* is posted, *light_1* turns blue over 100ms and light_2 goes white over 100ms."


## Supported types

The following config players support express configurations.

### [blinkenlight_player:](../blinkenlight_player.md)

Blinkenlights support turning the value into `{color: value}`, except if value is "stop" or "remove" in which case it's `{action: remove}`

``` yaml
blinkenlight_player:
  event1:
    my_blinkenlight: some_color
    my_other_blinkenlight: remove
```

### [coil_player:](../coil_player.md)

Coil player uses the value as `{action: pulse, pulse_ms: int(value)}`.
If the value is "disable" or "off", instead it issues `{action: disable}`.
If the value is "enable" or "on", instead it issues `{action: enable}`.

If it's unclear, then it sends it as `{action: pulse}`

``` yaml
coil_player:
  event1:
    my_coil: enable
    my_other_coil: 20ms # pulse
  event2:
    my_coil: disable
```

### [event_player:](../event_player.md)

Event_player supports handling value as a list, as `list(events(value))`, and supports event piped delays.

``` yaml
event_player:
  event1: event_1_out_a, event_1_out_b, event_1_delayed_out|1s
```

### [flasher_player:](../flasher_player.md)

Flasher_player converts value into `{ms: value}`, where value is how long the flash stays on.

``` yaml
flasher_player:
  event1:
    my_flasher: 100ms
```

### [hardware_sound_player:](../hardware_sound_player.md)

Hardware_sound_player converts value into `{action: value}`.

``` yaml
hardware_sound_player:
  event1:
    my_hardware_sound_system: stop
```

### [light_player:](../light_player.md)

Light player allows specification of both color and fade-in rate.

``` yaml
light_player:
  event1:
    light_1: on
    light_2: red
    light_3: ff00ff-f100ms
```

### [random_event_player:](../random_event_player.md)

Random_event_player supports turning a comma separated list of values int into the list of random event output options.

``` yaml
random_event_player:
  draw_random_event: random_out_1, random_out_2, random_out_3
```

### [score_queue_player:](../score_queue_player.md)

Score_queue_player supports "value" into `{int: value}`

``` yaml
score_queue_player:
  event1:
    my_score_queue: 250
```

### [segment_display_player:](../segment_display_player.md)

segment_display_player supports "value" into `{action: add, text: value}`

``` yaml
segment_display_player:
  event1:
    my_segment_display: HELLO
```

### [show_player:](../show_player.md)

Show_player supports "value" into `{action: value}`

``` yaml
show_player:
  event1:
    my_show: stop
  event2:
    my_show: advance
```

### [variable_player:](../variable_player.md)

Variable_player supports "value" into `{int: value}` or "value|block" into `{int: value, block: True}`.
Both cases are implicitly `{action: add}` as well.

``` yaml
variable_player:
  event1:
    score: 500
  event2:
    score: 1000|block
```

## Usage in shows

Express configurations are especially useful in shows, and `light_player` in particular has show token handling that allows making very reusable shows.

In shows, the light names (or tags) and colors may be specified with tokens. In MPF 0.82 and 0.59 support was adding for tokens setting light fade rates as well.

``` yaml
#show_version=6

# Show in file "my_show.yaml"
- duration: 100ms
  lights:
    (light_group_1): red  # use a token for the light name
    light_2: (color)-f100ms  # use a token for the color
    light_3: (color)-f(fade_rate)  # fade_rate token option only supported starting with MPF 0.82 and 0.59
```

``` yaml
show_player:
  event1:
    my_show:
      show_tokens:
        light_group_1: light_1
        color: blue
        fade_rate: 50ms
```
