---
title: '"Config Player" Config Reference'
---

# "Config Player" Config Reference

For more, see the [Config Player Info page](../../config_players/index.md).

Config Players are used to perform actions in response to events happening.

The name of the config player represents the kind of action that will be performed.
For example, a `show_player` will manage shows in response to events. The `lights_player`
will manage lights in response to events. And the `random_event_player` will play a random
event from a given list in response to a trigger event.

## Usage

Config players may be used inside machine and mode files in order to perform actions in
response to events, but the may also be used within shows to perform actions when the
show executes a step.

In machine and mode files, the section name used in the YAML is the name of the config
player type, with the suffix "\_player" attached. In show files, the suffix is dropped and replaced with "s".

For example, light_player in a mode file looks like:

``` yaml
#config_version=6

light_player:
  some_event:
    my_light: red
  another_event:
    my_light: blue
```

while in a show file, a flashing red and blue light might look like:

``` yaml
#show_version=6
- duration: 500ms
  lights:
    my_light: red
- duration: 500ms
  lights:
    my_light: blue
```

Config Players each have a structure with the same top and second level (the name of the config player type, and then the name of the event to listen for):

``` yaml
<thing>_player:
  <some_event>:
    ...
```

That's where the similarities end -- each config player type uses its own syntax and special semantics to manage their devices. Some config players support multiple
different syntaxes, depending on the complexity of the action you wish to perform.

## Combination in Shows

When writing config players in machine and mode files, you have to define them in their own top-level sections (like `event_player:`). which means you cannot combine
multiple types of player in a single event listener. In shows, on the other hand, you can combine as many config players in a single step as you like, and they will
all execute together.

For example, a show that plays a sound and flashes a light at the same time could look like:

``` yaml
#show_version=6

- duration: 500ms
  lights:
    my_light_2: on
  sounds:
    bird_chirp: play
- duration: 500ms
    my_light_2: off
```


## Index

* [blinkenlight_player:](../blinkenlight_player.md)
* [coil_player:](../coil_player.md)
* [display_light_player:](../display_light_player.md)
* [event_player:](../event_player.md)
* [flasher_player:](../flasher_player.md)
* [light_player:](../light_player.md)
* [queue_event_player:](../queue_event_player.md)
* [queue_relay_player:](../queue_relay_player.md)
* [random_event_player:](../random_event_player.md)
* [score_queue_player:](../score_queue_player.md)
* [segment_display_player:](../segment_display_player.md)
* [show_player:](../show_player.md)
* [slide_player:](../slide_player.md)
* [sound_player:](../sound_player.md)
* [variable_player:](../variable_player.md)
* [widget_player:](../widget_player.md)

## MPF-MC Config Players

MPF-MC included a few more player types, but these are deprecated with MPF version 0.80 onward.

* [playlist_player:](../playlist_player.md)
* [sound_loop_player:](../sound_loop_player.md)
* [track_player:](../track_player.md)
