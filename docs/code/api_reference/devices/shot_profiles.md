---
title: API Reference - shot_profiles
---

# shot_profiles API Reference

Config Reference:

* [shot_profiles:](../../../config/shot_profiles.md)

`self.machine.shot_profiles.*`

``` python
class mpf.devices.shot_profile.ShotProfile(machine: mpf.core.machine.MachineController, name: str)
```

Bases: `mpf.core.mode_device.ModeDevice`, `mpf.core.system_wide_device.SystemWideDevice`

A shot profile.

## Accessing shot_profiles in code

The device collection which contains the shot_profiles in your machine is available via `self.machine.shot_profiles`. For example, to access one called “foo”, you would use `self.machine.shot_profiles.foo`. You can also access shot_profiles in dictionary form, e.g. `self.machine.shot_profiles['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Shot_profiles have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enable() → None`

Enable handler.

`event_enable(**kwargs)`

Event handler for enable event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.
