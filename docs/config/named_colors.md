---
title: "named_colors:"
---

# named_colors:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `named_colors:` section of your config is where you define color
names that can be used for RGB lights throughout your machine code.
Anywhere in lights: or light_player: where a color can be specified,
named colors can be used.

Your named colors can be an array of R/G/B values or a hex string of hex
values (which can also include a brightness percentage, like all hex
color strings).

This is an example:

``` yaml
named_colors:
  custom_blue: [24, 65, 226]
  troll_green: 4a9b22
  troll_green_dark: 4a9b22%50
lights:
  troll_target:
    number: 10
    default_on_color: troll_green
  l_jackpot:
    number: 20
light_player:
  trolls_disabled:
    troll_target: troll_green_dark
  jackpot_lit:
    l_jackpot:
      color: custom_blue
      fade: 10
```

## Related How To guides

--8<-- "todo.md"
