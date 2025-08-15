---
title: Coil player
---

# Coil player


The *coil player* is a
[config player](index.md)
that's used pulse, enable, or disable coils and drivers.

This is an example:

``` yaml
coil_player:
  some_event: coil_1
  some_other_event:
    coil_2:
      action: enable
      hold_power: .5
```

In the example above, when the event called `some_event` is posted,
coil_1 will pulse. When the event `some_other_event` is posted, coil_2
will enable (be held on) at power level 0.5 (means 50% of maximum
power).

Note that the `some_event: coil_1` is entered in a different way than
the `some_other_event:`. The first one has a simple key/value pair,
whereas the second has a complete nested sub-configuration.

The first example shows the "express" config, while the second shows
the full config. (What's an "express config?" Details
[here](../config/instructions/express_config.md).

The coil player's express config is the "pulse" action.

Example coil player from a show:

``` yaml
##! show: test
- time: 0
  coils:
    coil1: pulse
```

## Usage in config files

In config files, the coil player is used via the `coil_player:` section.

## Usage in shows

In shows, the coil player is used via the `coils:` section of a step.

## Related Pages

* [Coils (Solenoids)](../mechs/coils/index.md)
* [coil_player: Config Reference](../config/coil_player.md)
* [coil_player Api Reference](../code/api_reference/config_players/coil_player.md)
