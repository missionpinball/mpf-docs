
# self.machine.dual_wound_coils.*

`class mpf.devices.dual_wound_coil.DualWoundCoil(machine, name)`

Bases: mpf.core.system_wide_device.SystemWideDevice

An instance of a dual wound coil which consists of two coils.

## Accessing dual_wound_coils in code

The device collection which contains the `dual_wound_coils` in your machine is available via `self.machine.dual_wound_coils`. For example, to access one called “foo”, you would use `self.machine.dual_wound_coils.foo`. You can also access dual_wound_coils in dictionary form, e.g. `self.machine.dual_wound_coils['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Dual_wound_coils have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable a driver.

`enable()`

Enable a dual wound coil. Pulse main coil and enable hold coil.

`event_disable(**kwargs)`

Event handler for disable event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_pulse(milliseconds: int = None, power: float = None, **kwargs)`

Event handler for pulse event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

 `pulse(milliseconds: int = None, power: float = None)`

Pulse this driver.

Parameters:

* **milliseconds** – The number of milliseconds the driver should be enabled for. If no value is provided, the driver will be enabled for the value specified in the config dictionary.
* **power** – A multiplier that will be applied to the default pulse time, typically a float between 0.0 and 1.0. (Note this is can only be used if milliseconds is also specified.)

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

