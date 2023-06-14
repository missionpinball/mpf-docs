---
title: logging:
---

# logging:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

In the logging section you can configure which how verbose parts of MPFs
should log.

``` mpf-config
logging:
  console:
    asset_manager: none
    ball_controller: none
    ball_search: basic
    bcp: basic
    bcp_client: basic
    bcp_interface: basic
    bcp_server: basic
    clock: none
    config_players: none       # todo
    data_manager: none       # todo subclasses
    delay_manager: none
    device_manager: none
    event_manager: none
    file_manager: none       # todo
    logic_blocks: none
    machine_controller: basic
    mode_controller: basic
    placeholder_manager: none
    platforms: none       # todo
    players: basic       # todo
    plugins: none       # todo
    score_reel_controller: none
    scriptlets: none       # todo
    service_controller: basic
    settings_controller: none
    show_controller: none
    switch_controller: basic
    timers: none
  file:
    asset_manager: basic
    ball_controller: basic
    ball_search: basic
    bcp: basic
    bcp_client: basic
    bcp_interface: basic
    bcp_server: basic
    clock: none
    config_players: basic
    data_manager: basic
    delay_manager: none
    device_manager: basic
    event_manager: basic
    file_manager: basic
    logic_blocks: basic
    machine_controller: basic
    mode_controller: basic
    placeholder_manager: basic
    platforms: basic
    players: full
    plugins: basic
    score_reel_controller: basic
    scriptlets: basic
    service_controller: basic
    settings_controller: basic
    show_controller: basic
    switch_controller: full
    timers: none
```

## Related How To guides

--8<-- "todo.md"
