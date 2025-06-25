
# self.machine.timed_switches.*

``` python
class mpf.devices.timed_switch.TimedSwitch(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

Timed Switch device.

## Accessing timed_switches in code

The device collection which contains the timed_switches in your machine is available via `self.machine.timed_switches`. For example, to access one called “foo”, you would use `self.machine.timed_switches.foo`. You can also access timed_switches in dictionary form, e.g. `self.machine.timed_switches['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Timed_switches have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enable() → None`

Enable handler.

`event_enable(**kwargs)`

Event handler for enable event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
