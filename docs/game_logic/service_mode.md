---
title: Service Mode
---

# Service Mode

MPF has a build in service mode which can be extended using settings (or
in code). Usually you map your
[service switches and door switches](../mechs/switches/service_and_door_switches.md) to control service mode. Additionally, you might want to add
keys of your [keyboard](../config/keyboard.md)
during development.

This is an example:

``` yaml
# include service mode in your modes list
modes:
  - service
# add tags to your switches
switches:
  s_door_open:
    number: 1
    tags: service_door_open, power_off
  s_service_enter:
    number: 17
    tags: service_enter
  s_service_esc:
    number: 18
    tags: service_esc
  s_service_up:
    number: 19
    tags: service_up
  s_service_down:
    number: 20
    tags: service_down
# add a setting (not used here)
settings:
  replay_score:
    label: Replay Score
    values:
      500000: "500000 (default)"
      1000000: "1000000"
      1500000: "1500000"
    default: 500000
    key_type: int
    sort: 100
# add keyboard switches
keyboard:
  right:
    switch: s_service_enter
  left:
    switch: s_service_esc
  up:
    switch: s_service_up
  down:
    switch: s_service_down
# you need to define a "sfx" sound track because the service mode brings some sounds (see the sound documentation for details)
sound_system:
  tracks:
    music:
      type: standard
      simultaneous_sounds: 1
      volume: 0.5
    voice:
      type: standard
      simultaneous_sounds: 1
      volume: 0.7
    sfx:
      type: standard
      simultaneous_sounds: 8
      volume: 0.4
# additionally you need to define some slide styles which are used in the mode
widget_styles:
  medium:
    font_name: pixelmix
    font_size: 8           # for LCDs you need to increase this to 30-40. also change the font above
    adjust_top: 1
    adjust_bottom: 1
  small:
    font_name: smallest_pixel-7
    font_size: 9           # for LCDs you need to increase this to 30-40. also change the font above
    adjust_top: 2
    adjust_bottom: 3
```

## Related Pages:

* [How to design a game in MPF using Modes](../game_design/index.md)
* [settings: Config Reference](../config/settings.md)

* [service API Reference](../code/api_reference/core/service.md)
* [service_mode API Reference](../code/api_reference/modes/service.md)
* [Machine Management: Service Mode](../machine_management/service_mode.md)
