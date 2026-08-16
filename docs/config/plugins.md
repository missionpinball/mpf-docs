---
title: "plugins: Config Reference"
---

# plugins: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `plugins:` section of your config is where you list all plugin
classes to load. By default it contains:

* [info_lights:](info_lights.md)
* [switch_player:](switch_player.md)
* [auditor:](auditor.md)
