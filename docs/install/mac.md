---
title: Installing MPF on Mac
---

# Installing MPF on Mac

This is the new process used to install MPF 0.56 on a Mac.

## Overview of MPF on macOS

MPF works on macOS running on both Intel and Apple Silicon (M1/M2
processors). Requirements are:

* Apple Silicon Mac (M1/M2 processors) require macOS 12 Monterey or
    newer and Python 3.9.
* Intel processors require MacOS 10.14 or newer, and Python 3.7 - 3.9.
* MPF does not work with Python 3.10+

To install MPF on a Mac:

1.  If you do not have Python, install Python 3.9.13 from python.org. If
    you have an M1/M2 Mac, be sure to get the Universal installer, not
    the Intel one.

    macOS 64-bit Intel-only installer
    (<https://www.python.org/ftp/python/3.9.13/python-3.9.13-macosx10.9.pkg>)

    macOS 64-bit universal installer
    (<https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg>)

    Choose the default installation location. If you want to install to
    a custom location, remember that location for later steps.

2.  Install Homebrew (<https://brew.sh/>). Open your command terminal
    and paste in this command:

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

    This will also install the Xcode command line tools if you don't
    have them. This process might take some time, so be patient.

3.  Use Homebrew (or 'brew') to install the libraries and other
    support files MPF needs:

    `brew install SDL2 SDL2_mixer SDL2_image gstreamer`

4.  Verify that pip is installed. If you installed Python from
    python.org, then pip should have been installed as well. You can
    verify this by running `pip --version` or `pip3 --version` in your
    terminal. If it's not installed, you can install it using
    `brew install pip`.

5.  Use pip to install MPF with the Text UI components:

    `pip install "mpf[cli]"` or `pip3 install "mpf[cli]"`

6.  Use pip to install the MPF Monitor (Note that the latest version
    requires PyQt6, priors required PyQt5):

    `pip install mpf-monitor` or `pip3 install mpf-monitor`

7.  Use pip to install MPF-MC:

    `pip install mpf-mc` or `pip3 install mpf-mc`

Note: For the commands that use pip, if you run into permission issues,
try prefixing the command with sudo (i.e.,
`sudo pip install "mpf[cli]"`). Be aware that sudo allows the command to
run with root permissions, which can pose a security risk if used
carelessly.

Also, pip installs Python packages globally by default. If you'd prefer
to keep your project and its dependencies isolated from your system's
Python, consider using a Python virtual environment. There are several
tools available for this, such as pipx, venv, or virtualenv.

## Testing

May 2023 Note: Some of this might not work: The mc_demo and demo_man
mentioned below might not work anymore as they haven't been updated in
a while. Feel free to fix and/or update them and we'll merge your
changes in!

To test, download the `mpf-examples` repo from here:
<https://github.com/missionpinball/mpf-examples>. You can either clone
it locally, or download the zip file and unzip it. Either is fine, just
do what you're most comfortable with. Be sure to download / switch to
the `dev` branch.

Then back in the terminal, change into the `mpf-examples` folder (or
whatever folder you just unzipped that into), then change into the
`mc_demo` folder, then run `mpf both`. That should launch the mc_demo
code (which is Media Controller demo). A window should open with a red
background and some text about slides, you should be able to use the
right arrow key to advance to the next slide. You should be able to use
the left arrow key to go back to the previous slide and you should hear
a drum and cymbal sound when you change the slide.

You will see a bunch of warnings about some classes implemented in
multiple locations, and how one will be used, but which one is
undefined. It sounds scary, but this is normal. (For now.) We are
investigating whether this is something we need to fix, and how we'll
fix it if it is. But for now, it's fine.

You can also run the "demo_man" game from the `mpf-examples` folder.
Change into the `demo_man` folder and run `mpf both -X`. You should see
the DMD window pop up. The window you ran the command from will have
some warnings which cover up the nice text UI display. Just grab a
corner of the window with the mouse and resize the window (just make it
a tiny bit bigger and smaller) and that will cause the window contents
to completely refresh and you should see the expected MPF text UI
display showing switch status, ball locations, etc. (See the screenshots
below for details)

At this point, MPF is ready to go!

## Notes, Caveats & Next Steps

If have existing SDL and Gstreamer libraries installed (check the
`/Library/Frameworks` folder), you can delete them. The versions that
brew installs will go into the `/opt/homebrew` folder.

Do NOT use brew to install Python. Why? Because the Python in brew is
meant to support other brew packages that need python, and as such it
will automatically "upgrade" you to the latest Python, even on its
own, which means your Python will flip to 3.10 and MPF won't work and
you'll be sad. So that's why we install the "Framework Python" from
python.org. (Why's it called "Framework Python"? Because it installs
like a framework to that `/Library/Frameworks` folder.)

The Apple Silicon Macs need the Xcode command-line tools installed
because the ruamel.yaml library that MPF uses to read YAML files
doesn't have a pre-built version for M1/M2 Macs, so it has to be built
locally. This process is automatic and transparent when the Xcode tools
are installed.

If you do not see the "normal" MPF text UI display, and instead see
something like this:

![image](images/bad-display.jpg)

This is because those warnings mentioned above print on top of the nice
MPF display. To fix this, just grab a corner of the window with the
mouse and resize it to be a bit bigger and then smaller again. This will
cause the entire window to update and you should see the expected MPF
text UI display showing switch status, ball locations, etc. (See the
screenshots below for details)

![image](images/good-display.jpg)

Alternately, if you don't want to resize the window every time, you can
open two different terminal windows, and run `mpf -X` in one and
`mpf mc` in the other.

## Keeping MPF up-to-date

Once you have MPF installed via the procedure above, you can keep it
up-to-date by running the final two pip commands from above which you
used to install MPF and MPF-MC.

Questions? Comments? Need help? You can post to the [forum](../community/index.md).

## What if you borked it?

There aren't too many things that could go wrong, but if your
environment is broken and you want to remove everything and start over,
here are some notes:

To remove homebrew, run the following command: ____
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"`

Homebrew installs everything to `/opt/homebrew`, which means if you just
delete that folder, everything will be gone.

To fix Python versions: ____ Another problem is sometimes the
system's default Python will be the homebrew one, and not that one that
you installed from python.org. This can be a problem because MPF
requires Python 3.7, 3.8, or 3.9 (3.9 only on M1/M2 Macs), but the
homebrew python could be version 3.10 which won't work with MPF. So if
you need to check or change this, you can use the following command:

`which python3`

You will see a path to the version of python that runs when you just
type `python3` from the command line. Ideally you want it to be the
version you installed, which will be:

`/Library/Frameworks/Python.framework/Versions/3.9/bin/python3`

If you see something else, then run `which -a python3` to see what other
versions are installed. Then copy the path to the version you installed
(which will be the `/Library/Frameworks/...` version), and use that in
Step 5 when you install MPF.

To fix errors about failing to load assets: ____ If you get an error
about a failure while loading assets, and you see some references to
PIL, there's a potential conflict with an image library that you can
remove. To do that, use the following command:

`pip3 uninstall pillow`

This command uses pip to uninstall a package called pillow.
