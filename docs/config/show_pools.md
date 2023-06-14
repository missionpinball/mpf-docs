---
title: "show_pools:"
---

# show_pools:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `show_pools:` section of your config is where you configure a pool
of shows. When used one of the shows is selected from the pool based on
a configurable pattern called `type`.

This is an example:

``` mpf-config
#! shows:
#!   show1:
#!     - duration: 1
#!   show2:
#!     - duration: 1
#!   show3:
#!     - duration: 1
show_pools:
  group1:
    shows:
      - show1
      - show2
      - show3
    type: random
```

## Required settings

The following sections are required in the `show_pools:` section of your
config:

### shows:

List of one (or more) values, each is a type: string name of a
[shows:](../shows/index.md) device. Defaults to empty.

A list of shows which are part of the show pool

## Optional settings

The following sections are optional in the `show_pools:` section of your
config. (If you don't include them, the default will be used).

### type:

Single value, type: one of the following options: random, sequence,
random_force_next, random_force_all. Default: `sequence`

How the next show is selected. See [Assets](../assets/index.md) for details.

## Related How To guides

* [Assets](../assets/index.md)
* [Shows](../shows/index.md)
