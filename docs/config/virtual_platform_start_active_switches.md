---
title: "virtual_platform_start_active_switches:"
---

# virtual_platform_start_active_switches:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `virtual_platform_start_active_switches:` section of your config is
where you define all switches which should start as active when running
your machine with the virtual or smart_virtual platform (e.g. when
running `mpf -X`).

This is an example:

``` yaml
switches:
  s_ball_switch1:
    number:
  s_ball_switch2:
    number:
  s_ball_switch3:
    number:
# Start with two (virtual) balls
virtual_platform_start_active_switches:
  - s_ball_switch1
  - s_ball_switch2
```

## Related How To guides

* [Using MPF without physical hardware](../hardware/virtual/index.md)
* [Troughs / Ball Drains](../mechs/troughs/index.md)
