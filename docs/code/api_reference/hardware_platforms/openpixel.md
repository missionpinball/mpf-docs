---
title: API Reference - openpixel
---

# openpixel API Reference

Config Reference:

* [open_pixel_control:](../../../config/open_pixel_control.md)

`self.machine.hardware_platforms['openpixel']`

``` python
class mpf.platforms.openpixel.OpenpixelHardwarePlatform(machine: MachineController)
```

Bases: `mpf.core.platform.LightsPlatform`

Base class for the open pixel hardware platform.

Parameters:

* **machine** – The main MachineController object.

## Accessing the openpixel platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the openpixel platform is available via `self.machine.hardware_platforms['openpixel']`.

## Methods & Attributes

The openpixel platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_light(number, subtype, platform_settings) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure an LED.

`initialize()`

Initialise openpixel platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse number to three channels.

`stop()`

Stop platform.
