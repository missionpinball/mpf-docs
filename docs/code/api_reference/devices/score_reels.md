# score_reels API Reference

`self.machine.score_reels.*`

``` python
class mpf.devices.score_reel.ScoreReel(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents an individual electro-mechanical score reel in a pinball machine.

Multiples reels of this class can be grouped together into ScoreReelGroups which collectively make up a display like “Player 1 Score” or “Player 2 card value”, etc.

This device class is used for all types of mechanical number reels in a machine, including reels that have more than ten numbers and that can move in multiple directions (such as the credit reel).

## Accessing score_reels in code

The device collection which contains the score_reels in your machine is available via `self.machine.score_reels`. For example, to access one called “foo”, you would use `self.machine.score_reels.foo`. You can also access score_reels in dictionary form, e.g. `self.machine.score_reels['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Score_reels have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`check_hw_switches()`

Check all the value switches for this score reel.

This check only happens if self.ready is True. If the reel is not ready, it means another advance request has come in after the initial one. In that case then the subsequent advance will call this method again when after that advance is done.

If this method finds an active switch, it sets self.physical_value to that. Otherwise it sets it to -999. It will also update self.assumed_value if it finds an active switch. Otherwise it leaves that value unchanged.

This method is automatically called (via a delay) after the reel advances. The delay is based on the config value self.config[‘hw_confirm_time’].

TODO: What happens if there are multiple active switches? Currently it will return the highest one. Is that ok?

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`set_destination_value(value)`

Return the integer value of the destination this reel is moving to.

Parameters:

* **value** – Destination value which this reel should try to reach.

Returns: The value of the destination. If the current
`self.assumed_value` is -999, this method will always return -999 since it doesn’t know where the reel is and therefore doesn’t know what the destination value would be.

`stop(**kwargs)`

Stop device.

`wait_for_ready()`

Return a future for ready.
