Installing MPF on Windows
=========================
MPF can be used on Windows 7, 8, and 10, in both 32-bit and 64-bit versions. The
installation process is pretty much automated, and the whole thing should only
take a few minutes.

Here are the steps:

1. Install Python 3.4
---------------------

MPF is written in a computer language called "Python". This means you have to install Python
first before you can use MPF. Luckily this is just a one-time install, and you don't have to
install it again if you update MPF later.

On Windows platforms, MPF requires Python 3.4, (Python 3.5 and newer will not work). You
can download and install from the Python website. (Keep reading for links)

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

This command will upgrade pip to the latest version.

3. Install MPF
--------------

Now that Python is installed and pip is up-to-date, it's time to install MPF!
To do this, run the following command from the command prompt:

::

    pip install mpf-mc


*pip* is the name of the Python Package Manager that we discussed in Step 2.
This command is telling pip to install a package called "mpf-mc", which is the
*Mission Pinball Framework - Media Controller* package. When you run this,
pip will connect to the internet and download MPF from the Python app store
and install it onto your computer.

Pip packages can include dependencies, which means that when you run this
command, you'll see a bunch of packages get downloaded and installed.

In this case, the ``mpf-mc`` package (which is MPF's media controller) will
also download and install the MPF core package, as well as various other
packages that MPF needs to run.

4. Install the video codec pack
-------------------------------

MPF uses an open source project called Gstreamer to play video. By default, Gstreamer
only comes with codecs that can play open source and free video formats.

So the next step is to install a codec pack that will let MPF play just about
any kind of video (H.264, MPG, etc.)

This is also installed via pip, like this:

::

   python -m pip install kivy.deps.gstreamer --extra-index-url https://mpf.kantert.net/simple/

Just copy-and-paste that entire line into the command line and press enter. It
will download the codec pack which is about 90 MB and install them.

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
only take 15-30 seconds or so.

These tests are the actual tests that the developers of MPF use to test MPF
itself. We wrote all these tests to make sure that updates and changes we add
to MPF don't break things. :) So if these tests pass, you know your MPF
installation is solid.

Remember though that MPF is actually two separate parts, the MPF core engine and
the MPF media controller. The command you run just tested the core engine, so
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
