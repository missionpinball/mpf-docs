
# self.machine.servos.*

`class mpf.devices.servo.Servo(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice

Represents a servo in a pinball machine.

Args: Same as the Device parent class.

## Accessing servos in code

The device collection which contains the servos in your machine is available via `self.machine.servos`. For example, to access one called “foo”, you would use `self.machine.servos.foo`. You can also access servos in dictionary form, e.g. `self.machine.servos['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Servos have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`event_reset(**kwargs)`

Event handler for reset event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`go_to_position(position)`

Move servo to position.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Go to reset position.

`set_acceleration_limit(acceleration_limit)`

Set acceleration parameter.

`set_speed_limit(speed_limit)`

Set speed parameter.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

