# Ball Search API Reference

``` python
class mpf.core.ball_search.BallSearch(machine: mpf.core.machine.MachineController, playfield: Playfield)
```

Bases: `mpf.core.mpf_controller.MpfController`

Implements Ball search for a playfield device.

In MPF, the ball search functionality is attached to each playfield device, rather than being done at the global level. (In other words, each playfield is responsible for making sure no balls get stuck on it, and it leverages an instance of this BallSearch class to handle it.)

## Methods & Attributes

The Ball Search has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`block(**kwargs)`

Block ball search for this playfield.

Blocking will disable ball search if it's enabled or running, and will prevent ball search from enabling if it's disabled until ball_search_unblock() is called.

`blocked = None`

If True, ball search will be blocked and will not start.

`cancel_ball_search(**kwargs)`

Cancel the current ball search and mark the ball as missing.

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

`disable(**kwargs)`

Disable ball search.

This method will also stop the ball search if it is running.

`enable(**kwargs)`

Enable the ball search for this playfield.

Note that this method does not start the ball search process. Rather it just resets and starts the timeout timer, as well as resetting it when playfield switches are hit.

`enabled = None`

Is ball search enabled.

`error_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the error level.

These messages will always be shown in the console and the log file.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`give_up()`

Give up the ball search.

This method is called when the ball search process Did not find the missing ball. It executes the failed action which depending on the specification of ball_search_failed_action, either adds a replacement ball, ends the game, or ends the current ball.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`info_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the info level.

Whether this message shows up in the console or log file is controlled by the settings used with configure_logging().

`iteration = None`

Current iteration of the ball search, or False if ball search is not started.

`phase = None`

Current phase of the ball search, or False if ball search is not started.

`playfield = None`

The playfield device this ball search instance is attached to.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`register(priority, callback, name, *, restore_callback=None)`

Register a callback for sequential ball search.

Callbacks are called by priority. Ball search only waits if the callback returns true.

Parameters:

* **priority** – priority of this callback in the ball search procedure
* **callback** – callback to call. ball search will wait before the next callback, if it returns true
* **name** – string name which is used for debugging & the logs
* **restore_callback** – optional callback to restore state of the device after ball search ended

`request_to_start_game(**kwargs)`

Handle result of the request_to_start_game event.

If ball search is running, this method will return False to prevent the game from starting while ball search is running.

This method also posts the ball_search_prevents_game_start event if ball search is started.

`reset_timer()`

Reset the timeout timer which starts ball search.

This method will also cancel an actively running (started) ball search.

This is called by the playfield anytime a playfield switch is hit.

`start()`

Start ball search the ball search process.

`started = None`

Is the ball search process started (running) now.

`stop()`

Stop an actively running ball search.

`unblock(**kwargs)`

Unblock ball search for this playfield.

This will check to see if there are balls on the playfield, and if so, enable ball search.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.
