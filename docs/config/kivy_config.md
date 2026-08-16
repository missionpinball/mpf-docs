---
title: "kivy_config: Config Reference"
---

# kivy_config: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `kivy_config:` section of your config is where you configure kivy.

You can directly configure kivy here. Usually you don't need this but
in some cases it allows some additional tweaking (e.g. for embedded
workloads). All options are documented in [the kivy config
documentation](https://kivy.org/docs/api-kivy.config.html#available-configuration-tokens).

This is an example:

``` yaml
kivy_config:
  kivy:
    desktop: 1
    exit_on_escape: true
  graphics:
    borderless: false
    fbo: hardware  # hardware, software, force-hardware
    fullscreen: false
    multisamples: 2
    position: auto  # auto, custom
    show_cursor: true
    resizable: true
```

## Related How To guides

* [Using multiple screens](../mc/displays/multiple_screens.md)
