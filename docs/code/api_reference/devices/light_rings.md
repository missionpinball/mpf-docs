# light_rings API Reference

`self.machine.light_rings.*`

``` python
class mpf.devices.light_group.LightRing(machine: mpf.core.machine.MachineController, name)
```

Bases: `mpf.devices.light_group.LightGroup`

A light ring.

## Accessing light_rings in code

The device collection which contains the `light_rings` in your machine is available via `self.machine.light_rings`. For example, to access one called “foo”, you would use `self.machine.light_rings.foo`. You can also access `light_rings` in dictionary form, e.g. `self.machine.light_rings['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Light_rings have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`color(color, fade_ms=None, priority=0, key=None)`

Call color on all lights in this group.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_token()`

Return all lights in group as token.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.
