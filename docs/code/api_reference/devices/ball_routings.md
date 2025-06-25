
# self.machine.ball_routings.*

``` python
class mpf.devices.ball_routing.BallRouting(*args, **kwargs)
```

Bases: `mpf.core.enable_disable_mixin.EnableDisableMixin`, `mpf.core.mode_device.ModeDevice`

Route balls from one device to another when captured.

## Accessing ball_routings in code

The device collection which contains the `ball_routings` in your machine is available via `self.machine.ball_routings`. For example, to access one called “foo”, you would use `self.machine.ball_routings.foo`. You can also access ball_routings in dictionary form, e.g. `self.machine.ball_routings['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Ball_routings have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable device.

`enable() → None`

Enable device.

`enabled`

Return true if enabled.

`event_disable(**kwargs)`

Handle disable control event.

`event_enable(**kwargs)`

Handle enable control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`persist_enabled`

Return if enabled is persisted.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
