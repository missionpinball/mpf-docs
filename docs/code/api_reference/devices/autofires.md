
# self.machine.autofires.*

``` python
class mpf.devices.autofire.AutofireCoil(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Autofire coils which fire based on switch hits with a hardware rule. Coils in the pinball machine which should fire automatically based on switch hits using defined hardware switch rules. Autofire coils work with rules written to the hardware pinball controller that allow them to respond “instantly” to switch hits versus waiting for the lag of USB and the host computer. Examples of Autofire Coils are pop bumpers, slingshots, and kicking targets. (Flippers use the same autofire rules under the hood, but flipper devices have their own device type in MPF.

## Accessing autofires in code

The device collection which contains the autofires in your machine is available via `self.machine.autofires`. For example, to access one called “foo”, you would use self.machine.autofires.foo. You can also access autofires in dictionary form, e.g. `self.machine.autofires['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Autofires have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`disable()`

Disable the autofire device. This is typically called at the end of a ball and when a tilt event happens.

Parameters:

* ****kwargs** – Not used, just included so this method can be used as an event callback.

`enable()`

Enable the autofire device. This causes the coil to respond to the switch hits. This is typically called when a ball starts to enable the slingshots, pops, etc. Note that there are several options for both the coil and the switch which can be incorporated into this rule, including recycle times, switch debounce, reversing the switch (fire the coil when the switch goes inactive), etc. These rules vary by hardware platform. See the user documentation for the hardware platform for details.

Parameters:

* ****kwargs** – Not used, just included so this method can be used as an event callback.

`event_disable(**kwargs)`

Handle disable control event. To prevent multiple rules at the same time we prioritize disable > enable.

`event_enable(**kwargs)`

Handle enable control event. To prevent multiple rules at the same time we prioritize disable > enable.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
