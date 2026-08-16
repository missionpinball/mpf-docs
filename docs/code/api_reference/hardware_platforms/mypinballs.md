---
title: API Reference - mypinballs
---

# mypinballs API Reference

Config Reference:

* [mypinballs:](../../../config/mypinballs.md)

`self.machine.hardware_platforms['mypinballs']`

``` python
class mpf.platforms.mypinballs.mypinballs.MyPinballsHardwarePlatform(machine)
```

Bases: `mpf.core.platform.SegmentDisplayPlatform`

Hardware platform for MyPinballs 7-segment controller.

## Accessing the mypinballs platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the mypinballs platform is available via `self.machine.hardware_platforms['mypinballs']`.

## Methods & Attributes

The mypinballs platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_segment_display(number: str, platform_settings) → mpf.platforms.interfaces.segment_display_platform_interface.SegmentDisplayPlatformInterface`

Configure display.

`initialize()`

Initialise hardware.

`send_cmd(cmd: bytes)`

Send a byte command.

`stop()`

Stop platform.
