
# self.machine.extra_balls.*

`class mpf.devices.extra_ball.ExtraBall(*args, **kwargs)`

Bases: mpf.core.mode_device.ModeDevice

An extra ball which can be awarded once per player.

## Accessing extra_balls in code

The device collection which contains the `extra_balls` in your machine is available via `self.machine.extra_balls`. For example, to access one called “foo”, you would use `self.machine.extra_balls.foo`. You can also access extra_balls in dictionary form, e.g. `self.machine.extra_balls['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Extra_balls have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`award()`

Award extra ball to player (if enabled).

`enable() → None`

Enable handler.

`enabled`

Return whether this extra ball group is enabled. This takes into consideration the enabled setting plus the max balls per game setting.

`event_award(**kwargs)`

Handle award control event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_light(**kwargs)`

Handle light control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`group`

The ExtraBallGroup this ExtraBall belongs to, or None.

`is_ok_to_award() → bool`

Check whether this extra ball can be awarded.  This method takes into consideration whether this extra ball is enabled, whether the max_per_game has been exceeded, and, if this extra ball is a member of a group, whether the group is enabled and will allow an additional extra ball to be awarded. Returns True or False.

`is_ok_to_light() → bool`

Check whether this extra ball can be lit. This method takes into consideration whether this extra ball is enabled, and, if this extra ball is a member of a group, whether the group is enabled and will allow an additional extra ball to lit. Returns True or False.

`light()`

Light an extra ball for potential collection by the player. Lighting an extra ball will immediately increase count against the max_per_game setting, even if the extra ball is a member of a group that’s disabled or if the player never actually collects the extra ball. Note that this only really does anything if this extra ball is a member of a group.

`player`

The current player

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

