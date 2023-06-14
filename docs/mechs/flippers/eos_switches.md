---
title: Flipper end-of-stroke (EOS) switches
---

# Flipper end-of-stroke (EOS) switches


Here's the thing about EOS switches in a modern pinball machine:
they're optional.

To be very clear, EOS switches are only optional if the software is
written to not use them. You can't just walk up to an existing game and
cut the wires to the EOS switches or you'll probably burn up your
coils. (I say "probably" because some games will detect that the EOS
switch wasn't hit when it should have been and cut the power anyway.)

If you wanted to program a game without EOS switches, you could do that.
The way you'd do that is to flip from "power" to "hold" mode after
a predefined time (like 30ms), rather than waiting for an EOS switch to
be engaged.

Why would you want to use the "pulse timing" method versus the "EOS
switch" method for the flipper power stroke? There are a few reasons:

* You can control the "strength" of the flippers in software, rather
    than with hardware. This means you can fine tuning the flipper feel
    for your game without having to swap coils or adjust voltages.
* You can allow operators to change flipper strength via a service
    menu item, compensating for mismatched coils, coil age, machine
    slope, etc. However, this could also be implemented using PWMed
    pulses with full stroke and EOS cut-off.
* Your software can change the strength as part of a game feature.
    (For example, Wizard of Oz has a "weak flippers" mode which makes
    the shots harder.) This can also be implemented with EOS by reducing
    the pulse time below the EOS (tpyical) cut-off time.

Having said this, there's still a reason you might want to use the EOS
switches today----the EOS switch can be used to detect if a fast-moving
ball has hit the flipper so hard that it broke through the hold power
and caused the flipper bat to fall down. The idea is you'd use the EOS
switch to reactivate the power winding (or to reapply full power if
you're using the pulse method) until the EOS switch is activated again,
and then you'd go back to holding the coil.

Whether you actually want to do this is a matter of opinion. Finding the
proper strength for your hold power----especially if you're using the
pulse method----is a balance between applying enough power to keep the
flipper bat up without using so much power that your coil overheats.
Some argue that if you get this balance right, your hold power should be
enough to stand up to a fast ball hitting an upheld flipper. The other
thing to consider with this is that even if a fast-moving ball does
knock the flipper bat down, there's no agreement on whether
automatically re-applying full power to raise the bat is the right thing
to do. Some have argued that that's confusing to the player, and that
if the flipper bat does fall down when the player is not expecting it,
that the player should choose to re-engage it by releasing and
reapplying the flipper button.

Even if you don't use EOS switches for action purposes in your game,
chances are your flipper mechanisms have them. Assuming you have enough
switch inputs available, we like the idea of wiring up your EOS switches
anyway and just audit logging whether an EOS switch is deactivated while
its associated flipper button is still active. Doing so means you
capture the number of times a ball inadvertently moves a flipper bat,
and you can make power adjustments to your hold phase accordingly. It
also lets the machine know if the flippers are broken.

## How does the machine know when the flipper is "up"?

You might notice that both of the options for not burning up the flipper
coils when they're held up require that the machine "knows" when the
coil is up in order to switch over to hold mode. So how exactly does a
machine know this?

Many flippers in pinball machines today have an "end of stroke" (or
"EOS") switch for each flipper. This switch was located under the
playfield near the flipper coil, and it is physically activated by the
flipper mechanism once it has rotated fully into the "up" position. In
the old days (like in EM machines), the flipper coils all used the dual
winding (i.e. "Option 1" from above) approach, and the EOS switch was
a normally-closed switch connected in series with the flipper cabinet
button which activated the power winding. So when the flipper button was
pressed, both the power and hold windings were activated, and then when
the flipper was all the way up it would open the EOS switch, cutting off
power to the power winding. The hold winding remains energized until the
player releases the flipper button.

When EOS switches are used in modern machines, they're typically
connected into into the game like any other switch, so the CPU can
process the EOS activation and disable the power winding or start
pulsing the power.

## Option 2: The flipper has one winding, and the game lowers the power once the flipper is up

The other type of flipper uses a normal coil with just a single winding.
When the flipper button is pressed, the machine fires the flipper coil
with normal full power. Then once the flipper makes it to the "up"
position, the game starts pulsing the power really quickly. (So fast
that it doesn't move the flipper back down, but with enough "spaces"
between the pulses that the coil doesn't burn up.)

Then when the flipper button is released, the power is cut to the
altogether. In case you're wondering why the machine pulses the power,
it's because the pinball machine doesn't have the ability to actually
change the voltage and current that is supplied to the coil. That's
fine, though, because what actually causes a coil to burn is the heat
generated from the current flowing through it. So a coil which is pulsed
on then off every millisecond would only have a "duty cycle" of 50%,
thereby generating far less heat and not burning up. (The 1ms on / 1ms
off is just an example for this illustration. In a real machine it might
be 1 on / 10 off, or 2/18, or 1/6---the exact pulse ratio depends on the
coil type and the amount of voltage used.)

This single-winding coil is less common. Stern used to do it though in
their current SPIKE system they've moved back to dual-wound flippers.

## Design Decision 2: Pulse timings or EOS switch to indicate "up" position?

Next you have to figure out how you're machine will know when to switch
to the low power hold mode. (How it switches depends on Design Decision
1, where it either cuts off the high power winding, or switches over
from the solid pulse to the quick on/off modulated pulses.) If you use
pulse timings then it switches over after a certain number of
milliseconds. If you use the EOS switch then it activates full power
until the EOS switch is activated. Our view is that using the EOS switch
to switch over to low-power hold mode is far less flexible than
configuring specific initial pulse times. We like that this allows game
designers and operators to precisely configure flipper power, and
certainly this is a much more modern approach than physically swapping
out flipper coils to increase or decrease power. Then again, if you're
old school and want to fire that flipper with full power until that EOS
switch is activated, fine, go for it.

## Design Decision 3: Will you use EOS switches to notify the game that a ball has "broken through" the hold?

Modern machines use [pulse-width modulation
(PWM)](https://en.wikipedia.org/wiki/Pulse-width_modulation) to keep
flipper bats up because most coils will instantly burst into flames if
you enable them at 48V which are typically used in today's machines.
PWM uses a so called duty-cycle which determines how much energy moves
into the flippers. More energy strictly results in more power but that
energy also turns into heat. Unfortunately, the resistance in copper
wires in the coil increases with the temperature and, consequently, the
less current and energy will flow through the coil. As a result the coil
will become weaker of time when it heats up. Since we do not know the
temperature in software this cannot easily be compensated as runtime
(and the coil would probably become even hotter and burn if we would
try).

Finding the right spot where the coil is strong enough, knockdowns do
not happen and the temperature stays low enough is not generally easy.
Parts age over time, environment temperature differs between location
and even the voltage might fluctuate. We have seen overheating of coils
in some machines by newer manufacturers.

So what can we do about this? We can detect when the EOS switch opens
while the flipper button is active and repulse the flipper coil.
Ideally, this should happen inside the pinball hardware but this is not
supported by all hardware platform in MPF. For all remaining platforms,
we mitigate this in software in MPF. This introduces a few milliseconds
of delay but it should be fast enough that the player does not notice
it.

This is how you can enable it in MPF:

``` mpf-config
#! switches:
#!   s_flipper_single:
#!     number: 1
#!   s_flipper_single_eos:
#!     number: 2
#!   s_flipper_dual_wound:
#!     number: 3
#!   s_flipper_dual_wound_eos:
#!     number: 4
#! coils:
#!   c_flipper_single_main:
#!     number: 0
#!   c_flipper_dual_wound_main:
#!     number: 2
#!   c_flipper_dual_wound_hold:
#!     number: 3
#!     allow_enable: true
flippers:
  single_wound_flipper:
    main_coil: c_flipper_single_main
    activation_switch: s_flipper_single
    eos_switch: s_flipper_single_eos
    use_eos: true
    repulse_on_eos_open: true
    eos_active_ms_before_repulse: 500
  dual_wound_flipper:
    main_coil: c_flipper_dual_wound_main
    hold_coil: c_flipper_dual_wound_hold
    activation_switch: s_flipper_dual_wound
    eos_switch: s_flipper_dual_wound_eos
    use_eos: true
    repulse_on_eos_open: true
    eos_active_ms_before_repulse: 500
```

To prevent repeated activations MPF will wait
`eos_active_ms_before_repulse` ms before a repulse can happen. There are
certain races between hardware rules and this mechanism which MPF tries
to handle (but we might have missed cases - let us know if you find any
rough edges or weird behavior with this).

In general, this should allow you to reduce PWM power by a lot and
instead use repulses in the rare case of knockdowns. This should work
with all platforms and will use hardware rules if your platform supports
them.
