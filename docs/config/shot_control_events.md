---
title: "shot_control_events:"
---

# shot_control_events:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Shot can contain `control_events:` which can move the shot to a specific
state.

## Required settings

The following sections are required in the `shot_control_events:`
section of your config:

### events:

One or more values, type: `string`. Use commas to separate multiple
values.

A list of one or more events, which triggers the move of the shot to a
specified state.

### state:

Single value, type: `int`.

The integer that is provided for the state the shot should move to when
the event is posted. States are indexed at `0`, which means the first
state is `0`, second state is `1`, etc.

## Optional settings

The following sections are optional in the `shot_control_events:`
section of your config. (If you don't include them, the default will be
used).

### force:

Single value, type: `boolean` (true/false). Default: `true`

If set to true, the state of shot will be modified even if the shot is
disabled. If set to false, this will be ignored unless the shot is
currently enabled when the event is posted.

### force_show:

Single value, type: `boolean` (true/false). Default: `false`

IF set to true, the show associated with this shot state will be played,
even if the shot is already in that state.

## Related How To Guides

* [shots:](shots.md)
