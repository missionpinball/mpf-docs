---
title: "open_pixel_control: Config Reference"
---

# open_pixel_control: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `open_pixel_control:` section of your config is where you configure
a openpixel light controller. This is usually used together with a
[fadecandy](../hardware/fadecandy/index.md)
but can also be used standalone. Usually, you don't have to change
anything.

## Optional settings

The following sections are optional in the `open_pixel_control:` section
of your config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see more debug log lines.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### host:

Single value, type: `string`. Default: `localhost`

Hostname of the openpixel server to connect.

### port:

Single value, type: `integer`. Default: `7890`

Port of the openpixel server to connect.

## Related How To guides

* [How to configure a FadeCandy RGB LED Controller](../hardware/fadecandy/index.md)
