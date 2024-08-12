
# self.machine.hardware_platforms[‘virtual_pinball’]

`class mpf.platforms.virtual_pinball.virtual_pinball.VirtualPinballPlatform(machine)`

Bases: mpf.core.platform.LightsPlatform, mpf.core.platform.SwitchPlatform, mpf.core.platform.DriverPlatform

VPX platform.

## Accessing the virtual_pinball platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the virtual_pinball platform is available via `self.machine.hardware_platforms['virtual_pinball']`.

## Methods & Attributes

The virtual_pinball platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Clear hw rule.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict) → mpf.platforms.interfaces.driver_platform_interface.DriverPlatformInterface`

Configure VPX driver.

`configure_light(number: str, subtype: str, platform_settings: dict) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure a VPX light.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.interfaces.switch_platform_interface.SwitchPlatformInterface`

Configure VPX switch.

`get_hw_switch_states()`

Return initial switch state.

`initialize()`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse channel str to a list of channels.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Pulse on hit and hold, disable on disable_switch hit.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Pulse on hit and hold.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Pulse on hit, disable on disable_switch hit.

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Pulse on hit and hold.

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Pulse on hit and release.

`vpx_changed_flashers()`

Return changed lamps since last call.

`vpx_changed_gi_strings()`

Return changed lamps since last call.

`vpx_changed_lamps()`

Return changed lamps since last call.

`vpx_changed_leds()`

Return changed lamps since last call.

`vpx_changed_solenoids()`

Return changed solenoids since last call.

`vpx_get_coilactive(number)`

Return True if a MPF hw rule for the coil(number) exists.

`vpx_get_hardwarerules()`

Return hardware rules.

`vpx_get_mech(number)`

Not implemented.

`vpx_get_switch(number)`

Return switch value.

`vpx_mech(number)`

Not implemented.

`vpx_pulsesw(number)`

Pulse switch from VPX.

`vpx_set_mech(number, value)`

Not implemented.

`vpx_set_switch(number, value)`

Update switch from VPX.

`vpx_start()`

Start machine.

`vpx_switch(number)`

Return switch value.

