# opp API Reference

Config Reference:

* [opp:](../../../config/opp.md)

`self.machine.hardware_platforms['opp']`

``` python
class mpf.platforms.opp.opp.OppHardwarePlatform(machine)
```

Bases: `mpf.core.platform.LightsPlatform`, `mpf.core.platform.SwitchPlatform`, `mpf.core.platform.DriverPlatform`

Platform class for the OPP hardware.

Parameters:

* **machine** – The main MachineController instance.

## Accessing the opp platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the opp platform is available via `self.machine.hardware_platforms['opp']`.

## Methods & Attributes

The opp platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Clear a hardware rule.

This is used if you want to remove the linkage between a switch and some driver activity. For example, if you wanted to disable your flippers (so that a player pushing the flipper buttons wouldn't cause the flippers to flip), you'd call this method with your flipper button as the sw_num.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Configure a driver.

Parameters:

* **config** – Config dict.
* **number** – Number of this driver.
* **platform_settings** – Platform specific settings.

`configure_light(number, subtype, platform_settings)`

Configure a led or matrix light.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure a switch.

Parameters:

* **number** – Number of this switch.
* **config** – Config dict.
* **platform_config** – Platform specific settings.

`static eom_resp(chain_serial, msg)`

Process an EOM.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`classmethod get_coil_config_section()`

Return coil config section.

`get_gen2_cfg_resp(chain_serial, msg)`

Process cfg response.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`get_hw_switch_states()`

Get initial hardware switch states.

This changes switches from active low to active high

`get_info_string()`

Dump infos about boards.

`initialize()`

Initialise connections to OPP hardware.

`inv_resp(chain_serial, msg)`

Parse inventory response.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse number and subtype to channel.

`process_received_message(chain_serial, msg)`

Send an incoming message from the OPP hardware to the proper method for servicing.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`read_gen2_inp_resp(chain_serial, msg)`

Read switch changes.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`read_gen2_inp_resp_initial(chain_serial, msg)`

Read initial switch states.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`read_matrix_inp_resp(chain_serial, msg)`

Read matrix switch changes.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`read_matrix_inp_resp_initial(chain_serial, msg)`

Read initial matrix switch states.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.

`register_processor_connection(serial_number, communicator)`

Register the processors to the platform.

Parameters:

* **serial_number** – Serial number of chain.
* **communicator** – Instance of OPPSerialCommunicator

`send_to_processor(chain_serial, msg)`

Send message to processor with specific serial number.

Parameters:

* **chain_serial** – Serial of the processor.
* **msg** – Message to send.

`set_delayed_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, delay_ms: int)`

Set pulse on hit and release rule to driver.

When a switch is hit and a certain delay passed it pulses a driver. When the switch is released the pulse continues. Typically used for kickbacks.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and enable and release and disable rule on driver.

Pulses a driver when a switch is hit. Then enables the driver (may be with pwm). When the switch is released the pulse is canceled and the driver becomes disabled. When the eos_switch is hit the pulse is canceled and the driver becomes enabled (likely with PWM). Typically used on the coil for single-wound coil flippers with eos switch.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and enable and relase rule on driver.

Pulses a driver when a switch is hit. Then enables the driver (may be with pwm). When the switch is released the pulse is canceled and the driver gets disabled. Typically used for single coil flippers.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and release and disable rule on driver.

Pulses a driver when a switch is hit. Then enables the driver (may be with pwm). When the switch is released the pulse is canceled and the driver gets disabled. When the second disable_switch is hit the pulse is canceled and the driver gets disabled. Typically used on the main coil for dual coil flippers with eos switch.

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and release rule to driver.

Pulses a driver when a switch is hit. When the switch is released the pulse is canceled. Typically used on the main coil for dual coil flippers without eos switch.

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit rule on driver.

Pulses a driver when a switch is hit. When the switch is released the pulse continues. Typically used for autofire coils such as pop bumpers.

`start()`

Start polling and listening for commands.

`stop()`

Stop hardware and close connections.

`update_incand()`

Update all the incandescents connected to OPP hardware.

This is done once per game loop if changes have been made.

It is currently assumed that the UART oversampling will guarantee proper communication with the boards. If this does not end up being the case, this will be changed to update all the incandescents each loop.

`vers_resp(chain_serial, msg)`

Process version response.

Parameters:

* **chain_serial** – Serial of the chain which received the message.
* **msg** – Message to parse.
