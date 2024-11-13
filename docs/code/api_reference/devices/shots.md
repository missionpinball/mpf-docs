
# self.machine.shots.*

`class mpf.devices.shot.Shot(*args, **kwargs)`

Bases: mpf.core.enable_disable_mixin.EnableDisableMixin, mpf.core.mode_device.ModeDevice

A device which represents a generic shot.

## Accessing shots in code

The device collection which contains the shots in your machine is available via `self.machine.shots`. For example, to access one called “foo”, you would use `self.machine.shots.foo`. You can also access shots in dictionary form, e.g. `self.machine.shots['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Shots have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`active_sequences`

(id, current_position_index, next_switch)
Type:	List of tuples

`advance(force=False) → bool`

Advance a shot profile forward.

If this profile is at the last step and configured to loop, it will roll over to the first step. If this profile is at the last step and not configured to loop, this method has no effect.

`can_rotate`

Return if the shot can be rotated according to its profile.

`disable()`

Disable device.

`enable() → None`

Enable device.

`enabled`

Return true if enabled.

`event_advance(force=False, **kwargs)`

Handle advance control event.

`event_disable(**kwargs)`

Handle disable control event.

`event_enable(**kwargs)`

Handle enable control event.

`event_hit(**kwargs)`

Handle hit control event.

`event_reset(**kwargs)`

Handle reset control event.

`event_restart(**kwargs)`

Handle restart control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`hit() → bool`

Advance the currently-active shot profile.

Note that the shot must be enabled in order for this hit to be processed.

Returns true if the shot was enabled or false if the hit has been ignored.

`jump(state, force=True, force_show=False)`

Jump to a certain state in the active shot profile.

Parameters:

* **state** – int of the state number you want to jump to. Note that states are zero-based, so the first state is 0.
* **force** – if true, will jump even if the shot is disabled
* **force_show** – if true, will update the profile show even if the jumped state index is the same as before the jump

`monitor_enabled = False`

Class attribute which specifies whether any monitors have been registered to track shots.

`persist_enabled`

Return if enabled is persisted.

`profile`

Return profile.

`profile_name`

Return profile name.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset the shot profile for the passed mode back to the first state (State 0) and reset all sequences.

`restart()`

Restart the shot profile by calling reset() and enable().

Automatically called when one fo the restart_events is called.

`state`

Return current state index.

`state_name`

Return current state name.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

