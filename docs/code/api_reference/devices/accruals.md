# accruals API Reference

Config Reference:

* [accruals:](../../../config/accruals.md)

`self.machine.accruals.*`

``` python
class mpf.devices.logic_blocks.Accrual(*args, **kwargs)
```

Bases: `mpf.devices.logic_blocks.LogicBlock`

A type of LogicBlock which tracks many different events (steps) towards a goal. The steps are able to happen in any order.

## Accessing accruals in code

The device collection which contains the accruals in your machine is available via `self.machine.accruals`. For example, to access one called “foo”, you would use `self.machine.accruals.foo`. You can also access accruals in dictionary form, e.g. `self.machine.accruals['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Accruals have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`complete()`

Mark this logic block as complete. Posts the 'events_when_complete' events and optionally restarts this logic block or disables it, depending on this block's configuration settings.

`completed`

Return if completed.

`disable()`

Disable this logic block. Automatically called when one of the disable_event events is posted. Can also manually be called.

`enable()`

Enable this logic block. Automatically called when one of the enable_event events is posted. Can also manually be called.

`enabled`

Return if enabled.

`event_advance_random(**kwargs)`

Event handler for advance random events.

`event_disable(**kwargs)`

Event handler for disable event.

`event_enable(**kwargs)`

Event handler for enable event.

`event_reset(**kwargs)`

Event handler for reset event.

`event_restart(**kwargs)`

Event handler for restart event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`get_start_value() → List[bool]`

Return start states.

`hit(step: int, **kwargs)`

Increase the hit progress towards completion. Automatically called when one of the count_events is posted. Can also manually be called.

Parameters:

* **step** – Integer of the step number (0 indexed) that was just hit.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset the progress towards completion of this logic block. Automatically called when one of the reset_event events is called. Can also be manually called.

`restart()`

Restart this logic block by calling reset() and enable(). Automatically called when one of the restart_event events is called. Can also be manually called.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.

`value`

Return value or None if that is currently not possible.
