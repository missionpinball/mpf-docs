
This page explains how to get MPF installed on a Windows computer.
These instructions work for Windows 7, 8, or 10, and they are valid
for both 32-bit and 64-bit Windows. You have two options for the
installation:


+ You can use our completely automated all-in-one installer. This will
  install everything you need from scratch, including Python, all the
  support libraries you need, your P-ROC/P3-ROC or FAST hardware drivers
  and libraries, and MPF itself. This should take 3-5 minutes.
+ You can do a manual install. This is still very easy, but nice if
  you want to customize how things are installed or if you already have
  some components. This should take about 10 minutes.


Let's look at each of these.



Using our all-in-one Windows installer
--------------------------------------

Our all-in-one Windows installer will literally install everything you
need starting from scratch, including Python 2.7, git, Pygame 1.9.2,
PyYAML, PyOSC, the drivers for the FAST and/or P-ROC/P3-ROC pinball
controllers, and MPF itself. It will work with 32-bit Windows and
64-bit Windows. Use it if you want an automated way to get everything
all at once. It should only take about 3 minutes. Steps include:


#. Download the `installer zip file`_.
#. Unzip it
#. Run or double-click `install.cmd`. (Be sure to run this from the
   location where you unzipped the package to. It will not work if you
   run it from within the zip file itself.)
#. Answer the few questions... done!


Note that this will install MPF into the `c:\pinball\mpf` folder.
There's nothing special about that folder and you can move it to
wherever you want after it's installed.



Manually installing on Windows
------------------------------

If for some reason you don't want to use the all-in-one Windows
installer, you can manually install everything. This is nice if you
already have some things installed (like Python) or if you want to use
custom options or paths. Even though this is a manual process, it's
still very easy and takes less than 10 minutes. In fact here's a video
walking through the entire process (which is also detailed in the
steps below). https://www.youtube.com/watch?v=8EfEaSKceW0



