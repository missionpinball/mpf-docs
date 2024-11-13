
# self.machine.kickbacks.*

`class mpf.devices.kickback.Kickback(*args, **kwargs)`

Bases: mpf.devices.autofire.AutofireCoil

A kickback device which will fire a ball back into the playfield.

## Accessing kickbacks in code

The device collection which contains the kickbacks in your machine is available via `self.machine.kickbacks`. For example, to access one called “foo”, you would use `self.machine.kickbacks.foo`. You can also access kickbacks in dictionary form, e.g. `self.machine.kickbacks['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Kickbacks have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable the autofire device.

This is typically called at the end of a ball and when a tilt event happens.

Parameters:

* ****kwargs** – Not used, just included so this method can be used as an event callback.

`enable()`

Enable the autofire device.

This causes the coil to respond to the switch hits. This is typically called when a ball starts to enable the slingshots, pops, etc.

Note that there are several options for both the coil and the switch which can be incorporated into this rule, including recycle times, switch debounce, reversing the switch (fire the coil when the switch goes inactive), etc. These rules vary by hardware platform. See the user documentation for the hardware platform for details.

Parameters:

* ****kwargs** – Not used, just included so this method can be used as an event callback.

`event_disable(**kwargs)`

Handle disable control event.

To prevent multiple rules at the same time we prioritize disable > enable.

`event_enable(**kwargs)`

Handle enable control event.

To prevent multiple rules at the same time we prioritize disable > enable.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

