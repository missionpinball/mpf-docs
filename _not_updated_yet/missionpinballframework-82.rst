


The Mission Pinball Framework Project
=====================================

The Mission Pinball Framework ("MPF") is a Python-based pinball
software framework that's used to run real pinball machines. Our goal
is to enablebothcasual builders andhard-core programmers to create the
software to run their pinball machines—whether it'snew game code for
an existing pinball machine, a "re-theme" of an old machine, or
totally custom / homebrew machine built from scratch. 95%+ of what you
need to do to program a pinball machine in MPF is done with text-based
configuration files, so even if you have no prior programming
experience, you can still do it! (We also have a well documented API
if you're a developer who prefers to write against that. Use as much
or as little of the config files as you want. It's all good.) MPF is
completely free and open source, released under the `MIT License`_. We
starting writing pinball code in 2013 and officially began the MPF
project in June 2014. At this point the framework is incomplete, but
we're making fast progress and we've already demonstrated a complete
game running on it. (Check out MPF'scurrent`feature list`_ here to see
what's done and what's left to do.) The MPF project was originally
started by *Brian Madden* and *Gabe Knuth*, though the MPF project
team has grown as more awesome people have contributed their time and
coding skills. (Check out the *AUTHORS* file in the download package
for the latest complete list.) Everyone working on MPF is doing it as
a labor of love, and there are typically 40-60 hours per week of total
coding, testing, and documentation writing. At this point MPF
represents over 5,000 hours of work! Think about that. If you've ever
dreamed of building your own pinball machine, MPF can give you a 5,000
hour head start on the software. :)



Project Goals
-------------

We have lofty (and ever evolving goals), including:


+ Be easy to use, so people with no prior programming experience can
  create a pinball machine.
+ Be powerful and flexible, so experienced programmers can easily
  understand its structure and shape it to their needs.
+ Support all "eras" of pinball machine hardware, from EM to early
  solid state with segmented displays to DMD to modern LCD-based and
  color DMD games.
+ Support converting existing machines to "new" code and brand-new
  games built from scratch.
+ Support as many different pinball controller hardware platforms as
  we can. (P-ROC, P3-ROC, FAST Pinball, Open Pinball Hardware, etc.)
  This should be done in a hardware-independent way, so you can
  literally switch between hardware controllers without having to make
  changes to your configs or code.
+ Support all the “traditional” pinball components, including ball and
  game handling, ball search, ball save, tilt, drop targets, lane
  change, pop bumpers, credit and coin counting, audits, service menus,
  game modes, multiball, high scores, etc.
+ Support the “new” pinball concepts, like player profiles, web-based
  reporting and control for operators, social media integration, iPhone
  integration, etc.
+ Most device, configuration, game logic, and modes should be done via
  simple-to-understand text-based configuration files.
+ Provide a solid API for experienced programmers who prefer to build
  games that way instead of using MPF's text-based configuration files.
+ Games should be easily customizable and should not look "stock" or
  like they're from the same template. (Fonts, text, images, animations,
  game flow, logic, display layout, modes, etc.) In other words, no one
  should be able to tell that a game is powered by MPF. :)
+ Be well-documented, both in terms of step-by-step “how to” guides
  and tutorials for beginners, as well as more advanced referencesfor
  hard-coreprogrammers.
+ Be extremely modular, allowing game programmers to subclass, extend,
  plug-in, and replace certain built-in functionality without breaking
  the everything or relying on "hacks".
+ Be robust enough to power commercial games, including games that are
  in revenue service in public locations.
+ Be 100% free with a liberal license that lets you do whatever you
  want, including selling games based on MPF without having to pay a
  license fee or give away your game's source code.


This website is very much a work in progress. (As is the MPF
software.) You followlatest updates via our `blog`_or
`@MissionPinball`_ on Twitter.



Compatible Pinball Machines and Hardware
----------------------------------------

The MPF project is software only. To use MPF with a physical pinball
machine, you need a hardware pinball controller which acts as the
"link" between the computer running MPF and the pinball machine's
driver and switch boards. (More details on how that works `here`_.)
MPF currently supports several different modern pinball controllers,
including:


+ `Multimorphic:`_ P-ROC and P3-ROC controllers
+ `FAST Pinball:`_ Core, WPC, and Nano controllers
+ `Open Pinball Project`_: Gen2 open source hardware hardware


MPF's architecture is hardware-independent, meaning we can write
interfaces for any pinball controller hardware out there. Some of
these hardware pinball controllers are replacements for the CPU boards
in existing machines, meaning you can use MPF to write your own
software to control existing machines. Williams / Bally / Midway WPC
machines, as well as Stern Whitestar and S.A.M. machines are the
easiest. Williams / Bally System 11 and Data East are pretty easy too.
(You have to replace the driver board in those too.) That said, MPF
can control any machine if you're up for building some custom wiring
harnesses to interface a modern pinball controller to the existing
machine. (We even `rewired a 1974 EM machine`_ which runs MPF great!)
You can also use these modern controllers with modern driver boards to
power your own completely custom-built brand new machines.



