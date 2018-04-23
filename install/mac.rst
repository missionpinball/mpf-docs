Installing MPF on Mac
=====================

MPF can be used on Mac OS X 10.9 and newer, including Mavericks, Yosemite,
El Capitan, Sierra and High Sierra.

.. note::

   MPF cannot run in a Mac virtual machine (like in VMware Fusion or Parallels)
   if the guest OS is Mac, though running MPF in a Windows or Linux VM on a
   Mac is fine.

Also at this time, installing all the components you need to run MPF on a Mac
will require almost 2 GB of disk space. MPF itself it only about 12 MB, but
there are a lot of supporting things that MPF needs as you'll see here.

We have a video which shows this entire installation process in action
which is available at `<https://www.youtube.com/watch?v=lJEfQGffXsA>`_

Here are the steps to install MPF on a Mac:

Step 0. Uninstall your previous MPF app installation
----------------------------------------------------

The process for running MPF on a Mac has changed as of Jan 10, 2017.
Previously we had an MPF.app that you downloaded which contained Python and
everything you needed.

If you used MPF on a Mac prior to this and you have the MPF.app, you need to
remove it first. If you have never installed MPF on your Mac before, then
proceed directly to Step 1 below.

To remove the old MPF Mac installation:

1. Delete the "MPF.app" from your Applications folder.
2. Delete the "mpf" alias in ``/usr/local/bin``.
3. Delete the "kivy" alias in ``/usr/local/bin``.

If you don't know how to find your ``/usr/local/bin`` folder, you can use
the "Go to Folder" technique shown in Step 1.

1. Download the Mac Multimedia Frameworks
-----------------------------------------

MPF uses open source multimedia frameworks called GStreamer and SDL2 for its
graphics, video, and sound features. So next you need to download these
frameworks and copy them to your Mac's frameworks folder. There are actually
five different frameworks MPF needs, and downloading them all separately is
kind of a pain (especially finding the right versions and everything), so we
have created a single ZIP file which has everything you need.

Download the zip of the multimedia frameworks `here <https://mpf.kantert.net/mpf_mac_frameworks.zip>`_.
(Thanks to MPF developer Jan Kantert for hosting it!) The zipped download is 170 MB,
and the unzipped size is 529 MB.

Unzip it, and copy (or drag and drop) the five things in the zip file's
``Frameworks`` folder to your own Mac's ``/Library/Frameworks`` folder.

Depending on your Mac's settings, you might not see the ``/Library/Frameworks``
folder in Finder. If this is the case, use the *Go -> Go to Folder...* menu,
and then type "/Library/Frameworks" and hit enter.

The following three images illustrate the steps:

.. image:: images/mac_finder_go_to_folder.jpg

.. image:: images/mac_finder_go_to_folder2.jpg

Note that you will need to authenticate (which just means you have to enter
your password) in order to be able to copy those frameworks into your Mac's
frameworks folder. The authentication message will automatically pop up when
you drag and drop the files:

.. image:: images/mac_copy_frameworks.jpg

When you're done, your Mac's ``/Library/Frameworks`` folder should have
the five new frameworks (plus whatever random ones you already had), which
should look something like this:

.. image:: images/mac_frameworks_copied.jpg

2. Install the Mac developer tools
----------------------------------

Next you have to install something called the "Command Line Developer Tools"
which is a package of software development tools created by Apple which MPF
relies on to get installed.

To do this, you need to use the "Terminal" app (which is essentially a
command prompt window for the Mac).

The easiest way to launch the Terminal app is to use Spotlight (press the
CMD + Spacebar) and then just type "Terminal", like this:

.. image:: images/mac_spotlight_terminal.jpg

Next, type the following command into the prompt in the terminal and press
Enter:

.. code-block:: console

   xcode-select --install

That should pop up a box which gives you the option to install the command
line tools, like this:

.. image:: images/mac_install_command_line_tools.jpg

Click the "Install" button here to get just the command line tools. The
"Get XCode" button installs more than you need.

The download will be about 150 MB, and the total install will be about 1.1 GB.

After the installation of the tools you need to accept the license agreeement from Apple.
The following command starts that process in the Terminal, just follow the instructions provided:

::

   sudo xcodebuild -license

If you already have the command line tools installed, that's fine. You'll get
some kind of error saying they're already installed and you can move on.

3. Install Python 3.5 (not Python 3.6)
--------------------------------------

