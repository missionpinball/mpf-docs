---
title: "logic_blocks:"
---

# logic_blocks:


Logic blocks moved one level up in MPF 0.50. Instead of

``` yaml
logic_blocks:
  counters:
    your_counter:
      count_events: count_it_up
```

just use:

``` mpf-config
counters:
  your_counter:
    count_events: count_it_up
```

There are three type of logic blocks:

* [accruals:](../game_logic/logic_blocks/accruals.md)
* [counters:](../game_logic/logic_blocks/counters.md)
* [sequences:](../game_logic/logic_blocks/sequences.md)

Click each of the links above for details and settings for each type of
logic block.
