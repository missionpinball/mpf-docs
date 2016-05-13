How MPF talks to physical pinball machines
==========================================

MPF is written in the Python computer language runs on a computer. That
computer is connected to your pinball machine controller (P-ROC, FAST, OPP,
etc.) via a USB cable.

So if you write your pinball machine's software using MPF, you need a computer connected
to your pinball machine the entire time the pinball machine is on. In a sense,
MPF running on this "host computer" is the brain of the pinball machine.

This doesn't mean that you have to have your laptop connected to your pinball
machine just to play a game. Most people use a laptop while they're developing
their MPF game, and then when their game is done, they permanently install
a small cheap computer inside their machine. (This could be something as small
as $35 Raspberry Pi 3, or maybe a $150 small form factor Intel Atom
motherboard. The exact requirements for the computer that runs MPF depend on
what you want to do in your game.)

This diagram shows how this looks and what does what:

.. image:: /_static/images/how-mpf-runs-a-pinball-machine.png

The most important thing to understand is that the P-ROC, FAST, or OPP hardware
controllers *do not actually run your Python-based code*, rather, they
act as the interface between your physical pinball machine and a host computer
running MPF (though they are configured to respond to some
time-critical events themselves, such as directly firing coils based on switches
like the flippers, slingshots, and pop bumpers).
