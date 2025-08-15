# motors API Reference

Config Reference:

* [motors:](../../../config/motors.md)

`self.machine.motors.*`

``` python
class mpf.devices.motor.Motor(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

A motor which can be controlled using drivers.

## Accessing motors in code

The device collection which contains the motors in your machine is available via `self.machine.motors`. For example, to access one called “foo”, you would use `self.machine.motors.foo`. You can also access motors in dictionary form, e.g. `self.machine.motors['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Motors have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`event_go_to_position(position=None, **kwargs)`

Event handler for go_to_position event.

`event_reset(**kwargs)`

Event handler for reset event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`go_to_position(position)`

Move motor to a specific position.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Go to reset position.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
