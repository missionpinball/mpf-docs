
self.machine.segment_displays.*

``` python
class mpf.devices.segment_display.SegmentDisplay(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

A physical segment display in a pinball machine.

## Accessing segment_displays in code

The device collection which contains the segment_displays in your machine is available via `self.machine.segment_displays`. For example, to access one called “foo”, you would use `self.machine.segment_displays.foo`. You can also access segment_displays in dictionary form, e.g. `self.machine.segment_displays['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Segment_displays have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_text(text: str, priority: int = 0, key: str = None) → None`

Add text to display stack.

This will replace texts with the same key.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_text_by_key(key: str)`

Remove entry from text stack.

`set_flashing(flashing: bool)`

Enable/Disable flashing.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
