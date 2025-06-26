# shot_groups API Reference

`self.machine.shot_groups.*`

``` python
class mpf.devices.shot_group.ShotGroup(*args, **kwargs)
```

Bases: `mpf.core.mode_device.ModeDevice`

Represents a group of shots in a pinball machine by grouping together multiple Shot class devices.

This is used so you get get “group-level” functionality, like shot rotation, shot group completion, etc. This would be used for a group of rollover lanes, a bank of standups, etc.

## Accessing shot_groups in code

The device collection which contains the shot_groups in your machine is available via `self.machine.shot_groups`. For example, to access one called “foo”, you would use `self.machine.shot_groups.foo`. You can also access shot_groups in dictionary form, e.g. `self.machine.shot_groups['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Shot_groups have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`common_state`

Return common state if all shots in this group are in the same state.

Will return None otherwise.

`disable()`

Disable all member shots.

`disable_rotation()`

Disable shot rotation.

If disabled, rotation events do not actually rotate the shots.

`enable()`

Enable all member shots.

`enable_rotation()`

Enable shot rotation.

If disabled, rotation events do not actually rotate the shots.

`event_disable(**kwargs)`

Handle disable control event.

`event_disable_rotation(**kwargs)`

Handle disable rotation control event.

`event_enable(**kwargs)`

Handle enable control event.

`event_enable_rotation(**kwargs)`

Handle enable_rotation control event.

`event_reset(**kwargs)`

Handle reset control event.

`event_restart(**kwargs)`

Handle restart control event.

`event_rotate(direction=None, **kwargs)`

Handle rotate control event.

`event_rotate_left(**kwargs)`

Handle rotate left control event.

`event_rotate_right(**kwargs)`

Handle rotate right control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset all member shots.

`restart()`

Restart all member shots.

`rotate(direction=None)`

Rotate (or “shift”) the state of all the shots in this group.

This is used for things like lane change, where hitting the flipper button shifts all the states of the shots in the group to the left or right.

This method actually transfers the current state of each shot profile to the left or the right, and the shot on the end rolls over to the taret on the other end.

Parameters:

* **direction** – String that specifies whether the rotation direction is to the left or right. Values are ‘right’ or ‘left’. Default of None will cause the shot group to rotate in the direction as specified by the rotation_pattern.

Note that this shot group must, and rotation_events for this shot group, must both be enabled for the rotation events to work.

`rotate_left()`

Rotate the state of the shots to the left.

This method is the same as calling rotate(‘left’)

`rotate_right()`

Rotate the state of the shots to the right.

This method is the same as calling rotate(‘right’)

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
