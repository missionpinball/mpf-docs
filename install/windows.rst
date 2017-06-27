Installing MPF on Windows
=========================
MPF can be used on Windows 7, 8, and 10, in both 32-bit and 64-bit versions. The
installation process is pretty much automated, and the whole thing should only
take a few minutes.

Here are the steps:

1. Install Python 3.4 (not Python 3.5 or 3.6)
---------------------------------------------

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
pip will connect to the internet and download MPF-MC from the Python app store
and install it onto your computer.

Pip packages can include dependencies, which means that when you run this
command, you'll see a bunch (like 10 or so) packages get downloaded and installed. The
total size of all these will be almost 200mb, and they include multimedia libraries,
graphics engines, codecs, and a bunch of other components that MPF needs.

The MPF MC package will also download and install the MPF game engine package.

Here's an example of what this looks like from the command prompt. (Note that the exact
versions and sizes might not be the same as what you have, but this should give you a
general idea. Also this may take a few minutes to run on your computer.)

.. code-block:: doscon

   C:\Users\BRIAN MADDEN>pip install mpf-mc
   Collecting mpf-mc
     Downloading mpf_mc-0.32.11-cp34-none-win_amd64.whl (11.3MB)
       100% |################################| 11.3MB 58kB/s
   Collecting kivy==1.9.1 (from mpf-mc)
     Downloading Kivy-1.9.1-cp34-none-win_amd64.whl (7.6MB)
       100% |################################| 7.6MB 114kB/s
   Collecting kivy.deps.sdl2==0.1.17 (from mpf-mc)
     Downloading kivy.deps.sdl2-0.1.17-cp34-cp34m-win_amd64.whl (2.5MB)
       100% |################################| 2.5MB 284kB/s
   Collecting ruamel.yaml<0.11,>=0.10 (from mpf-mc)
     Downloading ruamel.yaml-0.10.23-py3-none-win_amd64.whl (69kB)
       100% |################################| 71kB 1.1MB/s
   Collecting pypiwin32 (from mpf-mc)
     Downloading pypiwin32-219-cp34-none-win_amd64.whl (8.6MB)
       100% |################################| 8.6MB 75kB/s
   Collecting kivy.deps.glew==0.1.9 (from mpf-mc)
     Downloading kivy.deps.glew-0.1.9-cp34-cp34m-win_amd64.whl (161kB)
       100% |################################| 163kB 1.3MB/s
   Collecting kivy.deps.sdl2-dev==0.1.17 (from mpf-mc)
     Downloading kivy.deps.sdl2_dev-0.1.17-cp34-cp34m-win_amd64.whl (3.5MB)
       100% |################################| 3.6MB 242kB/s
   Collecting kivy.deps.gstreamer==0.1.12 (from mpf-mc)
     Downloading kivy.deps.gstreamer-0.1.12-cp34-cp34m-win_amd64.whl (129.5MB)
       100% |################################| 129.5MB 6.9kB/s
   Collecting mpf>=0.32.6 (from mpf-mc)
     Downloading mpf-0.32.6-cp34-none-any.whl (746kB)
       100% |################################| 747kB 819kB/s
   Collecting Kivy-Garden>=0.1.4 (from kivy==1.9.1->mpf-mc)
     Downloading kivy-garden-0.1.4.tar.gz
   Collecting ruamel.base>=1.0.0 (from ruamel.yaml<0.11,>=0.10->mpf-mc)
     Downloading ruamel.base-1.0.0-py3-none-any.whl
   Collecting pyserial>=3.2.0 (from mpf>=0.32.6->mpf-mc)
     Downloading pyserial-3.2.1-py2.py3-none-any.whl (189kB)
       100% |################################| 194kB 1.6MB/s
   Collecting pyserial-asyncio>=0.2 (from mpf>=0.32.6->mpf-mc)
     Downloading pyserial_asyncio-0.3-py3-none-any.whl
   Collecting requests (from Kivy-Garden>=0.1.4->kivy==1.9.1->mpf-mc)
     Downloading requests-2.12.4-py2.py3-none-any.whl (576kB)
       100% |################################| 583kB 1.1MB/s
   Installing collected packages: requests, Kivy-Garden, kivy, kivy.deps.sdl2, ruamel.base,
   ruamel.yaml, pypiwin32, kivy.deps.glew, kivy.deps.sdl2-dev, kivy.deps.gstreamer, pyserial,
   pyserial-asyncio, mpf, mpf-mc
     Running setup.py install for Kivy-Garden ... done
   Successfully installed Kivy-Garden-0.1.4 kivy-1.9.1 kivy.deps.glew-0.1.9 kivy.deps.gstreamer-0.1.12
   kivy.deps.sdl2-0.1.17 kivy.deps.sdl2-dev-0.1.17 mpf-0.32.6 mpf-mc-0.32.11 pypiwin32-219 pyserial-3.2.1
   pyserial-asyncio-0.3 requests-2.12.4 ruamel.base-1.0.0 ruamel.yaml-0.10.23

   C:\Users\BRIAN MADDEN>

If you want to make sure that MPF was installed, you can run:

::

   mpf --version

This command can be run from anywhere and should produce output something like
this:

.. code-block:: doscon

   C:\Users\BRIAN MADDEN> mpf --version
   MPF v0.32.6

(Note that the actual version number of your MPF installation will be whatever
version is the latest.)

4. Download & run the "Demo Man" example game
---------------------------------------------

Now that you have MPF installed, you probably want to see it in action. The easiest way to do that is
to download a bundle of MPF examples and run our "Demo Man" example game. To do that, follow
the instructions in the :doc:`/example_games/demo_man` guide.

There's another example project you can also check out if you want called the "MC Demo" (for media controller demo)
that lets you step through a bunch of example display things (slides, widgets, sounds, videos, etc).
Instructions for running the MC Demo are :doc:`here </example_games/mc_demo>`.

5. Install whatever drivers your hardware controller needs
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

  pip install mpf mpf-mc --upgrade

This will cause *pip* to contact PyPI to see if there's a newer version of the
MPF and MPF MC (and any new requirements). If newer versions are found, it
will download and install them.

Next steps!
-----------

Now that MPF is installed, you can follow our
:doc:`step-by-step tutorial </tutorial/index>` which will show you how to start
building your own game in MPF!