Alternatives to MPF
-------------------

When we first started searching for people writing their own software
for pinball machines in 2013, we found a lot of other projects. So if
you're just getting into this, we want to make sure you know about all
the options out there. (Many of these are free & open source.) Our
ultimate goal is to see more pinball in the world—regardless of
whether it's done with MPF! So instead ofthe Mission Pinball Framework
(which is what this site is about), you could also use one of the
following other software frameworks:


+ `PyProcGame`_ (Python framework for the Multimorphic P-ROC and
  P3-ROC pinball controllers, from Gerry Stellenberg and Adam Preble.)
+ `PyProcGameHD`_(Fork of Pyprocgame which uses an LCD-based HD full
  color DMD instead of the traditional DMD, from Michael Ocean and Josh
  Kugler. Includes a "Skeleton Game" to get you started quickly. Works
  with P-ROC and P3-ROC hardware only.)
+ `NetProcGame`_ (.NET version of PyProcGame for the P-ROC and P3-ROC,
  written by Jimmy Lipham)
+ `Rampant Slug Pinball Framework`_ (Very early framework written in
  .NET. Has an awesome GUI. Works with P-ROC and P3-ROC hardware only.)
+ `FreeWPC`_ (Write code in C and compile & burn it to ROMs which you
  can use in existing WPC machines, from Brian Dominy)
+ `Open Pinball Project`_ (Open source pinball framework for
  controlling OPP hardware.)
