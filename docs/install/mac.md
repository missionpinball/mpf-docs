---
title: Installing MPF on Mac
---

# Installing MPF on Mac

*Last updated Mar 10, 2024*

!!! warning "MPF 0.80 is Coming Soon"

    This installation guide is for MPF 0.57 and the legacy MC, which is being replaced in the upcoming MPF 0.80 with the Godot MC. If you are just getting started with MPF, we recommend you [install MPF 0.80](index.md) instead.


## Install Python

MPF 0.57 works on macOS running on both Intel and Apple Silicon (M1/M2
processors). For new installs, we recommend using Python 3.11, and that's
what these instructions will show. (MPF will work with Python 3.8 - 3.11.)

To check if you have python, type the following into your terminal:

`python3 --version`

You should see some output like `Python 3.9.13`, which means you have
python installed and it's a supported version. If so, proceed to the next step.

To install Python on a Mac:

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

## Create a Virtual Environment

It's strongly recommended to create a virtual environment for MPF,
which will keep the installed packages from conflicting with other
applications on your computer. Before proceeding, follow the steps on
the [virtual environment installation guide](virtual-environments.md)

## Install MPF

First, activate the virtual environment you setup in the previous step.

1.  Verify that pip is installed. If you installed Python from
    python.org, then pip should have been installed as well. You can
    verify this by running `pip --version` or `pip3 --version` in your
    terminal. If it's not installed, you can install it using
    `python -m ensurepip`.

2.  Use pip to install MPF:

    `pip install "mpf"`

    or if you want to include the Text UI for debugging in the console,
    install with the CLI parameter

    `pip install mpf[cli]`

3.  Use pip to install MPF-MC:

    `pip install mpf-mc`

4.  (Optional) Use pip to install the MPF Monitor (Note that the latest version
    requires PyQt6, priors required PyQt5):

    `pip install mpf-monitor`


Note: For the commands that use pip, if you run into permission issues,
try prefixing the command with sudo (i.e.,
`sudo pip install "mpf[cli]"`). Be aware that sudo allows the command to
run with root permissions, which can pose a security risk if used
carelessly.

Also, if the MC doesn't load due to an error that has to do with gstreamer,
try adding homebrew's gstreamer install location to the DYLD_LIBRARY_PATH
environment variable, like this (but check the version number since that might vary:

`export DYLD_LIBRARY_PATH=/usr/local/Cellar/gstreamer/1.22.5/lib:$DYLD_LIBRARY_PATH`

If this works, you'll need to update your `~/.zshenv` file (or create one) with that same command to
ensure that variable is set for each terminal window launched. (ZSH is the shell for MacOS Catalina
and onward. If you're somehow still running something older, you'd edit the `~/.bash_profile` file instead).

## Testing your MPF installation with the mpf-examples repo

Now that MPF is installed, you probably want to test it out to make sure
it worked properly. One of the easiest ways to do this is to use the
`mpf-examples` repo from GitHub. This repo contains a bunch of example
MPF projects.

Download the `mpf-examples` repo from [github.com/missionpinball/mpf-examples](https://github.com/missionpinball/mpf-examples)

Unzip it, and then back in the terminal, change into the `mpf-examples` folder (or
whatever folder you just unzipped that into), then change into the
`demo_man` folder, then run `mpf both`. You should see
the DMD window pop up.

At this point, MPF is ready to go!

## Keeping MPF up-to-date

Once you have MPF installed via the procedure above, you can keep it
up-to-date by running the pip commands from above which you
used to install the MPF components, but with the additional `--upgrade` flag.

Questions? Comments? Need help? You can post to the [forum](../community/index.md).
