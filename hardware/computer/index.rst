Choosing a PC for MPF
=====================

In addition to picking a pinball controller platform, you also need to
decide what type of host computer you'll use. (By "host computer,"
we're talking about the computer that will run MPF which will talk to
the pinball controller via USB.) There are lots of host computer
options, including small single-board computers, laptops, small-form
factor x86 motherboards, etc. You're also going to have to decide on
what OS you use (Windows, Linux, or Mac).

Generally speaking, MPF will run on any PC or embedded system which can run Python 3.
In most cases you also need a graphics card with working OpenGL to run the MPF Media Controller (MPF-MC).
Most operating systems work fine (we test on Linux, Windows, Mac OS X) but be careful with virtualized
environments because OpenGL might not work perfectly.


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

CPU
^^^

The trend in computing these days (for both "real" computers and small
single-board computers) is multi-core. Almost every computer these
days has a dual-core or quad-core processor.

MPF uses two processes (one for the game engine and one for the media
controller), so it can make use of a dual-core system. However there is probably
not much benefit to MPF running on machines with more than 2 cores (other than
it frees up more cores for other non-MPF things.)
During startup, when playing sound or loading assets additional cores may be used.
Therefore, we recommend a CPU with at least two cores. MPF certainly benefits from four cores but
everything above that will not help during normal games.
However, during development, when using MPF Monitor and an IDE more cores will certainly help.

Disk
^^^^
Disk space it not really an issue these days. The real question is disk
performance in terms of SSD versus traditional spinning magnetic hard disks.
SSD is fast, you can can get away with less memory since MPF can dynamically
load and unload assets.
To load assets quickly a SSD helps. You definitely want that during development
but you might use a cheaper option (such as a SD-card) for the final game.

Filesystems can become corrupted by unsafe shut downs, so consider running a
journaling filesystem or even mount them read-only.

Memory
^^^^^^

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

MPF needs at least 512MB RAM but we recommend 2-4GB depending on the amount of assets.
Again, during development you want to have more RAM (8GB+) for your IDE and other tools.


Development setup
-----------------

* CPU with at least four cores
* 8GB RAM or more
* SSD

Final game
----------

We cannot emphasize this enough: Do not use such a setup for game development.

* CPU with two to four cores
* 2-4GB RAM (mostly for assets)
* SD-Card/Embedded flash/SSD

See also the :doc:`discussion about the hardware in your final game </finalization/host_computer>`.
