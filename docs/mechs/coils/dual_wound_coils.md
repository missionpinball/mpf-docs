---
title: Dual-wound Coils
---

# Dual-wound Coils


Related Config File Sections:

* [dual_wound_coils:](../../config/dual_wound_coils.md)
* [flippers:](../../config/flippers.md)

--8<-- "common_ground_warning.md"

A *dual-wound coil* is a coil (solenoid) with two windings--one
"strong" power (or "main") winding for moving the coil, and a second
weaker / lower-power winding for "holding" the coil in the active
position.

image:: /mechs/images/dual_coil_no_diode.jpg

Dual-wound coils are typically used for flippers, diverters, gates, and
other devices in pinball machines that need a strong initial movement
followed by an extended hold period.

There are many places in MPF config files where you need to specify a
coil name. Rather than adding dual-wound coil logic in many different
sections of MPF, we have a dual-wound coil config where you can specify
the settings for a particular dual-wound coil (and give it a new name),
and then you can use that dual-wound coil anywhere in MPF that a coil is
configured.

## Hardware

Dual wound coils are like two coils in one but instead of two times two
terminals they only have three terminals. Both coils share one of those
terminals. Unfortunately, this is not standardized and different for
different types of coils.

To make sure you connect things right you need a multimeter and measure
the resistance between all three terminals. It might be wise to remove
all free-fly diodes while measuring (or at least make sure to measure
the inverse direction). You are looking for the main coil with low
resistance (2-20 Ohm) and one with higher resistance (50 to 200 Ohm).
You can look up the expected resistance in one of the linked charts in
our [coil hardware section](index.md).

Assumed you now got those three measurements:

* Terminal 1 to 2: 4 Ohm
* Terminal 2 to 3: 124 Ohm
* Terminal 1 to 3: 120 Ohm

What does that mean? It means that your main coil is between terminal 1
and 2 and your hold coil is between terminal 1 and 3. Terminal 2 and 3
is just the sum of the resistance of both coils. In general, the highest
of the three readings is the combination you want to remove from your
list.

How do you connect that? Typically, driver boards connect your coils to
ground so you connect power to the terminal which is common between both
coils. In this case this would be terminal 1. Terminal 2 and 3 would be
connected to your driver board. See the following picture for example:

![image](coil_correct.jpg)

The common terminal on the right (terminal 1) has both wires connected.
You see that the diode band is facing in that direction and that two
copper wires for the coil are connected here. One wire is a bit thicker,
which means less resistance thus more current thus stronger. Hence, the
thinner wire is for the hold position. You might not be able to spot
that on every coil.

Please note, that you not just connect two wires across each diode. But
that one pair of wires is across one diode and the other pair of wires
is across two diodes. If you don't do it that way you will fry one of
your FETs on the driver board.

!!! warning

    Please make sure that any diodes on your coil are in reverse to the
    voltage (i.e. the stripe needs to be at the HV side). This is often not
    the case for older coils as they have been connected differently in
    older machines. Ignoring this will fry the FET on your driver board.

See [coil hardware](index.md)
for more details about the current, resistance, number of windings and
the strength of coils.

## Config

This is an example for dual-wound coils which are configured separately:

``` yaml
coils:
  c_your_coil_main:
    number: 00   # depends on your platform and hardware
    default_pulse_ms: 20
  c_your_coil_hold:
    number: 01   # depends on your platform and hardware
    default_pulse_ms: 10
    default_hold_power: .2
```

On top of that you can configure
[dual_wound_coils:](../../config/dual_wound_coils.md) or other
devices such as [flippers:](../../config/flippers.md).

## Related How To guides

* [/mechs/flippers/dual_wound](dual_vs_single_wound.md)
* [How to configure dual-wound flippers](../flippers/dual_wound.md)
