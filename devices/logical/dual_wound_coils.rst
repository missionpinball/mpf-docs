Dual-wound coil
===============

A *dual-wound coil* is a coil (solenoid) with two windings--one "strong"
power (or "main") winding for moving the coil, and a second weaker / lower-power
winding for "holding" the coil in the active position.

Dual-wound coils are typically used for flippers, diverters, gates, and
other devices in pinball machines that need a strong initial movement
followed by an extended hold period.

The dual-wound coil logical device in MPF lets you group two regular
coil entries (one for the power winding and one for the hold winding)
into a single "coil" that MPF sees like any other regular coil.

Doing this means that MPF can use dual-wound coils anywhere that
regular coils are used and automatically apply the dual-wound timing
rules without needing to add special support for dual-wound coils everywhere
they're used.