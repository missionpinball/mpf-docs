
# self.machine.digital_outputs.*

``` python
class mpf.devices.digital_output.DigitalOutput(machine: mpf.core.machine.MachineController, name: str)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

A digital output on either a light or driver platform.

## Accessing digital_outputs in code

The device collection which contains the `digital_outputs` in your machine is available via `self.machine.digital_outputs`. For example, to access one called “foo”, you would use `self.machine.digital_outputs.foo`. You can also access digital_outputs in dictionary form, e.g. `self.machine.digital_outputs['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Digital_outputs have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable digital output.

`enable()`

Enable digital output.

`event_disable(**kwargs)`

Handle disable control event.

`event_enable(**kwargs)`

Handle enable control event.

`event_pulse(pulse_ms, **kwargs)`

Handle pulse control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`pulse(pulse_ms)`

Pulse digital output.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.
