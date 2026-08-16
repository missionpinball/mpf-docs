---
title: API Reference - achievements
---

# achievements API Reference

Config Reference:

* [achievements:](../../../config/achievements.md)

`self.machine.achievements.*`

``` python
class mpf.devices.achievement.Achievement(*args, **kwargs)
```

Bases: `mpf.core.mode_device.ModeDevice`

An achievement in a pinball machine. It is tracked per player and can automatically restore state on the next ball.

## Accessing achievements in code

The device collection which contains the achievements in your machine is available via `self.machine.achievements`. For example, to access one called “foo”, you would use `self.machine.achievements.foo`. You can also access achievements in dictionary form, e.g. `self.machine.achievements['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Achievements have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`can_be_selected_for_start`

Return if this achievement can be selected and started.

`complete()`

Complete achievement.

`disable()`

Disable achievement.

`enable()`

Enable the achievement. It can only start if it was enabled before.

`event_complete(**kwargs)`

Event handler for complete event.

`event_disable(**kwargs)`

Event handler for disable event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_reset(**kwargs)`

Event handler for reset event.

`event_select(**kwargs)`

Event handler for select event.

`event_start(**kwargs)`

Event handler for start event.

`event_stop(**kwargs)`

Event handler for stop event.

`event_unselect(**kwargs)`

Event handler for unselect event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset the achievement to its initial state.

`select()`

Highlight (select) this achievement.

`selected`

Return current selection state.

`start()`

Start achievement.

`state`

Return current state.

`stop()`

Stop achievement.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`unselect()`

Remove highlight (unselect) this achievement.