+ `PinKit`_ (Software & hardware combination from Kerry Imming)
+ `milliSoft PINterface`_ (Software & hardware combination from German
  company milliSot. Here's an `English manual`_ if you want to see what
  they're about.)


Please `contact us`_ if we've missed any! There's also a great wiki at
`PinballMakers.com`_ with lots of information for people who want to
create their own pinball machines.



Documentation
-------------

Pinball machines are complex, as is the software that runs them. We're
trying to make everything as easy as possible, and so far we have over
800pages of documentation explaining everything step-by-step.
(Concepts, how to guides, tutorials, programming references, etc.) The
user documentation lives at`missionpinball.com/docs`_, and the API
reference is available at `missionpinball.com/apidocs`_. You can
explore the documentation via the tree view menu in the left-hand
sidebar of this page, or download a PDF bundle of all the docsfrom our
`downloads`_ page.



Step-by-Step Tutorial
---------------------

We have a `getting started tutorial`_ which walks you through
everything, from downloading MPF to getting a full game playing (with
scoring, DMD, multiple players, game modes, etc.). You can literally
go from never having heard of MPF to a working game on a physical
pinball machine in a few days. (And you can go from "zero to flipping"
in a few hours.)



How-To guides
-------------

Once you complete the tutorial, you can browse our very detailed and
specific `How To guides`_ which show you how to add the features you
want. We have several guides available today, with dozens more in the
works. (If you want to learn how to do something, post a question in
our forum and we'll write a how to guide for it!)



Installing MPF
--------------

We have an `installation guide`_ that walks you through installing
MPF, either with our automated all-in-one installers (for Windows,
Mac, and Linux) or by doing it manually. The all-in-one installers
should get you from zero to running MPF in under three minutes, and
even manually installing everything should only take about 10 minutes.
It's all really easy.



MPF Projects & Source Code
--------------------------

The Mission Pinball Framework project has a few different components
which are available as separate GitHub repos:



The Mission Pinball Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This MPF core engine is in the ` *mpf*`_ repo. The MPF core is
responsible for: ` `_


+ Interfacing with the physical pinball hardware
+ Managing and controlling all devices, including drivers, lights,
  LEDs, switches, ball devices, diverters, drop targets, servos, etc.
+ Managing and tracking all shots, shot groups, status, progress, etc.
+ Game, ball, player, and machine management
+ All game logic
+ Starting and stopping modes
+ Shots, scoring, times, countdowns, bonus calculations, audits, etc.
+ Running and coordinating all effects shows
+ Interfacing with files, including the game config files, audits,
  game data, high scores, etc.
+ Running the main game loop, clock, and events system




The MPF Media Controller
~~~~~~~~~~~~~~~~~~~~~~~~

The MPF media controller is in the ` *mpf-mc*`_ repo. It's a
standalone process (so it works nice on multi-core processors) which
is responsible for:` `_


+ On screen display windows
+ DMD / Color RGB DMD displays
+ Images, animations, video, text, and all displays widgets
+ Sounds & audio
+ Multi-language translations (including alternate asset packages)
+ All game UI
+ Loading and unloading game assets (on demand, if needed)




The MPF Monitor
~~~~~~~~~~~~~~~

The MPF Monitor is an upcoming tool in the planning stages (it doesn't
exist yet) that you will be able to use to connect to a live running
instance of MPF to control, set, and view live information from a
running instance of MPF. It will let you do things like seeing the
current states of lights & LEDs, coils, and switches, as well as let
you activate switches via your computer just by clicking on them. The
MPF Monitor will be useful when you're developing your MPF machine
when you don't have your physical machine handy, and it will be great
for troubleshooting, even letting you "pause" MPF to dig into its
current state to find out exactly what's going on. The MPF Monitor
will let you view (and update) the states of devices, player and
machine variables, modes, logic blocks, timers, events, hardware, and
pretty much anything else that's part of MPF.



The MPF Wizard
~~~~~~~~~~~~~~

` `_The MPF Wizard is an upcoming project (in the ` *mpf-wizard*`_
repo) which is graphical tool you can use to build and configure your
MPF machine configurations. (Think "double click and change settings
for a device" versus "find the device in a config file, look up the
options, and re-save the file".) Whereas the MPF Monitor will be used
to view the state of a live running MPF instance, the MPF Wizard will
be used to actually build your configs, slides, modes, and all your
MPF game logic. The Wizard is in the very early stages and doesn't
really do anything yet (apart from being able to open your config
files), but we're working on it!



MPF Examples
~~~~~~~~~~~~

` `_The MPF Examples (in the ` *mpf-examples*`_ repo) contains code
and config examples you can use as you're learning MPF and working on
your own game.. There are demos and code that goes along with the How
To guides and the tutorial, as well as hardware configurations for a
bunch of real machines. None of these examples contained any
copyrighted material, so you can use everything you find here in your
own machines.



Support & Community & Fun People
--------------------------------

We have an active `user forum`_ with over 3,000 posts where we talk
about MPF use, development, ideas, and where people using MPF share
photos and videos of their projects. People using MPF attend many of
the major pinball conferences, and we're always happy to get together
and talk pinball! (We have a `forum dedicated to upcoming events`_
where MPF users can meet in person.)



Who owns MPF? What's the license?
---------------------------------

MPF is released under the `"MIT" license`_ (also called the "Expat
license") which is extremely permissive. You can do just about
anything you want with it. Use it. Copy it. Modify it. Merge, publish,
distribute, sublicense and/or sell it. If you make changes, you can
choose to share them back with the community. Or not. If you make a
sell a commercial pinball machine based on MPF, you do not have to pay
us anything. You also do not have to release your machine's source
code if you don't want to. We don't "own" MPF any more than you do.
You can even make closed-source derivatives of MPF and sell them. You
can do whatever you want with it. So go nuts. Rip us off. Take the
code. Make it yours. Don't give us credit... It's all good! Seriously.
We're just putting the code out there. We just want to see more
pinball in the world and we don't care what you do with MPF!



Next Steps & Getting Started with MPF
-------------------------------------

Feel free to browse the MPF documentation viathe tree-view menu on the
left side of this page, start reading our `MPF introduction`_, or jump
right into our `step-by-step tutorial`_ to get started!

.. _PinballMakers.com: http://pinballmakers.com/
.. _"MIT" license: https://en.wikipedia.org/wiki/MIT_License
.. _FreeWPC: https://code.google.com/p/freewpc/
.. _downloads: /downloads
.. _rewired a 1974 EM machine: https://missionpinball.com/blog/category/games/big-shot-em-conversion/
.. _Multimorphic:: http://pinballcontrollers.com
.. _FAST Pinball:: http://www.fastpinball.com
.. _mpf-examples: https://github.com/missionpinball/mpf-examples
.. _@MissionPinball: http://twitter.com/missionpinball
.. _installation guide: https://missionpinball.com/docs/installing-mpf/
.. _here: https://missionpinball.com/docs/introduction/hardware-controllers/
.. _blog: /
.. _English manual: http://www.millisoft.de/products/pinterface/PINterface_USB_Pinball_Interface_Kit_Manual.pdf
.. _PyProcGameHD: http://mjocean.github.io/PyProcGameHD-SkeletonGame/
.. _milliSoft PINterface: http://www.millisoft.de/pinterface_de.php
.. _MIT License: http://opensource.org/licenses/MIT
.. _forum dedicated to upcoming events: https://missionpinball.com/forum/f/events/
.. _mpf-mc: https://github.com/missionpinball/mpf-mc
.. _missionpinball.com/apidocs: https://missionpinball.com/apidocs
.. _How To guides: https://missionpinball.com/docs/howto/
.. _PinKit: http://www.planetimming.com/PinKit/
.. _mpf-wizard: https://github.com/missionpinball/mpf-wizard
.. _NetProcGame: https://github.com/Compy/NetProcGame
.. _feature list: https://missionpinball.com/docs/introduction/current-features/
.. _Rampant Slug Pinball Framework: http://rampantslug.com.au/tag/pinball-framework/
.. _Open Pinball Project: https://openpinballproject.wordpress.com/
.. _PyProcGame: http://www.pinballcontrollers.com/forum/index.php?board=9.0
.. _step-by-step tutorial: /docs/tutorial
.. _missionpinball.com/docs: /docs
.. _MPF introduction: https://missionpinball.com/docs/overview/
.. _mpf: https://github.com/missionpinball/mpf/
.. _user forum: /forum
.. _contact us: mailto:brian@missionpinball.com


