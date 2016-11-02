Flipper end-of-stroke (EOS) switches
====================================

Here's the thing about EOS switches in a modern pinball machine:
they're optional.

To be very clear, EOS switches are only optional if
the software is written to not use them. You can't just walk up to an
existing game and cut the wires to the EOS switches or you'll probably
burn up your coils. (I say "probably" because some games will detect
that the EOS switch wasn't hit when it should have been and cut the
power anyway.)

If you wanted to program a game without EOS switches,
you could do that. They way you'd do that is to flip from "power" to
"hold" mode after a predefined time (like 30ms), rather than waiting
for an EOS switch to be engaged.

Why would you want to use the "pulse
timing" method versus the "EOS switch" method for the flipper power
stroke? There are a few reasons:


+ You can control the "strength" of the flippers in software, rather
  than with hardware. This means you can fine tuning the flipper feel
  for your game without having to swap coils or adjust voltages.
+ You can allow operators to change flipper strength via a service
  menu item, compensating for mismatched coils, coil age, machine slope,
  etc.
+ Your software can change the strength as part of a game feature.
  (For example, Wizard of Oz has a "weak flippers" mode which makes the
  shots harder.)


Having said this, there's still a reason you might want to use the EOS
switches today—-the EOS switch can be used to detect if a fast-moving
ball has hit the flipper so hard that it broke through the hold power
and caused the flipper bat to fall down. The idea is
you'd use the EOS switch to reactivate the power winding (or to
reapply full power if you're using the pulse method) until the EOS
switch is activated again, and then you'd go back to holding the coil.

Whether you actually want to do this is a matter of opinion. Finding
the proper strength for your hold power—-especially if you're using the
pulse method—-is a balance between applying enough power to keep the
flipper bat up without using so much power that your coil overheats.
Some argue that if you get this balance right, your hold power should
be enough to stand up to a fast ball hitting an upheld flipper. The
other thing to consider with this is that even if a fast-moving ball
does knock the flipper bat down, there's no agreement on whether
automatically re-applying full power to raise the bat is the right
thing to do. Some have argued that that's confusing to the player, and
that if the flipper bat does fall down when the player is not
expecting it, that the player should choose to re-engage it by
releasing and reapplying the flipper button.

Even if you don't use
EOS switches for action purposes in your game, chances are your
flipper mechanisms have them. Assuming you have enough switch inputs
available, we like the idea of wiring up your EOS switches anyway
and just audit logging whether an EOS switch is deactivated while its
associated flipper button is still active. Doing so means you capture
the number of times a ball inadvertently moves a flipper bat, and you
can make power adjustments to your hold phase accordingly. It also lets
the machine know if the flippers are broken.

How does the machine know when the flipper is "up"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might notice that both of the options for not burning up the
flipper coils when they're held up require that the machine "knows"
when the coil is up in order to switch over to hold mode. So how
exactly does a machine know this?

Many flippers in pinball machines
today have an "end of stroke" (or "EOS") switch for each flipper. This
switch was located under the playfield near the flipper coil, and it
is physically activated by the flipper mechanism once it has rotated
fully into the "up" position. In the old days (like in EM machines),
the flipper coils all used the dual winding (i.e. "Option 1" from
above) approach, and the EOS switch was a normally-closed switch
connected in series with the flipper cabinet button which activated
the power winding. So when the flipper button was pressed, both the
power and hold windings were activated, and then when the flipper was
all the way up it would open the EOS switch, cutting off power to the
power winding. The hold winding remains energized until the player
releases the flipper button.

When EOS switches are used in modern
machines, they're typically connected into into the game like any
other switch, so the CPU can process the EOS activation and disable
the power winding or start pulsing the power.

Option 2: The flipper has one winding, and the game lowers the power once the flipper is up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The other type of flipper uses a normal coil with just a single
winding. When the flipper button is pressed, the machine fires the
flipper coil with normal full power. Then once the flipper makes it to
the "up" position, the game starts pulsing the power really quickly.
(So fast that it doesn't move the flipper back down, but with enough
"spaces" between the pulses that the coil doesn't burn up.)

Then when the flipper button is released, the power is cut to the altogether.
In case you're wondering why the machine pulses the power, it's
because the pinball machine doesn't have the ability to actually
change the voltage and current that is supplied to the coil. That's
fine, though, because what actually causes a coil to burn is the heat
generated from the current flowing through it. So a coil which is
pulsed on then off every millisecond would only have a "duty cycle" of
50%, thereby generating far less heat and not burning up. (The 1ms on
/ 1ms off is just an example for this illustration. In a real machine
it might be 1 on / 10 off, or 2/18, or 1/6—the exact pulse ratio
depends on the coil type and the amount of voltage used.)

This single-winding coil is less common. Stern used to do it though in their
current SPIKE system they've moved back to dual-wound flippers.

Design Decision 2: Pulse timings or EOS switch to indicate "up" position?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next you have to figure out how you're machine will know when to
switch to the low power hold mode. (How it switches depends on Design
Decision 1, where it either cuts off the high power winding, or
switches over from the solid pulse to the quick on/off modulated
pulses.) If you use pulse timings then it switches over after a
certain number of milliseconds. If you use the EOS switch then it
activates full power until the EOS switch is activated. Our view is
that using the EOS switch to switch over to low-power hold mode is far
less flexible than configuring specific initial pulse times. We like
that this allows game designers and operators to precisely configure
flipper power, and certainly this is a much more modern approach than
physically swapping out flipper coils to increase or decrease power.
Then again, if you're old school and want to fire that flipper with
full power until that EOS switch is activated, fine, go for it.


Design Decision 3: Will you use EOS switches to notify the game that a ball has "broken through" the hold?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, you have to decide whether you're going to use EOS switches
to notify the machine when a flipper has lost its hold while the
flipper button is still engaged. (And if so, what you're going to do
about it.) We believe the chances of a ball breaking the hold are
generally slim, and if it's something that happens often that
indicates that your hold power is not strong enough. (Assuming you're
holding the flipper with the pulse modulation to the power winding
rather than using a dual-wound coil.) We also believe that if a ball
breaks a flipper hold, automatically reapplying full power to restore
the hold can be confusing to the player. That said, all machines are
different, and tastes are different, so you should go with whatever
you want. The nice thing about not using EOS switches is again, you
can free up those switch inputs for other things if you're running
low. But even if you don't use them to automatically correct for a
broken holds, we like the idea of still connecting the EOS switches
and using them for audit logging purposes. (e.g. using them to record
any instances of a flipper hold being broken by a fast moving ball, a
broken hold winding, or a broken flipper.)
