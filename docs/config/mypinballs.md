---
title: "mypinballs:"
---

# mypinballs:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `mypinballs:` section of your config is where your mypinballs
segment display controller. See
[MyPinballs Segment Display Controller](../hardware/mypinballs/index.md) for details.

## Required settings

The following sections are required in the `mypinballs:` section of your
config:

### port:

Single value, type: `string`. Defaults to empty.

Serial port to use.

## Optional settings

The following sections are optional in the `mypinballs:` section of your
config. (If you don't include them, the default will be used).

### baud:

Single value, type: `integer`. Default: `115200`

Baud rate to use on the serial port.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set to true to see more debug output.

## Related How To guides

* [MyPinballs Segment Display Controller](../hardware/mypinballs/index.md)
