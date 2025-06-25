
# self.machine.hardware_platforms[‘spike’]

``` python
class mpf.platforms.spike.spike.SpikePlatform(machine)
```

Bases: `mpf.core.platform.SwitchPlatform`, `mpf.core.platform.LightsPlatform`, `mpf.core.platform.DriverPlatform`, `mpf.core.platform.DmdPlatform`, `mpf.core.platform.StepperPlatform`

Stern Spike Platform.

## Accessing the spike platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the spike platform is available via `self.machine.hardware_platforms['spike']`.

## Methods & Attributes

The spike platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch, coil)`

Disable hardware rule for this coil.

`configure_dmd()`

Configure a DMD.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Configure a driver on Stern Spike.

`configure_light(number, subtype, platform_settings) → Union[mpf.platforms.spike.spike.SpikeLight, mpf.platforms.spike.spike.SpikeBacklight]`

Configure a light on Stern Spike.

`configure_stepper(number: str, config: dict) → mpf.platforms.interfaces.stepper_platform_interface.StepperPlatformInterface`

Configure a stepper in Spike.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure switch on Stern Spike.

`get_hw_switch_states()`

Return current switch states.

`classmethod get_stepper_config_section()`

Return config validator name.

`classmethod get_switch_config_section()`

Return switch config section.

`initialize()`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Return a single light.

`send_cmd_and_wait_for_response(node, cmd, data, response_len) → Optional[bytearray]`

Send cmd and wait for response.

`send_cmd_async(node, cmd, data)`

Send cmd which does not require a response.

`send_cmd_raw(data, wait_ms=0)`

Send raw command.

`send_cmd_raw_async(data, wait_ms=0)`

Send raw cmd which does not require a response.

`send_cmd_sync(node, cmd, data)`

Send cmd which does not require a response.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and release rule to driver.

Used for high-power coil on single-wound flippers. Example from GoT: Node: 8 Command CoilSetReflex (0x41) Params: 0x00 0xff 0x33 0x00 0x1e 0x28 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x42 0x00 0x00 0x40 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x06 0x00 Len: 36

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and enable and release rule on driver.

Used for single coil flippers. Examples from WWE: Dual-wound flipper hold coil: Type: 8 Cmd: 65 Node: 8 Msg: 0x02 0xff 0x46 0x01 0xff 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x3a 0x00 0x42 0x40 0x00 0x00 0x01 0x00 Len: 25

Ring Slings (different flags): Type: 8 Cmd: 65 Node: 10 Msg: 0x00 0xff 0x19 0x00 0x14 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x80 0x00 0x4a 0x40 0x00 0x00 0x06 0x05 Len: 25

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and release rule to driver.

Used for high-power coil on dual-wound flippers. Example from WWE: Type: 8 Cmd: 65 Node: 8 Msg: 0x00 0xff 0x33 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x42 0x40 0x00 0x02 0x06 0x00 Len: 25

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and release rule to driver.

I believe that param2 == 1 means that it will cancel the pulse when the switch is released.

Used for high-power coils on dual-wound flippers. Example from WWE: Type: 8 Cmd: 65 Node: 8 Msg: 0x03 0xff 0x46 0x01 0xff 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x43 0x40 0x00 0x00 0x01 0x00 Len: 25

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit rule on driver.

This is mostly used for popbumpers. Example from WWE: Type: 8 Cmd: 65 Node: 9 Msg: 0x00 0xa6 0x28 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x14 0x00 0x00 0x00 0x38 0x00 0x40 0x00 0x00 0x00 0x00 0x00 Len: 25

`stop()`

Stop hardware and close connections.
