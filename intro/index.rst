Getting Started with MPF
========================

So, you want to write your own software to control a pinball machine. Awesome!
MPF will try to make that as easy as possible, but it's going to be a lot of
work. "Pinball is hard", as many have said, and even though MPF handles a lot
of the low-level stuff, you still need to figure out your game logic, modes,
game flow, scoring, light shows, displays, animations, sounds, bonus, etc.

We assume that if you're on this page, you know what the Mission Pinball
Framework is (which we refer to as *MPF*). If not, check out our overview
of the `MPF Project <https://missionpinball.com/mpf/>`_.

Anyway, you'll use MPF to configure and control everything in your machine,
including:

* Physical hardware (switches, LEDs, lights, motors, coils, servos, steppers,
  etc.)
* The display (or displays): DMD, RGB LED, and/or LCD
* Audio & Sounds
* Logical "pinball" things, like ball troughs, flippers, pop bumpers, diverters,
  locks, multiball, etc.
* Coordinated "shows" of actions to flash lights, fade LEDs, play sounds and
  video, etc.
* Game modes, including basic modes like attract, ball search, tilt, high score
  entry, match, bonus, etc., as well as whatever modes you think up for your
  machine (shoot the clown, zap the alien, etc.)
* Player management, including player progress and tracking towards goals.
* Plus lots of other things that we'll get to eventually.

We tried to build all this "standard" pinball stuff into the MPF project in
a way that lets you configure everything with text-based configuration files
that are easy for beginners and people without prior programming experience to
understand.

We also built MPF so that it's hardware-independent. (A list of all the hardware
MPF currently supports is :doc:`here</hardware/index>`, and we're always adding more.)

The Mission Pinball Framework is a work-in-progress!
----------------------------------------------------
MPF is far from complete. We're not even to our 1.0 release yet so the code is
very "alpha" at this point. That said, we have a lot done and you can absolutely
build a game with it today.

The core system is done. You can read in switches, track balls, and fire coils.
We have the game flow built, so the machine can track players and ball numbers
and drains and turns. You can start and end a game, build light shows, and
create game logic. You can create game modes. We have DMD, LCD, color DMD, and
audio support. But there's still a long, long way to go. We are sharing MPF now
just so you can get a preview of it to see where we're going, and (if you want)
so you can contribute ideas and code. We don't have specific timeframes in mind
for a 1.0 release. (We've been releasing new stable-ish versions every few
months with dev versions almost daily.) That said, we have a "to do" list with
probably `2 or 3 years' worth of ideas <https://missionpinball.com/blog/2014/10/the-mission-pinball-framework-roadmap-vision-for-the-future-of-pinball/>`_,
and we're sure that list will continue to grow.

Next steps
----------
We recommend that you at least glance over the following sections of the
documentation to get familiar with some additional MPF concepts. (Though if
you're really chomping at the bit to get started, go ahead and jump into the
:doc:`tutorial </tutorial/index>` now, and you can read these additional things
as they come up.)

.. toctree::
   :maxdepth: 1

   how_mpf_talks_to_hardware
   machine_config_files
   running_your_game
   config_files_vs_programming
