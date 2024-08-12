
# Delay Manager

`class mpf.core.delays.DelayManager(machine: MachineController)`

Bases: `mpf.core.mpf_controller.MpfController`

Handles delays for one object.

By default, a machine-wide instance is created and available via self.machine.delay.

Individual modes also have Delay Managers which can be accessed in mode code via self.delay. (Delays in mode-based delay managers are automatically removed when the mode stops.)

## Methods & Attributes

The delay_manager has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`add(ms: int, callback: Callable[[...], None], name: str = None, **kwargs) → str`

Add a delay.

Parameters:

* **ms** – The number of milliseconds you want this delay to be for.
* **callback** – The method that is called when this delay ends.
* **name** – String name of this delay. This name is arbitrary and only used to identify the delay later if you want to remove or change it. If you don’t provide it, a UUID4 name will be created.
* ****kwargs** – Any other (optional) kwarg pairs you pass will be passed along as kwargs to the callback method.

Returns string name or UUID4 of the delay which you can use to remove it later.

`add_if_doesnt_exist(ms: int, callback: Callable[[...], None], name: str, **kwargs) → str`

Add a delay only if a delay with that name doesn’t exist already.

Parameters:

* **ms** – Int of the number of milliseconds you want this delay to be for.
* **callback** – The method that is called when this delay ends.
* **name** – String name of this delay. This name is arbitrary and only used to identify the delay later if you want to remove or change it.
* ****kwargs** – Any other (optional) kwarg pairs you pass will be passed along as kwargs to the callback method.

Returns string name of the delay which you can use to remove it later.

`check(delay: str) → bool`

Check to see if a delay exists.

Parameters:

* **delay** – A string of the delay you’re checking for.

Returns true if the delay exists. False otherwise.

`clear() → None`

Remove (clear) all the delays associated with this DelayManager.

`configure_logging(logger: str, console_level: str = 'basic', file_level: str = 'basic', url_base=None)`

Configure logging.

Parameters:

* **logger** – The string name of the logger to use.
* **console_level** – The level of logging for the console. Valid options are “none”, “basic”, or “full”.
* **file_level** – The level of logging for the console. Valid options are “none”, “basic”, or “full”.
* **url_base** – Base URL for docs links in exceptions.

`debug_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the debug level.

Note that whether this message shows up in the console or log file is controlled by the settings used with configure_logging().

`error_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the error level.

These messages will always be shown in the console and the log file.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`info_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the info level.

Whether this message shows up in the console or log file is controlled by the settings used with configure_logging().

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove(name: str)`

Remove a delay by name.

Removing a delay prevents the callback from being called and cancels the delay.

Parameters:

* **name** – String name of the delay you want to remove. If there is no delay with this name, that’s ok. Nothing happens.

`reset(ms: int, callback: Callable[[...], None], name: str, **kwargs) → str`

Reset a delay.

Resetting will first delete the existing delay (if it exists) and then add new delay with the new settings. If the delay does not exist, that’s ok, and this method is essentially the same as just adding a delay with this name.

Parameters:

* **ms** – The number of milliseconds you want this delay to be for.
* **callback** – The method that is called when this delay ends.
* **name** – String name of this delay. This name is arbitrary and only used to identify the delay later if you want to remove or change it. If you don’t provide it, a UUID4 name will be created.
* ****kwargs** – Any other (optional) kwarg pairs you pass will be passed along as kwargs to the callback method.

Returns string name or UUID4 of the delay which you can use to remove it later.

`run_now(name: str)`

Run a delay callback now instead of waiting until its time comes.

This will cancel the future running of the delay callback.

Parameters:

* **name** – Name of the delay to run. If this name is not an active delay, that’s fine. Nothing happens.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.

