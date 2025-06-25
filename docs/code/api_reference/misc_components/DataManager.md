
# Data Manager

``` python
class mpf.core.data_manager.DataManager(machine, name, min_wait_secs=1)
```

Bases: `mpf.core.mpf_controller.MpfController`

Handles key value data loading and saving for the machine.

## Methods & Attributes

The data_manager has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

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

`get_data(section=None)`

Return the value of this DataManager’s data.

Parameters:

* **section** – Optional string name of a section (dictionary key) for the data you want returned. Default is None which returns the entire dictionary.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`info_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the info level.

Whether this message shows up in the console or log file is controlled by the settings used with configure_logging().

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`save_all(data)`

Update all data.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.
