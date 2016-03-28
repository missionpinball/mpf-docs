
If you want to use the Mission Pinball Framework to write software for
a real pinball machine, you need some way to get your code onto the
machines. Unfortunately you can't just install Python on a pinball
machine. "Real" machines don't have normal computers controlling them,
rather, they're based on custom-built control systems which run code
compiled specifically for each platform. Plus, a lot of pinball
machines are old, meaning their hardware is weak by today's standards.
(For example, all those mid-90s Williams WPC games that we love are
powered by a Motorola 6809 CPU running at 2 MHz with 64 KB of RAM.
(Yeah, that's 64 *kilo*bytes, not megabytes.) So you're not getting
the Mission Pinball Framework on there. (If you want to write software
which runs on the original 6809 Williams hardware, check out Brian
Dominy's `FreeWPC project`_. You can write new game code in C++,
compile it for the 6809, burn it to a ROM chip, and replace your
existing machine ROMs with your custom ones. Crazy! And awesome!) If
you want to use MPF to write your own custom game code for an
*existing* Williams or Stern pinball machine, you replace the
originalCPU board in the machine with a modern pinball controller
board (called a *hardware controller*) such as a P-ROC or FAST
Controller. (More on those in a bit.) That hardware controller
interfaces with the existing machine'sdriver boards tocontrol the
coils, lights, and DMD, and it provides a "bridge" (via USB) to a host
computerrunning Python and the Mission Pinball Framework. If you want
to use the MPF to power a new *custom* pinball machine that you build
yourself, you can buy new custom driver boards from the same people
who make the P-ROC orFAST Pinball controllers. (These P-ROC or
FASTdriver boards are typically only used with custom machines,
because if you're replacing the main CPU board in an existing machine
then it's easiest to just use the existing driver boards as they are.
i.e. there's no need to rewire anything.) The important takeaway is
that hardware controllers from FAST & P-ROC can control the original
Williams/Stern driver boards or their own custom driver boards. (More
on that in a bit too.) The most important thing to understand is that
the P-ROC and FAST hardware controllers *do notactually run your
Python-based code themselves*, rather, they act as the interface
between the physical pinball machine and a host computer running your
game code (though they are configured to respond to some time-critical
events themselves, such as directly firing coils based on switches
like the flippers, slingshots, and pop bumpers). ` `_ At this point
you might be thinking, "What??? I don't want to have my laptop
attached to my pinball machine to run it!" While it's true you
*could*just put a laptop in the bottom of the machine to run it, most
people end up buying a small form-factor PC board running Linux or
something and putthat inside the machine to run the actual python game
code. There are several options for this today, including
the`BeagleBone Black`_, `ODROID`_, `Raspberry Pi 2`_, etc. Or you can
use a mini-ITX Intel-based board and run Windows or put a Mac Mini in
your cabinet. Really it can be anything as long as it can run Python.



How the Mission Pinball Framework interfaces with hardware controllers
----------------------------------------------------------------------

One of the primary goals of MPFis to behardware-independent. In other
words we want MPF to work with any hardware pinball controller out
there. We achieve hardware independence by abstracting all the
hardware calls to our `platform interface module`_, and then our
platformmodule talks to a hardware-specific module which is specific
to the actual hardware platform you're using. (So in our
`/platforms`folder we have a Python module called `p_roc.py`which is
used to talk to a P-ROC, `p3_roc.py` talks to a P3-ROC, `fast.py`
talks to FAST controllers, etc.) It's sort of a *"we know the low-
level details of the different hardware controllers so you don't have
to"* kind of thing. :) This also means that a game programmer, you
have the flexibility to change your hardware platform at any time
without having to change any game code. You could even release a game
code update that works on multiple platforms—all with the same code!
If you're using your custom code in an existing Williams WPC game, you
can literally switch platforms by changing a single line in a config
file. `Here's a demo video`_ of us switching out a P-ROC controller
for a FAST controller in 3 minutes and running the same game code on
both.

.. _BeagleBone Black: http://beagleboard.org/black
.. _platform interface module: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/
.. _FreeWPC project: http://freewpc.googlecode.com/
.. _ODROID: http://www.hardkernel.com
.. _Here's a demo video: https://missionpinball.com/blog/2014/10/with-the-mission-pinball-framework-you-can-swap-between-a-p-roc-and-fast-pinball-controller-in-3-minutes/
.. _Raspberry Pi 2: https://www.raspberrypi.org/products/raspberry-pi-2-model-b/


