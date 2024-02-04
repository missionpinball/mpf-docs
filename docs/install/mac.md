---
title: Installing MPF on Mac
---

# Installing MPF on Mac

*Last updated Oct 13, 2023*

This guide will walk you through the process of installing MPF on a Mac. It's broken into two parts:

* Installing MPF 0.57 (current dev branch) on a Mac
* Installing MPF 0.56 (current stable branch) on a Mac

## Installing MPF 0.57 (dev) on a Mac

MPF 0.57 works on macOS running on both Intel and Apple Silicon (M1/M2
processors). For new installs, we recommend using Python 3.11, and that's
what these instructions will show. (MPF will work with Python 3.8 - 3.11.)

1.  The easiest way to install MPF on a Mac is to use the [Homebrew package manager](https://brew.sh).
    Open your command terminal and paste and run this command:

    ``` { .bash .copy}

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    ```

    This will also install the Xcode command line tools if you don't
    have them. This process might take some time, so be patient.

2. Use Homebrew (or 'brew') to install the Python and the multimedia libraries MPF and MPF-MC need:

    ``` { .bash .copy}

    brew install python@3.11 SDL2_mixer SDL2_image gstreamer

    ```

3. Install the various MPF packages. For example, to install MPF, MPF-MC, and MPF Monitor:

    ``` { .bash .copy}

    pip3 install mpf mpf-mc mpf-monitor --pre

    ```

   Note that the `--pre` flag tells pip to install "pre-release" versions, which is how you get the
   0.57 versions of these packages. If you omit that flag, you'll get 0.56 versions.

That's it! Skip down to the "Testing your MPF Installation" section to continue.

## Installing MPF 0.56 (stable) on a Mac

!!! note "These instructions are for MPF 0.56"

    These instructions are from 2022 for MPF 0.56. Every "MPF" reference below should be thought of as "MPF 0.56".

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

Also, if the MC doesn't load due to an error that has to do with gstreamer,
try adding homebrew's gstreamer install location to the DYLD_LIBRARY_PATH
environment variable, like this (but check the version number since that might vary:

`export DYLD_LIBRARY_PATH=/usr/local/Cellar/gstreamer/1.22.5/lib:$DYLD_LIBRARY_PATH`

If this works, you'll need to update your `~/.zshenv` file (or create one) with that same command to
ensure that variable is set for each terminal window launched. (ZSH is the shell for MacOS Catalina
and onward. If you're somehow still running something older, you'd edit the `~/.bash_profile` file instead).

Finally, pip installs Python packages globally by default. If you'd prefer
to keep your project and its dependencies isolated from your system's
Python, consider using a Python virtual environment. There are several
tools available for this, such as pipx, venv, or virtualenv.

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
