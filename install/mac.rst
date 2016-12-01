Installing MPF on Mac OS X
==========================

Installing MPF on Mac OS X is straightforward, though it's a bit different than how it works on
other platforms. For OS X, we have a pre-built MPF.app application package which contains everything
you need, including Python and all the graphics and audio libraries. So you just download this
app, copy it to your *Applications* folder, register it with your system, and you're all set!

MPF works on Mac OS X 10.9 and newer (Mavericks, Yosemite, El Capitan, and Sierra).

The reason went with the single MPF bundle which includes Python in is the because the Mac OS has Python
2.7 built-in, but MPF requires Python 3, so if you install Python 3 the normal way then you have to
deal with side-by-side Python installations which can get hairy. Plus MPF requires several graphics and
sound libraries which are sort of a pain to get installed, so really it's easier to just get everything
you need bundled up into a single application package which you can just drag and drop and be done.

.. note::

   MPF cannot run in an virtual machine (like in VMware Fusion or Parallels) if the guest OS is OS X.
   (Though running MPF in a Windows or Linux VM on OS X is fine.) Please direct complaints to Cupertino.

Download a zip of the latest MPF app for OS X from `here <https://dl.dropboxusercontent.com/u/51030/Mission%20Pinball%20Framework.dmg>`_.
The DMG file is 175 MB, and once it's installed it will consume 450 MB. (That
seems crazy huge, right? Remember though that it has *everything* in it, including
Python and all the multimedia and video playback libraries, audio libraries, etc.)

Once you've downloaded the file, here are the steps to install MPF on OS X:

1. Open the DMG and copy MPF to your Applications folder
--------------------------------------------------------

Double-click the .dmg file to mount and open it. You'll see a window that looks like this:

.. image:: images/MPFMacInstaller.jpg

Then drag and drop MPF.app file to your *Applications* folder.

2. Update MPF and link it with OS X
-----------------------------------

The final step is to run a command which will update MPF and make it available from anywhere on
your system. We've created a script to do this for you, so all you have to do is double click on the
RunMeOnce.command file. You may be told that you can't open this file due to security restrictions. If you do, go to the Security & Privacy pane in System Preferences and choose "Allow apps downloaded from anywhere." You can turn this off agian after you run the script (or it will turn off automatically after 30 days).

When you run the script, you'll be prompted for your password. After you enter it, you'll be ready to go in just a few seconds!

This command does a few things:

First, it connects to the internet and downloads / updates MPF to the latest
version.

Second, it registers a system-wide shortcut called ``mpf`` with your system, so
that when you're in your pinball
machine folder you can type ``mpf`` and it will be able to find the MPF launch command inside the MPF app.

Finally, it registers a command ``kivy`` which is a link to the copy of Python
that's included inside
the MPF app package, which is actually based on a media framework called Kivy. (You'll need this if
you want to update anything inside the MPF app without having to re-download the whole thing again.)

3. Test your installation
-------------------------

Once MPF is installed, you can run some automated tests to make sure that
everything is working. To do this, open a Terminal window, and then type the
following command and then press <enter>:

::

  kivy -m unittest discover mpf

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

  kivy -m unittest discover mpfmc

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

4. Install whatever drivers your hardware controller needs
----------------------------------------------------------

If you're using MPF with a physical machine, then there will be some specific
steps you'll need to take to get the drivers installed and configured for
whatever control system you've chosen. See the :doc:`control systems </hardware/index>`
documentation for details. (You don't have to worry about that now if you just
want to play with MPF first.)

Running MPF
-----------

Starting with MPF 0.30, you run MPF by running the "mpf" command directly. (e
.g. you do not have to run "python" from the command prompt). For example, to
launch both the MPF game engine and the media controller, you simply run:

::

   mpf both

In other words, you only have to use those ``kivy`` commands above for testing
MPF and keeping it up to date. You actually run MPF via the ``mpf`` command.

See the :doc:`/running/index` for details and command-line options.

Keeping MPF up-to-date
----------------------

Whenever we update MPF, you'll also have to update the MPF Mac app. Rather than
have you re-download and replace the MPF Mac app every time, the easiest approach
is to run a command which will just update the copy of MPF that's inside the MPF app.
To do this, open a Terminal window and run the following:

::

    kivy -m pip install mpf-mc --upgrade

Shout out to Kivy!
------------------

MPF uses a multimedia framework called *Kivy* to display graphics and sounds. The MPF Mac
app is based on the Kivy Mac app package, which the team from Kivy has made available for
Kivy users (like MPF) to use to package their own apps. So this amazingly simple MPF Mac
package we have is available thanks to the awesome people at Kivy. Thanks!
