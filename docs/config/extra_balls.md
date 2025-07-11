---
title: "extra_balls: Config Reference"
---

# extra_balls: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `extra_balls:` section of your config is where you configure which
events trigger and reset extra ball awards.

Note that this extra ball abstract device only takes care of awarding
the extra ball and can lit a light when enabled/available. The logic to
qualify for an extra ball has to be implemented in your mode. See
[Extra Balls](../game_logic/extra_balls.md) for more
details.

Here's an example:

``` yaml
##! mode: mode1
extra_balls:
  my_mode_eb:
    award_events: alien_smashed
```

In the above example, the extra ball called `my_mode_eb` will be given
to the player when the event `alien_smashed` is posted. After that,
future `alien_smashed` events will not lead to additional extra balls.
(The `my_mode_eb` extra ball is "used up", in a sense).

This is all tracked per-player in a player variable dictionary called
"extra_balls_awarded"

## Optional settings

The following sections are optional in the `extra_balls:` section of
your config. (If you don't include them, the default will be used).

### award_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Events in this list, when posted, award this extra ball to the current
player.

### enabled:

Single value, type: `boolean` (`true`/`false`). Default: `true`

Whether the device starts enabled or disabled.

### group:

Single value, type: `string` name of a
[extra_ball_groups:](extra_ball_groups.md)
device. Defaults to empty.

The extra ball group which this ball belongs to which can further limit
the maximum number of balls and enable/disable the device.

### light_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Defaults to empty.

Event to light the extra ball (if enabled).

### max_per_game:

Single value, type: `integer`. Default: `1`

Maximum number of extra balls to award per player for this particular
extra ball device. This might be further limited by the extra_ball_group
max_per_game limit. In that case if either of the two limits is exceeded
no more balls will be awarded.

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

A descriptive name for this device which will show up in the service
menu and reports.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Special / reserved tags for extra balls: *None*

See the
[documentation on tags](instructions/tags.md) for details.

## Related How To guides

* [Extra Balls](../game_logic/extra_balls.md)