1. Install Python 2.7, 32-bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download and install Python from
`https://www.python.org/downloads/`_. Choose the latest 2.7.x 32-bit
version. (Note that you need to install the 32-bit Python even if
you're using 64-bit Windows.) When you install it, ensure that the
options for "pip" and "Add python.exe to Path" are enabled: ` `_



1.1 What if you already have Python installed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have Python installed, that's fine, but we need to
check to make sure it can be used with MPF. First, make sure that the
version of Python you have is 2.7.x. You can do this by running
`python -V` from the command prompt. (Note that's an uppercase "V")
Next, verify that you're running the 32-bit version of Python since
some of the plug-ins we use require it. (This is fine for now. We may
look at supporting 64-bit in the future but it's not a priority at the
moment. MPF doesn't require enough memory to require 64-bit.) The
easiest way to know for sure is just to run a quick Python program to
test the maximum size item that Python can work with, which will tell
us whether it's 32-bit or 64-bit. To do this, from the command line,
run this:


::

    
    python -c "import sys;print(sys.maxsize < 2**32)"


If it prints "True" on the screen, then you know you have the 32-bit
version of Python and you're fine. If it prints "False" then you have
the 64-bit version and you need to install the 32-bit version of
Python and run that.



2. Install PyYAML
~~~~~~~~~~~~~~~~~

Next you need to install an add-in module to Python called PyYAML
which lets Python read & write YAML files. (`YAML`_ is the file format
MPF uses for all sorts of things, including its configuration files,
audit logs, high score data, etc.) The easiest way to do this is to go
to a command prompt and run:


::

    
    pip install pyyaml


"pip" is a Python package manager. When you run it, it goes online and
downloads and installs the package name you gave it. So `pip install
pyyaml` is using "pip" to "install" the package called "pyyaml." (You
have to be online for this to work.) If you get an error about pip not
being a valid command, that probably means you don't have pip
installed, so you can get it from `here`_. (pip was not included in
Python before 2.7.9.) Or you can `download and install PyYAML
manually`_. (Any version should work. We do not need the version with
the LibYAML bindings.)



3. Install Pygame
~~~~~~~~~~~~~~~~~

MPF uses another Python add-on library called *Pygame* which is lets
Python interact with graphics, sounds, and keyboard libraries.
Unfortunately Pygame is not part of the online Python repository where
pip downloads packages from, so you'll have to find and install it
manually.



3.1 Check to see if you have Pygame installed already
`````````````````````````````````````````````````````

First, you should check to see if you have Pygame already. (If you
just downloaded and installed Python then you don't have it, but if
you've had Python for awhile then it's possible that you already have
Pygame.) You can do this from the command prompt by typing:


::

    
    python -c "exec('import pygame\nprint pygame.version.ver')"


This command is a little crazy looking, but trust us—it works!
Basically this is a one-liner which tries to import Pygame and then
prints the version. If this command gives an error which says
*ImportError: No module named pygame*, then that means you don't have
Pygame and will have to download and install it as outlined below. If
this command just prints a number or some other words, like "1.9.1" or
"1.9.2pre" or "1.9.2pre-svn3227", then that means Pygame is installed.
For MPF, you need Pygame 1.9.2 or newer.



3.2 Install Pygame 1.9.2a0
``````````````````````````

The versions of Pygame are kind of confusing at the moment. The Pygame
group is supposedly in the process of releasing Pygame 1.9.3 which
should have new installers and be really nice, but they've been
working on that for
months
years so who knows when they'll be ready? In the meantime, you can
install Pygame 1.9.2a0 (32-bit) for Python 2.7 from the `Pygame
downloads page`_. (Note that the "a0" in the very means "alpha 0"
which sounds scary, but this has been the latest version of Pygame
literally since 2009, and so far it seems fine.)



4. Download the latest Mission Pinball Framework from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have MPF installed, you can check what version it is by
opening a command prompt and changing to the folder that has your
`mpf.py` file and running `python mpf.py --version`. We use `semantic
versioning`_ for MPF, with MPF versions being in the `x.y.z` format.
You can see what the latest version is at
`https://github.com/missionpinball/mpf/releases/latest`_. There's also
a link on that GitHub page to a `.zip` or `.tar.gz` file (they're both
the same) which contains MPF. The download file will be named
`mpf-<version>.zip` or `mpf-<version>.tar.gz`, depending on which link
you clicked. Unzip the download package to whatever location you want.
(This can be literally anywhere. It does not need to be in your Python
folder.) Note that there are several branches for MPF in GitHub. The
master branch is the most stable and is updated once a month or so.
The dev branch represents the next version we're working on. We try to
keep it somewhat stable, but there are usually more bugs. The dev
branch is updated a lot—probably 10 times a week or more!



5. Install your pinball controller's hardware drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using MPF to control a physical pinball machine via a
P-ROC/P3-ROC or FAST Pinball controller, you need to install the
software drivers and libraries they need. We have instructions here
for both, starting with the P-ROC/P3-ROC:



For P-ROC/P3-ROC:
`````````````````


#. Install the FTDI driver from `this page`_. (You can use the "Setup
   Executable" link on the right for a single exe that works with 32-bit
   and 64-bit Windows.)
#. Download our `zip file`_ which has everything else you need.
#. Run the file `pinproc-2.0.win32-py2.7.exe` from that zip file. Just
   click next next next through the popups. (This is also the file you
   use for 64-bit Windows, since we're using it with 32-bit Python.)
#. Copy the other three DLL files from the zip file into your
   `c:\Python27\Lib\site-packages` folder.


That's it! When you first plug in and power-on your P-ROC or P3-ROC,
you'll see this screen pop up: ` `_ It's just a progress bar which
shows Windows configuring the drivers. You don't have to click
anything to get it started and it should only take a 5-10 seconds. It
will only happen the first time you use the device.



For FAST Pinball:
`````````````````


#. Install the FTDI driver from `this page`_.

    #. Be sure to get the version (32-bit or 64-bit) that matches the
       version of Windows you're using.

#. Install the PySerial extension for Python.

    #. The easiest way to do this is to open a command prompt and run `pip
       install pyserial`.
    #. If you don't have pip, you can download an installer for PySerial
       from `here`_.



Once this is done, when you plug in and power on your FAST controller,
you might see some kind of notification that new hardware has been
detected. What exactly you see will depend on which FAST controller
you're using and what OS you have. For example, here's what happens
when you plug a FAST WPC controller into Windows 10 for the first time
(after you've installed the FTDI driver): ` `_ (This is just a
progress bar which shows Windows configuring the drivers. You don't
have to click anything to get it started, and it should only take 5-10
seconds. It will only happen the first time you use the device.) Then
if you go into your device manager, you should see four new COM ports
appear. These are "virtual" COM ports that your computer talks to via
USB, and these are the ports that MPF uses to communicate with your
FAST pinball controller. These ports will disappear when you power off
or unplug your FAST controller. Again the exact way you see your COM
ports varies depending on OS.



Next Steps
----------

At this point you're all set! Check out our `tutorial`_ which will
walk you through running the *Demo Man* sample game that comes with
MPF and will show you how to build your own game!

.. _this page: http://www.ftdichip.com/Drivers/D2XX.htm
.. _https://github.com/missionpinball/mpf/releases/latest: https://github.com/missionpinball/mpf/releases/latest
.. _Pygame downloads page: http://www.pygame.org/download.shtml
.. _installer zip file: https://github.com/missionpinball/mpf-windows-installer/archive/master.zip
.. _download and install PyYAML manually: http://pyyaml.org/wiki/PyYAML
.. _YAML: http://en.wikipedia.org/wiki/YAML
.. _zip file: https://missionpinball.com/wp-content/uploads/2015/08/p-roc-win32-python27.zip
.. _tutorial: /tutorial
.. _https://www.python.org/downloads/: https://www.python.org/downloads/
.. _this page: http://www.ftdichip.com/Drivers/VCP.htm
.. _here: https://pypi.python.org/pypi/pyserial
.. _semantic versioning: http://semver.org/
.. _here: https://pip.pypa.io/en/latest/installing.html


