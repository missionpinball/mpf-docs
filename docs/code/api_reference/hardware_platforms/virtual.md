
# self.machine.hardware_platforms[‘virtual’]

``` python
class mpf.platforms.virtual.VirtualHardwarePlatform(machine)
```

Bases: `mpf.core.platform.AccelerometerPlatform`, `mpf.core.platform.I2cPlatform`, `mpf.core.platform.ServoPlatform`, `mpf.core.platform.LightsPlatform`, `mpf.core.platform.SwitchPlatform`, `mpf.core.platform.DriverPlatform`, `mpf.core.platform.DmdPlatform`, `mpf.core.platform.RgbDmdPlatform`, `mpf.core.platform.SegmentDisplayPlatform`, `mpf.core.platform.StepperPlatform`, `mpf.core.platform.HardwareSoundPlatform`

Base class for the virtual hardware platform.

## Accessing the virtual platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the virtual platform is available via `self.machine.hardware_platforms['virtual']`.

## Methods & Attributes

The virtual platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch, coil)`

Clear hw rule.

`configure_accelerometer(number, config, callback)`

Configure accelerometer.

`configure_dmd()`

Configure DMD.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Configure driver.

`configure_hardware_sound_system() → mpf.platforms.interfaces.hardware_sound_platform_interface.HardwareSoundPlatformInterface`

Configure virtual hardware sound system.

`configure_i2c(number: str) → mpf.platforms.interfaces.i2c_platform_interface.I2cPlatformInterface`

Configure virtual i2c device.

`configure_light(number, subtype, platform_settings)`

Configure light channel.

`configure_rgb_dmd(name: str)`

Configure DMD.

`configure_segment_display(number: str, platform_settings) → mpf.platforms.interfaces.segment_display_platform_interface.SegmentDisplayPlatformInterface`

Configure segment display.

`configure_servo(number: str)`

Configure a servo device in platform.

`configure_stepper(number: str, config: dict)`

Configure a smart stepper / axis device in platform.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure switch.

`get_hw_switch_states()`

Return hw switch states.

`initialize() → None`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse channel str to a list of channels.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set rule.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch, coil)`

Set rule.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set rule.

`set_pulse_on_hit_and_release_rule(enable_switch, coil)`

Set rule.

`set_pulse_on_hit_rule(enable_switch, coil)`

Set rule.

`stop()`

Stop platform.

`validate_coil_section(driver, config)`

Validate coil sections.

`validate_stepper_section(stepper, config)`

Validate stepper sections.

`validate_switch_section(switch, config)`

Validate switch sections.
