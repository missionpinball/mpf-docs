---
title: Arduino Pinball Controller
---

# Arduino Pinball Controller


MPF can control System3 to System11c machines directly using the Arduino
Pinball Controller (APC). It contains CPU and drivers so it can also be
used to build full custom machines. Uses the
[LISY protocol](../lisy/protocol.md).

This is how APC generally works:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/w4Po8OE5Zkw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

See [Arduino Pinball Controller
Documentation](https://github.com/AmokSolderer/APC) on github for
details.

This is an example config:

``` mpf-config
#config_version=5
hardware:
  platform: lisy
lisy:
  connection: serial
  port: com1      # change this for your setup
  baud: 115200
digital_outputs:
  game_over_relay:
    number: 1
    type: light
    enable_events: ball_started
    disable_events: ball_will_end
segment_displays:
  info_display:
    number: 0
  player1_display:
    number: 1
  player2_display:
    number: 2
  player3_display:
    number: 3
  player4_display:
    number: 4
hardware_sound_systems:
  default:
    label: APC
```

See the [LISY platform](../lisy/index.md) for more details on configuring hardware.

* [Connecting a System3 to System11c Machine to APC](connection.md)
