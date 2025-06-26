# rgb_dmds API Reference

`self.machine.rgb_dmds.*`

``` python
class mpf.devices.rgb_dmd.RgbDmd(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

A physical DMD.

## Accessing rgb_dmds in code

The device collection which contains the rgb_dmds in your machine is available via `self.machine.rgb_dmds`. For example, to access one called “foo”, you would use `self.machine.rgb_dmds.foo`. You can also access rgb_dmds in dictionary form, e.g. `self.machine.rgb_dmds['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Rgb_dmds have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

` format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

` raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

` update(data: bytes)`

Update data on the dmd.

Parameters:

* **data** – bytes to send
