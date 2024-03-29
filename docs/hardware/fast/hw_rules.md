---
title: How to configure Flippers, Slingshots, Pop Bumpers, and other
  "quick response" devices (FAST Pinball)
---

MPF uses some special tricks to ensure that "quick response" devices
like flippers, slingshots, and pop bumpers are able to respond to switch
changes as fast as possible. (Read more about that [here](../hw_rules.md).)

When using FAST Pinball hardware, there are a few things you should know
about these hardware rules.

First, remember that FAST I/O boards contain both switch inputs and
driver outputs.

For best performance when using a FAST Nano Controller, either:

1.  Make sure switches & drivers for hardware rules are on the same IO
    board, *or*
2.  Make sure switches are the first 8 switches on the first I/O board

!!! note "This applies to the FAST Nano Controller only"

    If you're using a FAST Neuron Controller, any switch from any
    I/O board can be used with hardware rules for any driver, so none
    of this applies.

In other words, if you have a pop bumper or slingshot, make sure that
the activation switch for that device and the coil for that device are
plugged into the same IO board. That shouldn't be too hard, since
you'll have multiple IO boards underneath your playfield.

For flippers, however, that's probably not possible, so FAST Pinball
controllers use the concept of "priority" switches which are the first
8 switches plugged into the first board in the chain. (These will be the
switches numbered `0-0` through `0-7`.)

These priority switches are sent across the FAST loop network
immediately which means they can be used with hardware rules to trigger
drivers (coils) on any I/O board in the network.

If you only have two flippers in your machine, this is probably nothing
you'll ever need to worry about since it will be easy to connect the
flipper switches and coils to the same IO board (and of course the same
will be true for all the other quick response devices in your machine).

But if you have more than two flippers, there's a good chance that the
additional flippers will be somewhere far away from the flipper buttons
and the main flippers. In that case, no problem, but make sure the IO
board that has your flipper buttons connected to it is the first one in
the chain, and make sure your flipper buttons are connected to one of
the 0-7 positions on that IO board, and then everything will be fine.

## What if it did not work?

Have a look at our
[FAST troubleshooting guide](../../troubleshooting/index.md).
