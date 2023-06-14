---
title: counter_control_events:
---

# counter_control_events:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Counter can contain `control_events:` which can add or substract to the
count of your counter. Alternatively, you can set the counter to a
certain value using an event.

## Required settings

The following sections are required in the `counter_control_events:`
section of your config:

### action:

Single value, type: one of the following options: add, subtract, jump.

`add` will add `value` to the current count of your counter. `subtract`
will subtract `value` from the current count of your counter. `jump`
will set your counter to `value`.

### event:

Single value, type: `string`.

The event to trigger the `action`.

## Optional settings

The following sections are optional in the `counter_control_events:`
section of your config. (If you don't include them, the default will be
used).

### value:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)).

The value to use in `action`.

## Related How To guides

* [counters:](counters.md)
