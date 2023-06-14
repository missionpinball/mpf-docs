---
title: spike_node:
---

# spike_node:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `node_config:` section of your config is where you configure your
node boards in your `spike:` section.

## Optional settings

The following sections are optional in the `spike_node:` section of your
config. (If you don't include them, the default will be used).

### coil_priorities:

List of one (or more) values, each is a type: `integer`.

A list of coils ordered by priority. This list is send to the hardware
to priorize coils when multiple hardware rules active. The exact logic
is unknown.

### num_inputs:

Single value, type: `integer`.

Number of inputs on that node board.

### num_leds:

Single value, type: `integer`.

Number of LEDs on that node board.

## Related How To guides

* [How to use MPF with Stern SPIKE / SPIKE 2 machines](../hardware/spike/index.md)
