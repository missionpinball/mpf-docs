# extra_ball_groups API Reference

Config Reference:

* [extra_ball_groups:](../../../config/extra_ball_groups.md)

`self.machine.extra_ball_groups.*`

``` python
class mpf.devices.extra_ball_group.ExtraBallGroup(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Tracks and manages groups of extra balls devices.

## Accessing extra_ball_groups in code

The device collection which contains the `extra_ball_groups` in your machine is available via `self.machine.extra_ball_groups`. For example, to access one called “foo”, you would use `self.machine.extra_ball_groups.foo`. You can also access extra_ball_groups in dictionary form, e.g. `self.machine.extra_ball_groups['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Extra_ball_groups have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`award(posted_unlit_events=False)`

Immediately awards an extra ball. This event first checks to make sure the limits of the max extra balls have not been exceeded and that this group is enabled. Note that this method will work even if this group does not have any extra balls or extra balls lit. You can use this to directly award an extra ball.

`award_disabled()`

Post the events when an extra ball connect be awarded.

`award_lit()`

Award a lit extra ball. If the player does not have any lit extra balls, this method does nothing.

`enabled`

Return whether this extra ball group is enabled. This attribute considers the enabled setting plus the max balls per game and ball settings.

`event_award(posted_unlit_events=False, **kwargs)`

Handle award control event.

`event_award_lit(**kwargs)`

Handle award_lit control event.

`event_light(**kwargs)`

Handle light control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`is_ok_to_light() → bool`

Check if it's possible to light an extra ball. Returns True or False. This method checks to see if the group is enabled and whether the max_lit setting has been exceeded.

`light()`

Light the extra ball for possible collection by the player. This method checks that the group is enabled and that the max lit value has not been exceeded. If so, this method will post the extra ball disabled events.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
