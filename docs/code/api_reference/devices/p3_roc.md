# p3_roc API Reference

`self.machine.hardware_platforms['p3_roc']`

``` python
class mpf.platforms.p3_roc.P3RocHardwarePlatform(machine)
```

Bases: `mpf.platforms.p_roc_common.PROCBasePlatform`, `mpf.core.platform.I2cPlatform`, `mpf.core.platform.AccelerometerPlatform`

Platform class for the P3-ROC hardware controller.

Parameters:

* **machine** – The MachineController instance.

## Accessing the p3_roc platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the p3_roc platform is available via `self.machine.hardware_platforms['p3_roc']`.

## Methods & Attributes

The p3_roc platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_accelerometer(number, config, callback)`

Configure the accelerometer on the P3-ROC.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Create a P3-ROC driver.

Typically drivers are coils or flashers, but for the P3-ROC this is also used for matrix-based lights.

Parameters:

* **config** – Dictionary of settings for the driver.
* **number** – Number of this driver.
* **platform_settings** – Platform specific settings

Returns a reference to the PROCDriver object which is the actual object you can use to pulse(), patter(), enable(), etc.

`configure_i2c(number: str)`

Configure I2C device on P3-Roc.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure a P3-ROC switch.

Parameters:

* **number** – Number of this switch
* **config** – Dictionary of settings for the switch.
* **platform_config** – Platform specific settings.

Returns: A configured switch object.

`connect()`

Connect to the P3-Roc.

`get_hw_switch_states() → Dict[str, bool]`

Read in and set the initial switch state.

The P-ROC uses the following values for hw switch states: 1 - closed (debounced) 2 - open (debounced) 3 - closed (not debounced) 4 - open (not debounced)

`get_info_string()`

Dump infos about boards.

`process_events(events)`

Process events from the P3-Roc.

`classmethod scale_accelerometer_to_g(raw_value)`

Convert internal representation to g.

`set_gpio(index, state)`

Set GPIO state.

`start()`

Start GPIO poller.

`stop()`

Stop platform.
