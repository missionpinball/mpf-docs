Installing MPF on Mac OS X
==========================

Installing MPF on Mac OS X is straightforward, though it's a bit different than how it works on
other platforms. For OS X, we have a pre-built MPF.app application package which contains everything
you need, including Python and all the graphics and audio libraries. So you just download this
app, copy it to your *Applications* folder, register it with your system, and you're all set!

MPF works on Mac OS X 10.9 and newer (Mavericks, Yosemite, El Capitan, and Sierra).

.. note::

   There's a chance the MPF 0.32+ packages won't work on OS X 10.9 (Mavericks) and 10.10 (Yosemite). If
   you have one of these versions and the installation fails,
   `post a message in the mpf-users Google Group <https://groups.google.com/forum/#!forum/mpf-users>`_
   and we'll figure it out. We don't have an older OS to test. :)

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

Double click on the RunMeOnce.command file. You may be told that you can't open this file due to security restrictions.
If you do, go to the Security & Privacy pane in System Preferences and choose "Allow apps downloaded from anywhere." You
can turn this off again after you run the script (or it will turn off automatically after 30 days).

When you run the script, you'll be prompted for your password. After you enter it, you'll be ready to go in just a few
seconds!

This command does a few things:

* Connects to the internet and downloads / updates MPF and MPF-MC to the latest versions.
* Registers a system-wide shortcut called ``mpf`` so when you're in your pinball machine folder you can type ``mpf`` and
  it will be able to find the MPF launch command inside the MPF app.
* Registers registers a system-wide shortcut called ``kivy`` which is a link to the copy of Python that's included
  inside the MPF app package, (which is based on the `Kivy Python media library <https://kivy.org>`_ (You'll use this
  command in the future to update MPF and MPF-MC in your MPF.app package without having to re-download the whole thing
  again.)

3. Download & run the "Demo Man" example game
---------------------------------------------

Now that you have MPF installed, you probably want to see it in action. The easiest way to do that is
to download a bundle of MPF examples and run our "Demo Man" example game. To do that, follow
the instructions in the :doc:`/example_machines/demo_man` guide.

There's another example project you can also check out if you want called the "MC Demo" (for media controller demo)
that lets you step through a bunch of example display things (slides, widgets, sounds, videos, etc).
Instructions for running the MC Demo are :doc:`here </example_machines/mc_demo>`.

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

MPF uses an open source multimedia framework called `Kivy <https://kivy.org>`_ to display graphics and sounds.
The MPF Mac app is based on the Kivy Mac app package, which the team from Kivy has made available for
Kivy users (like us!) to use to package their own apps. So this amazingly simple MPF Mac
package we have is available thanks to the awesome people at Kivy.
