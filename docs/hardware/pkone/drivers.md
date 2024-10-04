---
title: How to configure coils/drivers/magnets (Penny K Pinball PKONE)
---

# How to configure coils/drivers/magnets (Penny K Pinball PKONE)


Related Config File Sections:

* [pkone:](../../config/pkone.md)
* [coils:](../../config/coils.md)

To configure coils, drivers, motors, and/or magnets (basically anything
connected to a PKONE Extension board's driver outputs) with Penny K
Pinball hardware, you can follow the guides and instructions in the
[Coils (Solenoids)](../../mechs/coils/index.md) docs.

--8<-- "common_ground_warning.md"

There are a few things to know about controlling drivers and coils with
PKONE hardware that are discussed here.

## number:

When you're using PKONE Extension boards, drivers plug into individual
Extension boards. Then the Extension boards are connected together in a
chain to the controller.

![image](../images/pkone-extension.png)

The `number:` setting for each coil/driver is its board's Address ID
number in the PKONE chain, then the dash, then the coil/driver output
number (1-10).

``` mpf-config
coils:
  my_coil:
    number: 0-1    # Extension board with Address ID 0, coil/driver 1
  some_other_coil:
    number: 2-10    # Extension board with Address ID 2, coil/driver 10
```

Notes:

* The PKONE Extension board Address ID switches can be set from 0 to
    7.

## Pulse Power

In the [Coils (Solenoids)](../../mechs/coils/index.md) section of the
documentation, we talked about
[how adjusting a coil's pulse time can affect its strength](../../mechs/coils/pulse_power.md). Adjusting the coil's pulse times still assumes that 100%
power will be applied to that coil during that pulse time.

Penny K Pinball PKONE controllers allow you to specify the power that's
applied to the coil during the initial pulse time. This is similar to
the [Adjust coil hold power](../../mechs/coils/hold_power.md), except it
applies to the initial pulse time instead of the extended hold time.

You can configure the pulse power by adding a `default_pulse_power:`
setting to a coil definition and then specifying the power value from
0-1. (Like default_hold power, 0% to 100%)

For example, consider the following configuration:

``` mpf-config
coils:
  some_coil:
    number: 1-3
    default_pulse_ms: 30
    default_pulse_power: 0.5
```

When MPF sends this coil a pulse command, the coil will be fired for
30ms at 50% power. You can even combine default_pulse_power and
default_hold_power, like this:

``` mpf-config
coils:
  some_coil:
    number: 1-3
    default_pulse_ms: 30
    default_pulse_power: 0.5
    default_hold_power: 0.25
```

In this case, if MPF enables this coil, the coil will be fired at 50%
power for 30ms, then drop down to 25% power for the remainder of the
time that it's on.

## Setting Recycle Times

Penny K Pinball controllers allow you to precisely control the
[recycle time](../../mechs/coils/recycle.md) for
coils or drivers.

A coil's `recycle:` setting is a boolean (True/False), which is set to
`False` by default. When using Penny K Pinball hardware, if you set
`recycle: true`, then the recycle time is automatically set to twice the
coil's `default_pulse_ms:` setting. (e.g. a coil with a
`default_pulse_ms: 30` and `recycle: true` will have a 60ms recycle
time).

With Penny K Pinball hardware, you can manually set a coil's recycle
time by adding a `recycle_ms:` setting, like this:

``` mpf-config
coils:
  slingshot_r:
    number: 1-4
    default_pulse_ms: 30
    platform_settings:
      recycle_ms: 100
```

If you manually specify a recycle_ms value, then that's the value
that's used and the coil's `recycle:` (true/false) setting is ignored.

## What if it did not work?

Have a look at our
[PKONE troubleshooting guide](../../troubleshooting/index.md).

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
