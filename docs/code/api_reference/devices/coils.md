# self.machine.coils.*

``` python
class mpf.devices.driver.Driver(machine: mpf.core.machine.MachineController, name: str)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Generic class that holds driver objects. A ‘driver’ is any device controlled from a driver board which is typically the high-voltage stuff like coils and flashers. This class exposes the methods you should use on these driver types of devices. Each platform module (i.e. P-ROC, FAST, etc.) subclasses this class to actually communicate with the physical hardware and perform the actions.

Args: Same as the Device parent class

## Accessing coils in code

The device collection which contains the coils in your machine is available via `self.machine.coils`. For example, to access one called “foo”, you would use `self.machine.coils.foo`. You can also access coils in dictionary form, e.g. `self.machine.coils['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Coils have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable this driver.

`enable(pulse_ms: int = None, pulse_power: float = None, hold_power: float = None)`

Enable a driver by holding it ‘on’.

Parameters:

* **pulse_ms** – The number of milliseconds the driver should be enabled for. If no value is provided, the driver will be enabled for the value specified in the config dictionary.
* **pulse_power** – The pulse power. A float between 0.0 and 1.0.
* **hold_power** – The pulse power. A float between 0.0 and 1.0.

If this driver is configured with a holdpatter, then this method will use that holdpatter to pwm pulse the driver. If not, then this method will just enable the driver. As a safety precaution, if you want to enable() this driver without pwm, then you have to add the following option to this driver in your machine configuration files: `allow_enable: True`

`event_disable(**kwargs)`

Event handler for disable control event.

`event_enable(pulse_ms: int = None, pulse_power: float = None, hold_power: float = None, **kwargs)`

Event handler for control enable.

`event_pulse(pulse_ms: int = None, pulse_power: float = None, max_wait_ms: int = None, **kwargs) → None`

Event handler for pulse control events.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_and_verify_hold_power(hold_power: Optional[float]) → float`

Return the hold power to use. If hold_power is None it will use the default_hold_power. Additionally it will verify the limits.

`get_and_verify_pulse_ms(pulse_ms: Optional[int]) → int`

Return and verify pulse_ms to use. If pulse_ms is None return the default.

`get_and_verify_pulse_power(pulse_power: Optional[float]) → float`

Return the pulse power to use. If pulse_power is None it will use the default_pulse_power. Additionally it will verify the limits.

`pulse(pulse_ms: int = None, pulse_power: float = None, max_wait_ms: int = None) → int`

Pulse this driver.

Parameters:

* **pulse_ms** – The number of milliseconds the driver should be enabled for. If no value is provided, the driver will be enabled for the value specified in the config dictionary.
* **pulse_power** – The pulse power. A float between 0.0 and 1.0.
* **max_wait_ms** – Maximum time this pulse may be delayed for PSU optimization.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.
