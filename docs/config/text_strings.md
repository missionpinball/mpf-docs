---
title: "text_strings: Config Reference"
---

# text_strings: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `text_strings:` section of your config is where you define text
strings which can be used in slides or widgets.

This is an example:

``` yaml
text_strings:
  greeting: HELLO PLAYER. THIS IS YOUR BALL (ball)
slides:
  slides_with_text:
    - type: text
      text: $greeting
#! slide_player:
#!   game_started: slides_with_text
##! test
#! start_game
#! advance_time_and_run .1
#! assert_text_on_top_slide "HELLO PLAYER. THIS IS YOUR BALL 1"
```

## Related How To guides

* [Text Widget](../mc/widgets/text/index.md)
