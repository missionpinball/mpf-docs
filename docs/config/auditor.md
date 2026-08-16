---
title: "auditor: Config Reference"
---

# auditor: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The *auditor:* section of the machine configuration file lets you
control what events the MPF's auditor module includes in its audits.

Here's an example which is the settings we including in the default
*mpfconfig.yaml* file. (So these are the settings that are included by
default with every game you run.) Also, by default, the auditor saves
its audits to `/audits/audits.yaml` in the folder for each machine.
(Check out the documentation on the Auditor to see a sample audit log
file.)

``` yaml
auditor:
    save_events:
      -  game_started
      -  ball_ended
      -  game_ended
    num_player_top_records: 10
    audit:
      -  shots
      -  switches
      -  events
      -  player
    events:
      -  game_started
      -  game_ended
    player:
      -  score

```

## Optional settings

The following sections are optional in the `auditor:` section of your
config. (If you don't include them, the default will be used).

### audit:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

This is a list of the various types of things you want to include in
your audit file. There are currently four options:

* shots - tracks the number of times each shot has been made
* switches - tracks the number of times each switch has been hit.
* events - whether the auditor should audit certain events. (Add the
    events you want to track to the *events* section.)
* player - includes player variables (score, maybe shots or goals
    they've achieved, etc.) See the *player* section below for details.

### events:

List of one (or more) events. The device will add handlers for those
events. Defaults to empty.

A list of which events you want to audit. These are the names of any
events you want.

### num_player_top_records:

Single value, type: `integer`. Default: `1`

For player-specific variables, you have the option of track the "top"
number of each. So in the example above, since the only player item is
*score*, the auditor will track the top 10 highest scores, plus the
total count and the overall average.

### player:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

A list of player variables you want to audit. The auditor will save a
certain number (configurable via the `num_player_top_records:` setting),
as well as the total number of entries and the current average.

### reset_audit_events:

List of one (or more) events. The device will add handlers for those
events. Default: `auditor_reset,factory_reset`

Events to reset audits in the machine. This is used by the service mode.

### save_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `ball_ended`

Default: `ball_ended`

Events in this list, when posted, trigger the auditor to save its audits
to disk.

## Related Pages:

* [Auditor](../machine_management/auditor.md)
* [auditor API Reference](../code/api_reference/core/auditor.md)
