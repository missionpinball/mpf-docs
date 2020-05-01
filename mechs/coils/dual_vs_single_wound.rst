Dual-Wound versus Single-Wound coils
====================================

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

It's common for pinball machines to include coils that are "held on" for
periods of time longer than the maximum pulse time of 255ms. The obvious
example of this is for flipper coils, though other types of devices use these
too. (Diverters, the trolls in *Medieval Madness*, certain ball release coils,
etc.)

In many cases, these types of coils need to have strong initial pulses to
quickly move the mechanism from its resting to active position, but they also
need to be able to be held "on" for a long period of time.

These two requirements are conceptually incompatible.

The way you make a coil strong is you give it lots of power and make it really
big. Unfortunately the byproduct of that is heat, which means if you make a
nice, big, powerful coil that's strong enough to move the mechanism with the
quick power it needs, then when the coil is left in the "on" state, it
generates so much heat that it will burn up the coil. :(

Fortunately the pinball companies solved this 60+ years ago with the concept
of "dual wound" coils. A dual-wound coil is essentially two separate
coils in one. (There are literally two separate wires wrapped around the coil
sleeve instead of one.)

Dual-wound coils have a strong (often called the "main" or "power") winding
which is used for the initial "kick" of the coil, and they also have a
lower-powered ("hold") winding which is used to hold the active position.

.. note::

   You can tell if a coil is dual-wound because the coil will have
   three wire connection points instead of two. There's a power
   winding connector, a hold winding connector, and a common connector that's
   shared by both.

The way these are used is that the strong winding is pulsed initially (usually
for a fraction of a second) to provide the initial strength to move the mechanism,
then it cuts off, leaving just the weaker hold winding active to keep the
mechanism active. The hold winding can safely be enabled for a long time, even
multiple minutes. When the machine wants to disable the device (or when the
player releases the flipper button in the case of a flipper), the power to the
hold winding is cut, and a spring causes the mechanism to return to the initial
position.

Transitioning from the power to the hold winding: The old way
-------------------------------------------------------------

In old pinball machines (from the 1940s through the early 2000s), the
"transition" from the power winding to the hold winding was purely mechanical
and done using something called an "end of stroke" (EOS) switch.

The EOS switch is a physical leaf switch in the mechanism under the
playfield with a switch that is mechanically opened by the movement of the
device. When the coil is first activated, the current flows to both the power
and the hold windings, and the mech starts to move. A few fractions of a
second later, the mech reaches its full "up" position, and a little arm under
it hits the EOS switch which opens it and breaks the connection to the
power winding, leaving only the hold winding energized.

When the hold winding is de-energized, the spring causes the mechanism to move
back to the original position, and the EOS switch is closed (by the movement of
the mech) meaning that the next time the mech is activated, the current will
again flow to both the power and hold windings.

Advantages of using this "old style" EOS switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* It's simple. No computers or fancy timing has to be involved, and the
  transition from the power to the hold windings is automatic.
* If a coil gets dirty, gummed up, or weak, the transition from the
  power to the hold winding always occurs only after the mech is all the way
  in the "active" position.
* Only a single "driver" connection from the control system is needed since that
  single control line is used for both the power and hold windings.

Downsides to using this "old style" EOS switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* No fine tuning. Since the transition from the power to the hold winding is
  purely mechanical, you can't change the power of the mechanism unless you
  physically switch out the coil and/or change the voltage used.
* For flippers, you don't get any "novelty" flipper modes. You can't do things
  like "weak flippers" or "no   hold flippers" since the flipper behavior is
  mechanically controlled.

Transitioning from the power to the hold winding: The modern way
----------------------------------------------------------------

Modern machines do not use EOS switches in the same way they have been used in
older machines.

The main reason for this is that modern pinball control systems (including all
the :doc:`control systems </hardware/index>` that MPF supports) have the ability
to activate coils with millisecond-level precision (something that was not
possible even in 1990s WPC machines).

Using flippers as an example, in modern machines, when the player presses the flipper button,
the control system will send current to both the power and hold windings at the
same time, and then at a very precise moment (e.g. 27ms later or 14ms later or
whatever), the control system will cut off the power winding, leaving just the
hold winding active.

This has the same effect of the mechanical EOS switch in that the power winding
is only used for the initial power motion, and the lower-current hold winding
is then used to keep the flipper in the up position.

Advantages of using the modern transition from power to hold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You can fine-tune coil strength by changing settings in software.
* You can use novelty modes like weak flippers, no hold flippers, etc.

Downsides of using the modern transition from power to hold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You have to play with your settings to get them right.
* A dirty, gummed up, or worn-out coil or mechanism might mean that the
  initial power timing setting you originally configured might not be strong
  enough to move the mechanism all the way into the "up" position.

Single-wound coils
------------------

So far both options (EOS and non-EOS) we discussed use dual-wound coils with
power and hold windings.

However there's a third option that some modern machines use as well. The third
option is to use more traditional (e.g. "single wound") coils for your machine that do
not have the dual "power" and "hold" windings.

Of course you might be thinking, "How does that work? Wouldn't the coil
burn up if the mechanism was active for too long?"

This is another case where modern technology can be used to address that.

In electronics, there's a concept called "Pulse Width Modulation" (or "PWM"),
which (in this case) basically means the control hardware turns the power on and
off really fast. (Like, hundreds of times per second.)

So the way this works is that you have a high-powered, strong coil which is
activated a full strength in order to provide the strong initial motion.
However once the mechanism is in the up position (based on either an EOS switch,
or based on the millisecond-level precise timing), the control system stops
powering that coil at 100% and instead cuts the power back (using that PWM thing)
to a smaller percent (like maybe 12.5% or 25% or so). That reduced power is
enough to keep the mech in the up position, but not enough to cause the coil
to overheat and burn out.

Advantages to using single-wound coils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You only need a single driver output per coil (instead of two).
* You can still do the modern things, like use software to tune the strength of
  the coil and novelty flipper modes.

Downsides to using single-wound coils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* You have to figure out the PWM (low power) settings which need to be strong
  enough to hold the mechanism up but not too strong so they don't burn it up.
* Sometimes the PWM "hold" makes an annoying buzzing sound (since the power is
  being turned on and off hundreds of times per second).

We should note that the decision to use a single-wound versus dual-wound flipper
coil is technically a separate decision from whether or not to use an EOS
switch. See the :doc:`/mechs/flippers/eos_switches` for more on that decision.

Which option should you choose?
-------------------------------

Ok, so basically there are three options for coils that need to be held on for
more than 255ms:

* Dual-wound, with a mechanical EOS switch to transition from power to hold.
* Dual-wound, with the control system timing to transition from power to hold.
* Single-wound

The good news is that MPF supports all three options.

If you're retheming an existing machine, and you're using the original driver
boards and power supplies, then you should probably just use whatever method
was used in that machine and keep it simple.

If you're building a new machine, most people choose the second option, where
you use a dual-wound coil but with the transition of the power to hold
windings done via software and the modern control systems. The reasons for this
include:

* It's simple. You don't have to mess with trying to figure out the PWM timings
  for the hold winding.
* It works. You know the hold winding was designed to be held on at full power,
  so you don't have to worry about breaking things.
* It's less wear-and-tear and emissions. Rapidly cycling power (in the PWM way)
  for the hold phase in a single-wound coil has the potential to add wear to the
  components in your system and potential to cause EMI emissions.

People have also pointed out that Stern's S.A.M. system (which they used in from
about 2006-2015) used the single-wound PWM-style flippers, but then with the
SPIKE system (from 2015 onwards) went back to the dual-wound computer controlled
option for a while. However, they later switched back to single-wound PWM-style
flippers. We can only speculate why they did that and it might involve that
dual-wound flippers are easier to control from software with a new control system.

Really the only reasons to use the single-wound coils are:

* You already have mechanisms that use single-wound coils
* You're running out of driver outputs in your control system and you don't want
  to "waste" two drivers per mech.
* Single-wound are cheaper to produce
