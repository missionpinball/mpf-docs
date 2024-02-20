---
title: Flippers
---

# Flippers


Related Config File Sections:

* [flippers:](../../config/flippers.md)

!!! danger

    Please ensure that you have established
    [common ground between logic and coil power](../../hardware/voltages_and_power/voltages_and_power.md) before turning on high voltage on your coils (especially on
    homebrew machines). Ignoring this might lock on your coils, overheat
    them, burn down your house or kill you. We are serious, floating grounds
    are dangerous. If you are not an electrical engineer read the
    [guide about voltages and power](../../hardware/voltages_and_power/index.md).

    In a nutshell: You need to connect your logic ground (5V/12V) and your
    high voltage ground (48V or 80V). A
    [power entry or power filter board](../../hardware/voltages_and_power/index.md) is a convenient solution to solve this (and more) issues.

    Always turn all PSUs off when connecting power or you might fry all
    boards at once. This is generally a good idea but even more important
    when connecting more than one power supply to a board.

    IF YOU DID NOT UNDERSTAND WHAT THIS WARNING MEANS STOP NOW AND TRY TO
    UNDERSTAND IT. OTHERWISE YOUR HARDWARE WILL LIKELY BURST INTO FLAMES AND
    YOU NEED TO WAIT A FEW DAYS FOR A REPLACEMENT OR EVEN WORSE IT MIGHT
    KILL YOU. IGNORING THIS IS THE MOST COMMON CAUSE FOR BROKEN DRIVER
    BOARDS.

Flippers are probably the first thing you think of when you think about
building your own pinball machine. In fact when most people get their
own hardware and start drilling holes in a piece of plywood, the first
visible thing they do is to get their flippers flipping.

![Pinball flippers](/mechs/images/flippers.png){width="400px"}

MPF has support for lots of different kinds of flippers (as there are
many different ways they've been wired over the years), as well as a
lot of different options for how flippers are fine tuned.

MPF also has support for various "novelty" flipper modes (no-hold
flippers, reversed flipper buttons,
[weak flippers](weak_flippers.md), etc.)

We recommend you read the
[Dual-Wound versus Single-Wound coils](../coils/dual_vs_single_wound.md) guide
to understand the difference between "dual wound" and "single wound"
coils, as flippers in pinball machines can be either type.

You should also probably read the
[EOS Switches guide](eos_switches.md) if
your machine has flipper EOS switches. (In general EOS switches are not
needed for flippers with MPF.)

See [coil hardware](../coils/index.md)
for more details about the current, resistance, number of windings and
the strength of coils.

## Debounce and Recycle on Flipper Coils

In MPF you can
[configure debounce for each switch](../switches/debounce.md) and
[recycle for each coil](../coils/recycle.md). However, both will be overwritten when you enable flippers.
Debounce will be set to `quick` and `recycle` will be disabled. In some
platforms MPF might reconfigure your switch debounce settings when
activating the hardware rules (if the platform does not allow separate
settings) which might lead to more switch events when flippers are
active.

Generally, this is how flipper work in most machines and this is how
players will expect flippers to behave. If you want to change this let
us know in the forum (or you could change it in by overloading the
flipper device class).

## Default Events

MPF contains built-in support for the flipper cancel combo. If you add
the tag `left_flipper` to your left flipper switch, and `right_flipper`
to your right flipper switch, then whenever the player hits both
flippers at the same time, an MPF event called *flipper_cancel* will be
posted. This is implemented as
[combo switch](../../game_logic/combo_switches.md).

Additionally, MPF contains a default
[timed switch](../../game_logic/timed_switches.md) for flipper cradle. It will post `flipper_cradle` when a
player cradles a ball for 3s. Later it will post
`flipper_cradle_release` when the player releases the ball.

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for flippers is `device.flippers.(name)`.

*enabled*

:   Boolean (true/false) which shows whether this ball hold is enabled.

## Related How To guides

* [dual wound flippers](dual_wound.md)
* [single wound flippers](single_wound.md)
* [disabled flippers](disabled_flippers.md)
* [enabling secondary flippers](enabling_secondary_flippers.md)
* [weak flippers](weak_flippers.md)
* [Flipper end-of-stroke (EOS) switches](eos_switches.md)
* [inverted flippers](inverted_flippers.md)
* [multiple flippers](multiple.md)
* [no hold flippers](no_hold_flippers.md)
* [reversed flippers](reversed_flippers.md)
