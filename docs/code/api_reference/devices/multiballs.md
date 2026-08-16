---
title: API Reference - multiballs
---

# multiballs API Reference

Config Reference:

* [multiballs:](../../../config/multiballs.md)

`self.machine.multiballs.*`

``` python
class mpf.devices.multiball.Multiball(*args, **kwargs)
```

Bases: `mpf.core.enable_disable_mixin.EnableDisableMixin`, `mpf.core.system_wide_device.SystemWideDevice`, `mpf.core.mode_device.ModeDevice`

Multiball device for MPF.

## Accessing multiballs in code

The device collection which contains the multiballs in your machine is available via `self.machine.multiballs`. For example, to access one called “foo”, you would use `self.machine.multiballs.foo`. You can also access multiballs in dictionary form, e.g. `self.machine.multiballs['foo']`. You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Multiballs have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_a_ball()`

Add a ball if multiball has started.

`disable()`

Disable device.

`enable() → None`

Enable device.

`enabled`

Return true if enabled.

`event_add_a_ball(**kwargs)`

Event handler for add_a_ball event.

`event_disable(**kwargs)`

Handle disable control event.

`event_enable(**kwargs)`

Handle enable control event.

`event_reset(**kwargs)`

Event handler for reset event.

`event_start(**kwargs)`

Event handler for start event.

`event_start_or_add_a_ball(**kwargs)`

Event handler for start_or_add_a_ball event.

`event_stop(**kwargs)`

Event handler for stop event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`get_placeholder_value(item)`

Get the value of a placeholder.

`persist_enabled`

Return if enabled is persisted.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`reset()`

Reset the multiball and disable it.

`start()`

Start multiball.

`start_or_add_a_ball()`

Start multiball or add a ball if multiball has started.

`stop()`

Stop shoot again.

`subscribe_attribute(item, machine)`

Subscribe to an attribute.
