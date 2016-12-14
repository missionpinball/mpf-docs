How MPF handles "quick response" mechs (flippers, slingshots, etc.)
===================================================================

As you can imagine, many types of mechanisms in a pinball machine require
near "instant" response to switches. For example, you do not want any "lag"
between the time you press the flipper button and the time the flipper
physically moves.

To address this, MPF and the control systems handle "quick response" devices
in a special way. This includes things like:

* flippers
* pop bumpers
* slingshots
* kicking targets
* kickback lanes
* diverters
* and maybe others?

What's the problem?
-------------------

To understand why MPF and the hardware control systems work this way, first
think about how MPF works in general.

When you configure (and enable) a flipper in MPF, what you're really doing is
saying, "when this switch becomes active, fire this coil" (and do that as fast
as possible).

The challenge is that MPF is software running on a computer connected to a
pinball control system via USB. So if you think about the entire process that
needs to happen to flip a flipper, you have:

1. The hardware control system is continuously scanning switches to see if they
   change state.
2. The player pushes the flipper button.
3. The hardware control system notices the change.
4. The hardware control system adds the message with the switch state change
   to the queue to be sent to the computer via USB.
5. The computer processes the USB message.
6. MPF gets notification of the switch change.
7. MPF looks at its configuration and notices that a coil should be fired.
8. MPF creates the instruction to fire the coil.
9. That instruction is put in the queue to be sent to the hardware controller
   via USB.
10. The USB bus transfers that command to the hardware controller.
11. The hardware controller receives that command and fires the coil attached
    to the flipper.

Of course computers are really fast, and this can all happen in 10 or 20ms.
But again, with the desire for "instant" response of these devices, that isn't
fast enough.

The solution? "Hardware rules"
------------------------------

So the way this is handled is that all the pinball control systems have the
ability to have simple "rules" written to them which lets them do simple things
on their own.

These rules are *very* simple and only involve switches and coils. For example,
a rule might be "when this switch is activated, pulse that coil", or "when this
switch is released, cut off the power to that coil".

Then when one of these "hardware rules" (as we call them in MPF) is written
to the hardware pinball controller, that controller can handle it all be itself
with minimal delay (usually in a millisecond or two) without having to deal with
USB and MPF and all that.

These rules are *not* permanently stored on the hardware controller, and in
fact they're constantly added, removed, and updated throughout the course of
a game. (Rules for flipper buttons and coils are removed when a ball ends and
added when a ball starts, etc.)

By the way, even when MPF writes hardware rules to the pinball controller, the
switch notification is still sent to MPF (since you might want to have
scoring or play a sound or something when that switch is hit). It's just that
in that case, the switch notification is sent to MPF for MPF's game logic
purposes, but the actual coil firing would have already happened thanks to the
hardware rule on the pinball controller.

This is all automatic
---------------------

The good news about these hardware rules is that there's nothing you need to
do to use them. This is just one of the things that MPF does behind the
scenes, thanks to the smart people who designed the pinball controllers.
