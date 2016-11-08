Choosing a computer to run MPF
==============================

In addition to picking a pinball controller platform, you also need to
decide what type of host computer you'll use. (By "host computer,"
we're talking about the computer that will run MPF which will talk to
the pinball controller via USB.) There are lots of host computer
options, including small single-board computers, laptops, small-form
factor x86 motherboards, etc. You're also going to have to decide on
what OS you use (Windows, Linux, or Mac).

What kind of performance is required?
-------------------------------------

One of the biggest things that will affect your choice of host
computer will be the performance you need. Obviously the host computer
has to "keep up" with your game, so if you pick an under-powered host
computer then your game loop can slow down and you'll have issues. The
computing needs of a pinball machine are actually pretty small. The
core game, modes, ball tracking, dealing with switches, etc.—-all of
that can probably be done on a very tiny computer. The real driver
these days is your video and graphics. If you have a hi-def LCD window
with lots of full video and layers and on-screen elements all blended
together, then you're going to need a "real" computer to drive it
and will not be happy with a small single-board computer.

Memory
~~~~~~

MPF itself doesn't require much memory. The real memory use comes from loading
all the images, sounds, and videos into memory. MPF can load those on demand
(or automatically when a mode starts, and unload them when the mode ends). This
works well if you have a fast disk (SSD).

However, if you have enough memory, MPF can pre-load everything when it starts.
This will increase the startup time of your machine, but will make it so that
everything runs fast once its booted.

Note that 32-bit OSes only allow individual applications to access 2GB of
memory, so if you have 6 gigs of assets and want to buy an machine with 8GB of
RAM, you need to run a 64-bit OS. (MPF supports both 32-bit and 64-bit systems.
If you run on 64-bit, make sure you also get the 64-bit version of Python.)

CPU
~~~

The trend in computing these days (for both "real" computers and small
single-board computers) is multi-core. Almost every computer these
days has a dual-core or quad-core processor.

MPF uses two processes (one for the game engine and one for the media
controller), so it can make use of a dual-core system. However there is probably
not much benefit to MPF running on machines with more than 2 cores (other than
it frees up more cores for other non-MPF things.)

Disk
~~~~
Disk space it not really an issue these days. The real question is disk
performance in terms of SSD versus traditional spinning magnetic hard disks.

SSD is fast, you can can get away with less memory since MPF can dynamically
load and unload assets. However SSD can be damaged by unsafe shut downs, so to
put an SSD in a pinball machine requires batteries to keep the computer alive
while it shuts down or some partition configuration to set up read-only
partitions and to disable wear leveling.

Single-board versus "real" computers?
-------------------------------------

Picking an OS
-------------

The checklist
-------------

Now that you've read about all the background information that goes
into picking a host computer, let's break it down into the questions
you need to answer to pick the one that makes sense for you.

What OS are you familiar with?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More and more commercial machines are running Linux. But if you're
comfortable with Windows and you've never used Linux, then by all
means do not put a Linux computer in your pinball machine. It's just
not worth the headache. Sure, this might mean that you have to buy a
$150 motherboard/SSD/RAM/PSU combination versus a $50 single board
computer, but meh, that 100 bucks will be worth it in terms of future
pain avoided. And besides, pinball machines cost thousands of dollars
to build. What's another 100 bucks to make your life easier?

Do you have anything you can use now?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best host computer is the one that you already have. :) Seriously,
if you have something laying around, just start using it. You can
always change it out later. BTW, we've received a few questions from
people wanting to use Mac Minis.

Is this a one-off machine, or are you taking something into production?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What are your graphics and display requirements?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Bottom Line
---------------

Remember that MPF and Python work identically regardless of whether
they're running on Windows, Mac, or Linux. So even if you pick the
"wrong" host computer now, you can always change it out later without
having to change any of your code or configuration files. So if you
have an old laptop sitting around then go ahead and use it for MPF.
You can always swap it out with a small single-board computer down the
road.
