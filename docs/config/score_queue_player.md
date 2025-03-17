---
title: "score_queue_player:"
---

# score_queue_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `score_queue_player:` section of your config is where you configure
your SS style scoring. This is an example:

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
    debug: true
##! mode: my_mode
# in your mode
score_queue_player:
  score_2k:
    score: 2000
  score_200:
    score: 200
```

## Optional settings

The following sections are optional in the `score_queue_player:` section
of your config. (If you don't include them, the default will be used).

### int:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)). Defaults to empty.

Score value to add to the queue.

## Related How To guides

* [How to implement solid state game style score queues in MPF](../game_logic/scoring/ss_style_score_queues.md)
