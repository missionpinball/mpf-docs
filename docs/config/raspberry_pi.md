---
title: "raspberry_pi:"
---

# raspberry_pi:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `raspberry_pi:` section of your config is where you configure your
Raspberry Pi running pigpio. See [Raspberry PI (pigpio)](../hardware/rpi.md) for details.

This is an example:

``` yaml
raspberry_pi:
  ip: localhost
  port: 8888
```

## Required settings

The following sections are required in the `raspberry_pi:` section of
your config:

### ip:

Single value, type: `string`. Defaults to empty.

IP of your Raspberry Pi. MPF will connect to this IP. Hostname does not
work here.

## Optional settings

The following sections are optional in the `raspberry_pi:` section of
your config. (If you don't include them, the default will be used).

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this platform.

### port:

Single value, type: `integer`. Default: `8888`

Port of the pigpio daemon on your Raspberry Pi (in case you change it).

## Related How To guides

* [Raspberry PI (pigpio)](../hardware/rpi.md)
