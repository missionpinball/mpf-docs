
# self.machine.accelerometers.*

`class mpf.devices.accelerometer.Accelerometer(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice

Implements a multi-axis accelerometer. In modern machines, accelerometers can be used for tilt detection and to detect whether a machine is properly leveled. The accelerometer device produces a data stream of readings which MPF converts to g-forces, and then events can be posted when the “hit” (or g-force) of an accelerometer exceeds a predefined threshold.

## Accessing accelerometers in code

The device collection which contains the accelerometers in your machine is available via self.machine.accelerometers. For example, to access one called “foo”, you would use self.machine.accelerometers.foo. You can also access accelerometers in dictionary form, e.g. `self.machine.accelerometers['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Accelerometers have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_level_xyz() → float`

Return current 3D level.

`get_level_xz() → float`

Return current 2D x/z level.

`get_level_yz() → float`

Return current 2D y/z level.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`update_acceleration(x: float, y: float, z: float) → None`

Calculate acceleration based on readings from hardware.

