
Now that you know the conceptual overview of how MPF works, how do you
choose a physical pinball machine to use it with? You have three
options:


+ Use an existing machine, keep it as it is, and write your own rules
  using MPF.
+ Use an existing machine, strip it down and "retheme" it to your own
  theme, and use MPF for the software.
+ Build a new machine from scratch.


Certainly the easiest way to get started is to use an existing
machine. In fact many machines will let you replace the built-in CPU
board with a P-ROC or FAST controller in about 5 minutes, and you can
be up and running with your own custom code in a few hours! The
easiest existing machines to work with:


+ Williams / Bally / Midway "WPC"-era (1990-1998, Funhouse
  throughCactus Canyon)
+ Stern S.A.M (2006-2014, World Poker Tour through The Walking Dead)
+ Sega/Stern Whitestar (1995-2006, Apollo 13 through Terminator 3)


These machines are easiest because you can just "drop in" a modern
controller. You can use a P-ROC or FAST WPC controller for WPC
machines, and you can use a P-ROC with Stern machines. In both of
these cases you reuse the existing driver boards, so all you need is
the P-ROC or the FAST WPC controller (about $300 each) and you're all
set. After these, machines, the next-easist batch of machines are:


+ Williams / Bally System 11 machines
+ Data East (which were clones of the System 11 boards)


To use System 11 / Data East, you need a driver board from Mark
Sunnucks (about $200) that will connect your P-ROC or FAST WPC
controller to the existing wiring. (See this `How To guide for more
details`_.) Finally, if you want to use an older solid state machine
with MPF (late '70s through early '90s), that's still possible, but
you would need to replace the existing driver boards with newer P-ROC
or FAST driver boards. You'd also need to build custom wiring adapters
to interface the existing wiring to the specific connectors and
pinouts the new driver boards need. This is still pretty
straightforward and something you can probably do in a day or so. This
will cost you around $600 (depending on the machine) because you'd
have to buy the P-ROC or FAST controller as well as a few hundred
dollars in new driver boards. If you really want to go crazy and use
an EM machine with MPF, that's possible too. (In fact `we did this`_
with a 1974 Gottlieb Big Shot machine.) In this case you most likely
have to remove all of the existing wiring and solder all new
connections, so you're looking at probably 100 hours (again, depending
on the machine). This might be a bit more expensive (perhaps
$800-$1000) because all those score reels have lots of extra switches,
lights, and coils you need to hook up, so you'll need more driver
boards. (MPF has a score reel module so you can hook right into the
mechanical score reels with modern technology. It's very cool!)

.. _How To guide for more details: https://missionpinball.com/docs/howto/system-11/
.. _we did this: https://missionpinball.com/blog/category/games/big-shot-em-conversion/


