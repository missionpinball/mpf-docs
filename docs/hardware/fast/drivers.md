---
title: How to configure coils/drivers/magnets (FAST Pinball)
---

# How to configure coils/drivers/magnets (FAST Pinball)


Related Config File Sections:

* [fast:](../../config/fast.md)
* [coils:](../../config/coils.md)

To configure coils, drivers, motors, and/or magnets (basically anything
connected to an IO board's driver outputs) with FAST Pinball hardware,
you can follow the guides and instructions in the
[Coils (Solenoids)](../../mechs/coils/index.md) docs.

!!! warning "High voltage can be dangerous."

    It's important that you wire your boards correctly. FAST Pinball has
    detailed wiring guides which you should follow. Please see the wiring
    guide for the [FAST Nano Controller](https://fastpinball.com/wiring/nano)
    on their website.

Once everything is wired, here's how you configure MPF to use a FAST
Nano Controller.

## number:

When you're using FAST IO boards, drivers plug into individual IO
boards. Then the IO boards are connected together in a loop.

![image](../images/fast-io-3208.png)

The `number:` setting for each driver is its board's position number in
the chain, then the dash, then the driver output number. Note that the
position number starts with zero, so the first IO board in the chain is
0, the second is 1, etc.

``` yaml
coils:
  my_coil:
    number: 0-0    # first board, driver 0
  some_other_coil:
    number: 2-14    # third board, driver 14
```

Notes:

* The first board in the chain is board 0.
* The boards are counted in the direction of the "out" connector
    on the controller board.
* Different models of IO boards have different numbers of drivers,
    and MPF will make sure that the numbers work for each type of
    board. (e.g. a driver number 10 isn't valid on an 0804 board
    since that board only has 4 drivers numbered 0-3).

Also note that prior versions of MPF just numbered all the drivers in
one continuous sequence from the first board through the last, but that
was confusing. You can still do that if you want (in integer format),
but we feel the board-input format is much easier to understand.

## Pulse Power

In the [Coils (Solenoids)](../../mechs/coils/index.md) section of the
documentation, we talked about
[how adjusting a coil's pulse time can affect its strength](../../mechs/coils/pulse_power.md). Adjusting the coil's pulse times still assumes that 100%
power will be applied to that coil during that pulse time.

However, FAST Pinball controllers allow you to specify the power that's
applied to the coil during the initial pulse time. This is similar to
the [Adjust coil hold power](../../mechs/coils/hold_power.md), except it
applies to the initial pulse time instead of the extended hold time.

You can configure the pulse power by adding a `default_pulse_power:`
setting to a coil definition and then specifying the power value from
0-1. (Like default_hold power, 0% to 100%)

For example, consider the following configuration:

``` yaml
coils:
  some_coil:
    number: 1-3
    default_pulse_ms: 30
    default_pulse_power: 0.5
```

When MPF sends this coil a pulse command, the coil will be fired for
30ms at 50% power. You can even combine default_pulse_power and
default_hold_power, like this:

``` yaml
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

FAST Pinball controllers allow you to precisely control the
[recycle time](../../mechs/coils/recycle.md) for
coils or drivers.

A coil's `recycle:` setting is a boolean (True/False), which is set to
`False` by default. When using FAST Pinball hardware, if you set
`recycle: true`, then the recycle time is automatically set to twice the
coil's `default_pulse_ms:` setting. (e.g. a coil with a
`default_pulse_ms: 30` and `recycle: true` will have a 60ms recycle
time).

However, with FAST Pinball hardware, you can manually set a coil's
recycle time by adding a `recycle_ms:` setting, like this:

``` yaml
coils:
  slingshot_r:
    number: 1-4
    default_pulse_ms: 30
    platform_settings:
      recycle_ms: 100
```

If you manually specify a recycle_ms value, then that's the value
that's used and the coil's `recycle:` (true/false) setting is ignored.

## Replacing FETs on FAST Driver Boards

In case you burned one of your FETs on a FAST board those can be
replaced. Usually, FETs will turn on permanently when burned. As a
result your coils will be stuck on and your fuse should burn (if not
your coil will). If you output does not activate at all a burned FET is
rather unlikely the culprit.

Consult the FAST support for an official repair. Alternatively, you can
buy `IRL540NSTRLPBF` FETs from your electronics supplier and replace
them yourself. Replacing SMD FETs is possible with a decent soldering
iron and some practice.

## What if it did not work?

Have a look at our
[FAST troubleshooting guide](../../troubleshooting/index.md).

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
