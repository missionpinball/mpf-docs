Getting Started with MPF
========================

We assume that if you're on this page, you know what the Mission Pinball
Framework is (which we often refer to as *MPF*). If not, checkout out our overview of the `MPF Project <https://missionpinball.com/mpf/>`_.

If you're still reading, it's because you want to write your own software to
control a pinball machine. Awesome! MPF will try to make that as easy as
possible, but it's going to be a lot of work. "Pinball is hard", as many have
said. Even with MPF, pinball is still hard.

The good news is that MPF tries to make the software part of creating a pinball
machine easy. MPF does all the boring stuff so you can focus on the fun parts.

You'll use MPF to configure and control everything in your machine, including:

* Physical hardware (switches, LEDs, lights, motors, coils, etc.)
* Your display (DMD, RGB LED, or LCD)
* Audio & Sounds
* Logical "pinball" things, like ball troughs, flippers, pop bumpers, diverters, locks, multiball, etc.
* Coordinated "Shows" of actions to flash lights, fade LEDs, play sounds and video, etc.
* Game "modes", including base modes like attract, ball search, tilt, high score entry, bonus, etc., as well as whatever
  modes you think up for your machine (shoot the clown, zap the aliean, etc.)
* Player management, including player progress and tracking towards goals.
* Plus lots of other things that we'll get to eventually.

We tried to build all this "standard" pinball stuff into the base MPF project in
a way that lets you configure everything with text-based configuration files
that are easy for beginners and people without prior programming experience to
understand.

We also built MPF so that it's hardware-independent. It currently supports `FAST Pinball <http://fastpinball.com>`_ (Core,
WPC, and Nano) controllers, `Multimorphic <http://www.pinballcontrollers.com>`_ (P-ROC and P3-ROC) controllers, and the
`Open Pinball Project's <https://openpinballproject.wordpress.com/>`_ Gen2 open source controllers. (And if anyone else
enters the pinball controller market, we'll try to support them as well!) We love that there's competition in the
market, but don't want to get bogged down into "Ford vs. Chevy" arguments. Pick whatever hardware you want, and MPF will
be there to run on it!

The Mission Pinball Framework is a work-in-progress!
----------------------------------------------------
MPF is far from complete. We're not even to our 1.0 release yet so the code is very "alpha" at this point. That said,
we have a lot done and you can absolutely build a game with it today.

The core system is done. You can read in switches, track balls, and fire coils. We have the game flow built,
so the machine can track players and ball numbers and drains and turns. You can start and end a game, build
light shows, and create game logic. You can create game modes. We have DMD, LCD, color DMD, and audio
support. But there's still a long, long way to go. We are sharing MPF now just so you can get a preview of
it to see where we're going, and (if you want) so you can contribute ideas and code. We don't have specific
timeframes in mind for a 1.0 release. (We've been releasing new stable-ish versions every few months with
dev versions almost daily.) That said, we have a "to do" list with probably `2 or 3 years' worth of ideas
<https://missionpinball.com/blog/2014/10/the-mission-pinball-framework-roadmap-vision-for-the-future-of-pinball/>`_,
and we're sure that list will continue to grow.

.. toctree::

   machine_config_files
   running_your_game
   config_files_vs_programming
