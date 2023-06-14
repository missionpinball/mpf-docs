---
title: "modes:"
---

# modes:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `modes:` section of your config is where you configure which modes
can be loaded in your machine.

This is an example:

``` yaml
modes:
  - my_mode1
  - my_mode2
```

See [Modes](../game_logic/modes/index.md) and
[How to design a game in MPF using Modes](../game_design/index.md) for details about
modes.

## Related How To guides

* [How to design a game in MPF using Modes](../game_design/index.md)
* [Tutorial step 14: Add your first game mode](../tutorial/14_add_a_mode.md)
* [Modes](../game_logic/modes/index.md)
