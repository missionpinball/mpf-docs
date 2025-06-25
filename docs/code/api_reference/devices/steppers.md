
# self.machine.steppers.*

``` python
class mpf.devices.stepper.Stepper(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents an stepper motor based axis in a pinball machine.

Args: Same as the Device parent class.

## Accessing steppers in code

The device collection which contains the steppers in your machine is available via `self.machine.steppers`. For example, to access one called “foo”, you would use `self.machine.steppers.foo`. You can also access steppers in dictionary form, e.g. `self.machine.steppers['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Steppers have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`event_move_to_position(position=None, **kwargs)`

Event handler for move_to_position event.

`event_reset(**kwargs)`

Event handler for reset event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`move_to_position(position)`

Move stepper to a position.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Move to reset position.

`stop()`

Stop motor.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
