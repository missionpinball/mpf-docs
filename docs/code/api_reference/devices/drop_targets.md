
# self.machine.drop_targets.*

`class mpf.devices.drop_target.DropTarget(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice

Represents a single drop target in a pinball machine.

Args: Same as the Target parent class

## Accessing drop_targets in code

The device collection which contains the `drop_targets` in your machine is available via `self.machine.drop_targets`. For example, to access one called “foo”, you would use `self.machine.drop_targets.foo`. You can also access drop_targets in dictionary form, e.g. `self.machine.drop_targets['foo']`.  You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Drop_targets have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_to_bank(bank)`

Add this drop target to a drop target bank. This allows the bank to update its status based on state changes to this drop target.

Parameters:
* **bank** – DropTargetBank object to add this drop target to.

`disable_keep_up()`

No longer keep up the target up.

`enable_keep_up()`

Keep the target up by enabling the coil.

`event_disable_keep_up(**kwargs)`

Handle disable_keep_up control event.

`event_enable_keep_up(**kwargs)`

Handle enable_keep_up control event.

`event_knockdown(**kwargs)`

Handle knockdown control event.

`event_reset(**kwargs)`

Handle reset control event.

`external_reset_from_bank()`

Handle the reset from our bank. The bank might pulse the coil from this device or it might have a separate reset coil which will trigger a reset on switch of this device. Make sure we do not mark the playfield as active.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`knockdown()`

Pulse the knockdown coil to knock down this drop target.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_from_bank(bank)`

Remove the DropTarget from a bank.

Parameters:

* **bank** – DropTargetBank object to remove

`reset()`

Reset this drop target. If this drop target is configured with a reset coil, then this method will pulse that coil. If not, then it checks to see if this drop target is part of a drop target bank, and if so, it calls the reset() method of the drop target bank. This method does not reset the target profile, however, the switch event handler should reset the target profile on its own when the drop target physically moves back to the up position.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

