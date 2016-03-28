
This How To guide walks you through updating your machine configs and
code from MPF 0.21 (released in Dec, 2015) to MPF 0.30. Note that we
skipped a few versions since so much changed from 0.21, which is why
this is now 0.30. Also note that 0.30 is pronounced "thirty", not
"three", as MPF 0.3 was released in July 2014. (We use semantic
versioning, which means version number order is different than
mathematical order. Details `here`_.) This guide was last updated on
March 16, 2016. At this point MPF 0.30 is not actually released. So
this documentation currently applies to the pre-release "dev" version.
Feel free to use it to start playing with MPF 0.30 today, but know
that not everything is done yet for MPF 0.30, so some things do not
work yet. This document is written to work with the following versions
of MPF:


+ MPF core engine `0.30.0.dev700` <-- yeah, there have been 700(!)
  commits since MPF 0.21.
+ MPF Media Controller `0.30.0.dev270`


You can view the latest version of MPF by running `mpf --version` from
a command prompt. (If this command gives you an error, that means
you're not on MPF 0.30.)



What's still missing in MPF 0.30.0.dev700
-----------------------------------------

This guide has been written for a pre-release version of MPF 0.30.
There are currently several things missing and things that we still
need to finish for MPF 0.30. Here's a list of what does not work
currently that we are planning on finishing for the final release of
MPF 0.30:


+ Shows don't automatically stop when modes end
+ Slide and widget expiration time
+ Show stopping needs to be tested to ensure that lights and LEDs are
  properly restored
+ Priorities of things launched from shows (LEDs, lights, sounds,
  slides, etc.) and modes are not set yet.
+ The "move out" transition doesn't work
+ Physical DMD and physical RGB DMD's are not there yet. (You can
  still display virtual versions of them in on-screen windows, it's just
  that connecting to physical ones isn't done yet.)
+ Entered_chars and character_picker display widgets aren't written.
  (This also means that high score entry modes will crash since they
  need them.)
+ Fonts have to be installed in your system in order to work. (Before
  we release we'll fix it so they can also be in a *fonts* folder in
  your machine folder.)
+ The settings for cropping the tops and bottoms of fonts are not
  written yet, so vertical placement of fonts will not be exactly right
  at the moment.


Please read this entire guide as a lot has changed. Here are the steps
to migrate to 0.30:



(1) Review the Changes in MPF 0.30
----------------------------------

We've posted a `release notes guide with a list of changes to MPF
0.30`_. Before you start your migration to MPF 0.30, you should read
that guide to see what's new.



(2) Installation for Windows
----------------------------

Note that these instructions are only for Windows. If you're on a Mac,
skip to Section 3.



(2A) Install Python 3
~~~~~~~~~~~~~~~~~~~~~

Since MPF 0.30 requires Python 3, the first thing you need to do is
install Python 3. On Windows you should use Python 3.4.4, because Kivy
does not support Python 3.5 on Windows at this time. If you're on
64-bit Windows, install the 64-bit version of Python. 32-bit should
use 32-bit. The easiest way to tell whether you have 32-bit or 64-bit
Windows is to open a command prompt and run (note this is case-
sensitive):


::

    
    echo %PROCESSOR_ARCHITECTURE%


If it prints "x86", that's 32-bit. If it prints "x64", that's 64-bit.


+ You can download the Python 3.4.4. x86 / 32-bit MSI installer
  `here`_.
+ You can download the Python 3.4.4 x64 / 64-bit MSI installer
  `here`_.


Python 3 and Python 2 can run side-by-side no problem. If you just
installed Python for use with MPF, then you can first just remove the
old version of Python (via Add/Remove Programs). This will eventually
be our recommendation, but since MPF 0.30 is not done yet, you may
want to keep Python 2 and MPF 0.21 around for awhile. Then install
Python 3.4.4. On the "Customize Python 3.4.4" screen, we like to
select the option "Add python.exe" to Path. That way you can run
Python from anywhere. If you have both Python 3 and Python 2 installed
side-by-side, then every Python 3 command will have a "3" added to it.
(So you run "python3" instead of "python", "pip3" instead of "pip",
etc.) Once Python is installed, open a command prompt and type `python
--version <enter>`. It should print *Python 3.4.4*. If you get a
message about how 'python' is not recognized, log out and log back in.
(You have to do this when running a non-admin command prompt so it can
update the system path setting.) If you get a message that says you
have Python 2.x.x, then try `python3 --version`.



(2B) Install MPF
~~~~~~~~~~~~~~~~

Now open a command prompt and run this (type this, then press
<enter>):


::

    
    pip install mpf-mc


If you have both Python 2 and Python 3 installed on your system, you
need to use the Python 3 version of this command, which is:


::

    
    pip3 install mpf-mc


Pip is the name of the Python Package Manager. This command is telling
pip to install a package called "mpf-mc", which is the *Mission
Pinball Framework - Media Controller* package. When you run this, pip
will connect to the internet to the `Python Package Index`_ (called
"PyPI") where the *mpf-mc* is registered as a package. Pip will
download MPF-MC, as well as all the prerequisites for MPF-MC, and then
install them onto your computer. Note that the MPF-MC package is
technically the package for the MPF Media Controller, however, MPF-MC
includes MPF in its list of prerequisites, meaning if you install MPF-
MC then you also get MPF. So installing MPF-MC right off the bat is
just a shortcut to install both MPF and MPF-MC in a single step.



(2C) Install the fonts
~~~~~~~~~~~~~~~~~~~~~~

The current preview build of MPF does not support using fonts from the
MPF *fonts* folder. So if your machine used any of the built-in MPF
fonts, you need to install them to your system now. You can find them
in the `old MPF 0.21 (master) repository`_, in the
*mpf/media_controller/fonts* folder. Just double-click each one to
install it.



(2D) Download the mpf-examples so you can run the demo_man test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the changes we made in MPF 0.30 is we removed all the example
machine code from the MPF package. We figured there was no need to
include all the examples in every single MPF installation. In this
case, however, we want the examples, so download a zip file containing
the lastest mpf-examples from `here`_. (Note that if you have git, you
can simply clone the `mpf-examples repository`_ so they'll always be
up-to-date. Just make sure you get the master/dev to match which
branch of MPF you're using. If you have no idea what "git" means,
that's fine, just ignore that. :) You can download the mpf-examples
zip file and expand it to wherever you want. Once you have it
expanded, open two command prompt windows to the *demo_man* folder in
mpf-examples, for example:


::

    
    c:\mpf-examples\demo_man\


Then from within the first one, run:


::

    
    mpf mc


And from within the second one, run:


::

    
    mpf


If you see the *demo_man* window with a DMD in it pop up, you're good
to go. You can play around with this if you want. Click on the popup
window so it has focus, and then the `S` key starts a game and adds
players, the `X` key is a slingshot which will give points, and the
`1` key will drain the ball. It will probably crash when the game ends
since we don't have the *character_picker* and *entered_chars* display
widgets done that the high score entry mode needs. Now skip to Step
(4) below



(3) Installation for Mac OS X
-----------------------------

We don't have a procedure ready yet for the Mac. Actually we have the
MPF package for Mac done (it's precompiled and everything), but at the
moment we've having issues getting Kivy installed for Mac in a
repeatable way. (See `here`_ and `here`_.) Ultimately we're planning
to create a proper Mac MPF.app in a DMG file, so we'll just proceed
with that. Until then, sorry Mac users. (Which, btw, is 2 out of the 4
core MPF devs. :(



(4) Migrate your machine files
------------------------------

One of the big changes in MPF 0.30 is that MPF is installed into the
central Python site-packages folder. With old versions of MPF, you
downloaded and worked within the MPF folder itself. That doesn't
happen anymore, as the MPF folder is essentially hidden away inside
your computer. So instead, you now work within your actual machine
folder. Since you're migrating from MPF 0.21, you probably have an
mpf/machine_files folder (or something like it, with your machine
inside there. So the first thing to do is to move or copy your own
machine folder to some location that's not part of the old MPF
installation. Then you can delete the old MPF folder.



(4A) Migrate your machine's config and show files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now open a console window (Command Prompt on Windows, or Terminal on
Mac) and switch to your machine's root folder. You want to be in the
folder of your machine, that contains subfolders like config, shows,
modes, etc. (e.g. you're not in your config folder, you're in the
folder containing your config folder.) Now you'll run the MPF
migration tool which will scan through your machine folder and migrate
any YAML configuration and show files it finds. To do this, on
windows, just run:


::

    
    mpf migrate


The migrator should migrate everything for you. You'll notice that it
creates a folder called "previous_config_files" in your machine
folder, and under there is a folder with the time and date stamp, and
then under that is your old folder structure with all your original
YAML files in their original locations. You'll also see a "logs"
folder (in MPF 0.30, logs are stored in your machine folder instead of
in the MPF folder since MPF is now in a central installed location.)
You should see a log for the migration which will show you details of
everything the migrator did. As far as we know, the migrator does
everything and there are no known bugs. (We tested it on 6 or 7
different machine configs.) But really who knows? If it crashes or
does something weird, we can take your config files and test them
ourselves and get the migrator fixed and/or manually fix your files.
The only weird thing about the migrator is we couldn't figure out how
to add spaces between new sections that are added to existing config
files. So while everything the migrator generates will be
syntactically correct, you might need to go in and clean things up
visually a little bit. Also the migrator exports files with four
spaces for indentation. We'll add an option soon to let you specify if
you want to use two spaces, so if that's the case, hold off for a few
days.



(4B) Update any custom mode code or scriptlets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have any custom Python code as part of your machine (either in
mode code or in scriptlets), you'll need to migrate that code too. The
first part of the migration is to convert your code to Python 3.
Python 3 includes a tool called "2to3" which you can use for this. You
might be nervous to run an automated tool to convert your code, but
you should be fine. We used the same 2to3 tool for the 15k lines of
code in the entire MPF package when we converted MPF to Python 3, and
there were only 4 little things we had to go back and fix manually.
And most likely everything you're doing in your mode code or
scriptlets is pretty straightforward and should migrate easily. Run
this tool from the command line, from the root of your machine folder,
like this: On Windows:


::

    
    2to3 -w .


The tool is called "2to3", the -w means you want to "write" your
changes, and the dot means to use your current folder. Also you'll
need to do a "find and replace" for your all your code. If you're
using PyCharm or Atom, it's just SHIFT+CTRL+F (or SHIFT+CMD+F), so it
should just take a second. Old value (find): `mpf.system` New value
(replace): `mpf.core` It's possible you might need to change some
other things in your code too. If so, just post to the dev forum. You
can just try to run your game and see what happens. Also, you can
remove all those empty `__init__.py` files you had to add to your
machine folder and scriptlets and mode code folders, as Python 3 does
not require them. Here's an overview of this entire migration process
in action from the *demo_man* sample machine:
https://www.youtube.com/watch?v=GrRnYFGslL8



(5) Run your game and see what happens!
---------------------------------------

Now you're ready to run your game. To do this (for now), open two
command windows. Then from within your machine folder (the same folder
you ran the migration utility from), in the first window run:


::

    
    mpf mc


This will start the media controller. In the second window, run:


::

    
    mpf


This will start MPF. Then cross your fingers and hope it doesn't
explode! All of the test games we tried now work except for two which
have a lot of custom code that will need to be ported manually. (In
both cases we offered to do this for the game creators, since it's
faster for us to do it rather than explain what to do. :)



(6) Next Steps
--------------

At this point you can feel free to start editing your config files and
playing with MPF 0.30. We understand that with no documentation yet
(apart from what's in the `release notes`_), there's probably not much
you can do. And again, if you have problems, post to the forum. We
want to make this process as painless as possible, and will help you
get everything converted over. The good news is the config file and
show file formats are finalized for MPF 0.30, so even though not
everything works yet, you can start working with your config and show
files now with the confidence that they won't change between now and
the final release.

.. _here: https://github.com/missionpinball/mpf-examples/archive/dev.zip
.. _here: https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi
.. _Python Package Index: https://pypi.python.org/pypi
.. _old MPF 0.21 (master) repository: https://github.com/missionpinball/mpf
.. _mpf-examples repository: https://github.com/missionpinball/mpf-examples
.. _here: https://groups.google.com/forum/#!topic/kivy-users/YAZ64mNt9Kg
.. _release notes: https://missionpinball.com/docs/mpf-0-30-release-notes/
.. _here: https://www.python.org/ftp/python/3.4.4/python-3.4.4.amd64.msi
.. _here: https://groups.google.com/forum/#!topic/kivy-users/5H5tSJAX1bs
.. _here: http://semver.org/


