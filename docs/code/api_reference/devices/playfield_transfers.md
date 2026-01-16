---
title: API Reference - playfield_transfers
---

# playfield_transfers API Reference

Config Reference:

* [playfield_transfers:](../../../config/playfield_transfers.md)

`self.machine.playfield_transfers.*`

``` python
class mpf.devices.playfield_transfer.PlayfieldTransfer(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Device which move a ball from one playfield to another.

## Accessing playfield_transfers in code

The device collection which contains the playfield_transfers in your machine is available via `self.machine.playfield_transfers`. For example, to access one called “foo”, you would use `self.machine.playfield_transfers.foo`. You can also access playfield_transfers in dictionary form, e.g. `self.machine.playfield_transfers['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

`Playfield_transfers have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`event_transfer(**kwargs)`

Event handler for transfer event.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`transfer()`

Transfer a ball to the target playfield.
