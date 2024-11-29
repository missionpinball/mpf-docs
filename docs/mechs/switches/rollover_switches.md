---
title: Rollover Switches
---

# Rollover Switches


Related Config File Sections:

* [switches:](../../config/switches.md)

Rollover switches in MPF are configured as normal switches. Furthermore,
they are often paired with a light (below an insert) which qualifies
them as candidate for a shots in MPF. They are usually
[mechanical micro switches](mechanical_switches.md).

![image](../images/rollover_micro_switch.jpg)

Typical part numbers:

* Stern/Sega/Data East: 500-6227-01/500-6227-03 or
    500-6227-02/500-6227-04 or 500-5707-00
* Spooky Pinball: SP-SW-001 or SP-SW-002

This is an example config:

``` mpf-config
# this is in your machine-wide config
switches:
  s_outlane_left:
    number: 0
  s_inlane_left:
    number: 1
  s_inlane_right:
    number: 6
  s_outlane_right:
    number: 7
lights:
  l_outlane_left:
    number: 0
  l_inlane_left:
    number: 1
  l_inlane_right:
    number: 6
  l_outlane_right:
    number: 7
##! mode: my_mode
# put this into a mode
shots:
  shot_outlane_left:
    switches: s_outlane_left
    show_tokens:
      leds: l_outlane_left
  shot_inlane_left:
    switches: s_inlane_left
    show_tokens:
      leds: l_inlane_left
  shot_inlane_right:
    switches: s_inlane_right
    show_tokens:
      leds: l_inlane_right
  shot_outlane_right:
    switches: s_outlane_right
    show_tokens:
      leds: l_outlane_right
shot_groups:
  sg_lanes:
    shots: shot_outlane_left, shot_inlane_left, shot_inlane_right, shot_outlane_right
    rotate_left_events: s_flipper_left_active
    rotate_right_events: s_flipper_right_active
    reset_events:
      sg_lanes_lit_complete: 1s
```

We configure four lane rollover switches (and their corresponding
lights). Then inside a mode we define one shot for each group and a
shot_group which enables rotation of the shots using the flipper
buttons.
