# sequence_shots API Reference

`self.machine.sequence_shots.*`

``` python
class mpf.devices.sequence_shot.SequenceShot(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

A device which represents a sequence shot.

## Accessing sequence_shots in code

The device collection which contains the sequence_shots in your machine is available via `self.machine.sequence_shots`. For example, to access one called “foo”, you would use `self.machine.sequence_shots.foo`. You can also access sequence_shots in dictionary form, e.g. `self.machine.sequence_shots['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Sequence_shots have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enable() → None`

Enable handler.

`event_cancel(**kwargs)`

Event handler for cancel event.

`event_enable(**kwargs)`

Event handler for enable event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset_all_sequences()`

Reset all sequences.
