# diverters API Reference

`self.machine.diverters.*`

``` python
class mpf.devices.diverter.Diverter(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents a diverter in a pinball machine.

Args: Same as the Device parent class.

## Accessing diverters in code

The device collection which contains the `diverters` in your machine is available via `self.machine.diverters`. For example, to access one called “foo”, you would use `self.machine.diverters.foo`. You can also access diverters in dictionary form, e.g. `self.machine.diverters['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Diverters have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`activate()`

Physically activate this diverter's coil.

`deactivate()`

Deactivate this diverter.  This method will disable the activation_coil, and (optionally) if it's configured with a deactivation coil, it will pulse it.

`disable(auto=False)`

Disable this diverter. This method will remove the hardware rule if this diverter is activated via a hardware switch.

Parameters:

* **auto** – Boolean value which is used to indicate whether this diverter disabled itself automatically. This is passed to the event which is posted.
* ****kwargs** – This is here because this disable method is called by whatever event the game programmer specifies in their machine configuration file, so we don't know what event that might be or whether it has random kwargs attached to it.

`enable(auto=False)`

Enable this diverter.

Parameters:

* **auto** – Boolean value which is used to indicate whether this diverter enabled itself automatically. This is passed to the event which is posted.

If an `activation_switches` is configured, then this method writes a hardware autofire rule to the pinball controller which fires the diverter coil when the switch is activated. If no activation_switches is specified, then the diverter is activated immediately.

`event_activate(**kwargs)`

Handle activate control event.

`event_deactivate(**kwargs)`

Handle deactivate control event.

`event_disable(auto=False, **kwargs)`

Handle disable control event.

`event_enable(auto=False, **kwargs)`

Handle enable control event.

`event_reset(**kwargs)`

Handle reset control event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset and deactivate the diverter.

`schedule_deactivation()`

Schedule a delay to deactivate this diverter.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
