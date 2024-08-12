
# self.machine.hardware_platforms[‘lisy’]

`class mpf.platforms.lisy.lisy.LisyHardwarePlatform(machine)`

Bases: mpf.core.platform.SwitchPlatform, mpf.core.platform.LightsPlatform, mpf.core.platform.DriverPlatform, mpf.core.platform.SegmentDisplaySoftwareFlashPlatform, mpf.core.platform.HardwareSoundPlatform, mpf.core.logging.LogMixin

LISY platform.

## Accessing the lisy platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the lisy platform is available via `self.machine.hardware_platforms['lisy']`.

## Methods & Attributes

The lisy platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Clear hw rule for driver.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict) → mpf.platforms.interfaces.driver_platform_interface.DriverPlatformInterface`

Configure a driver.

`configure_hardware_sound_system() → mpf.platforms.interfaces.hardware_sound_platform_interface.HardwareSoundPlatformInterface`

Configure hardware sound.

`configure_light(number: str, subtype: str, platform_settings: dict) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure light on LISY.

`configure_segment_display(number: str, platform_settings) → mpf.platforms.interfaces.segment_display_platform_interface.SegmentDisplaySoftwareFlashPlatformInterface`

Configure a segment display.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.interfaces.switch_platform_interface.SwitchPlatformInterface`

Configure a switch.

`get_hw_switch_states()`

Return current switch states.

`get_info_string()`

Dump infos about LISY platform.

`initialize()`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Return a single light.

`send_byte(cmd: int, byte: bytes = None)`

Send a command with optional payload.

`send_byte_and_read_response(cmd: int, byte: bytes = None, read_bytes=0)`

Send byte and read response.

`send_string(cmd: int, string: str)`

Send a command with null terminated string.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and enable and release and disable rule on driver.

Pulses a driver when a switch is hit. Then enables the driver (may be with pwm). When the switch is released the pulse is canceled and the driver becomes disabled. When the eos_switch is hit the pulse is canceled and the driver becomes enabled (likely with PWM). Typically used on the coil for single-wound coil flippers with eos switch.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and enable and release rule on driver.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and enable and release and disable rule on driver.

Pulses a driver when a switch is hit. When the switch is released the pulse is canceled and the driver gets disabled. When the eos_switch is hit the pulse is canceled and the driver becomes disabled. Typically used on the main coil for dual-wound coil flippers with eos switch.

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and release rule to driver.

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit rule on driver.

`start()`

Start reading switch changes.

`stop()`

Stop platform.