MPF is written in a computer language called "Python". This means you have to install Python
first before you can use MPF. Luckily this is just a one-time install, and you don't have to
install it again if you update MPF later.

On Mac platforms, MPF requires Python above 3.4. We lately tested Python 3.6 and it can be used.

You can download Python 3.6 directly via `this link <https://www.python.org/ftp/python/3.6.5/python-3.6.5-macosx10.9.pkg>`_.
(Note that the final digit in the Python version number is the "patch" number,
so 3.6.5 is the latest version of Python 3.6 as of the time this document was last updated.)

.. image:: images/mac_install_python_1.jpg

Installing Python is pretty straightforward. It's a standard Mac installation
package. You can click next, next, next, agree to the license, enter your
password, and you're all set.

.. note::

   Macs have an older version of Python built in, but it's Python 2.x, and MPF
   requires Python 3, so that's why you have to install Python now. The new
   Python 3 that you install here will happily live alongside the Python 2.x
   that your Mac already has.

You can check to make sure Python 3.5 installed correctly from the Terminal
window. To do that, run the command:

.. code-block:: console

   python3 --version

You should see it print something like "Python 3.6.5". Note that you have
to run the command "Python3", not "Python", since the regular python command
without the "3" on the end points to the Python 2.x that's built into your
Mac. Here's a screenshot showing running "python" and "python3" and the
different between the two:

.. image:: images/mac_python_versions.jpg

4. Install/upgrade some Python components
-----------------------------------------

Python includes a utility called "pip" which is the name of the Python Package
Manager. Pip is used to install Python packages and applications from
the web. (It's kind of like an app store for Python apps.)

Due to a bug in versions of pip older than 9.0.2 on the Mac, we cannot update *pip*
using *pip*. So the next step is to download and run a special Python script to install
the latest version of pip.

Update pip by running the following command:

.. code-block:: console

    curl -O https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py

The latest version of pip should now be installed (9.0.3 or newer).

Next, we need to install and update a few other python packages required to run mpf by
running the following command:

So next run the following command:

.. code-block:: console

    pip3 install setuptools cython==0.25.2 --upgrade

This command will download and install the latest versions of the *setuptools*
package, as well as version 0.25.2 of a package called *cython*. The results will
look something like this (though the exact version numbers might be different
depending on what's the latest whenever you're running this):

.. code-block:: console

   Collecting setuptools
     Downloading setuptools-32.3.1-py2.py3-none-any.whl (479kB)
       100% |################################| 481kB 4.3MB/s
   Collecting cython==0.25.2
     Downloading Cython-0.25.2-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.8MB)
       100% |################################| 3.8MB 7.6MB/s
   Installing collected packages: setuptools, cython
   Successfully installed cython-0.25.2 setuptools-32.3.1
   
We recommend to stick to the specific cython Version, as others broke our installation process while testing the installation on different Macs.

5. Install MPF
--------------

Next you can run pip again to install MPF itself. Technically what you're
installing is "mpf-mc", which is the
`Mission Pinball Framework Media Controller <http://docs.missionpinball.org/en/latest/start/media_controller.html>`_
package, but that package will also install the MPF game engine. Install MPF
like this:

.. code-block:: console

   pip3 install mpf-mc --pre

.. note::

   Since MPF 0.50 is not yet released, the command you need to run is
   "pip install mpf-mc --pre" to get the latest "pre-release" version, so that MPF runs under Mac.
   
   If you Upgrade your installation add --upgrade to the call like this:   

::

   pip3 install mpf-mc --pre --upgrade
   
If you are using High Sierra please add the --user option to get around a specific rights problem:

::

   pip3 install mpf-mc --pre --upgrade --user

Your results should look something like the results below. The MPF install will
download and install several other packages which what all these other things
are.

.. note::

   The "kivy" component will take awhile to install. Maybe a minute or two
   where it looks like it's not doing anything, but it's fine.

