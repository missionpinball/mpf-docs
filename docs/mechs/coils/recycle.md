---
title: Recycle / "Cool Down" Time
---

# Recycle / "Cool Down" Time


Related Config File Sections:

* [coils:](../../config/coils.md)

Recycle time is the time a coil will rest after it has been pulsed. This
is either calculated as ratio on the pulse time (for instance, two times
the pulse time) or as absolute time. In both cases this time is used to
prevent thermal overheating of coils similar to hold_power.

If your machine constantly triggers a coil with 50ms pulse time for some
reason then it would practically stay on permanently without recycle
time. Howver, with a recycle factor of 2 (or 100ms cool down time) it
would be enabled for at most 33% of the time.

How this recycle is implemented differs between platforms. MPF exposes a
very basic interface to enable or disable `recycle` per coil. Usually,
you want to keep it enabled. This is an example:

``` yaml
coils:
  c_coil_with_recycle:
    number:
    default_recycle: true
  c_coil_without_recycle:
    number:
    default_recycle: false
```

Some platforms allow you to fine tune the recycle time.

* [recycle_factor for OPP](../../hardware/opp/drivers.md)
* [recycle_ms for FAST](../../hardware/fast/drivers.md)
