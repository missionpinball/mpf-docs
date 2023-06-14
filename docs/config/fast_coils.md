---
title: "fast_coils:"
---

# fast_coils:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `fast_coils:` section of your config is where you configure platform
specific settings for coils in the FAST platform.

## Optional settings

The following sections are optional in the `fast_coils:` section of your
config. (If you don't include them, the default will be used).

### connection:

Single value, type: one of the following options: network, local, auto.
Default: `auto`

How is your coil connected? For WPC this might be `local` otherwise
`network`.

### recycle_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)).

The cooldown time of a coil after each pulse. Any pulse during that time
will be ignored to prevent overheating the coil.

## Related How To guides

* [How to configure MPF for FAST Pinball hardware](../hardware/fast/index.md)
