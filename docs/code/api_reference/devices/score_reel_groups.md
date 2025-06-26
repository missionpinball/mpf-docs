# score_reel_groups API Reference

`self.machine.score_reel_groups.*`

``` python
class mpf.devices.score_reel_group.ScoreReelGroup(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents a logical grouping of score reels in a pinball machine.

Multiple individual ScoreReel object make up the individual digits of this group. This group also has support for the blank zero “inserts” that some machines use. This is a subclass of mpf.core.device.Device.

## Accessing score_reel_groups in code

The device collection which contains the score_reel_groups in your machine is available via `self.machine.score_reel_groups`. For example, to access one called “foo”, you would use `self.machine.score_reel_groups.foo`. You can also access score_reel_groups in dictionary form, e.g. `self.machine.score_reel_groups['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Score_reel_groups have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`classmethod chime(chime, **kwargs)`

Pulse chime.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`int_to_reel_list(value)`

Convert an integer to a list of integers that represent each positional digit in this ScoreReelGroup.

The list returned is in reverse order. (See the example below.)

The list returned is customized for this ScoreReelGroup both in terms of number of elements and values of None used to represent blank plastic zero inserts that are not controlled by a score reel unit.

For example, if you have a 5-digit score reel group that has 4 phyiscial reels in the tens through ten-thousands position and a fake plastic “0” insert for the ones position, if you pass this method a value of 12300, it will return [None, 0, 3, 2, 1]

This method will pad shorter ints with zeros, and it will chop off leading digits for ints that are too long. (For example, if you pass a value of 10000 to a ScoreReelGroup which only has 4 digits, the returns list would correspond to 0000, since your score reel unit has rolled over.)

Parameters:

* **value** – The interger value you'd like to convert.

Returns a list containing the values for each corresponding score reel, with the lowest reel digit position in list position 0.

`light(**kwargs)`

Light up this ScoreReelGroup based on the 'light_tag' in its config.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`set_value(value)`

Reset the score reel group to display the value passed.

This method will “jump” the score reel group to display the value that's passed as an it. (Note this “jump” technique means it will just move the reels as fast as it can, and nonsensical values might show up on the reel while the movement is in progress.)

This method is used to “reset” a reel group to all zeros at the beginning of a game, and can also be used to reset a reel group that is confused or to switch a reel to the new player's score if multiple players a sharing the same reel group.

Note you can choose to pass either an integer representation of the value, or a value list.

Parameters:

* **value** – An integer value of what the new displayed value (i.e. score) should be. This is the default option if you only pass a single positional argument, e.g. set_value(2100).

`unlight(**kwargs)`

Turn off the lights for this ScoreReelGroup based on the 'light_tag' in its config.

`wait_for_ready()`

Return a future which will be done when all reels reached their destination.
