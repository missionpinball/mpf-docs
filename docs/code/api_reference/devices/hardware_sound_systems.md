# hardware_sound_systems API Reference

`self.machine.hardware_sound_systems.*`

``` python
class mpf.devices.hardware_sound_system.HardwareSoundSystem(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Hardware sound system using in EM and SS machines.

## Accessing hardware_sound_systems in code

The device collection which contains the `hardware_sound_systems` in your machine is available via `self.machine.hardware_sound_systems`. For example, to access one called “foo”, you would use `self.machine.hardware_sound_systems.foo`. You can also access hardware_sound_systems in dictionary form, e.g. `self.machine.hardware_sound_systems['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Hardware_sound_systems have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`decrease_volume(volume: float, track: int = 1)`

Increase volume.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`increase_volume(volume: float, track: int = 1)`

Increase volume.

`play(sound_number: int, track: int = 1)`

Play a sound.

`play_file(file: str, platform_options, track: int = 1)`

Play a sound file.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`set_volume(volume: float, track: int = 1)`

Set volume.

`stop_all_sounds(track: int = 1)`

Stop all sounds on track.

`text_to_speech(text: str, platform_options, track: int = 1)`

Text to speech output.
