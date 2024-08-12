
self.machine.playfields.*

class mpf.devices.playfield.Playfield(*args, **kwargs)

Bases: mpf.core.system_wide_device.SystemWideDevice

One playfield in a pinball machine.

## Accessing playfields in code

The device collection which contains the playfields in your machine is available via `self.machine.playfields`. For example, to access one called “foo”, you would use `self.machine.playfields.foo`. You can also access playfields in dictionary form, e.g. `self.machine.playfields['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Playfields have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_ball(balls=1, source_device=None, player_controlled=False) → bool`

Add live ball(s) to the playfield.

Parameters:

* **balls** – Integer of the number of balls you’d like to add.
* **source_device** – Optional ball device object you’d like to add the ball(s) from.
* **player_controlled** – Boolean which specifies whether this event is player controlled. (See not below for details)

Returns True if it’s able to process the add_ball() request, False if it cannot.

The source_device arg is included to give you an options for specifying the source of the ball(s) to be added. This argument is optional, so if you don’t supply them then MPF will use the default_source_device of this playfield.

This method does not increase the game controller’s count of the number of balls in play. So if you want to add balls (like in a multiball scenario), you need to call this method along with self.machine.game.add_balls_in_play().)

MPF tracks the number of balls in play separately from the actual balls on the playfield because there are numerous situations where the two counts are not the same. For example, if a ball is in a VUK while some animation is playing, there are no balls on the playfield but still one ball in play, or if the player has a two-ball multiball and they shoot them both into locks, there are still two balls in play even though there are no balls on the playfield. The opposite can also be true, like when the player tilts then there are still balls on the playfield but no balls in play.

Explanation of the player_controlled parameter:

Set player_controlled to True to indicate that MPF should wait for the player to eject the ball from the source_device rather than firing a coil. The logic works like this:

If the source_device does not have an eject_coil defined, then it’s assumed that player_controlled is the only option. (e.g. this is a traditional plunger.) If the source_device does have an eject_coil defined, then there are two ways the eject could work. (1) there could be a “launch” button of some kind that’s used to fire the eject coil, or (2) the device could be the auto/manual combo style where there’s a mechanical plunger but also a coil which can eject the ball.

If player_controlled is true and the device has an eject_coil, MPF will look for the player_controlled_eject_tag and eject the ball when a switch with that tag is activated.

If there is no player_controlled_eject_tag, MPF assumes it’s a manual plunger and will wait for the ball to disappear from the device based on the device’s ball count decreasing.

`add_incoming_ball(incoming_ball: mpf.devices.ball_device.incoming_balls_handler.IncomingBall)`

Track an incoming ball.

`add_missing_balls(balls)`

Notify the playfield that it probably received a ball which went missing elsewhere.

`ball_arrived()`

Confirm first ball in queue.

`ball_search`

An instance of mpf.core.ball_search.BallSearch which handles ball search for this playfield.

`balls`

Return the number of balls on the playfield.

`delay`

An instance of mpf.core.delays.DelayManager which handles delays for this playfield.

`event_ball_search_block(**kwargs)`

Block ball search for this playfield.

Blocking will disable ball search if it’s enabled or running, and will prevent ball search from enabling if it’s disabled until ball_search_resume() is called.

`event_ball_search_disable(**kwargs)`

Disable ball search for this playfield.

If the ball search timer is running, it will stop and disable it. If an actual ball search process is running, it will stop.

`event_ball_search_enable(**kwargs)`

Enable ball search for this playfield.

Note this does not start the ball search process, rather, it starts the timer running.

`event_ball_search_unblock(**kwargs)`

Unblock ball search for this playfield.

This will check to see if there are balls on the playfield, and if so, enable ball search.

`expected_ball_received()`

Handle an expected ball.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`classmethod get_additional_ball_capacity()`

Return the number of ball which can be added.

Used to find out how many more balls this device can hold. Since this is the playfield device, this method always returns 999.

Returns: 999

`get_placeholder_value(item)`

Get the value of a placeholder.

`classmethod is_playfield()`

Return true since it is a playfield.

`mark_playfield_active_from_device_action()`

Mark playfield active because a device on the playfield detected activity.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_incoming_ball(incoming_ball: mpf.devices.ball_device.incoming_balls_handler.IncomingBall)`

Stop tracking an incoming ball.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`unexpected_ball_received()`

Handle an unexpected ball.

`static wait_for_ready_to_receive(source)`

Playfield is always ready to receive.

