# timers API Reference

`self.machine.timers.*`

``` python
class mpf.devices.timer.Timer(*args, **kwargs)
```

Bases: `mpf.core.mode_device.ModeDevice`

Parent class for a mode timer.

Parameters:

* **machine** – The main MPF MachineController object.
* **name** – The string name of this timer.

## Accessing timers in code

The device collection which contains the timers in your machine is available via `self.machine.timers`. For example, to access one called “foo”, you would use `self.machine.timers.foo`. You can also access timers in dictionary form, e.g. `self.machine.timers['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Timers have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add(timer_value, **kwargs)`

Add ticks to this timer.

Parameters:

* **timer_value** – The number of ticks you want to add to this timer’s current value.
* **kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`change_tick_interval(change=0.0, **kwargs)`

Change the interval for each “tick” of this timer.

Parameters:

* **change** – Float or int of the change you want to make to this timer’s tick rate. Note this value is multiplied by the current tick interval: >1 will increase the tick interval (slow the timer) and <1 will decrease the tick interval (accelerate the timer). To set an absolute value, use the set_tick_interval() method.
* **`**kwargs`** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`enable() → None`

Enable handler.

`event_enable(**kwargs)`

Event handler for enable event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`jump(timer_value, **kwargs)`

Set the current amount of time of this timer.

This value is expressed in “ticks” since the interval per tick can be something other than 1 second).

Parameters:

* **timer_value** – Integer of the current value you want this timer to be.
* ****kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`pause(timer_value=0, **kwargs)`

Pause the timer and posts the `timer_(name)_paused` event.

Parameters:

* **timer_value** – How many seconds you want to pause the timer for. Note that this pause time is real-world seconds and does not take into consideration this timer’s tick interval.
* ****kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset(**kwargs)`

Reset this timer based to the starting value that’s already been configured.

Does not start or stop the timer.

Parameters:

* ****kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`restart(**kwargs)`

Restart the timer by resetting it and then starting it.

Essentially this is just a reset() then a start().

Parameters:

* ****kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`set_tick_interval(timer_value, **kwargs)`

Set the number of seconds between ticks for this timer.

This is an absolute setting. To apply a change to the current value, use the change_tick_interval() method.

Parameters:

* **timer_value** – The new number of seconds between each tick of this timer. This value should always be positive.
* **`**kwargs`** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`start(**kwargs)`

Start this timer based on the starting value that’s already been configured.

Use jump() if you want to set the starting time value.

Parameters:

* ****kwargs** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`stop(**kwargs)`

Stop the timer and posts the `timer_(name)_stopped` event.
Parameters:	`**kwargs` – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`subtract(timer_value, **kwargs)`

Subtract ticks from this timer.

Parameters:

* **timer_value** – The number of ticks you want to subtract from this timer’s current value.
* **`**kwargs`** – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.

`ticks`

Return ticks.

`timer_complete(**kwargs)`

Automatically called when this timer completes.

Posts the `timer_(name)_complete` event. Can be manually called to mark this timer as complete.
Parameters:	`**kwargs` – Not used in this method. Only exists since this method is often registered as an event handler which may contain additional keyword arguments.
