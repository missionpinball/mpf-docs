---
title: How to configure coils & drivers (Stern SPIKE)
---

# How to configure coils & drivers (Stern SPIKE)


Related Config File Sections:

* [spike:](../../config/spike.md)
* [coils:](../../config/coils.md)

To configure coils, drivers, motors, and/or magnets (basically anything
connected to an node's driver outputs) for Stern SPIKE machines, you
can follow the guides and instructions in the
[Coils (Solenoids)](../../mechs/coils/index.md) docs.

--8<-- "common_ground_warning.md"

However there are a few things to know and some additional options you
get with SPIKE hardware that are discussed here.

## number:

The `number:` setting for each driver is a combination of the node it's
connected to and its address from the manual. For example, here's the
driver reference table from Page 11 of the Wrestlemania Pro manual:

![image](../images/spike_driver_table.jpg)

The address for each driver is in the highlighted column. To enter the
number for the driver into MPF, remove the middle "DR" letters so you
just have the node number and address number (with a dash between them).
For example, the driver for the left flipper coil with the address
`8-DR-0` would be entered into the MPF config as `8-0`, etc.

``` mpf-config
coils:
  c_shaker:
    number: 1-10    # Node 1, coil 10
    default_pulse_ms: 100
    allow_enable: true
  c_flipper:
    number: 8-1    # Node 8, coil 1
```

## What if it did not work?

Have a look at our
[SPIKE troubleshooting guide](../../troubleshooting/index.md).

## Related How To guides

* [Coil Resistance and Hardware Details](../../mechs/coils/index.md)
* [Wiring Dual Wound Coils](../../mechs/coils/dual_wound_coils.md)
* [Dual-Wound versus Single-Wound coils](../../mechs/coils/dual_vs_single_wound.md)
* [Adjust coil hold power](../../mechs/coils/hold_power.md)
* [Adjust coil strength (pulse times)](../../mechs/coils/pulse_power.md)
* [Recycle / "Cool Down" Time](../../mechs/coils/recycle.md)
* [Details About Flippers](../../mechs/flippers/index.md)
* [How to configure single-wound flippers](../../mechs/flippers/single_wound.md)
* [How to configure dual-wound flippers](../../mechs/flippers/dual_wound.md)
* [Flipper end-of-stroke (EOS) switches](../../mechs/flippers/eos_switches.md)
