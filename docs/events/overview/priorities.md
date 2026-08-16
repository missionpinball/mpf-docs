---
title: Handler Priorities
---

# Handler Priorities


When you have some code you want to register to be a handler for an
event, you can optionally specify a priority. (Priority is just an
integer value.) The default priority for events is 1. If you want a
guarantee that a certain event handler will fire last, then register
that handler with a priority that's lower than any other handler for
that event. And if you want to guarantee that a handler fires first,
register it with a higher priority. (In this case, "higher" and
"lower" are literal. A handler with a priority of 500 will be called
before a handler of 100.)

The actual integer values of the priorities are arbitrary. They're
called one-by-one, one after the other, in order from highest to lowest.
Whether your priorities are 3, 2, and 1, or 1000, 100 and 0, or 1000,
999, 998, and 1 makes no difference.

MPF automatically registers event handlers from modes with the priority
of that mode, meaning high-priority modes get access to an event before
lower-priority modes. (This is useful since it gives higher-priority
modes a chance to "block" events from lower-priority modes.)

See [Device Control Events](../../config/instructions/device_control_events.md) on how to use event handlers in devices.
