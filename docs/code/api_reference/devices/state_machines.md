---
title: API Reference - state_machines
---

# state_machines API Reference

Config Reference:

* [state_machines:](../../../config/state_machines.md)

`self.machine.state_machines.*`

``` python
class mpf.devices.state_machine.StateMachine(*args, **kwargs)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

A generic state machine.

## Accessing state_machines in code

The device collection which contains the state_machines in your machine is available via `self.machine.state_machines`. For example, to access one called “foo”, you would use `self.machine.state_machines.foo`. You can also access state_machines in dictionary form, e.g. `self.machine.state_machines['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

State_machines have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enable() → None`

Enable handler.

`event_enable(**kwargs)`

Event handler for enable event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`state`

Return the current state.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
