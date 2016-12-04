Installing MPF on Windows
=========================
MPF can be used on Windows 7, 8, and 10, in both 32-bit and 64-bit versions. The
installation process is pretty much automated, and the whole thing should only
take a few minutes.

Here are the steps:

1. Install Python 3.4 (not Python 3.5)
--------------------------------------

MPF is written in a computer language called "Python". This means you have to install Python
first before you can use MPF. Luckily this is just a one-time install, and you don't have to
install it again if you update MPF later.

On Windows platforms, MPF requires Python 3.4, (Python 3.5 and newer will not work). You
can download and install from the Python website. (Keep reading for links)

.. warning::

   To be very clear, on Windows, MPF requires Python 3.4. It will not run on
   Python 3.5+.

There are two versions of Python, a 32-bit version and a 64-bit version, and you
should pick the one that matches the version of Windows you're using.

To find out whether you have 32-bit or 64-bit Windows, open a command prompt
by right-clicking on the Windows button and selecting "Command Prompt" from the
menu:

.. image:: images/windows_command_prompt.jpg

Then inside that window, type the following command and press Enter. This
command is case-sensitive, so copy it exactly:

::

    echo %PROCESSOR_ARCHITECTURE%

If it prints ``x86``, that's 32-bit. If it prints ``x64`` or ``AMD64``, that's 64-bit. (Note that it might print "AMD64"
even if you have an Intel processor.)

Here's an example of running this on a 64-bit Windows 10 machine:

.. image:: images/check_windows_processor_architecture.png

Then go to the Python website download the version you need. (Note that the final digit in the Python version
number is the "patch" number, so 3.4.4 is the latest version of Python 3.4.) Or use the direct-download links here:

+ `For 32-bit (x86) Windows <https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi>`_
+ `For 64-bit (x64 or AMD64) Windows <https://www.python.org/ftp/python/3.4.4/python-3.4.4.amd64.msi>`_

Installing Python 3.4 is pretty straightforward. It's a normal Windows installer.

The only thing you should change from the defaults is on the "Customize Python
3.4.4" screen, we like to select the option "Add python.exe to Path". That way
you can run ``python`` from any folder, rather than having to specify the full
path to it. (Also make sure the "pip" option is selected, but that should be
selected by default.)

.. image:: images/python_win_pip_path.jpg

Note that you have to log out and then log back in for the path to be updated
once you install Python. If you don't, then you'll get an error about Python not
being found when you try to install MPF.

After you log out and log back in, (or just restart your computer), open a command prompt
again and type the following command, then press ENTER: (note there are two dashes before
the word "version")

::

    python --version

That should print which version of Python is installed, like this:

.. image:: images/windows_python_from_command_prompt.jpg

Make sure the version is Python 3.4.4. If you see a version number that starts with 2,
that means you also have Python version 2 installed. (This is ok. You can have Python 2
and Python 3 installed at the same time.) However, if this is your case, you need to
use a different command to start Python 3. See the :doc:`2_and_3` page for details.

2. Upgrade pip
--------------

