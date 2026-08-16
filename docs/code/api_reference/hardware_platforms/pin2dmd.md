---
title: API Reference - pin2dmd
---

# pin2dmd API Reference

Config Reference:

* [pin2dmd:](../../../config/pin2dmd.md)

`self.machine.hardware_platforms['pin2dmd']`

``` python
class mpf.platforms.pin2dmd.Pin2DmdHardwarePlatform(machine)
```

Bases: `mpf.core.platform.RgbDmdPlatform`

PIN2DMD RGB DMD hardware.

## Accessing the pin2dmd platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the pin2dmd platform is available via `self.machine.hardware_platforms['pin2dmd']`.

## Methods & Attributes

The pin2dmd platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_rgb_dmd(name: str)`

Configure rgb dmd.

`initialize()`

Initialise platform.

`stop()`

Stop platform.
