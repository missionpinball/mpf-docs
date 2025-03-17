---
title: Using LEDs as display (display_light_player)
---

# Using LEDs as display (display_light_player)


You can map any display to your playfield LEDs or any LEDs (e.g. a LED
matrix) in your machine. This enables you to leverage any MC features
and display them on any LEDs (or more specifically any lights) in your
machine.

Video about display_light_player:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/38hc7IIfVJI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

To use this in a show you can use this:

``` yaml
##! show: test_show
- display_lights:
    your_source_display:     # use any display defined in your machine
      lights: "*"            # map all lights. you can also use a tag
```

Or standalone:

``` yaml
display_light_player:
  your_event:
    your_source_display:
      lights: "*"
```

Then map your lights to a position on the display:

``` yaml
lights:
  l_light1:
    number: 1
    x: 0.3595817467355206
    y: 0.026751757949132805
  l_light2:
    number: 2
    x: 0.34303657433971446
    y: 0.02873336964906857
```

You can map those in the MPF monitor and then copy the locations using
the script in `tools/monitor_to_config.py` or manually. You may need to
adjust config names in the script (improvements welcome).

## Usage in config files

In config files, the display light player is used via the
`display_light_player:` section.

## Usage in shows

In shows, the display light player is used via the `display_lights:`
section of a step.

## Config Options

See [display_light_player:](../config/display_light_player.md) for
config details.
