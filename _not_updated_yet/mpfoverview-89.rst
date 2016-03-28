
Writing your own software for a pinball machine is a lot of
work—regardless of whether you're writing brand-new code for your
favorite '90sWilliams machine or you're designing and building your
own machine from scratch. In addition to configuring all your hardware
devices, you have to figure out your shots, scoring, modes, and game
features, and you also have to build light shows, DMD and/or LCD
animations, sound effects, music, dialog callouts, and probably a
million other little things. Our goal with the Mission Pinball
Framework (which we often refer to as *MPF*) is to create a pinball
machine software platform you can use to run a real pinball machine.
Our view is that many of the "standard" features of modern pinball
machines are pretty similar from game-to-game, so we ought to be able
to create a software platform that does 90% of the basics right out of
the box—allowing you to get to the fun stuff as soon as possible.
We've built MPF so that it's hardware-independent. MPF currently
supports `Multimorphic`_ (P-ROC and P3-ROC) and `FAST Pinball`_(Core,
WPC, and Nano) controllers, and if anyone else enters the pinball
controller market, we'll try to support them as well! Regardless of
the hardware platform you choose, getting your game fully built on MPF
is going to take some time. Downloading and installing the software is
easy, but building and programming the actual configuration for your
machine can be pretty involved. We're trying to make that as easy as
possible, (and we have a `step-by-step tutorial`_ that can get you
flipping in a few hours and running a full game with modes and scoring
and display and sound effects in a few days), but with with all your
game modes, rules, light shows, animations, and audio, it's definitely
going to be a labor of love!



The Mission Pinball Framework is a work-in-progress. (And probably
always will be!)
----------------

MPFis far from complete. We're not even to our 1.0 release yet so the
code is very "alpha" at this point. That said, we have a lot done and
you can absolutely build a game with it today.The core system is done.
You can read in switches, track balls, and fire coils. We have the
game flow built, so the machine can track players and ball numbers and
drains and turns. You can start and end a game, build light shows, and
create game logic. You can create game modes. We have DMD, LCD, color
DMD, andaudio support. But there's still a long, long way to go. We
are sharingMPF now just so you can get a preview of it to see where
we're going, and (if you want) so you can contribute ideas and code.
We don't have specific timeframes in mind for a 1.0 release. (We've
been releasing new stable-ish versions every 6 weeks or so with dev
versions almost daily.) That said, we have a "to do" list withprobably
`2 or 3 years' worth of ideas`_, and we're sure that list will
continue to grow. Brian Madden & Gabe Knuth,Mission Pinball

.. _FAST Pinball: http://www.fastpinball.com
.. _Multimorphic: http://www.pinballcontrollers.com
.. _2 or 3 years' worth of ideas: /blog/2014/10/the-mission-pinball-framework-roadmap-vision-for-the-future-of-pinball/
.. _step-by-step tutorial: https://missionpinball.com/docs/tutorial/


