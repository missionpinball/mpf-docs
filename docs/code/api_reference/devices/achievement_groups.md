# achievement_groups API reference

Config Reference:

* [achievement_groups:](../../../config/achievement_groups.md)

`self.machine.achievement_groups.*`

``` python
class mpf.devices.achievement_group.AchievementGroup(*args, **kwargs)
```

Bases: `mpf.core.mode_device.ModeDevice`

An achievement group in a pinball machine. It is tracked per player and can automatically restore state on the next ball.

## Accessing achievement_groups in code

The device collection which contains the achievement_groups in your machine is available via `self.machine.achievement_groups`. For example, to access one called “foo”, you would use `self.machine.achievement_groups.foo`. You can also access `achievement_groups` in dictionary form, e.g. `self.machine.achievement_groups['foo']`.  You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Achievement_groups have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable achievement group.

`enable()`

Enable achievement group.

`enabled`

Return enabled state.

`event_disable(**kwargs)`

Event handler for disable event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_rotate_left(**kwargs)`

Event handler for rotate_left event.

`event_rotate_right(reverse=False, **kwargs)`

Event handler for rotate_right event.

`event_select_random_achievement(**kwargs)`

Event handler for select_random_achievement event.

`event_start_selected(**kwargs)`

Event handler for start_selected event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`member_state_changed(**kwargs)`

Notify the group that one of its members has changed state.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`rotate_left()`

Rotate to the left.

`rotate_right(reverse=False)`

Rotate to the right.

`select_random_achievement()`

Select a random achievement.

`start_selected()`

Start the currently selected achievement.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
