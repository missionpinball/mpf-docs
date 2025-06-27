---
title: "trinamics_steprocker: Config Reference"
---

# trinamics_steprocker: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `trinamics_steprocker:` section of your config is where you
configure the
[trinamics steprocker platform](../hardware/trinamics.md).

## Required settings

The following sections are required in the `trinamics_steprocker:`
section of your config:

### port:

Single value, type: `string`. Defaults to empty.

Serial port to use to connect to the steprocker.

## Related How To guides

* [Trinamic's StepRocker](../hardware/trinamics.md)