.. code-block:: console

   Brians-Mac:~ brian$ pip3 install mpf-mc
   Collecting mpf-mc
     Downloading mpf-mc-0.32.12.tar.gz (11.1MB)
       100% |################################| 11.1MB 29.6MB/s
   Collecting ruamel.yaml<0.11,>=0.10 (from mpf-mc)
     Downloading ruamel.yaml-0.10.23.tar.gz (228kB)
       100% |################################| 235kB 9.0MB/s
   Collecting mpf>=0.32.6 (from mpf-mc)
     Downloading mpf-0.32.6.tar.gz (556kB)
       100% |################################| 563kB 18.0MB/s
   Collecting kivy>=1.9.1 (from mpf-mc)
     Downloading kivy-1.9.1.tar.gz (16.4MB)
       100% |################################| 16.4MB 7.4MB/s
   Collecting ruamel.base>=1.0.0 (from ruamel.yaml<0.11,>=0.10->mpf-mc)
     Downloading ruamel.base-1.0.0-py3-none-any.whl
   Collecting pyserial>=3.2.0 (from mpf>=0.32.6->mpf-mc)
     Downloading pyserial-3.2.1-py2.py3-none-any.whl (189kB)
       100% |################################| 194kB 4.1MB/s
   Collecting pyserial-asyncio>=0.2 (from mpf>=0.32.6->mpf-mc)
     Downloading pyserial_asyncio-0.3-py3-none-any.whl
   Collecting Kivy-Garden>=0.1.4 (from kivy>=1.9.1->mpf-mc)
     Downloading kivy-garden-0.1.4.tar.gz
   Collecting requests (from Kivy-Garden>=0.1.4->kivy>=1.9.1->mpf-mc)
     Downloading requests-2.12.4-py2.py3-none-any.whl (576kB)
       100% |################################| 583kB 4.8MB/s
   Installing collected packages: ruamel.base, ruamel.yaml, pyserial, pyserial-asyncio, mpf, requests, Kivy-Garden, kivy, mpf-mc
     Running setup.py install for ruamel.yaml ... done
     Running setup.py install for mpf ... done
     Running setup.py install for Kivy-Garden ... done
     Running setup.py install for kivy ... done
     Running setup.py install for mpf-mc ... done
   Successfully installed Kivy-Garden-0.1.4 kivy-1.9.1 mpf-0.32.6 mpf-mc-0.32.12 pyserial-3.2.1 pyserial-asyncio-0.3 requests-2.12.4 ruamel.base-1.0.0 ruamel.yaml-0.10.23
   Brians-Mac:~ brian$
   
Now you will have to install PyQt5 to get the rest of the system running later on:

::

   sudo pip3 install PyQt5
   
Patch your Terminal undr High Sierra, so that it can show the UI correctely (otherwise it produces an error in "curs_set()"):

::

    export TERM=xterm-256color
    

If you want to make sure that MPF was installed, quit the Terminal app and restart it, and then run:

.. code-block:: console

   mpf --version

This command can be run from anywhere and should produce output something like
this:

.. code-block:: console

   Brians-Mac:~ brian$ mpf --version
   MPF v0.50.82

(Note that the actual version number of your MPF installation will be whatever
version is the latest.)

6. Download & run the "Demo Man" example game
---------------------------------------------

Now that you have MPF installed, you probably want to see it in action. The easiest way to do that is
to download a bundle of MPF examples and run our "Demo Man" example game. To do that, follow
the instructions in the :doc:`/example_games/demo_man` guide. But make sure to get the -dev Version for 0.50.

There's another example project you can also check out if you want called the "MC Demo" (for media controller demo)
that lets you step through a bunch of example display things (slides, widgets, sounds, videos, etc).
Instructions for running the MC Demo are :doc:`here </example_games/mc_demo>`.

7. Install whatever drivers your hardware controller needs
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

.. code-block:: console

  pip3 install mpf mpf-mc --upgrade

This will cause *pip* to contact PyPI to see if there's a newer version of the
MPF MC (and any of its requirements, like MPF). If newer versions are found, it
will download and install them.

To install the latest dev release (not generally recommended) which allows you to try bleeding-edge features run:

.. code-block:: console

  pip3 install mpf mpf-mc --pre --upgrade

To downgrade (or install a specific release x.yy.z) run:

.. code-block:: console

  pip3 install mpf=x.yy.z
  pip3 install mpf-mc=x.yy.z

.. warning::

   If you are upgrading from MPF 0.33 to 0.50 you will need to manually perform
   several migration steps to modify your configuration files or they will not
   work in MPF 0.50. Please refer to :doc:`Migrating from config version 4 to 5 of MPF </install/migrate4to5>`
   for step-by-step instructions.

Next steps!
-----------

Now that MPF is installed, you can follow our
:doc:`step-by-step tutorial </tutorial/index>` which will show you how to start
building your own game in MPF!

Make sure to lookup mpf-monitor later, if you want to simulate and configure a machine you own in hardware.
