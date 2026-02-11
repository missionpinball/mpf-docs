---
title: Shakers
---

# Shakers


Related Config File Sections:

* [coils:](../config/coils.md)
* [coil_player:](../config/coil_player.md)
* [shakers:](../config/shakers.md)

Shaker motors cause vibrations to give the player tactile feedback.
Shakers can be implemented through coil or motor control, or using the dedicated `shaker` device type.
Currently this device config type is only supported by the FAST system (using the 1313 EXP board),
so for other integrations, you will need to define your 12v power control as a coil.

## Hardware

[TODO: Add a picture of a shaker](../about/help.md)

--8<-- "todo.md"

Part numbers:

* Spooky: #100-0054-00
* Stern Spike: #502-5027-01
* Stern SAM: #502-5027-00
* Data East/Sega/Stern: #515-5893-01

Most shaker motors are not meant to be enabled without PWM. Depending on
the voltage your PWM should have a duty cycle between 10% and 30%.

## Config as a Coil

This is an example on how to use a shaker using coil_player:

``` yaml
coils:
  c_shaker:
    number:
    default_pulse_ms: 1
    default_hold_power: 0.125    # keep this low

##! mode: your_mode
coil_player:
  enable_shaker_event:
    c_shaker: enable
  disable_shaker_event:
    c_shaker: disable
##! test
#! start_game
#! mock_event test_event
#! start_mode your_mode
#! post enable_shaker_event
#! advance_time_and_run .5
#! post disable_shaker_event
```

Alternatively, you can use it inside a show:

``` yaml
coils:
  c_shaker:
    number:
    default_pulse_ms: 1
    default_hold_power: 0.125    # keep this low

##! mode: your_mode
shows:
  my_show_with_shaker:
    - duration: 1s
      coils:
        c_shaker: enable
#!       events: test_event
      # add some slides, lights or sounds here
    - duration: 1s
      coils:
        c_shaker: disable
      # add some more slides, lights or sounds here

show_player:
  play_show_with_shaker:
    my_show_with_shaker:
      loops: -1
##! test
#! start_game
#! mock_event test_event
#! start_mode your_mode
#! post play_show_with_shaker
#! advance_time_and_run .5
#! assert_event_called test_event
```

## Config as a Shaker device:

``` yaml
fast:
  exp:
    boards:
      1313board:
        model: FP-EXP-1313

shakers:
  shaker:
    number: 1313board-1
    control_events:
      mid_shaker:
        duration: 500ms
        power: 0.25
      hi_shaker:
        duration: 2s
        power: 0.75

event_player:
  my_trigger_event:
    - mid_shaker
    - hi_shaker|500ms
```
