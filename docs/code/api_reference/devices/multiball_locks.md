# multiball_locks API Reference

`self.machine.multiball_locks.*`

``` python
class mpf.devices.multiball_lock.MultiballLock(*args, **kwargs)
```

Bases: `mpf.core.enable_disable_mixin.EnableDisableMixin`, `mpf.core.mode_device.ModeDevice`

Ball lock device which locks balls for a multiball.

## Accessing multiball_locks in code

The device collection which contains the multiball_locks in your machine is available via `self.machine.multiball_locks`. For example, to access one called “foo”, you would use `self.machine.multiball_locks.foo`. You can also access multiball_locks in dictionary form, e.g. `self.machine.multiball_locks['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Multiball_locks have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

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

`event_reset_all_counts(**kwargs)`

Event handler for reset_all_counts event.

`event_reset_count_for_current_player(**kwargs)`

Event handler for reset_count_for_current_player event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`is_virtually_full`

Return true if lock is full.

`locked_balls`

Return the number of locked balls for the current player.

`persist_enabled`

Return if enabled is persisted.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

 Raise a ConfigFileError exception.

`remaining_virtual_space_in_lock`

Return the remaining capacity of the lock.

`reset_all_counts()`

Reset the locked balls for all players.

`reset_count_for_current_player()`

Reset the locked balls for the current player.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