Python includes a utility called "pip" which is the name of the Python Package
Manager. Pip is used to install Python packages and applications from
the web. (It's kind of like an app store for Python apps.)

So the next step is to update the "pip" program itself to make sure you have the
latest one. It's not really important to know exactly what this means right now,
just run it.

::

    pip install pip --upgrade

This command will upgrade pip to the latest version which should be 9 or newer.

Note that if you're running the command prompt *without* admin rights, you might get
some red text and a permissions error, but that's ok. You can run the following command
to show the version of pip (and the packages you have installed) like this:

::

   pip list

That will print out something like this:

.. code-block:: doscon

   C:\Users\BRIAN MADDEN>pip list
   pip (9.0.1)
   setuptools (18.2)

   C:\Users\BRIAN MADDEN>

Notice that pip is now version 9.0.1 (or later, depending on the latest version when you're doing
this), and not the 7.x version that came with Python 3.4.4.

3. Install MPF
--------------

Now that Python is installed and pip is up-to-date, it's time to install MPF!
To do this, run the following command from the command prompt:

::

    pip install mpf-mc

This command is telling pip to install a package called "mpf-mc", which is the
*Mission Pinball Framework - Media Controller* package. When you run this,
pip will connect to the internet and download MPF from the Python app store
and install it onto your computer.

Pip packages can include dependencies, which means that when you run this
command, you'll see a bunch of packages get downloaded and installed.

In this case, the ``mpf-mc`` package will also download and install the MPF
game engine package, as well as various other packages that MPF needs to run.

4. Install the video codec pack
-------------------------------

MPF uses an open source project called Gstreamer to play video. By default, Gstreamer
only comes with codecs that can play open source and free video formats which are somewhat
obscure and things you probably never heard of.

So the next step is to install a codec pack that will let MPF play just about
any kind of video (H.264, MPG, etc.)

This is also installed via pip, like this:

::

   pip install kivy.deps.gstreamer --extra-index-url https://mpf.kantert.net/simple/

Just copy-and-paste that entire line into the command line and press enter. It
will download the codec pack which is 93mb and install it.

The URL is from one of the MPF developers (Jan Kantert, thanks!), who is hosting this file for us.

5. Test your installation
-------------------------

Once MPF is installed, you can run some automated tests to make sure that
everything is working. To do this, open a command prompt, and then type the
following command and then press <enter>:

::

  python -m unittest discover mpf

When you do this, you should see a bunch of dots on the screen (one for each
test that's run), and then when it's done, you should see a message showing
how many tests were run and that they were successful. The whole process should
take less a minute or so.

(If you see any messages about some tests taking more than 0.5s, that's ok.)

The important thing is that when the tests are done, you should have a message
like this:

::

   Ran 501 tests in 62.121s

   OK

   C:\>

Note that the number of tests is changing all the time, so it probably won't
be exactly 501. And also the time they took to run will be different depending
on how fast your computer is.

These tests are the actual tests that the developers of MPF use to test MPF
itself. We wrote all these tests to make sure that updates and changes we add
to MPF don't break things. :) So if these tests pass, you know your MPF
installation is solid.

Remember though that MPF is actually two separate parts, the MPF game engine and
the MPF media controller. The command you run just tested the game engine, so
now let's test the media controller. To do this, run the following command
(basically the same thing as last time but with an "mc" added to the end, like
this):

::

  python -m unittest discover mpfmc

(Note that ``mpfmc`` does not have a dash in it, like it did when you installed
it via *pip*.)

When you run these tests, you should see a graphical window pop up on the
screen, and many of the tests will put graphics and words in that window. Also,
some of the tests include audio, so if your speakers are on you should hear some
sounds at some point.

These tests take longer, but when they're done, that
graphical window should close, and you'll see all the dots in your command
window and a note that all the tests were successful.

Notes about the mpfmc tests:

 * These tests create a window on the screen and then just re-use the same
   window for all tests (to save time). So don't worry if it looks like the
   window content is scaled weird or doesn't fill the entire window.

 * Many of these tests are used to test internal workings of
   the media controller itself, so there will be lots of time when the pop up
   window is blank.

 * The animation and transition tests include testing functionality to stop,
   restart, pause, and skip frames. So if things look "jerky" in the tests,
   don't worry, that doesn't mean your computer is slow, it's just how the
   tests work! :)

At this point you should have a fully working copy of MPF. Congrats!

6. Install whatever drivers your hardware controller needs
----------------------------------------------------------

If you're using MPF with a physical machine, then there will be some specific
steps you'll need to take to get the drivers installed and configured for
whatever control system you've chosen. See the :doc:`control systems </hardware/index>`
documentation for details. (You don't have to worry about that now if you just
want to play with MPF first.)

Running MPF
-----------

See the section :doc:`/running/index` for details and command-line options.

Keeping MPF up-to-date
----------------------

Since MPF is a work-in-progress, you can use the *pip* command to update your
MPF installation.

To to this, run the following:

::

  pip install mpf-mc --upgrade

This will cause *pip* to contact PyPI to see if there's a newer version of the
MPF MC (and any of its requirements, like MPF). If newer versions are found, it
will download and install them.

Next steps!
-----------

Now that MPF is installed, you can follow our
:doc:`step-by-step tutorial </tutorial/index>` which will show you how to start
building your own game in MPF!
