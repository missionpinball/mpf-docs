---
title: How to configure dual-wound flippers
---

# How to configure dual-wound flippers


!!! warning

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

This guide shows you how to configure dual-wound flippers in MPF. If you
don't know what "dual-wound" flippers are, or whether you have them,
take a look at the coil that your flipper uses. If it has three wires
(or three tabs to connect three wires), then it's a dual-wound coil and
this guide is for you.

If it has two wires (or two tabs), then read the
[How to configure single-wound flippers](single_wound.md) guide.

Read more about "dual wound" versus "single wound" coils in the
[Dual-Wound versus Single-Wound coils](../coils/dual_vs_single_wound.md) guide.

See [coil hardware](../coils/index.md)
for more details about the current, resistance, number of windings and
the strength of coils. See
[dual-wound hardware](../coils/dual_wound_coils.md) for details about how to find out which terminals on your
coils are hold, which are the main coil and how to connect them.

## 1. Add your flipper buttons

First, make sure you have entries in your machine config for your
flipper buttons.

Here's an example `config.yaml` with two switches added:

``` yaml
switches:
  s_left_flipper:
    number: 1
    tags: left_flipper
  s_right_flipper:
    number: 2
    tags: right_flipper
```

You can pick whatever names you want for your switches. We chose
`s_left_flipper` and `s_right_flipper`.

Note that we configured this switches with numbers `1` and `2`, but you
should use the actual switch numbers for your control system that the
flipper buttons are connected to. (See
[How to configure "number:" settings](../../hardware/numbers.md) for instructions for
each type of control system.)

We also added tags called `left_flipper` and `right_flipper`. These are
optional, but recommended. The reason is that MPF includes a
[combo switch](../../game_logic/combo_switches.md) feature which posts events when player switches are held in
combination. If you add these tags to your flipper switches, an event
called *flipper_cancel* will be posted when the player hits both flipper
buttons at the same time which you can use to cancel shows and other
things you want the player to be able to skip.

## 2. Add your flipper coils

Next you need to add entries for your flipper coils to your machine-wide
config. These will be added to a section called `coils:`. Since we're
using dual-wound coils, there will actually be two coil entries for each
coil---one for the power (main) winding, and one for the hold winding.

``` yaml
coils:
  c_flipper_left_main:
    number: 0
  c_flipper_left_hold:
    number: 1
    allow_enable: true
  c_flipper_right_main:
    number: 2
  c_flipper_right_hold:
    number: 3
    allow_enable: true
```

Again, the `number:` entries in your config will vary depending on your
actual hardware, and again, you can pick whatever names you want for
your coils.

Also note that the two hold coils have `allow_enable: true` entries
added. (In MPF config files, values of "yes" and "true" are the
same.) The purpose of the `allow_enable: true` setting is that as a
safety precaution, MPF does not allow you to enable (that is, to hold a
coil in its "on" position) unless you specifically add
`allow_enable: true` to that coil's config.

So in the case if your flippers, the hold coil of a flipper needs to
have `allow_enable: true` since in order for it to act as a flipper,
that coil needs to be allowed to be enabled (held on).

## 3. Add your flipper entries

At this point you have your coils and switches defined, but you can't
flip yet because you don't have any flippers defined. Now you might be
thinking, "Wait, but didn't I just configure the coils and switches?"
Yes, you did, but now you have to tell MPF that you want to create a
flipper mechanism which links together the switch and the coils to
become a "flipper".

You create your flipper mechanisms by adding a `flippers:` section to
your machine config, and then specifying the switch and coils for each
flipper that you defined in Steps 1 and 2.

Here's what you would create based on the switches and coils we've
defined so far:

``` yaml
#! switches:
#!   s_left_flipper:
#!     number: 1
#!     tags: left_flipper
#!   s_right_flipper:
#!     number: 2
#!     tags: right_flipper
#! coils:
#!   c_flipper_left_main:
#!     number: 0
#!   c_flipper_left_hold:
#!     number: 1
#!     allow_enable: true
#!   c_flipper_right_main:
#!     number: 2
#!   c_flipper_right_hold:
#!     number: 3
#!     allow_enable: true
flippers:
  left_flipper:
    main_coil: c_flipper_left_main
    hold_coil: c_flipper_left_hold
    activation_switch: s_left_flipper
  right_flipper:
    main_coil: c_flipper_right_main
    hold_coil: c_flipper_right_hold
    activation_switch: s_right_flipper
```

## 4. Enabling your flippers

By default, MPF only enables flippers when a game is in progress. So if
this is a first-time config and you haven't configured your ball
devices and start button and everything, you can't actually start a
game yet, which means you can't test your flippers.

Fortunately we can get around that by configuring your flippers to just
automatically enable themselves when MPF starts. To do this, add the
following entry to each of your flippers in your config file:

    enable_events: machine_reset_phase_3

So now the `flippers:` section of your config file should look like
this:

``` yaml
#! switches:
#!   s_left_flipper:
#!     number: 1
#!     tags: left_flipper
#!   s_right_flipper:
#!     number: 2
#!     tags: right_flipper
#! coils:
#!   c_flipper_left_main:
#!     number: 0
#!   c_flipper_left_hold:
#!     number: 1
#!     allow_enable: true
#!   c_flipper_right_main:
#!     number: 2
#!   c_flipper_right_hold:
#!     number: 3
#!     allow_enable: true
flippers:
  left_flipper:
    main_coil: c_flipper_left_main
    hold_coil: c_flipper_left_hold
    activation_switch: s_left_flipper
    enable_events: machine_reset_phase_3
  right_flipper:
    main_coil: c_flipper_right_main
    hold_coil: c_flipper_right_hold
    activation_switch: s_right_flipper
    enable_events: machine_reset_phase_3
```

## 5. Configure your control system hardware

At this point your flipper configuration is technically complete, though
there are two other important things you may have to do first:

If you're using physical hardware, you may need an additional section
in your machine config for your control system. (For example, FAST
Pinball and Open Pinball Project controllers require a one-time port
configuration, etc.) See the
[control system documentation](../../hardware/index.md) for details.

## 6. Adjust your flipper power

As a safety precaution, MPF uses very low (10ms) default pulse times for
coils. In most cases, 10ms will not be enough power to physically move
the flippers when you hit the button. (You might hear them click or buzz
without actually seeing them move.)

So check out the documentation in the coils section for instructions on
how to adjust the
[pulse power](../coils/pulse_power.md)
and the [hold power](../coils/hold_power.md) for the coils you're using for your flippers.

## Related How To guides

* [Dual-wound Coils](../coils/dual_wound_coils.md)
* [Dual-Wound versus Single-Wound coils](../coils/dual_vs_single_wound.md)
