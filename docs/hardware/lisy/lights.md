---
title: Configuring Lights in LISY
---

# Configuring Lights in LISY


Related Config File Sections:

* [flippers_slings_popbumpers](../../config/lights.md)

Lights in LISY can be configured as
[lights](../../config/lights.md) using their
number from the game manual.

This is an example:

``` yaml
lights:
  your_light:
    number: 03
```

There are some features in the light list like the `game_over_relay`
which are not real lights. Those can be configured as
[digital outputs](../../config/digital_outputs.md). See [Configuring and Enabling Flippers/Pop Bumpers/Slingshots in LISY](flippers_slings_popbumpers.md) for details about the `game_over_relay`.

## What if it did not work?

Have a look at our
[LISY troubleshooting guide](../../troubleshooting/index.md).
