# drop_target_banks API Reference

Config Reference:

* [drop_target_banks:](../../../config/drop_target_banks.md)

`self.machine.drop_target_banks.*`

``` python
class mpf.devices.drop_target.DropTargetBank(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

A bank of drop targets in a pinball machine by grouping together multiple DropTarget class devices.

## Accessing drop_target_banks in code

The device collection which contains the `drop_target_banks` in your machine is available via `self.machine.drop_target_banks`. For example, to access one called “foo”, you would use `self.machine.drop_target_banks.foo`. You can also access drop_target_banks in dictionary form, e.g. `self.machine.drop_target_banks['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Drop_target_banks have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enable() → None`

Enable handler.

`event_enable(**kwargs)`

Event handler for enable event.

`event_reset(**kwargs)`

Handle reset control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`member_target_change()`

Handle that a member drop target has changed state.  This method causes this group to update its down and up counts and complete status.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset this bank of drop targets. This method has some intelligence to figure out what coil(s) it should fire. It builds up a set by looking at its own reset_coil and reset_coils settings, and also scanning through all the member drop targets and collecting their coils. Then it pulses each of them. (This coil list is a “set” which means it only sends a single pulse to each coil, even if each drop target is configured with its own coil.)

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
