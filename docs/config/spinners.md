---
title: "spinners:"
---

# spinners:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Spinner devices provide accruals for switches that are hit in rapid
succession, and post events based on timeouts after switch hits.

``` yaml
#! switches:
#!   s_orbit_spinner:
#!     number:
#!   s_top_loop_left:
#!     number:
#!   s_top_loop_right:
#!     number:
spinners:
  basic_spinner:
    switch: s_orbit_spinner
    active_ms: 500
  dual_spinner:
    switches: s_top_loop_left, s_top_loop_right
    labels: left, right
    active_ms: 1200
    idle_ms: 2400
```

A spinner becomes "active" when a `switch:` or `switches:` is hit, and
remains active as long as switch hits continue. The time specified by
`active_ms:` determines how long the spinner will wait after the last
hit before it is no longer active.

If an `idle_ms:` time is specified, the spinner will move from
"active" to "inactive" for that duration, before finally settling on
"idle". If a switch is hit while idle, the spinner will become active
again. If no `idle_ms:` time is specified, the spinner will go directly
from active to idle.

The basic flow:

1. Spinner sits in idle state

2. A spinner switch is hit
    1. The spinner becomes "active" and sets a timeout for `active_ms:` duration
    2. The spinner posts [*spinner_\(name\)_active*](../events/spinner_spinner_active.md) event
    3. The spinner posts [*spinner_\(name\)_hit*](../events/spinner_spinner_hit.md) event

3. Additional switch hits occur
    1. The spinner resets the timeout for another `active_ms:` duration
    2. The spinner posts a [*spinner_\(name\)_hit*](../events/spinner_spinner_hit.md) event for each hit

4. Switch hits stop and the active delay timer expires
    1. The spinner switches to "inactive" state
    2. The spinner posts [*spinner_\(name\)_inactive*](../events/spinner_spinner_inactive.md) event
    3. (Optional) If `idle_ms:` is defined, the spinner sets a timeout for idle_ms duration

5. (Optional) No switch hits occur and the idle delay timer expires
    1. The spinner posts [*spinner_\(name\)_idle*](../events/spinner_spinner_idle.md) event
    2. The spinner switches to "idle" state

## Optional settings

The following sections are optional in the `spinners:` section of your
config. (If you don't include them, the default will be used).

### active_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `1000ms`

How long the spinner should stay active after the last switch hit. The
hit count resets each time the spinner becomes active, so this value
determines when one group of spins ends and the next begins.

### disable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Default: `None`

Events in this list, when posted, disable this spinner. If a spinner is
disabled, then hits to it have no effect.

### enable_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Default: `None`

Events in this list, when posted, enable this spinner. If a spinner is
not enabled, then hits to it have no effect.

### idle_ms:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

How long the spinner should stay inactive before going idle. This time
is counted *after* the `active_ms:` has expired, and is useful for
displaying slides or widgets for a while after switch hits stop.

### labels:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

A list of labels to apply to the switches in the spinner. If used, the
number of labels should equal the number of switches.

When a spinner switch is hit and `labels:` are defined, additional
events will be posted with [*spinner_\(name\)_\(label\)_active*](../events/spinner_spinner_label_active.md) and
[*spinner_\(name\)_\(label\)_hit*](../events/spinner_spinner_label_hit.md). This allows the game to trigger
different behavior based on which spinner switch is hit first or spins
more times.

### playfield:

Single value, type: `string` name of a
[playfields:](playfields.md) device. Default:
`playfield`

The name of the playfield that this spinner is on. The default setting
is "playfield", so you only have to change this value if you have more
than one playfield and you're managing them separately.

### reset_when_inactive:

Single value, type: `boolean` (`true`/`false`). Default: `true`

When true, the spinners `hit` count will reset when the spinner goes
inactive (after the `active_ms:` expires).

When false, the spinner's `hit` count will reset when the spinner goes
idle (after the `idle_ms:` expires)

This value has no effect if `idle_ms:` is not set.

### switch:

List of one (or more) values, each is a type: string name of a
[switches:](switches.md) device. Defaults to
empty.

The name of the switch (or a list of switches) for this spinner. You can
use multiple switches if the playfield has a series of spinners that
work together (for example at both ends of a horseshoe loop).

### switches:

List of one (or more) values, each is a type: string name of a
[switches:](switches.md) device. Defaults to
empty.

This setting is the same as the `switch:` setting above. You can
technically enter a single switch or a list of switches in either the
`switch:` setting or the `switches:` setting, but we include both since
it was confusing to be able to enter multiple switches for a singlular
"switch" setting and vice versa.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the
[documentation on the debug setting](instructions/debug.md) for details.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this device in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

## Related How To guides

* [Spinners](../mechs/spinners.md)
