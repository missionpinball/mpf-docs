---
title: "coil_overwrites:"
---

# coil_overwrites:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Some devices offer one or multiple `coil_overwrites:` settings where you
can overwrite coil settings.

Most commonly this is used in [flippers:](flippers.md)
and [autofire_coils:](autofire_coils.md).

## Optional settings

The following sections are optional in the `coil_overwrites:` section of
your config. (If you don't include them, the default will be used).

### hold_power:

Single value, type: float(0,1).

Overwrite the `hold_power` of the coil for this device. See
`default_hold_power` in [coils:](coils.md) for
details.

### pulse_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)).

Overwrite the `pulse_ms` of the coil for this device. See
`default_pulse_ms` in [coils:](coils.md) for details.

### pulse_power:

Single value, type: float(0,1).

Overwrite the `pulse_power` of the coil for this device. See
`default_pulse_power` in [coils:](coils.md) for
details.

### recycle:

Single value, type: `boolean` (Yes/No or True/False).

Overwrite the `recycle` setting of the coil for this device. See
`recycle` in [coils:](coils.md) for details.

## Related How To guides

* [flippers:](flippers.md)
* [kickbacks:](kickbacks.md)
* [autofire_coils:](autofire_coils.md)
