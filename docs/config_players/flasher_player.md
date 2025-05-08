---
title: Flasher player
---

# Flasher player


The *flasher player* is a [config player](index.md) that's used to flash lights.

## Usage in config files

In config files, the flasher player is used via the `flasher_player:` section.

## Usage in shows

In shows, the flasher player is used via the `flashers:` section of a step.

## Config Options

See [flasher_player:](../config/flasher_player.md) for config details.

## Examples

Simple flasher behavior on a [switch_active](../events/switch_active.md) event with default length and color:

``` yaml
flasher_player:
  my_switch_active: my_light
```

Flasher with customized color and timing:

``` yaml
flasher_player:
  my_second_switch_active:
    my_second_light:
      color: red
      ms: 300ms
```

Multiple flashers triggered by a single event:

``` yaml
flasher_player:
  my_trigger_event:
    my_double_flasher_light_1:
      color: blue
      ms: 250ms
    my_double_flasher_light_2:
      color: green
      ms: 250ms
```
