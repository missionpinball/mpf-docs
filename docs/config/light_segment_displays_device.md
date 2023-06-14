---
title: light_segment_displays:
---

# light_segment_displays:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

lights: listNone light_groups: listNone type: single

## lights:

List of one (or more) values, each is a type: dictionary consisting of
`string` : string name of a [lights:](lights.md) device.

In this setting you provide a list of mapping for each segment. This is
an example for a two 7-segment display:

``` mpf-config
#! hardware:
#!   segment_displays: light_segment_displays
#! light_segment_displays:
#!   display_flash_frequency: 2  # overrides default frequency
#! lights:
#!   segment1_a:
#!     number: 1
#!   segment1_b:
#!     number: 2
#!   segment1_c:
#!     number: 3
#!   segment1_d:
#!     number: 4
#!   segment1_e:
#!     number: 5
#!   segment1_f:
#!     number: 6
#!   segment1_g:
#!     number: 7
#!   segment2_a:
#!     number: 8
#!   segment2_b:
#!     number: 9
#!   segment2_c:
#!     number: 10
#!   segment2_d:
#!     number: 11
#!   segment2_e:
#!     number: 12
#!   segment2_f:
#!     number: 13
#!   segment2_g:
#!     number: 14
segment_displays:
  display1:
    number: 1
    platform_settings:
      lights:
        - a: segment1_a
          b: segment1_b
          c: segment1_c
          d: segment1_d
          e: segment1_e
          f: segment1_f
          g: segment1_g
        - a: segment2_a
          b: segment2_b
          c: segment2_c
          d: segment2_d
          e: segment2_e
          f: segment2_f
          g: segment2_g
      type: 7segment
```

## type:

Single value, type: one of the following options: 7segment, bcd,
14segment, 16segment.

The type of your hardware segment display. This is used to calculate the
mapping from text to segment.

The mapping is different per type:
