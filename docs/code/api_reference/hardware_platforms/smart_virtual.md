# smart_virtual API Reference

`self.machine.hardware_platforms['smart_virtual']`

``` python
class mpf.platforms.smart_virtual.SmartVirtualHardwarePlatform(machine)
```

Bases: `mpf.platforms.virtual.VirtualHardwarePlatform`

Base class for the smart_virtual hardware platform.

## Accessing the smart_virtual platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the smart_virtual platform is available via `self.machine.hardware_platforms['smart_virtual']`.

## Methods & Attributes

The smart_virtual platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_ball_to_device(device: mpf.devices.ball_device.ball_device.BallDevice)`

Add ball to device.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Configure driver.

`start()`

Initialise platform when all devices are ready.
