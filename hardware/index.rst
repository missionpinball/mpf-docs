How MPF talks to "real" pinball machines
========================================

MPF is written in the Python computer language and requires a "real" computer
to that can run Windows, Mac OS X, or Linux in order to function. So if you
write your pinball machine's software using MPF, you need a computer connected
to your pinball machine the entire time the pinball machine is on. In a sense,
MPF and the "host computer" is the brain of the pinball machine.

This doesn't mean that you have to have your laptop connected to your pinball
machine just to play a game. Most people use a laptop while they're developing
their MPF game code, and then when their game is done, they permanently install
a small cheap computer inside their machine. (This could be something as small
and cheap as $30 Raspberry Pi 3, or maybe a $100 small form factor Intel Atom
motherboard. The exact requirements for the computer that runs MPF depend on
what you want to do in your game. More on that later...)

.. image:: /_static/images/how-mpf-runs-a-pinball-machine.png

The most important thing to understand is that the P-ROC and FAST hardware
controllers *do notactually run your Python-based code themselves*, rather, they
act as the interface between the physical pinball machine and a host computer
running your game code (though they are configured to respond to some
time-critical events themselves, such as directly firing coils based on switches
like the flippers, slingshots, and pop bumpers). At this point you might be
thinking, "What??? I don't want to have my laptop attached to my pinball machine
to run it!" While it's true you *could* just put a laptop in the bottom of the
machine to run it, most people end up buying a small form-factor PC board
running Linux or something and putthat inside the machine to run the actual
python game code. There are several options for this today, including
theBeagleBone Black, ODROID, Raspberry Pi 2, etc. Or you can use a
mini-ITX Intel-based board and run Windows or put a Mac Mini in your cabinet.
Really it can be anything as long as it can run Python.

.. toctree::

   custom_machines
   existing_machines
   supported_hardware
