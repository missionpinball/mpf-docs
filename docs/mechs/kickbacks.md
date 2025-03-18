---
title: Kickbacks
---

# Kickbacks


Related Config File Sections:

* [kickbacks:](../config/kickbacks.md)
* [ball_saves:](../config/ball_saves.md)

A kickback mechanism is a type of
[autofire coil](autofire_coils.md) that kicks the ball back into play, typically located in an
outlane. It is often paired with a
[ball_save](../config/ball_saves.md) to
compensate for missed kickbacks.

[TODO: Add a picture of a kickback](../about/help.md)

This is an example:

``` yaml
switches:
  s_kickback:
    number: 5
coils:
  c_kickback:
    number: 7
    default_pulse_ms: 15
kickbacks:
  ac_kickback:
    coil: c_kickback
    switch: s_kickback
ball_saves:
  kickback_ball_save:
    active_time: 5s
    enable_events: kickback_ac_kickback_fired
    auto_launch: true
    balls_to_save: 1
```

## Monitorable Properties

For
[dynamic values](../config/instructions/dynamic_values.md) and
[conditional events](../events/overview/conditional.md), the prefix for kickbacks is `device.kickbacks.(name)`.

*enabled*

:   Boolean (true/false) which shows whether this kickback is enabled.

## Related Events

* [kickback_(name)_fired](../events/kickback_kickback_fired.md)
