---
title: Mode config files
---

# Mode config files


Modes usually start with a `mode:` section (see
[mode](../mode.md)) which defines their
priority and when they start or stop:

``` yaml
##! mode: mode1
mode:
  start_events: ball_starting
  stop_events: timer_mode_timer_complete, shot_right_ramp
  priority: 300
```

Not all config sections can be used in your machine-wide config (see
[Machine config files](machine_config.md)). Some
devices may only exist in modes (usually if they require an active game
with one or more players). You can see if this is the case at the top of
the relevant [config](../index.md)
section. For instance
[extra_balls](../extra_balls.md) are
player-bound and can only be used in modes.
