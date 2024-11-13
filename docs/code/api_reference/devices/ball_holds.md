
# self.machine.ball_holds.*

`class mpf.devices.ball_hold.BallHold(*args, **kwargs)`

Bases: mpf.core.enable_disable_mixin.EnableDisableMixin, mpf.core.system_wide_device.SystemWideDevice, mpf.core.mode_device.ModeDevice

Ball hold device which can be used to keep balls in ball devices and control their eject later on.

## Accessing ball_holds in code

The device collection which contains the ball_holds in your machine is available via `self.machine.ball_holds`. For example, to access one called “foo”, you would use `self.machine.ball_holds.foo`. You can also access ball_holds in dictionary form, e.g. `self.machine.ball_holds['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Ball_holds have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

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

`event_release_all(**kwargs)`

Event handler for release_all event.

`event_release_one(**kwargs)`

Event handler for release_one event.

`event_release_one_if_full(**kwargs)`

Event handler for release_one_if_full event.

`event_reset(**kwargs)`

Event handler for reset event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`is_full()`

Return true if hold is full.

`persist_enabled`

Return if enabled is persisted.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`release_all()`

Release all balls in hold.

`release_balls(balls_to_release)`

Release all balls and return the actual amount of balls released.

Parameters:

* **balls_to_release** – number of ball to release from hold

`release_one()`

Release one ball.

`release_one_if_full()`

Release one ball if hold is full.

`remaining_space_in_hold()`

Return the remaining capacity of the hold.

`reset()`

Reset the hold. Will release held balls. Device status will stay the same (enabled/disabled). It will wait for those balls to drain and block ball_ending until they do. Those balls are not included in ball_in_play.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

