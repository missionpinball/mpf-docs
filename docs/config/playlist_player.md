---
title: "playlist_player:"
---

# playlist_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `playlists:` section
    of a step.

The `playlist_player:` section of your config is where you specify
actions to perform on playlists when MPF events are received. Additional
information may be found in the
[playlist_player](../config_players/playlist_player.md) documentation.

Examples:

``` mpf-config
playlist_player:
  play_attract_music:
    playlist:
      playlist: attract_music
      action: play
  advance_playlist:
    playlist:
      action: advance
  stop_playlist:
    playlist:
      action: stop
```

Basic usage:

``` yaml
playlist_player:
  <triggering_event_name>:
    <playlist track name>:
      action: <action name>
      <optional settings>
  <triggering_event_name>:
    <playlist track name>:
      action: <action name>
      <optional settings>
```

## Optional settings

The following sections are optional in the `playlist_player:` section of
your config. (If you don't include them, the default will be used).

### action:

Single value, type: one of the following options: play, stop, advance,
set_repeat. Default: `play`

--8<-- "todo.md"

## Related How To guides

--8<-- "todo.md"
