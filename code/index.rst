Adding custom code
==================

One of the goals of the Mission Pinball Framework is that we want to
get as much machine configuration as possible into the *machine
configuration files*. It's our intention that maybe 90-to-95% of a
machine's "code" can be built out of the box just by configuring those
files.

So far we're pretty close. In addition to controlling
switches, lights, and coils, you can also use the config files
to set up shots, scoring, audio, DMD animations, events, game
modes, and game logic. We've also included many built-in modes and
devices which you can configure completely with config files, including
tilt, high score, ball save, ball search, multiball, ball locks,
extra balls, etc.

That said, we recognize that to "finish" a game, you'll have to write
some custom Python code. Our goal is that these code snippets should
be easy to write and test, and (most importantly), they should not
require you to "hack" the framework code itself. (Not that we have a
problem with hacking—-we love it! The problem though is if you hack the
MPF code then it's really difficult to reintegrate your hacks with the
official builds which are released every few weeks.)

The decision as
to when to use config files versus when to use custom code is not a
black-or-white one. Really it comes down to what you want to do,
what examples are out there, and how comfortable you are with Python.

Some people who love coding in Python just use MPF config files to get
the bare bones game up and running, while other people choose do as
much as they can in config files and to keep the custom coding to a
bare minimum. Regardless of where you fall on that spectrum, we tried
to build MPF to make it as easy as possible to mix in actual Python
code. We also created a few Python classes that hide a lot of the
complexity of MPF, meaning you can get your custom code integrated
with just some basic Python knowledge. There are two easy ways to add
custom Python code to your game project:

+ Sciptlets , which are "machine-wide" chunks of code that are always
  active.
+ Mode-specific code, which allows you to write custom Python code
  which is only active when a particular game mode is active.

As for when to use scriptlets versus mode-specific code, we tend to
use scriptlets for any custom code that will be used through MPF
(either in multiple game modes or when a game is not running). For
example, we used scriptlets to hold the Python code to control the
Claw in *Demolition Man*, the cannons in *Star Trek: The Next
Generation*, and the Dead World lock and crane unloader in *Judge
Dredd*.

API Documentation
-----------------

We have documented the API for MPF and MPF-MC. That documentation
lives at `api.missionpinball.org <http://api.missionpinball.org>`_, and it's the reference we use
ourselves when writing MPF.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   API / programmer's reference <http://api.missionpinball.org>
   best_practices

