---
title: API Reference - mode_controller
---

# mode_controller API Reference

`self.machine.mode_controller`

``` python
class mpf.core.mode_controller.ModeController(machine: mpf.core.machine.MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

Responsible for loading, unloading, and managing all modes in MPF.

## Accessing the mode_controller in code

There is only one instance of the mode_controller in MPF, and it's accessible via self.machine.mode_controller.

## Methods & Attributes

The mode_controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`create_mode_devices()`

Create mode devices.

`dump()`

Dump the current status of the running modes to the log file.

`initialise_modes(**kwargs)`

Initialise modes.

`is_active(mode_name) → bool`

Return true if the mode is active, False if it is not.

Parameters:

* **mode_name** – String name of the mode to check.

`load_mode_devices()`

Load mode devices.

`load_modes(**kwargs)`

Load the modes from the modes: section of the machine configuration file.

`register_load_method(load_method, config_section_name=None, priority=0, **kwargs)`

Register a method which is called when the mode is loaded. Used by core components, plugins, etc. to register themselves with the Mode Controller for anything they need a mode to do when it's registered.

Parameters:

* **load_method** – The method that will be called when this mode code loads.
* **config_section_name** – An optional string for the section of the configuration file that will be passed to the load_method when it's called.
* **priority** – Int of the relative priority which allows remote methods to be called in a specific order. Default is 0. Higher values will be called first.
* ****kwargs** – Any additional keyword arguments specified will be passed to the load_method.

Note that these methods will be called once, when the mode code is first initialized during the MPF boot process.

`register_start_method(start_method, config_section_name=None, priority=0, **kwargs)`

Register a method which is called anytime a mode is started. Used by core components, plugins, etc. to register themselves with the Mode Controller for anything that they a mode to do when it starts.

Parameters:

* **start_method** – The method that will be called when this mode code loads.
* **config_section_name** – An optional string for the section of the configuration file that will be passed to the start_method when it's called.
* **priority** – Int of the relative priority which allows remote methods to be called in a specific order. Default is 0. Higher values will be called first.
* ****kwargs** – Any additional keyword arguments specified will be passed to the start_method.

`remove_start_method(start_method, config_section_name=None, priority=0, **kwargs)`

Remove an existing start method.

`set_mode_state(mode: mpf.core.mode.Mode, active: bool)`

Remember mode state.
