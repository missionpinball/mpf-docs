---
title: fast_firmware_update:
---

# fast_firmware_update:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `firmware_updates:` section of your `fast:` config is where you list
all your firmware images. Those can then be installed using
[mpf hardware firmware_update](../running/commands/hardware.md).

## Required settings

The following sections are required in the `fast_firmware_update:`
section of your config:

### file:

Single value, type: `string`.

The path of your firmware file.

### type:

Single value, type: one of the following options: net, rgb.

For which CPU is this firmware file?

### version:

Single value, type: `string`.

The exact version of the firmware. MPF will check that if this is higher
than the installed version reported by the FAST CPU.

## Related How To guides

* [How to configure MPF for FAST Pinball hardware](../hardware/fast/index.md)
