# magnets API Reference

Config Reference:

* [magnets:](../../../config/magnets.md)

`self.machine.magnets.*`

``` python
class mpf.devices.magnet.Magnet(*args, **kwargs)
```

Bases: `mpf.core.enable_disable_mixin.EnableDisableMixinSystemWideDevice`, `mpf.core.system_wide_device.SystemWideDevice`

Controls a playfield magnet in a pinball machine.

## Accessing magnets in code

The device collection which contains the magnets in your machine is available via `self.machine.magnets`. For example, to access one called “foo”, you would use `self.machine.magnets.foo`. You can also access magnets in dictionary form, e.g. `self.machine.magnets['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Magnets have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable device.

`enable() → None`

Enable device.

`event_disable(**kwargs)`

Handle disable control event.

`event_enable(**kwargs)`

Handle enable control event.

`event_fling_ball(**kwargs)`

Event handler for fling_ball event.

`event_grab_ball(**kwargs)`

Event handler for grab_ball event.

`event_release_ball(**kwargs)`

Event handler for release_ball event.

`event_reset(**kwargs)`

Event handler for reset event.

`fling_ball()`

Fling the grabbed ball.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`grab_ball()`

Grab a ball.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`release_ball()`

Release the grabbed ball.

`reset()`

Release ball and disable magnet.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
