
# self.machine.psus.*

`class mpf.devices.power_supply_unit.PowerSupplyUnit(machine, name)`

Bases: mpf.core.system_wide_device.SystemWideDevice

Represents a power supply in a pinball machine.

## Accessing psus in code

The device collection which contains the psus in your machine is available via `self.machine.psus`. For example, to access one called “foo”, you would use `self.machine.psus.foo`. You can also access psus in dictionary form, e.g. `self.machine.psus['foo']`.  You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Psus have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_wait_time_for_pulse(pulse_ms, max_wait_ms) → int`

Return a wait time for a pulse or 0.

`notify_about_instant_pulse(pulse_ms)`

Notify PSU about pulse.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

