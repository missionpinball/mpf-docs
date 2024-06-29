---
title: Installing MPF 0.56 on Windows
---

# Installing MPF on Windows

This process walks through installing MPF 0.57 a Windows machine.


!!! warning "MPF 0.80 is Coming Soon"

    This installation guide is for MPF 0.57 and the legacy MC, which is being replaced in the upcoming MPF 0.80 with the Godot MC. If you are just getting started with MPF, we recommend you [install MPF 0.80](index.md) instead.

Note that installing MPF is more complicated than a normal application.
This is because MPF is a development tool you use to create your pinball
software, not a finished app itself. So, like everything in pinball,
there are a lot of steps.

!!! note

    If you're an expert Python user, you can skip most of this page. Just
    know you need Python 3.9 (newer or older won't work, see below), and
    you can install MPF-MC via pip. `pip install mpf-mc` This will also
    install MPF. You probably also want to install MPF Monitor via
    `pip install mpf-monitor`.

## Remove prior versions of MPF

MPF and the MPF-MC have many dependencies and requirements. If you have
an older version of MPF installed, it may have installed some of these
dependencies in a way that is incompatible with the latest version of
MPF. So it's best to remove any prior versions of MPF before installing
the latest version.

Uninstall MPF by using this command:

``` doscon
pip uninstall mpf
```

If you are unsure which version of MPF you have installed, you can run
this command to check what is installed:

``` doscon
mpf --version
```

If you are using a virtual environment for MPF (recommended!) then
you don't need to uninstall anything, just create a new one.

## Windows System Requirements

MPF 0.57 requires Python 3.9, 3.10, or 3.11.

MPF can run on 3.8, but the MPF-MC audio doesn't work on Windows in
those versions. So you should use Python 3.9.

## Install Python

If you open a command prompt on a fresh Windows machine and type
`python`, the Microsoft App Store will open and try to install Python
3.7. This is not the version of Python you want. So don't do that.

So instead, install Python from python.org. Here's the direct link to
the newest installer for the final version of Python 3.9:
<https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe>

Run the installer, and choose the "Customize installation" option, and
make sure to check the box for "py launcher" and "pip". (The others
don't matter either way.) Then on the next screen, check the box for
"Add Python to environment variables". Then click "Install".

Then open a command prompt (you can just run "cmd"), and type each of
these commands one at a time (and hit enter after each one). First, make
sure Python is installed and make sure when you run "python" that
it's the proper version. (Sometimes Windows will have multiple versions
of Python installed and it's not always clear which one will be used
when you type "python".)

``` doscon
python --version
```

You want a result like "Python 3.9.13" or whatever version you just
installed. If you see a version other than that, trying running
`python3 --version` instead.

## Create a Virtual Environment

It's strongly recommended to create a virtual environment for MPF,
which will keep the installed packages from conflicting with other
applications on your computer. Before proceeding, follow the steps on
the [virtual environment installation guide](virtual-environments.md)

!!! danger "Do not skip the Virtual Environment"

    Virtual environments are important for keeping your computer clean and preventing different packages from
    conflicting. Without virtual environments, you may encounter dependency conflicts and stale packages that
    will prevent MPF from running. Troubleshooting and manually cleaning up packages is a pain—do your future
    self a favor and setup an MPF virtual environment now!

## Install MPF

Now you're ready to install MPF. Open a new command window (cmd.exe),
activate your virtual environment, and type these commands and hit enter.

``` doscon
pip install "mpf"
```

A bunch of things will scroll by, and then hopefully MPF is installed.
You can test it by typing this command:

``` doscon
mpf --version
```

This should print out something like [MPF 0.57.0](#). If you
get an error, something went wrong. If you get a different version, then
you might have an older version of MPF which you need to uninstall
first. (See the "Remove prior versions of MPF" section above.)

## Install MPF Monitor

MPF Monitor the developers "god view" into your running MPF code. It
has windows to show the states of every device, events, variables,
modes, etc. You can even add a photo of your playfield and it will show
all the lights and switches on it animated in real time to show you
what's happening in your game.

MPF Monitor is also nice because it's a simple install, so you can
visualize your game quickly. The MPF-MC (which will drive the displays
in your machine) is a more complicated install, so you can get your game
working with MPF Monitor first, and then add the MPF-MC later.

``` doscon
pip install mpf-monitor
```

You can now proceed with the getting started tutorials, or, go on to
install the MPF Media Controller (MPF-MC).

## Install the MPF Media Controller (MPF-MC)

The MPF Media Controller (MPF-MC) is a standalone package used to
control the graphics, sounds, and music in a pinball machine. It's a
separate package from MPF. Not every pinball machine uses MPF-MC, but
most do. (There are also other media controllers that are not MPF-MC.
For example, some people use Unity, the Unreal Engine, or Godot as their
media controllers.)

To install MPF-MC, open your virtual environment and use the following command:

``` doscon
pip install mpf-mc
```

If you encounter permission issues during the installation, try running
the commands with administrator privileges (Right-click on cmd.exe ->
Run as Administrator).

## Testing MPF-MC

Installing MPF-MC is pretty straightforward. Unfortunately just because
it installs doesn't mean it works. :(

Dec. 2023 Note: mc_demo and demo_man aren't working, but you can get
the demo_man loading screen to display after performing the following:

Because 0.57 is the current release, download the `0.57.x` branch of
the `mpf-examples` repo from here:
<https://github.com/missionpinball/mpf-examples>.

![image](images/version-select.png)

You can download the zip file and unzip it, or clone it. If you
download the `dev` branch, you will have config version mismatch
issues.

From the commmand terminal, change to the `mpf-examples-0.57.x`
directory, where ever it was downloaded. Then, change to the
`demo_man` directory. Finally, run the following command:

``` doscon
mpf mc
```

You should have text displayed in the terminal, showing that MPF MC
is loading, then the MPF BCP server should wait for a connection:

![image](images/mpf-mc-output.jpg)

The Demo Man loading screen should also be displayed:

![image](images/mpf-demo-man-display.png)


May 2023 Note: Some of this might not work: The mc_demo and demo_man
mentioned below might not work anymore as they haven't been updated in
a while. Feel free to fix and/or update them and we'll merge your
changes in!

One way to test the MC is download the `mpf-examples` repo from here:
<https://github.com/missionpinball/mpf-examples>. You can either clone
it locally, or download the zip file and unzip it. Either is fine, just
do what you're most comfortable with. Be sure to download / switch to
the `dev` branch.

Then back in the command terminal, change into the `mpf-examples` folder
(or whatever folder you just unzipped that into), then change into the
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
fix it if so. But for now it's fine.

You can also run the "demo_man" game from the `mpf-examples` folder.
Change into the `demo_man` folder and run `mpf both -X`. You should see
the DMD window pop up. The window you ran the command from will have
some warnings which cover up the nice text UI display. Just grab a
corner of the window with the mouse and resize the window (just make it
a tiny bit bigger and smaller) and that will cause the window contents
to completely refresh and you should see the expected MPF text UI
display showing switch status, ball locations, etc. (See the screenshots
below for details)

If you do not see the "normal" MPF text UI display, and instead see
something like this:

![image](images/bad-display.jpg)

This is because those warnings mentioned above print on top of the nice
MPF display. To fix this, just grab a corner of the window with the
mouse and resize it to be a bit bigger or smaller, which will cause the
entire window to update and you should see the expected MPF text UI
display showing switch status, ball locations, etc. (See the screenshots
below for details)

![image](images/good-display.jpg)

Alternately if you don't want to resize the window every time, you can
open two different command prompt windows, and run `mpf -X` in one and
`mpf mc` in the other.

At this point, MPF is ready to go!

## Keeping MPF up-to-date

Once you have MPF installed via the procedure above, you can keep it
up-to-date by running the final two pip commands from above which you
used to install MPF and MPF-MC.

Questions? Comments? Need help? You can post in the [forum](../community/index.md).
