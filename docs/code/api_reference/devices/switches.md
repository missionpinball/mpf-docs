
# self.machine.switches.*

`class mpf.devices.switch.Switch(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice, mpf.devices.device_mixins.DevicePositionMixin

A switch in a pinball machine.

## Accessing switches in code

The device collection which contains the switches in your machine is available via `self.machine.switches`. For example, to access one called “foo”, you would use `self.machine.switches.foo`. You can also access switches in dictionary form, e.g. `self.machine.switches['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Switches have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_handler(callback, state=1, ms=0, return_info=False, callback_kwargs=None)`

Add switch handler (callback) for this switch which is called when this switch state changes.

Note that this method just calls the Switch Controller’s add_switch_handler() method behind the scenes.

Parameters:

* **callback** – A callable method that will be called when the switch state changes.
* **state** – The state that the switch which change into which triggers the callback to be called. Values are 0 or 1, with 0 meaning the switch changed to inactive, and 1 meaning the switch changed to an active state.
* **ms** – How many milliseconds the switch needs to be in the new state before the callback is called. Default is 0 which means that the callback will be called immediately. You can use this setting as a form of software debounce, as the switch needs to be in the state consistently before the callback is called.
* **return_info** – If True, the switch controller will pass the parameters of the switch handler as arguments to the callback, including switch_name, state, and ms.
* **callback_kwargs** – Additional kwargs that will be passed with the callback.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_ms_since_last_change(current_time=None) → int`

Get ms since last change.

Will use the current time from clock if you do not pass it.

`get_placeholder_value(item)`

Get the value of a placeholder.

`hw_state`

The physical hardware state of the switch. 1 = active, 0 = inactive. This is what the actual hardware is reporting and does not consider whether a switch is NC or NO.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_handler(callback, state=1, ms=0)`

Remove switch handler for this switch.

`state`

The logical state of a switch. 1 = active, 0 = inactive. This takes into consideration the NC or NO settings for the switch.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`x`

Get the X value from the config.

Returns the devices x position from config

`y`

Get the Y value from the config.

Returns the devices y position from config

`z`

Get the Z value from the config.

Returns the devices z position from config

