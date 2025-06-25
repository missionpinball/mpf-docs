
# TestMachineController

`class mpf.tests.MpfTestCase.TestMachineController(options, config, config_patches, config_defaults, clock, mock_data, enable_plugins=False)`

Bases: `mpf.core.machine.MachineController`

A patched version of the MachineController used in tests.

The TestMachineController has a few changes from the regular machine controller to facilitate running unit tests, including:

* Use the TestDataManager instead of the real one.
* Use a test clock which we can manually advance instead of the regular clock tied to real-world time.
* Only load plugins if self._enable_plugins is True.
* Merge any test_config_patches into the machine config.
* Disabled the config file caching to always load the config from disk.

## Methods & Attributes

The TestMachineController has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`add_crash_handler(handler: Callable)`

Add a crash handler which is called on a crash.

This can be used to restore the output and prepare logging.

`add_platform(name: str) → None`

Make an additional hardware platform interface available to MPF.

Parameters:

* **name** – String name of the platform to add. Must match the name of a platform file in the mpf/platforms folder (without the .py extension).

`clear_boot_hold(hold: str) → None`

Clear a boot hold.

`create_data_manager(config_name)`

Create TestDataManager.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_platform_sections(platform_section: str, overwrite: str) → SmartVirtualHardwarePlatform`

Return platform section.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`init_done() → None`

Finish init.

Called when init is done and all boot holds are cleared.

`initialise() → None`

Initialise machine.

`initialise_core_and_hardware() → None`

Load core modules and hardware.

`initialise_mpf()`

Initialise MPF.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`register_boot_hold(hold: str) → None`

Register a boot hold.

`register_monitor(monitor_class: str, monitor: Callable[[...], Any]) → None`

Register a monitor.

Parameters:

* **monitor_class** – String name of the monitor class for this monitor that’s being registered.
* **monitor** – Callback to notify

MPF uses monitors to allow components to monitor certain internal elements of MPF.

For example, a player variable monitor could be setup to be notified of any changes to a player variable, or a switch monitor could be used to allow a plugin to be notified of any changes to any switches.

The MachineController’s list of registered monitors doesn’t actually do anything. Rather it’s a dictionary of sets which the monitors themselves can reference when they need to do something. We just needed a central registry of monitors.

`reset() → None`

Reset the machine.

This method is safe to call. It essentially sets up everything from scratch without reloading the config files and assets from disk. This method is called after a game ends and before attract mode begins.

`run() → None`

Start the main machine run loop.

`set_default_platform(name: str) → None`

Set the default platform.

It is used if a device class-specific or device-specific platform is not specified.

Parameters:

* **name** – String name of the platform to set to default.

`shutdown() → None`

Shutdown the machine.

`stop(reason=None, **kwargs) → None`

Perform a graceful exit of MPF.

`validate_machine_config_section(section: str) → None`

Validate a config section.

`verify_system_info()`

Dump information about the Python installation to the log.

Information includes Python version, Python executable, platform, and core architecture.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.
