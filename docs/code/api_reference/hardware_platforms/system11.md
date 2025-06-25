
# self.machine.hardware_platforms[‘system11’]

``` python
class mpf.platforms.system11.System11OverlayPlatform(machine: mpf.core.machine.MachineController)
```

Bases: `mpf.core.platform.DriverPlatform, mpf.core.platform.SwitchPlatform`

Overlay platform to drive system11 machines using a WPC controller.

## Accessing the system11 platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the system11 platform is available via `self.machine.hardware_platforms['system11']`.

## Methods & Attributes

The system11 platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`a_side_active`

Return if A side cannot be switches off right away.

`a_side_busy`

Return if A side cannot be switches off right away.

`c_side_active`

Return if C side cannot be switches off right away.

`c_side_busy`

Return if C side cannot be switches off right away.

`clear_hw_rule(switch, coil)`

Clear a rule for a driver on the system11 overlay.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Configure a driver on the system11 overlay.

Parameters:

* **config** – Driver config dict
* **number** – Number of the driver.
* **platform_settings** – Platform specific config.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure switch on system11 overlay.

`driver_action(driver, pulse_settings: Optional[mpf.platforms.interfaces.driver_platform_interface.PulseSettings], hold_settings: Optional[mpf.platforms.interfaces.driver_platform_interface.HoldSettings], side: str)`

Add a driver action for a switched driver to the queue (for either the A-side or C-side queue).

Parameters:

* **driver** – A reference to the original platform class Driver instance.
* **pulse_settings** – Settings for the pulse or None
* **hold_settings** – Settings for hold or None
* **side** – Whatever the driver is on A or C side.

This action will be serviced immediately if it can, or ASAP otherwise.

`get_hw_switch_states()`

Get initial hardware state.

`initialize()`

Automatically called by the Platform class after all the core modules are loaded.

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Configure a rule for a driver on the system11 overlay.

Will pass the call onto the parent platform if the driver is not on A/C relay.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch, coil)`

Configure a rule for a driver on the system11 overlay.

Will pass the call onto the parent platform if the driver is not on A/C relay.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Configure a rule for a driver on the system11 overlay.

Will pass the call onto the parent platform if the driver is not on A/C relay.

`set_pulse_on_hit_and_release_rule(enable_switch, coil)`

Configure a rule for a driver on the system11 overlay.

Will pass the call onto the parent platform if the driver is not on A/C relay.

`set_pulse_on_hit_rule(enable_switch, coil)`

Configure a rule on the system11 overlay.

Will pass the call onto the parent platform if the driver is not on A/C relay.

`stop()`

Stop the overlay. Nothing to do here because stop is also called on parent platform.

`tick()`

System11 main loop.

Called based on the timer_tick event.

`validate_coil_section(driver, config)`

Validate coil config for platform.
