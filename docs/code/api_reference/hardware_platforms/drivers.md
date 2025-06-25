
# self.machine.hardware_platforms[‘drivers’]

``` python
class mpf.platforms.driver_light_platform.DriverLightPlatform(machine)
```

Bases: `mpf.core.platform.LightsPlatform`

Lights on drivers.

## Accessing the drivers platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms dictionary`, so the drivers platform is available via `self.machine.hardware_platforms['drivers']`.

## Methods & Attributes

The drivers platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_light(number: str, subtype: str, platform_settings: dict) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure a light on a driver.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse number.

`stop()`

Stop all fades.
