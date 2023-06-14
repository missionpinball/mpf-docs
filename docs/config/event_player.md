---
title: event_player:
---

# event_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `events:` section of
    a step.

You can use the `event_player:` section of your config files to cause
additional events to be automatically posted when a specific event is
posted. The event_player can be thought of as a really simple way to
implement game logic. (e.g. "When this happens, do this.")

If you add this section to your machine-wide config file, the entries
here will always be active. If you enter it into a mode-specific config
file, entries will only be active while that mode is active.

This is an example:

``` mpf-config
event_player:
  ball_starting:
    - show_ball_start_animation
    - play_start_sound
    - start_first_mode
  ball_ending:
    - show_ball_ending_animation
    - play_drain_sound
```

See [Event player](../config_players/event_player.md) for
details.

## Related How To guides

* [Event player](../config_players/event_player.md)
