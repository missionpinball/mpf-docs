# p_roc API Reference

`self.machine.hardware_platforms['p_roc']`

``` python
class mpf.platforms.p_roc.PRocHardwarePlatform(machine)
```

Bases: `mpf.platforms.p_roc_common.PROCBasePlatform`, `mpf.core.platform.DmdPlatform`, `mpf.core.platform.SegmentDisplayPlatform`

Platform class for the P-ROC hardware controller.

Parameters:

* **machine** – The MachineController instance.

## Accessing the p_roc platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the p_roc platform is available via `self.machine.hardware_platforms['p_roc']`.

## Methods & Attributes

The p_roc platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_dmd()`

Configure a hardware DMD connected to a classic P-ROC.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict)`

Create a P-ROC driver.

Typically drivers are coils or flashers, but for the P-ROC this is also used for matrix-based lights.

Parameters:

* **config** – Dictionary of settings for the driver.
* **number** – Number of this driver
* **platform_settings** – Platform specific setting for this driver.

Returns a reference to the PROCDriver object which is the actual object you can use to pulse(), patter(), enable(), etc.

`configure_segment_display(number: str, platform_settings) → mpf.platforms.interfaces.segment_display_platform_interface.SegmentDisplayPlatformInterface`

Configure display.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict)`

Configure a P-ROC switch.

Parameters:

* **number** – String number of the switch to configure.
* **config** – SwitchConfig settings.
* **platform_config** – Platform specific settings.

Returns: A configured switch object.

`connect()`

Connect to the P-Roc.

`get_hw_switch_states() → Dict[str, bool]`

Read in and set the initial switch state.

The P-ROC uses the following values for hw switch states: 1 - closed (debounced) 2 - open (debounced) 3 - closed (not debounced) 4 - open (not debounced)

`get_info_string()`

Dump infos about boards.

`process_events(events)`

Process events from the P-Roc.
