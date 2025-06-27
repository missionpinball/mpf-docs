---
title: "smartmatrix: Config Reference"
---

# smartmatrix: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `smartmatrix:` section of your config is where you configure RGB DMD
devices.

This is an example:

``` yaml
#config_version=5
hardware:
  rgb_dmd: smartmatrix
smartmatrix:
  my_smartmatrix:
    port: com4
    baud: 4000000
displays:
  dmd:
    width: 128
    height: 32
rgb_dmds:
  my_smartmatrix:
    hardware_brightness: .5
```

## Required settings

The following sections are required in the `smartmatrix:` section of
your config:

### baud:

Single value, type: `integer`. Defaults to empty.

Baud rate of your serial port. Depends on the smartmatrix firmware.

### port:

Single value, type: `string`. Defaults to empty.

Name of the serial port of your smartmatrix device. This will be
`comX` on Windows. On Linux and Mac it depends on the
usb-serial chip (usually /dev/ttyUSBX on linux or /dev/tty.usbmodemYYY
on Mac).

## Optional settings

The following sections are optional in the `smartmatrix:` section of
your config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

--8<-- "todo.md"

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

--8<-- "todo.md"

### old_cookie:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set to true to use the old cookie. Will use the new cookie by default.

## Related How To guides

* [How to configure a "SmartMatrix" RGB LED DMD](../hardware/smartmatrix.md)
