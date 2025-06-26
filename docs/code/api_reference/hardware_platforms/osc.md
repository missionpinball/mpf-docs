# osc API Reference

`self.machine.hardware_platforms['osc']`

``` python
class mpf.platforms.osc.OscPlatform(machine)
```

Bases: `mpf.core.platform.LightsPlatform`, `mpf.core.platform.SwitchPlatform`

A platform to control lights via OSC.

## Accessing the osc platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms dictionary`, so the osc platform is available via `self.machine.hardware_platforms['osc']`.

## Methods & Attributes

The osc platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_light(number: str, subtype: str, platform_settings: dict) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure an OSC light.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.interfaces.switch_platform_interface.SwitchPlatformInterface`

Config an OSC switch.

`get_hw_switch_states() → Dict[str, bool]`

Return all switches as false.

`initialize()`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse light number to three RGB channels.

`stop()`

Stop server.
