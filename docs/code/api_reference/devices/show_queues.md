# show_queues API Reference

`self.machine.show_queues.*`

``` python
class mpf.devices.show_queue.ShowQueue(machine, name)
```

Bases: `mpf.core.system_wide_device.SystemWideDevice`

Represents a show queue.

## Accessing show_queues in code

The device collection which contains the show_queues in your machine is available via `self.machine.show_queues`. For example, to access one called “foo”, you would use `self.machine.show_queues.foo`. You can also access show_queues in dictionary form, e.g. `self.machine.show_queues['foo']`.

You can also get devices by tag or hardware number. See the DeviceCollection documentation for details.

## Methods & Attributes

Show_queues have the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`enqueue_show(show_config: mpf.assets.show.ShowConfig, start_step: int)`

Add a show to the end of the queue.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.
