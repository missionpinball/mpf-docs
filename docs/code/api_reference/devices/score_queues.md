---
title: API Reference - score_queues
---

# score_queues API Reference

Config Reference:

* [score_queues:](../../../config/score_queues.md)

`self.machine.score_queues.*`

``` python
class mpf.devices.score_queue.ScoreQueue(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Score queues for SS games.

Add scores over time and play a lot of chimes.

## Accessing score_queues in code

The device collection which contains the score_queues in your machine is available via `self.machine.score_queues`. For example, to access one called “foo”, you would use `self.machine.score_queues.foo`. You can also access score_queues in dictionary form, e.g. `self.machine.score_queues['foo']`.  You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Score_queues have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`score(value, **kwargs)`

Score a value via the queue.

`stop_device()`
Stop queue.
