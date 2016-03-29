Config files versus "real" programming. Is MPF the right choice?
================================================================

When we talk about MPF, we really play up the fact that when you use MPF, you
can do 90%+ of your of your "programming" with MPF's YAML configuration files.

We've received criticism of that over the past few years, typically falling into
one of the following categories:

* Since everything in MPF is in config files, that's something new you have to
  learn. If you don't know MPF, you can't just look at a config file and know
  what's happening.
* Since config files insulate the game programmer from the code, when something
  doesn't work, you don't know if it's your config or a bug in MPF.
* Using config files limits game programmers in that they have to do everything
  the "MPF way."
* Coding is fun! MPF deprives people of that.

We understand the motivation behind all these thoughts, so in this document,
we're providing our perspective on these issues.

Config files in MPF: Use as much or as little as you want
---------------------------------------------------------

The most important thing to know about MPF is that even though we talk about how
you can do so much with config files in MPF, it's important to keep in mind
that you don't *have* to use config files for everything.

One way to think about MPF is that it's a solid set of pinball functionality
with a nice API, and then the config file interface is a separate component that
rides on top of that API and exposes it via easy-to-use YAML files.

That said, if you're a programmer and prefer to program against the API
directly, go for it! The API is well-documented and fairly stable now, so if you
don't want to use a single config file for anything, you can just use the MPF
API and do whatever you want.

The reality, though, is that building a complete game in MPF is a balance
between doing things in config files and writing code in Python. MPF supports
adding Python code to both your base game as well as to individual modes, so if
you want to write your entire game in Python, go for it!

At the end of the day, it doesn't matter whether your game is 90% configs and
10% code, or 80/20, 50/50, 20/80, etc. The exact balance depends on the
personal preference of the person building the game.

Personally there have been lots of times when we think, "Yeah, X action would be
like 20 confusing config lines or just two lines of Python, so I'm writing it in
Python." That's perfectly fine.

The real power comes when you start to mix-and-match. For example, you could use
the MPF config files to build out your base hardware interface and mode
structures, then use your own Python code to do the logic within a mode, then
use your mode code to post an event to use MPF's scoring system, etc.

I already know Python. Why learn obscure config files?
------------------------------------------------------

The software that runs pinball machines is complex. The complete MPF codebase is
over 15,000 lines of code, with thousands of lines of code to do things that
*seem* simple on the surface, like managing ball devices and tracking where all
the balls are at all times.

MPF's config files provide a friendly interface to all that complexity. So yes,
it's true that you have to spend a few hours learning about the ``ball_devices:``
section of the MPF config files in order to learn how to use them effectively.
But what's the alternative? You want to learn everything about how ball tracking
works in a pinball machine and then write all that from scratch yourself? That
will take a lot longer than it will to learn about how to configure ball
tracking in MPF. :)

Config files are limiting
-------------------------

Even though we have tried to envision many different scenarios and many
different types of pinball machines as we built MPF, it's true that MPF does
things a certain way, and the config files are a manifestation of the way MPF
does things. So there could be scenarios where you want to do something
different than how MPF does it.

But this does not mean that MPF is not the right framework for you.
If you don't like the way something works in MPF's ball tracking, you don't have
to completely write your own ball tracking from scratch. Rather you can use
MPF's ball tracking, subclass the methods and objects you want to change, and
then tweak them to work in your specific scenario.

Even if you want to completely replace one component of MPF, there hundreds of
different components, modules, and systems that go into a pinball machine.
Unless you want to write all of those from scratch, using an existing framework
lets you get a head start on many of the things that you need in your machine
that you don't want to write yourself.


Coding is fun! MPF deprives people of that
------------------------------------------

Some people have said, "I like to code. I don't *want* to just build my machine
quickly." Certainly we appreciate that, because we like to code too!

If you decide to write the software for your own pinball machine from scratch,
you will spend hundreds of hours writing low-level pinball things, like
hardware device management, ball tracking, a mode queue, player objects, a
display and sound system, etc.

If you use MPF, even if you write your own game logic in Python code, then you
can focus on the fun stuff while the core MPF team focuses on the boring low-level
pinball stuff.

Of course, if you're thinking, "But I *like* the low-level stuff, I want to
write that," then we would love to have you on our team helping to make MPF
better. :) We have a to-do list for MPF which will take years to complete, so if
you like to code, we'd love to have you help.

And if there's something that MPF does that you think you can do better, that's
an even better reason to contribute back to MPF. Please, help us make MPF
better!

We have success stories of this already. Brian Madden and Gabe Knuth started
writing MPF in 2014. Since then, MPF user Jan Kantert started using MPF, and
then he started tweaking things here and there (and submitting his changes back
to the MPF project.) Now Jan has completely rewritten MPF's ball device code,
our hardware platform interface, he's added multiball, ball lock, and ball
search functionality... the list goes on.

Another MPF user, Quinn Capen, has rewritten MPF's RGB LED interface, written
a complete pinball-focused advanced audio system, written an alternative
media controller based on Unity 3D...

John Marsh said, "It would be cool if there was a GUI wizard to help people set
up their machines," so now he's building that.

Hugh Spahr created his own pinball controller hardware (the Open Pinball
Project), and then wrote a platform interface for MPF so MPF users can use OPP
hardware too.

You get the idea.

The bottom line is that these are all users who love to code, so rather than
being scared away by MPF's config file interface, instead they embraced MPF, dug
in, and are making MPF better. So now all the time they spend writing code isn't
just limited to running on their machine which sits in their basement for 360
days a year, instead their code is running on pinball machines all over the
world, which is very fulfilling and cool!

When something breaks, I don't know if it's my config or an MPF bug?
--------------------------------------------------------------------

This is true. However if you're someone who knows how to program, then you can
go through the MPF code to see if it's a bug, and if so, you can fix it and
submit a pull request to fix that bug for everyone!

And if it's a configuration error, you can also edit the MPF documentation to
be more clear, and then submit a pull request to the docs, and now you've also
helped fix this issue for everyone!

Using MPF means you have a team of programmers making your machine better
-------------------------------------------------------------------------

The MPF project was started in May 2014. Since then we have over 5,000 hours of
time spent (both in code and documentation). More importantly, we're continuing
to update and expand MPF, with dozens of commits to the core code and docs
every week. (Probbly an average of 60 hours a week of work.)

If you use MPF, you get all that work for free. :) It's like having a team of
developers working 60 hours a week to make your game better. Pretty cool!

The bottom line
---------------

The creators of MPF are passionate about pinball, as is anyone who decides to
build a pinball machine and anyone who has to make the decision as to whether
they should use an existing framework like MPF or write their own code.

The beauty of MPF is that it's a bunch of people, from all over the world,
writing software and documentation which helps more people create more pinball
machines.

If you decide to go your own way, that's great. We support you! (Feel free to
rip off any ideas from MPF. We'd love it!) But don't write off MPF just because
you want to do "real" programming and MPF is a "config-based" project. We could
use the help of real programmers like you. :)
