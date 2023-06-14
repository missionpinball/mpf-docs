---
title: mode_settings:
---

# mode_settings:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `mode_settings:` section of your config is a generic section that
contains settings that you might want to use in a specific mode. It's
nice because it's pretty much ignored by the general MPF config
processing, meaning you can put whatever settings you want in here for a
specific mode.

In fact, several of the built-in MPF modes make use of the
`mode_settings:` section, including:

* [End of Ball Bonus mode](bonus.md)

## Related How To guides

* [End of Ball Bonus mode](bonus.md)
* [Mode Selection](../game_design/mode_selection.md)
* [Carousel](../cookbook/carousel.md)
* [End of Ball Bonus](../game_logic/bonus/index.md)
