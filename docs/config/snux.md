---
title: "snux: Config Reference"
---

# snux: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `snux:` section of your config is where you configure the
[snux platform](../hardware/snux.md).

This is an example:

``` yaml
hardware:
  platform: virtual    # use your platform here
  driverboards: wpc
  coils: snux
  switches: snux
system11:
  ac_relay_delay_ms: 75
  ac_relay_driver: c_ac_relay
snux:
  diag_led_driver: c_diag_led_driver
coils:
  c_diag_led_driver:
    number: c24
    default_hold_power: 1.0
  c_flipper_enable_driver:
    number: c23
    default_hold_power: 1.0
  c_ac_relay:
    number: c25
    default_hold_power: 1.0
  c_side_a1:
    number: c11a
  c_side_a2:
    number: c12a
    default_hold_power: 0.5
  c_side_c1:
    number: c11c
  c_side_c2:
    number: c12c
    default_hold_power: 0.5
  c_flipper_left_main:
    number: FLLM
  c_flipper_left_hold:
    number: FLLH
    allow_enable: true

switches:
  s_flipper_left:
    number: sf01
  s_test:
    number: s77

flippers:
  f_test_single:
    main_coil: c_flipper_left_main
    hold_coil: c_flipper_left_hold
    activation_switch: s_flipper_left
```

## Required settings

The following sections are required in the `snux:` section of your
config:

### diag_led_driver:

Single value, type: `string` name of a [coils:](coils.md) device. Defaults to empty.

The coil to use to drive the diag LED on the snux board. This is usually
driver 23 on the Snux board.

## Optional settings

The following sections are optional in the `snux:` section of your
config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

## Related How To guides

[WPC Platform](../machines/wpc.md) to connect to the
[SNUX board](../hardware/snux.md).
