Installing MPF on Mac OS X
==========================

Installing MPF on Mac OS X is straightforward, though it's a bit different than how it works on other platforms.
For OS X, we have a pre-built MPF.app application package which contains everything you need, including Python and all
the graphics and audio libraries. So you just download this app, copy it to your *Applications* folder, register it with
your system, and you're all set!

MPF works on Max OS X 10.9 and newer (Mavericks, Yosemite, and El Capitan).

The reason went with the single MPF bundle which has everything built in is because Mac OS X has Python 2.7 built-in,
but MPF requires Python 3, so if you install Python 3 the normal way then you have to deal with side-by-side Python
installations which can get hairy. Plus MPF requires several graphics and sound libraries which are sort of a pain to
get installed, so really it's easier to just get everything you need bundled up into a single application package which
you can just drag and drop and be done.

.. note::

   MPF cannot run in an OS X virtual machine (like in VMware Fusion or Parallels). Please direct complaints to
   Cupertino.

Here are the steps to install MPF on OS X:

1. Download the MPF OS X app
----------------------------

Download a zip of the latest MPF app for OS X from `here <https://missionpinball.com/mac/mpf.zip>`_. The zipped file is
154 MB, and once it's unzipped it's 450 MB. (That seems crazy huge, right? Remember though that it has *everything* in
it, including Python and all the multimedia and video playback libraries, audio libraries, etc.)

2. Copy it to your Applications folder
--------------------------------------

Just drag and drop the unzipped MPF.app file into your *Applications* folder.

3. Register MPF with your system
--------------------------------

The final step is to run a command which will make MPF available from anywhere on your system. To do this, open a
terminal window, which you can do by running the Terminal app. (It's easiest just to do this from Spotlight, Press
CMD + Space, then type "terminal". Then paste the following command in and press Enter. You will be prompted for your
password.

::

    sudo ln -s /Applications/MPF.app/Contents/Resources/script /usr/local/bin/mpf; ln -s /Applications/MPF.app/Contents/Resources/mpython /usr/local/bin/mpython

This command does two things.

First, it registers a system-wide shortcut called ``mpf`` with your system, so that whwen your in your pinball machine
folder you can type ``mpf`` and it will be able to find the MPF launch command inside the MPF app. Second it registers a
command ``mpython`` which is a link to the copy of Python that's included inside the MPF app package. (You'll need this
if you want to update anything inside the MPF app without having to re-download the whole thing again.)

4. Test your installation
-------------------------

Once MPF is installed, you can run some automated tests to make sure that
everything is working. To do this, open a Terminal window, and then type the
following command and then press <enter>:

::

  mpython -m unittest discover mpf

When you do this, you should see a bunch of dots on the screen (one for each
test that's run), and then when it's done, you should see a message showing
how many tests were run and that they were successful. The whole process should
only take 15-30 seconds or so.

These tests are the actual tests that the developers of MPF use to test MPF
itself. We wrote all these tests to make sure that updates and changes we add
to MPF don't break things. :) So if these tests pass, you know your MPF
installation is solid.

Remember though that MPF is actually two separate parts, the MPF core engine and
the MPF media controller. The command you run just tested the core engine, so
now let's test the media controller. To do this, run the following command:

::

  mpython -m unittest discover mpfmc


When you run these tests, you should see a graphical window pop up on the
screen, and many of the tests will put graphics and words in that window. Also,
some of the tests include audio, so if your speakers are on you should hear some
sounds at some point.

These tests take longer, maybe a minute or more, but when they're done, that
graphical window should close, and you'll see all the dots in your command
window and a note that all the tests were successful.

Note: Many of the media controller tests are used to test internal workings of
the media controller itself, so there will be lots of time when the pop up
window is blank. That's fine.

Also, the animation and transition tests include testing functionality to stop,
restart, pause, and skip frames. So if things look "jerky" in the tests, don't
worry, that doesn't mean your computer is slow, it's just how the tests work! :)

At this point you should have a fully working copy of MPF. Congrats!

Next we'd recommend following our :doc:`step-by-step tutorial </tutorial/index>`
which will show you how to start building your own game in MPF!

Keeping MPF up-to-date
----------------------

Whenever we update MPF, we also update the MPF Mac app. So if you want to use the latest version of MPF, you can always
re-download mpf.zip and just drag the new version into your *Applications* folder to replace the old version.

That's kind of annoying though, because the MPF app is huge, and the actual MPF code is tiny (about 10 MB total).

As an alternative, you can run a command which will just update the copy of MPF that's inside the MPF app. To do this,
open a Terminal window and run the following:

::

    mpython -m pip install mpf-mc --upgrade


Shout out to Kivy!
------------------

MPF uses a multimedia framework called *Kivy* to display graphics and sounds. The MPF Mac app is based on the Kivy Mac
app package, which the team from Kivy has made available for Kivy users (like MPF) to use to package their own apps. So
this amazingly simple MPF Mac package we have is available thanks to the awesome people at Kivy. Thanks!
