
# self.machine.ball_saves.*

`class mpf.devices.ball_save.BallSave(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice, mpf.core.mode_device.ModeDevice

Ball save device which will give back the ball within a certain time.

## Accessing ball_saves in code

The device collection which contains the `ball_saves` in your machine is available via `self.machine.ball_saves`. For example, to access one called “foo”, you would use `self.machine.ball_saves.foo`. You can also access ball_saves in dictionary form, e.g. `self.machine.ball_saves['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Ball_saves have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`delayed_eject()`

Trigger eject of all scheduled balls.

`disable() → None`

Disable ball save.

`early_ball_save() → None`

Perform early ball save if enabled.

`enable() → None`

Enable ball save.

`event_delayed_eject(**kwargs)`

Event handler for delayed_eject event.

`event_disable(**kwargs)`

Event handler for disable event.

`event_early_ball_save(**kwargs)`

Event handler for early_ball_save event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_timer_start(**kwargs)`

Event handler for timer start event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`timer_start() → None`

Start the timer.  This is usually called after the ball was ejected while the ball save may have been enabled earlier.

