---
title: "logging: Config Reference"
---

# logging: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

In the logging section you can configure which how verbose parts of MPFs
should log.

``` yaml
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
        config_players: none
        data_manager: none
        delay_manager: none
        device_manager: none
        event_manager: basic
        extra_balls: none
        light_controller: none
        logic_blocks: none
        machine_controller: basic
        machine_vars: basic
        mode_controller: basic
        placeholder_manager: none
        platform_controller: none
        score_reel_controller: none
        service_controller: basic
        settings_controller: none
        show_controller: none
        switch_controller: basic
        text_ui: none
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
        extra_balls: basic
        light_controller: basic
        logic_blocks: basic
        machine_controller: basic
        machine_vars: basic
        mode_controller: basic
        placeholder_manager: basic
        platform_controller: basic
        score_reel_controller: basic
        service_controller: basic
        settings_controller: basic
        show_controller: basic
        switch_controller: basic
        text_ui: none
        timers: none
```

## Related How To guides

--8<-- "todo.md"
