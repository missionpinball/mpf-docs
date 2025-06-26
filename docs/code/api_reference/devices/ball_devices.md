# ball_devices API Reference

`self.machine.ball_devices.*`

``` python
class mpf.devices.ball_device.ball_device.BallDevice(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Base class for a ‘Ball Device’ in a pinball machine. A ball device is anything that can hold one or more balls, such as a trough, an eject hole, a VUK, a catapult, etc.

Args: Same as Device.

## Accessing ball_devices in code

The device collection which contains the ball_devices in your machine is available via self.machine.ball_devices. For example, to access one called “foo”, you would use `self.machine.ball_devices.foo`. You can also access `ball_devices` in dictionary form, e.g. `self.machine.ball_devices['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

`Ball_devices` have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_incoming_ball(incoming_ball: mpf.devices.ball_device.incoming_balls_handler.IncomingBall)`

Notify this device that there is a ball heading its way.

`available_balls`

Number of balls that are available to be ejected. This differs from balls since it’s possible that this device could have balls that are being used for some other eject, and thus not available.

`balls`

Return the number of balls we expect in the near future.

`cancel_path_if_target_is(start, target)`

Check if the ball is going to a certain target and cancel the path in that case.

`capacity`

Return the ball capacity.

`eject(balls=1, target=None) → int`

Eject balls to target. Return the number of balls found for eject. The remaining balls are queued for eject when available.

`eject_all(target=None) → bool`

Eject all the balls from this device.

Parameters:

* **target** – The string or BallDevice target for this eject. Default of None means playfield.
* ****kwargs** – unused

Returns True if there are balls to eject. False if this device is empty.

`event_eject(balls=1, target=None, **kwargs)`

Handle eject control event.

`event_eject_all(target=None, **kwargs)`

Handle eject_all control event.

`event_entrance(**kwargs)`

Event handler for entrance events.

`event_request_ball(balls=1, **kwargs)`

Handle request_ball control event.

`expected_ball_received()`

 Handle an expected ball.

`find_available_ball_in_path(start)`

Try to remove available ball at the end of the path.

`find_next_trough()`

Find next trough after device.

`find_one_available_ball(path=deque([]))`

Find a path to a source device which has at least one available ball.

`find_path_to_target(target)`

Find a path to this target.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`handle_mechanial_eject_during_idle()`

Handle mechanical eject.

`classmethod is_playfield()`

Return True if this ball device is a Playfield-type device, False if it’s a regular ball device.

`lost_ejected_ball(target)`

Handle an outgoing lost ball.

`lost_idle_ball()`

Lost an ball while the device was idle.

`lost_incoming_ball(source)`

Handle lost ball which was confirmed to have left source.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_incoming_ball(incoming_ball: mpf.devices.ball_device.incoming_balls_handler.IncomingBall)`

Remove a ball from the incoming balls queue.

`request_ball(balls=1)`

Request that one or more balls is added to this device.

Parameters:

* **balls** – Integer of the number of balls that should be added to this device. A value of -1 will cause this device to try to fill itself.
* ****kwargs** – unused

`requested_balls`

Return the number of requested balls.

`result = None`

`balldevice_(name)_ball_enter` A ball (or balls) have just entered the ball device called “name”. Note that this is a relay event based on the “unclaimed_balls” arg. Any unclaimed balls in the relay will be processed as new balls entering this device. Please be aware that we did not add those balls to balls or available_balls of the device during this event.

args:

* **unclaimed_balls**: The number of balls that have not yet been claimed. device: A reference to the ball device object that is posting this event.
* **Type**:	event

`set_eject_state(state)`

Set the current device state.

vsetup_eject_chain(path, player_controlled=False)`

Set up an eject chain.

`setup_eject_chain_next_hop(path, player_controlled)`

Set up one hop of the eject chain.

`setup_player_controlled_eject(target=None)`

Set up a player controlled eject.

`state`

Return the device state.

`stop_device()`

 Stop device.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`unexpected_ball_received()`

Handle an unexpected ball.

`wait_for_ready_to_receive(source)`

Wait until this device is ready to receive a ball.
