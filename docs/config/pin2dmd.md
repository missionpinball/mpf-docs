---
title: "pin2dmd: Config Reference"
---

# pin2dmd: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `pin2dmd:` section of your config is where you configure your
[PIN2DMD RGB DMD display](../hardware/pin2dmd/index.md).

## Optional settings

The following sections are optional in the `pin2dmd:` section of your
config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### panel:

Single value, type: one of the following options: rgb, rbg. Default:
`rgb`

The order of the LEDs in your panels. If your blue and green appear to
be swapped change this.

### resolution:

Single value, type: one of the following options: 128x32, 192x64.
Default: `128x32`

The resolution of your panel. PIN2DMD XL is `192x64` and the standard
PIN2DMD is `128x32`.

## Related How To guides

* [How to configure a PIN2DMD RGB LED DMD](../hardware/pin2dmd/index.md)
