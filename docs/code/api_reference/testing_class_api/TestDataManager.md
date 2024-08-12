
# TestDataManager

`class mpf.tests.TestDataManager.TestDataManager(data)`

Bases: mpf.core.data_manager.DataManager

A patched version of the DataManager which is used in unit tests.

The main change is that the `save_all()` method doesn’t actually write anything to disk so the tests don’t fill up the disk with unneeded data.

## Methods & Attributes

The TestDataManager has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_data(section=None)`

Return the value of this DataManager’s data.

Parameters:

* **section** – Optional string name of a section (dictionary key) for the data you want returned. Default is None which returns the entire dictionary.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`save_all(data)`

Update all data.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.

