---
title: "switch_overwrites: Config Reference"
---

# switch_overwrites: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Some devices offer a `switch_overwrites:` setting where you can
overwrite settings of a switch used in that devices. This is commonly
used in [switches](flippers.md) and
[switches](autofire_coils.md).

## Optional settings

The following sections are optional in the `switch_overwrites:` section
of your config. (If you don't include them, the default will be used).

### debounce:

Single value, type: one of the following options: quick, normal, None.
Default: `None`

Overwrite the `debounce` setting on a coil. See `debounce` in
[switches:](switches.md) for details.

## Related How To guides

* [Switches](../mechs/switches/index.md)
