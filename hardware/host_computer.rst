Choosing a computer to run MPF
==============================

In addition to picking apinball controller platform you also need to
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
core game, modes, ball tracking, dealing with switches, etc.—all of
that can probably be done on a very tiny computer. The real driver
these days is your video and graphics. If you have a hi-def LCD window
with lots of full video and layers and on-screen elements all blended
together, then you're going to need a "real" computer to drive it
versus some $50 Raspberry Pi or Beaglebone.



Memory
~~~~~~

Preload assets versus on demand loading. 32-bit OSes only make 2GB
available to individual applications. So if your host computer has 8GB
of RAM in it, Python will still only have access to 2GB. So at this
point it's probably not worth putting more than 4GB in your host
computer. 64-bit OSes can provide much more than 2GB to single
applications, but at this point there are other issues with running
MPF on 64-bit Python. (You can still use MPF on a 64-bit machine, but
you need to use the 32-bit version of Python.)



CPU
~~~

The trend in computing these days (for both "real" computers and small
single-board computers) is multi-core. Almost every computer these
days has a dual-core or quad-core processor. Something about multi-
process, about how the MC and MPF can run on different cores. Also
want to talk about game loop speed, about how we don't need more than
20 or 30 Hz and something about the ms wait time in the loop to keep
the host computer responsive and not running too hot.



Disk
~~~~





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
always change it out later. BTWwe've received a few questions from
people wanting to use Mac Minis. As we've mentioned elsewhere, it's
really hard to get MPF running on a Mac, so if you have a Mac Mini
then by all means use it, but just install Windows or Linux on it
instead of Mac OS X. There's nothing you get from OS X that you don't
have with other platforms in terms of MPF. (Except for the headaches.
You get headaches with OS X with MPF.)



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
