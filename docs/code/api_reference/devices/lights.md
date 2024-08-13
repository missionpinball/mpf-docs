
# self.machine.lights.*

`class mpf.devices.light.Light(*args, **kwargs)`

Bases: mpf.core.system_wide_device.SystemWideDevice, mpf.devices.device_mixins.DevicePositionMixin

A light in a pinball machine.

## Accessing lights in code

The device collection which contains the lights in your machine is available via `self.machine.lights`. For example, to access one called “foo”, you would use `self.machine.lights.foo`. You can also access lights in dictionary form, e.g. `self.machine.lights['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Lights have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_stack()`

Remove all entries from the stack and resets this light to ‘off’.

`color(color, fade_ms=None, priority=0, key=None, start_time=None)`

Add or update a color entry in this light’s stack.

Calling this methods is how you tell this light what color you want it to be.

Parameters:

* **color** – RGBColor() instance, or a string color name, hex value, or 3-integer list/tuple of colors.
* **fade_ms** – Int of the number of ms you want this light to fade to the color in. A value of 0 means it’s instant. A value of None (the default) means that it will use this light’s and/or the machine’s default fade_ms setting.
* **priority** – Int value of the priority of these incoming settings. If this light has current settings in the stack at a higher priority, the settings you’re adding here won’t take effect. However they’re still added to the stack, so if the higher priority settings are removed, then the next-highest apply.
* **key** – An arbitrary identifier (can be any immutable object) that’s used to identify these settings for later removal. If any settings in the stack already have this key, those settings will be replaced with these new settings.
* **start_time** – Time this occured to synchronize lights.

`color_correct(color)`

Apply the current color correction profile to the color passed.

Parameters:

* **color** – The RGBColor() instance you want to get color corrected.

Returns an updated RGBColor() instance with the current color correction profile applied.

Note that if there is no current color correction profile applied, the returned color will be the same as the color that was passed.

`fade_in_progress`

Return true if a fade is in progress.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`gamma_correct(color)`

Apply max brightness correction to color.
Parameters:

* **color** – The RGBColor() instance you want to have gamma applied.

Returns an updated RGBColor() instance with gamma corrected.

`get_color()`

Return an RGBColor() instance of the ‘color’ setting of the highest color setting in the stack.

This is usually the same color as the physical light, but not always (since physical lights are updated once per frame, this value could vary.

Also note the color returned is the “raw” color that does has not had the color correction profile applied.

`get_color_below(priority, key)`

Return an RGBColor() instance of the ‘color’ setting of the highest color below a certain key.

Similar to get_color.

`get_hw_numbers()`

Return a list of all hardware driver numbers.

`get_placeholder_value(item)`

Get the value of a placeholder.

`get_successor_number()`

Get the number of the next light channel.

We first have to find the last channel and then get the next number based on that.

`off(fade_ms=None, priority=0, key=None, **kwargs)`

Turn light off.

Parameters:

* **key** – key for removal later on
* **priority** – priority on stack
* **fade_ms** – duration of fade

`on(brightness=None, fade_ms=None, priority=0, key=None, **kwargs)`

Turn light on.

Parameters:

* **brightness** – Brightness factor for “on”.
* **key** – key for removal later on
* **priority** – priority on stack
* **fade_ms** – duration of fade

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`remove_from_stack_by_key(key, fade_ms=None)`

Remove a group of color settings from the stack.

Parameters:

* **key** – The key of the settings to remove (based on the ‘key’ parameter that was originally passed to the color() method.)
* **fade_ms** – Time to fade out the light.

This method triggers a light update, so if the highest priority settings were removed, the light will be updated with whatever’s below it. If no settings remain after these are removed, the light will turn off.

`stack`

A list of dicts which represents different commands that have come in to set this light to a certain color (and/or fade). Each entry in the list contains the following key/value pairs:

        `priority`:
            The relative priority of this color command. Higher numbers take precedent, and the highest priority entry will be the command that’s currently active. In the event of a tie, whichever entry was added last wins (based on ‘start_time’ below).
        `start_time`:
            The clock time when this command was added. Primarily used to calculate fades, but also used as a tie-breaker for multiple entries with the same priority.
        `start_color`:
            RGBColor() of the color of this light when this command came in.
        `dest_time`:
            Clock time that represents when a fade (from start_color to dest_color) will be done. If this is 0, that means there is no fade. When a fade is complete, this value is reset to 0.
        `dest_color`:
            RGBColor() of the destination this light is fading to. If a command comes in with no fade, then this will be the same as the ‘color’ below.
        `key`:
            An arbitrary unique identifier to keep multiple entries in the stack separate. If a new color command comes in with a key that already exists for an entry in the stack, that entry will be replaced by the new entry. The key is also used to remove entries from the stack (e.g. when shows or modes end and they want to remove their commands from the light).

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`wait_for_loaded()`

Return future.

`x`

Get the X value from the config.

Returns the devices x position from config

`y`

Get the Y value from the config.

Returns the devices y position from config

`z`

Get the Z value from the config.

Returns the devices z position from config

