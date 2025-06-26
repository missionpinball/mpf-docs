# combo_switches API Reference

`self.machine.combo_switches.*`

``` python
class mpf.devices.combo_switch.ComboSwitch(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

Combo Switch device.

## Accessing combo_switches in code

The device collection which contains the `combo_switches` in your machine is available via `self.machine.combo_switches`. For example, to access one called “foo”, you would use `self.machine.combo_switches.foo`. You can also access combo_switches in dictionary form, e.g. `self.machine.combo_switches['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Combo_switches have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

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

`state`

Return current state.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
