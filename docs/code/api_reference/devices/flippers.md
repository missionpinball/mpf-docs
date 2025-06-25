
# self.machine.flippers.*

``` python
class mpf.devices.flipper.Flipper(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents a flipper in a pinball machine. Subclass of Device. Contains several methods for actions that can be performed on this flipper, like enable(), disable(), etc. Flippers have several options, including player buttons, EOS swtiches, multiple coil options (pulsing, hold coils, etc.)

Parameters:

* **machine** – A reference to the machine controller instance.
* **name** – A string of the name you’ll refer to this flipper object as.

## Accessing flippers in code

The device collection which contains the `flippers` in your machine is available via `self.machine.flippers`. For example, to access one called “foo”, you would use `self.machine.flippers.foo`. You can also access flippers in dictionary form, e.g. `self.machine.flippers['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Flippers have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable the flipper.  This method makes it so the cabinet flipper buttons no longer control the flippers. Used when no game is active and when the player has tilted.

`enable()`

Enable the flipper by writing the necessary hardware rules to the hardware controller.  The hardware rules for coils can be kind of complex given all the options, so we’ve mapped all the options out here. We literally have methods to enable the various rules based on the rule letters here, which we’ve implemented below. Keeps it easy to understand. Note there’s a platform feature saved at: `self.machine.config['platform']['hw_enable_auto_disable']`. If True, it means that the platform hardware rules will automatically disable a coil that has been enabled when the trigger switch is disabled. If False, it means the hardware platform needs its own rule to disable the coil when the switch is disabled. Methods F and G below check for that feature setting and will not be applied to the hardware if it’s True.

Two coils, using EOS switch to indicate the end of the power stroke: Rule Type Coil Switch Action A. Enable Main Button active D. Enable Hold Button active E. Disable Main EOS active

One coil, using EOS switch: Rule Type Coil Switch Action A. Enable Main Button active H. PWM Main EOS active

Two coils, not using EOS switch: Rule Type Coil Switch Action B. Pulse Main Button active D. Enable Hold Button active

One coil, not using EOS switch: Rule Type Coil Switch Action C. Pulse/PWM Main button active

Use EOS switch for safety (for platforms that support multiple switch rules). Note that this rule is the letter “i”, not a numeral 1. I. Enable power if button is active and EOS is not active

`event_disable(**kwargs)`

Handle disable control event.  To prevent multiple rules at the same time we prioritize disable > enable.

`event_enable(**kwargs)`

Handle enable control event.  To prevent multiple rules at the same time we prioritize disable > enable.

`event_sw_flip(**kwargs)`

Handle sw_flip control event.

`event_sw_release(**kwargs)`

Handle sw_release control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`sw_flip()`

Activate the flipper via software as if the flipper button was pushed. This is needed because the real flipper activations are handled in hardware, so if you want to flip the flippers with the keyboard or OSC interfaces, you have to call this method. Note this method will keep this flipper enabled until you call sw_release().

`sw_release()`

Deactivate the flipper via software as if the flipper button was released. See the documentation for sw_flip() for details.
