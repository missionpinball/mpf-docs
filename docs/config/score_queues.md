---
title: "score_queues: Config Reference"
---

# score_queues: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `score_queues:` section of your config is where you configure SS
style scoring queues in MPF. This is an example:

``` yaml
coils:
  c_chime_1000:
    number:
  c_chime_100:
    number:
  c_chime_10:
    number:
score_queues:
  score:
    chimes: c_chime_1000, c_chime_100, c_chime_10,  None
##! mode: my_mode
# in your mode
score_queue_player:
  score_2k:
    score: 2000
  score_200:
    score: 200
```

## Required settings

The following sections are required in the `score_queues:` section of
your config:

### chimes:

List of one (or more) values, each is a type: string name of a
[coils:](coils.md) device. Defaults to empty.

A list of chimes to pulse when adding score via the score queue. Start
from the left the right on your digits. You might use None if a certain
digit does not have a chime. Example:
`c_chime_1000, c_chime_100, c_chime_10, None`

## Optional settings

The following sections are optional in the `score_queues:` section of
your config. (If you don't include them, the default will be used).

### delay:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `200ms`

The delay between adding scores (and pulsing a chime).

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

Not used.

## Related How To guides

* [How to implement solid state game style score queues in MPF](../game_logic/scoring/ss_style_score_queues.md)
