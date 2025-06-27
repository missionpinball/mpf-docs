# machine API Reference

`self.machine`

``` python
class mpf.core.machine.MachineController(options: dict, config: mpf.core.config_loader.MpfConfig)
```

Bases: `mpf.core.logging.LogMixin`

Parameters:

* **config (MpfConfig)** – The machine configuration
* **options (dict)** – A dictionary of options built from the command line options used to launch mpf.py.

## Accessing the machine controller in code

The machine controller is the main component in MPF, accessible via self.machine. See the Overview & Tour of MPF code for details.

## Methods & Attributes

The machine controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_crash_handler(handler: Callable)`

Add a crash handler which is called on a crash. This can be used to restore the output and prepare logging.

`add_platform(name: str) → None`
Make an additional hardware platform interface available to MPF.

Parameters:

* **name** – String name of the platform to add. Must match the name of a platform file in the mpf/platforms folder (without the .py extension).

`clear_boot_hold(hold: str) → None`

Clear a boot hold.

`create_data_manager(config_name: str) → mpf.core.data_manager.DataManager`

Return a new DataManager for a certain config.

Parameters:

* **config_name** – Name of the config

`get_platform_sections(platform_section: str, overwrite: str) → SmartVirtualHardwarePlatform`

Return platform section.

`init_done() → None`

Finish init. Called when init is done and all boot holds are cleared.

`initialise() → None`

Initialise machine.

`initialise_core_and_hardware() → None`

Load core modules and hardware.

`initialise_mpf()`

Initialise MPF.

`register_boot_hold(hold: str) → None`

Register a boot hold.

`register_monitor(monitor_class: str, monitor: Callable[[...], Any]) → None`

Register a monitor.

Parameters:

* **monitor_class** – String name of the monitor class for this monitor that's being registered.
* **monitor** – Callback to notify

MPF uses monitors to allow components to monitor certain internal elements of MPF. For example, a player variable monitor could be setup to be notified of any changes to a player variable, or a switch monitor could be used to allow a plugin to be notified of any changes to any switches. The MachineController's list of registered monitors doesn't actually do anything. Rather it's a dictionary of sets which the monitors themselves can reference when they need to do something. We just needed a central registry of monitors.

`reset() → None`

Reset the machine. This method is safe to call. It essentially sets up everything from scratch without reloading the config files and assets from disk. This method is called after a game ends and before attract mode begins.

`run() → None`

Start the main machine run loop.

`set_default_platform(name: str) → None`

Set the default platform. It is used if a device class-specific or device-specific platform is not specified.

Parameters:

* **name** – String name of the platform to set to default.

`shutdown() → None`

Shutdown the machine.

`stop(reason=None, **kwargs) → None`

Perform a graceful exit of MPF.

`validate_machine_config_section(section: str) → None`

Validate a config section.

`verify_system_info()`

Dump information about the Python installation to the log. Information includes Python version, Python executable, platform, and core architecture.
