---
title: API Reference - counters
---

# counters API Reference

Config Reference:

* [counters:](../../../config/counters.md)

`self.machine.counters.*`

``` python
class mpf.devices.logic_blocks.Counter(machine: mpf.core.machine.MachineController, name: str)
```

Bases: `mpf.devices.logic_blocks.LogicBlock`

A type of LogicBlock that tracks multiple hits of a single event. This counter can be configured to track hits towards a specific end-goal (like number of tilt hits to tilt), or it can be an open-ended count (like total number of ramp shots). It can also be configured to count up or to count down, and can have a configurable counting interval.

## Accessing counters in code

The device collection which contains the counters in your machine is available via `self.machine.counters`. For example, to access one called “foo”, you would use `self.machine.counters.foo`. You can also access counters in dictionary form, e.g. `self.machine.counters['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Counters have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`check_complete(count_complete_value=None)`

Check if counter is completed. Return true if the counter has reached or surpassed its specified completion value, return False if no completion criteria or is not complete.

`complete()`

Mark this logic block as complete. Posts the`events_when_complete` events and optionally restarts this logic block or disables it, depending on this block's configuration settings.

`completed`

Return if completed.

`count()`

Increase the hit progress towards completion. This method is also automatically called when one of the count_events is posted.

`disable()`

Disable this logic block. Automatically called when one of the disable_event events is posted. Can also manually be called.

`enable()`

Enable this logic block. Automatically called when one of the enable_event events is posted. Can also manually be called.

`enabled`

Return if enabled.

`event_add(value, **kwargs)`

Add to the value of this counter.

Parameters:

* **value** – Value to add to the counter.
* **kwargs** – Additional arguments.

`event_count(**kwargs)`

Event handler for count events.

`event_disable(**kwargs)`

Event handler for disable event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_jump(value, **kwargs)`

Set the internal value of the counter.

Parameters:

* **value** – Value to add to jump to.
* **kwargs** – Additional arguments.

`event_reset(**kwargs)`

Event handler for reset event.

`event_restart(**kwargs)`

Event handler for restart event.

`event_subtract(value, **kwargs)`

Subtract from the value of this counter.

Parameters:

* **value** – Value to subtract from the counter.
* **kwargs** – Additional arguments.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`get_start_value() → int`

Return start count.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset the progress towards completion of this logic block. Automatically called when one of the reset_event events is called. Can also be manually called.

`restart()`

Restart this logic block by calling reset() and enable(). Automatically called when one of the restart_event events is called. Can also be manually called.

`stop_ignoring_hits(**kwargs)`

Cause the Counter to stop ignoring subsequent hits that occur within the 'multiple_hit_window'. Automatically called when the window time expires. Can safely be manually called.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`value`

Return value or None if that is currently not possible.
