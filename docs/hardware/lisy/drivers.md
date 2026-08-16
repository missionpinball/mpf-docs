---
title: Configuring Drivers in LISY
---

# Configuring Drivers in LISY


Related Config File Sections:

* [coils:](../../config/coils.md)

--8<-- "common_ground_warning.md"

Configure drivers according to the manual of your machine. LISY does not
support any `hold_power` or `pulse_power` other than 1.0. So the coil
will always enable with full power (which is fine in older machines and
should not break things). However, you can still choose the pulse length
using `pulse_ms`.

``` yaml
coils:
  c_some_coil:
    number: 04
    default_pulse_ms: 10
    allow_enable: true
```

In some Gottlieb machines coils were connected to the lights bank. To
address those you have to add 100 to their number from the manual. For
instance, to address a coil which is connected to the light output `05`
use coil `105`:

``` yaml
coils:
  c_coil_on_light_bank:
    number: 107
    default_pulse_ms: 10
```

## What if it did not work?

Have a look at our
[LISY troubleshooting guide](../../troubleshooting/index.md).

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
