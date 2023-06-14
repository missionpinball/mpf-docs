---
title: How to enable "secondary playfield" flippers
---

# How to enable "secondary playfield" flippers


Related Config File Sections:

* [flippers:](../../config/flippers.md)

Secondary or upper flippers (e.g. on an upper playfield) are enabled and
defined just like normal lower flipper.

This is an example:

``` mpf-config
#! switches:
#!   s_flipper_left:
#!     number:
#!   s_flipper_right:
#!     number:
#!   flipperUpL:
#!     number:
#!   flipperUpR:
#!     number:
#! coils:
#!   c_flipper_lower_left_main:
#!     number:
#!   c_flipper_lower_right_main:
#!     number:
#!   flipperUpLMain:
#!     number:
#!   flipperUpRMain:
#!     number:
flippers:
  lower_left:
    main_coil: c_flipper_lower_left_main
    activation_switch: s_flipper_left
    label: Left Main Flipper
  lower_right:
    main_coil: c_flipper_lower_right_main
    activation_switch: s_flipper_right
    label: Right Main Flipper
  upper_left:
    main_coil: flipperUpLMain
    activation_switch: flipperUpL
    enable_events: ball_started, enable_upper_flippers
    disable_events: ball_will_end, service_mode_entered, disable_upper_flippers
    label: Upper Left Flipper
  upper_right:
    main_coil: flipperUpRMain
    activation_switch: flipperUpR
    enable_events: ball_started, enable_upper_flippers
    disable_events: ball_will_end, service_mode_entered, disable_upper_flippers
    label: Upper Right Flipper
```

Additionally, we defined `disable_upper_flippers` as event to disable
the upper flippers and `enable_upper_flippers` to re-enable them. This
might be useful if you want to disable flippers in some mode. If you do
not want them to be enabled by default remove `ball_started` from
`enable_events`.
