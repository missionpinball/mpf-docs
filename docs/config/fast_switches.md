---
title: fast_switches:
---

# fast_switches:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `fast_switches:` section of your config is where you configure
platform specific details about switches when using
[fast hardware](../hardware/fast/index.md).

``` mpf-config
switches:
  some_switch:
    number:
    platform_settings:
      debounce_close: 2ms
      debounce_open: 4ms
```

Please make sure to read [Debouncing in Pinball Machines](../mechs/switches/debounce.md) before changing those times.

## Optional settings

The following sections are optional in the `fast_switches:` section of
your config. (If you don't include them, the default will be used).

### debounce_close:

Single value, type: `string`.

Set the switch debounce time for closing the switch.

### debounce_open:

Single value, type: `string`.

Set the switch debounce time for opening the switch.

## Related How To guides

* [How to configure MPF for FAST Pinball hardware](../hardware/fast/index.md)
