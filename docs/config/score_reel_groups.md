---
title: "score_reel_groups: Config Reference"
---

# score_reel_groups: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `score_reel_groups:` section of your config is where you configure
groups of [score reels](score_reels.md).
Every reel only displays one digits so they have to be grouped to
display longer scores. See [How to Configure Score Reels](../mechs/score_reels.md) for more details.

## Required settings

The following sections are required in the `score_reel_groups:` section
of your config:

### reels:

List of one (or more) values, each is a type: string name of a
[score_reels:](score_reels.md) device.
Defaults to empty.

List the [score reels](score_reels.md) which
make up this group. Start with the highest digit. The last entry will be
the right most digit. You may use None if there is no reel for a digit.

## Optional settings

The following sections are optional in the `score_reel_groups:` section
of your config. (If you don't include them, the default will be used).

### chimes:

List of one (or more) values, each is a type: string name of a
[coils:](coils.md) device. Defaults to empty.

List the [coils:](coils.md) driving the chime
which are rung when the reel overflows. Start with the highest digit.
The last entry will be the right most digit. You may use None if there
is no chime for a digit.

### enable_chimes_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `ball_started`

Event(s) that enable chimes to activate when the corresponding score_reel advances.
available starting with mpf 0.57.5

### disable_chimes_events:

List of one (or more) device control events
([Instructions for entering device control events](instructions/device_control_events.md)). Default: `game_ended`

Event(s) that disable chimes activating when the corresponding score_reel advances. Useful for something like a
night mode for quieter gameplay.
available starting with mpf 0.57.5

### lights_tag:

Single value, type: `string`. Defaults to empty.

Lights to turn on when this group is active.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

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

Tag groups with the player which uses it. Add `player1` to use this reel
for player 1. Use `player2` for player 2 and so on. A reel can be used
for more than one player.

## Related How To guides

* [How to Configure Score Reels](../mechs/score_reels.md)
